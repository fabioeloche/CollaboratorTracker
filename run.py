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

# Function to ensure headers in the Google Sheet
def ensure_headers():
    headers = ["Name", "Task", "Date", "Hours", "Type", "Recorded At"]
    existing_data = sheet.get_all_records()

    # Check if headers are missing or don't match
    if not existing_data:  # If the sheet is empty
        sheet.append_row(headers)
        print("Headers added to Google Sheets.")
    elif list(existing_data[0].keys()) != headers:  # If headers don't match
        print("Warning: The headers in the sheet don't match expected format.")

# Call ensure_headers to make sure headers are in place
ensure_headers()

# Helper functions
def get_date():
    while True:
        date_input = input("Enter the date (DD-MM-YYYY) or press Enter to use today's date: ")

        if not date_input.strip():  # User pressed Enter
            return datetime.now().strftime("%d-%m-%Y")

        try:
            # Validate and format the custom date
            custom_date = datetime.strptime(date_input, "%d-%m-%Y")
            return custom_date.strftime("%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")


