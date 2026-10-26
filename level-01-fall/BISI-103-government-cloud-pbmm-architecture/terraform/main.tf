# =========================================================================
# BISI-103: Terraform Module - Protected B (PBMM) Cloud Landing Zone
# Target Region: Canada Central (ca-central-1)
# Compliance: CCCS ITSG-33 / TBS Cloud Security Guardrails
# =========================================================================

terraform {
  required_version = ">= 1.8.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.50"
    }
  }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Environment         = "Protected-B"
      Department          = "Public-Sector-BI"
      SecurityClassification = "Protected-B-Medium-Medium"
      ManagedBy           = "Terraform"
    }
  }
}

# 1. Customer Managed KMS Key for Envelope Encryption
resource "aws_kms_key" "pbmm_kms_key" {
  description             = "KMS Key for Protected B Analytics Data Storage"
  deletion_window_in_days = 30
  enable_key_rotation     = true

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "Enable IAM User Permissions"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::${var.account_id}:root"
        }
        Action   = "kms:*"
        Resource = "*"
      }
    ]
  })
}

# 2. Hardened S3 Bucket for Protected B Data Lakehouse
resource "aws_s3_bucket" "pbmm_datalake_bucket" {
  bucket        = "gc-protected-b-datalake-${var.environment_name}"
  force_destroy = false
}

# Enforce Versioning
resource "aws_s3_bucket_versioning" "pbmm_versioning" {
  bucket = aws_s3_bucket.pbmm_datalake_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Enforce Server-Side KMS Encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "pbmm_encryption" {
  bucket = aws_s3_bucket.pbmm_datalake_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = aws_kms_key.pbmm_kms_key.arn
      sse_algorithm     = "aws:kms"
    }
    bucket_key_enabled = true
  }
}

# Block all Public Ingress (CCCS Guardrail #1)
resource "aws_s3_bucket_public_access_block" "pbmm_public_block" {
  bucket = aws_s3_bucket.pbmm_datalake_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Enforce TLS 1.2+ and In-Transit Encryption
resource "aws_s3_bucket_policy" "enforce_tls" {
  bucket = aws_s3_bucket.pbmm_datalake_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "EnforceTLSRequestsOnly"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:*"
        Resource = [
          aws_s3_bucket.pbmm_datalake_bucket.arn,
          "${aws_s3_bucket.pbmm_datalake_bucket.arn}/*"
        ]
        Condition = {
          Bool = {
            "aws:SecureTransport" = "false"
          }
          NumericLessThan = {
            "s3:TlsVersion" = 1.2
          }
        }
      }
    ]
  })
}
