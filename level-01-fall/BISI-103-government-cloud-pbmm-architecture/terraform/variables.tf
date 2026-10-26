variable "aws_region" {
  type        = string
  default     = "ca-central-1"
  description = "Canadian sovereign cloud region"
}

variable "account_id" {
  type        = string
  default     = "123456789012"
  description = "AWS Account Identifier"
}

variable "environment_name" {
  type        = string
  default     = "prod-analytics"
  description = "Environment identifier"
}
