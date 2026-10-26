-- =========================================================================
-- BISI-204: Lab 01 - Data Vault 2.0 Architecture (Hubs, Links, Satellites)
-- Modeling: Public Sector Citizen & Benefit Administration
-- =========================================================================

-- 1. HUB: Citizen Entity (Unique Business Key with MD5/SHA256 Hash)
CREATE TABLE IF NOT EXISTS hub_citizen (
    h_citizen_hash_key CHAR(32) PRIMARY KEY,
    citizen_business_id VARCHAR(50) NOT NULL UNIQUE,
    load_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    record_source VARCHAR(50) NOT NULL
);

-- 2. HUB: Public Benefit Program Entity
CREATE TABLE IF NOT EXISTS hub_benefit_program (
    h_program_hash_key CHAR(32) PRIMARY KEY,
    program_code VARCHAR(20) NOT NULL UNIQUE,
    load_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    record_source VARCHAR(50) NOT NULL
);

-- 3. LINK: Citizen Benefit Enrollment (Many-to-Many Relationship)
CREATE TABLE IF NOT EXISTS link_benefit_enrollment (
    l_enrollment_hash_key CHAR(32) PRIMARY KEY,
    h_citizen_hash_key CHAR(32) NOT NULL REFERENCES hub_citizen(h_citizen_hash_key),
    h_program_hash_key CHAR(32) NOT NULL REFERENCES hub_benefit_program(h_program_hash_key),
    load_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    record_source VARCHAR(50) NOT NULL
);

-- 4. SATELLITE: Citizen Demographics (Descriptive attributes with change history)
CREATE TABLE IF NOT EXISTS sat_citizen_demographics (
    h_citizen_hash_key CHAR(32) NOT NULL REFERENCES hub_citizen(h_citizen_hash_key),
    load_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    hash_diff CHAR(32) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    postal_code VARCHAR(7),
    record_source VARCHAR(50) NOT NULL,
    PRIMARY KEY (h_citizen_hash_key, load_timestamp)
);
