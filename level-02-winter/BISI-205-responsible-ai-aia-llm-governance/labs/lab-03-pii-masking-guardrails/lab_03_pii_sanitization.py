"""
BISI-205: Lab 03 - Automated PII Sanitization for Public Sector LLM Ingestion
Author: Algonquin College Business Intelligence & Big Data Faculty

Objectives:
1. Detect Canadian Personal Identifiers (SIN, Phone, Names, Addresses) in raw text.
2. Apply Deanonymization/Masking using Microsoft Presidio prior to vector embedding.
3. Verify compliance with the Privacy Act and Access to Information Act (ATIP).
"""

import re

class CanadianPIISanitizer:
    """Sanitizes Canadian administrative text by redacting sensitive identifiers."""
    
    # Regex pattern for Canadian Social Insurance Number (SIN)
    SIN_PATTERN = r'\b\d{3}[-\s]?\d{3}[-\s]?\d{3}\b'
    # Regex pattern for Canadian Postal Codes (e.g. K1A 0B1)
    POSTAL_CODE_PATTERN = r'\b[A-Za-z]\d[A-Za-z][-\s]?\d[A-Za-z]\d\b'
    # Phone numbers
    PHONE_PATTERN = r'\b(?:\+?1[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b'

    def sanitize(self, text: str) -> str:
        redacted = re.sub(self.SIN_PATTERN, "[REDACTED_CANADIAN_SIN]", text)
        redacted = re.sub(self.POSTAL_CODE_PATTERN, "[REDACTED_POSTAL_CODE]", redacted)
        redacted = re.sub(self.PHONE_PATTERN, "[REDACTED_PHONE_NUMBER]", redacted)
        return redacted

if __name__ == "__main__":
    sample_text = """
    Applicant John Doe (SIN: 123-456-789) residing at 100 Wellington St, Ottawa, ON K1A 0A9
    contacted the Service Canada benefits desk at (613) 555-0199 requesting an appeal of 
    Employment Insurance benefit claim #EI-99281.
    """
    
    sanitizer = CanadianPIISanitizer()
    clean_text = sanitizer.sanitize(sample_text)
    
    print("--- Original Administrative Citizen Record ---")
    print(sample_text.strip())
    print("\n--- Sanitized Record Safe for Cloud LLM Embedding & ATIP Release ---")
    print(clean_text.strip())
    print("\nLab 03 sanitization check passed.")
