-- =========================================================================
-- BISI-102: Lab 01 - 3NF Public Procurement Schema & Integrity Constraints
-- Author: Algonquin College Business Intelligence & Big Data Faculty
-- =========================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Departments Reference Table
CREATE TABLE IF NOT EXISTS departments (
    dept_id SERIAL PRIMARY KEY,
    dept_code VARCHAR(10) NOT NULL UNIQUE,
    dept_name_en VARCHAR(150) NOT NULL,
    dept_name_fr VARCHAR(150) NOT NULL,
    ministerial_portfolio VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Vendors Reference Table
CREATE TABLE IF NOT EXISTS vendors (
    vendor_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    business_number VARCHAR(15) NOT NULL UNIQUE,
    legal_name VARCHAR(200) NOT NULL,
    city VARCHAR(100) NOT NULL,
    province_code CHAR(2) NOT NULL CHECK (province_code IN ('ON','QC','BC','AB','MB','SK','NS','NB','NL','PE','NT','YT','NU')),
    is_canadian_majority_owned BOOLEAN DEFAULT TRUE,
    security_clearance_level VARCHAR(20) DEFAULT 'Reliability' CHECK (security_clearance_level IN ('None', 'Reliability', 'Secret', 'Top Secret'))
);

-- 3. Federal Contracts Transaction Table
CREATE TABLE IF NOT EXISTS contracts (
    contract_id SERIAL PRIMARY KEY,
    contract_number VARCHAR(50) NOT NULL UNIQUE,
    dept_id INT NOT NULL REFERENCES departments(dept_id) ON DELETE RESTRICT,
    vendor_id UUID NOT NULL REFERENCES vendors(vendor_id) ON DELETE RESTRICT,
    contract_value NUMERIC(14, 2) NOT NULL CHECK (contract_value >= 0.00),
    award_date DATE NOT NULL,
    delivery_deadline DATE NOT NULL,
    procurement_tool VARCHAR(50) NOT NULL,
    is_amendment BOOLEAN DEFAULT FALSE,
    CONSTRAINT check_dates CHECK (delivery_deadline >= award_date)
);

-- Seed Minimal Data
INSERT INTO departments (dept_code, dept_name_en, dept_name_fr, ministerial_portfolio)
VALUES 
('PWGSC', 'Public Services and Procurement Canada', 'Services publics et Approvisionnement Canada', 'Procurement'),
('SSC', 'Shared Services Canada', 'Services partagés Canada', 'Digital Government'),
('STATCAN', 'Statistics Canada', 'Statistique Canada', 'Innovation, Science and Industry')
ON CONFLICT (dept_code) DO NOTHING;
