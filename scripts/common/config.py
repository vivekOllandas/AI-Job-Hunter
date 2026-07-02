import os

# ===== OpenAI =====
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ===== Gmail =====
GMAIL_EMAIL = os.getenv("GMAIL_EMAIL")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

# ===== Google Sheets =====
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")

# ===== Job Sites =====
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASSWORD = os.getenv("NAUKRI_PASSWORD")

INDEED_EMAIL = os.getenv("INDEED_EMAIL")
INDEED_PASSWORD = os.getenv("INDEED_PASSWORD")

# ===== Filters =====
JOB_KEYWORDS = [
    "Data Analyst",
    "Product Analyst",
    "BI Analyst",
    "MIS Analyst",
    "SQL Developer"
]

LOCATION = "India"

MIN_MATCH_SCORE = 8.5