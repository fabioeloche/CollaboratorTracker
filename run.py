import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from collections import defaultdict
import json
import os
from prettytable import PrettyTable

# Google Sheets Setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDS_INFO = json.loads(os.environ['creds'])  # Decodes the environment variable
SPREADSHEET_ID = "1jNF9dM8jqkJBCoWkHhPYtRDOtXTDtGt6Omdq5cZpX8U"  # Update with your Google Sheets ID
SHEET_NAME = "Foglio1"  # Name of the sheet

print("Welcome to the Task Logger Program!")

# Authorize and open the sheet
creds = Credentials.from_service_account_info(CREDS_INFO, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

# Function to get the current date and time
def get_current_datetime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Format: DD-MM-YYYY HH:MM:SS



