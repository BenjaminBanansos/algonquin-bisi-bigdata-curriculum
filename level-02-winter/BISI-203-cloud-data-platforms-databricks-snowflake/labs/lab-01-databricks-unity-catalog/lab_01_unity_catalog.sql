-- =========================================================================
-- BISI-203: Lab 01 - Databricks Unity Catalog 3-Level Namespace Governance
-- Hierarchy: catalog.schema.table
-- Compliance: Canadian Sovereign Data Governance & Auditing
-- =========================================================================

-- 1. Create Sovereign Top-Level Catalog
CREATE CATALOG IF NOT EXISTS canada_sovereign_catalog
MANAGED LOCATION 's3://gc-protected-b-datalake-prod-analytics/unity-catalog/'
COMMENT 'Top-level catalog for Canadian Federal Administrative Data';

-- 2. Create Functional Schemas (Medallion Pattern)
CREATE SCHEMA IF NOT EXISTS canada_sovereign_catalog.bronze_ingestion
COMMENT 'Raw unverified source payloads';

CREATE SCHEMA IF NOT EXISTS canada_sovereign_catalog.silver_cleansed
COMMENT 'De-identified, standardized public sector records';

CREATE SCHEMA IF NOT EXISTS canada_sovereign_catalog.gold_marts
COMMENT 'Business-ready aggregated data models for executive reporting';

-- 3. Define Fine-Grained Column Masking Function for SIN / Personal Identifiers
CREATE OR REPLACE FUNCTION canada_sovereign_catalog.silver_cleansed.mask_sin(sin STRING)
RETURN CASE 
    WHEN is_account_group_member('data_security_officers') THEN sin
    ELSE CONCAT('XXX-XXX-', RIGHT(sin, 3))
END;

-- 4. Apply Dynamic Column Mask to Sensitive Table
-- ALTER TABLE canada_sovereign_catalog.silver_cleansed.taxpayer_filings
-- ALTER COLUMN social_insurance_number 
-- SET MASKING FUNCTION canada_sovereign_catalog.silver_cleansed.mask_sin;
