-- =========================================================================
-- BISI-102: Lab 04 - Row-Level Security (RLS) & Multi-Tenant Public Sector Isolation
-- Author: Algonquin College Business Intelligence & Big Data Faculty
-- =========================================================================

-- Step 1: Enable RLS on Contracts
ALTER TABLE contracts ENABLE ROW LEVEL SECURITY;

-- Step 2: Create Roles for Departmental Analysts
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'ssc_analyst') THEN
        CREATE ROLE ssc_analyst WITH LOGIN PASSWORD 'PasswordSSC2026!';
    END IF;
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'pwgsc_analyst') THEN
        CREATE ROLE pwgsc_analyst WITH LOGIN PASSWORD 'PasswordPWGSC2026!';
    END IF;
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'auditor_general') THEN
        CREATE ROLE auditor_general WITH LOGIN PASSWORD 'AuditorGen2026!';
    END IF;
END $$;

-- Grant base table permissions
GRANT SELECT ON departments, vendors, contracts TO ssc_analyst, pwgsc_analyst, auditor_general;

-- Step 3: Implement Departmental Tenant Isolation Policy
DROP POLICY IF EXISTS departmental_isolation_policy ON contracts;

CREATE POLICY departmental_isolation_policy ON contracts
    FOR SELECT
    USING (
        -- Departmental users only see their own department's contracts
        dept_id IN (
            SELECT d.dept_id FROM departments d
            WHERE (current_user = 'ssc_analyst' AND d.dept_code = 'SSC')
               OR (current_user = 'pwgsc_analyst' AND d.dept_code = 'PWGSC')
        )
        -- Auditor General role has unrestricted visibility
        OR current_user = 'auditor_general'
    );

-- Verification:
-- SET ROLE ssc_analyst; SELECT * FROM contracts; (Only returns SSC contracts)
-- SET ROLE auditor_general; SELECT * FROM contracts; (Returns all contracts)
-- RESET ROLE;
