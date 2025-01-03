"""
run.py

This script is part of the Task Logger program. It provides functionality
for logging tasks, viewing logs, and displaying task statistics using
Google Sheets as the backend.

Features:
- Log tasks with details such as name, task description, date, hours, and type.
- View logged tasks in a tabular format.
- Generate and display task statistics filtered by month.

Usage:
- Execute the script to start the interactive task logger program.

Author: Fabio Loche
"""
from datetime import datetime
from collections import defaultdict
import json
import os
import calendar
from prettytable import PrettyTable
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets Setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# Decodes the environment variable
CREDS_INFO = json.loads(os.environ["creds"])
# Update with your Google Sheets ID
SPREADSHEET_ID = "1jNF9dM8jqkJBCoWkHhPYtRDOtXTDtGt6Omdq5cZpX8U"
SHEET_NAME = "Foglio1"  # Name of the sheet

# Global variables for Google Sheets integration
CREDS = None
CLIENT = None
SHEET = None


def init():
    """
    Initialize the Google Sheets connection and set up global variables.
    This function uses service account credentials to authorize the
    Google Sheets client and opens the specified sheet for operations.
    @return
        None
    """
    global CREDS, CLIENT, SHEET
    CREDS = Credentials.from_service_account_info(CREDS_INFO, scopes=SCOPES)
    CLIENT = gspread.authorize(CREDS)
    SHEET = CLIENT.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)


def welcome_message():
    """
    Prints the introduction and instructions for the Task Logger Program.
    """
    print("Welcome to the Task Logger Program!")
    print(
        "Managers can track team tasks, hours, and view detailed stats by "
        "member or month."
    )
    print(
        "Team members can log tasks in under 30 seconds with our easy "
        "interface."
    )
    print(
        "For Managers: Get real-time stats to monitor team performance "
        "and contributions."
    )
    print(
        "For Team Members: Quickly log tasks in the 'Log Task' section "
        "in no time!"
    )


def get_current_datetime():
    """
    Get the current date and time in the format
    DD-MM-YYYY HH:MM:SS.

    @return
        str: The current date and time as a formatted string.
    """
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def ensure_headers():
    """
    Ensure that the Google Sheet has the correct headers.

    This function checks whether the first row of the Google Sheet contains
    the expected headers. If the sheet is empty, it adds the headers. If the
    headers are present but do not match the expected format, it displays
    a warning.

    Expected headers:
        ["Name", "Task", "Date", "Hours", "Type", "Recorded At"]

    Args:
        None

    @return
        None
    """
    headers = ["Name", "Task", "Date", "Hours", "Type", "Recorded At"]
    existing_data = SHEET.get_all_records()

    # Check if headers are missing or don't match
    if not existing_data:  # If the sheet is empty
        SHEET.append_row(headers)
        print("Headers added to Google Sheets.")
    elif list(existing_data[0].keys()) != headers:  # If headers don't match
        print("Warning: The headers in the sheet don't match expected format.")


def get_date():
    """
    Prompt the user to enter a date in the format DD-MM-YYYY or use today's
    date by default.

    Validates user input to ensure the date is in the correct format.
    If the input is empty, the current date is returned in DD-MM-YYYY format.
    Prompts the user until a valid date is entered for invalid input.

    @return
        str: A valid date in the format DD-MM-YYYY.
    """
    while True:
        date_input = input(
            "Enter the date (DD-MM-YYYY) or press Enter to use today's date: "
        )

        if not date_input.strip():  # User pressed Enter
            return datetime.now().strftime("%d-%m-%Y")

        try:
            # Validate and format the custom date
            custom_date = datetime.strptime(date_input, "%d-%m-%Y")
            return custom_date.strftime("%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")


def select_task_type():
    """
    Prompt the user to select a task type from a predefined list.

    Displays a menu of task types: Administrative, Marketing, Product.
    and allows the user to choose by entering the corresponding number.
    If the user enters an invalid choice, they are prompted again until
    a valid selection is made.

    @return
        str: The selected task type as a string ("Administrative",
        "Marketing", or "Product").
    """
    while True:
        print("\nSelect Task Type:")
        print("1. Administrative")
        print("2. Marketing")
        print("3. Product")
        type_choice = input(
            "Enter the number corresponding to the task type: ")

        if type_choice == "1":
            return "Administrative"
        if type_choice == "2":
            return "Marketing"
        if type_choice == "3":
            return "Product"

        print("Invalid choice. Please enter 1, 2, or 3.")


def log_task():
    """
    Log a new task to the Google Sheet.

    Prompts the user to provide task details, including:
        - Name: The name of the person logging the task.
        - Task: A description of the task performed.
        - Date: The task date (custom or today's).
        - Hours: The number of hours spent on the task.
        - Task Type: Administrative, Marketing, or Product.
        - Recorded At: The current date and time of the task entry.

    Validates user inputs before appending to Google Sheets. Displays an
    error message if logging fails.

    @return
        None
    """
    while True:
        name = input("Enter your name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please enter a valid name.")

    # Validate and ensure the task input is not empty or just spaces
    while True:
        task = input("Enter the task: ").strip()
        if task:
            break
        print("Task description cannot be empty. Please enter a valid task.")

    date = get_date()  # Function to get date (custom or current)

    # Validate and ensure the hours input is a positive float
    while True:
        hours_input = input("Enter hours worked: ").strip()
        try:
            hours = float(hours_input)
            if hours > 0:
                break
            print("Hours must be greater than 0.")
        except ValueError:
            print("Invalid input for hours. Please enter a valid number.")

    task_type = select_task_type()  # Function to select the task type
    recorded_at = get_current_datetime()  # Get the current date and time

    # Append data to the Google Sheet
    try:
        SHEET.append_row([name, task, date, hours, task_type, recorded_at])
        print("Task logged successfully.")
    except gspread.exceptions.APIError as e:
        print("Failed to log task due to an API error:", e)
    except gspread.exceptions.SpreadsheetNotFound:
        print("Spreadsheet not found. Please check your spreadsheet ID.")
    except ValueError as e:
        print("Provided data is invalid:", e)


def view_logs():
    """
    Display all logged tasks in a tabular format in the terminal.

    This function retrieves all records from the Google Sheet and displays them
    in a neatly formatted table using the PrettyTable library. If there are no
    logs available, it informs the user. In case of any errors during the
    process, an error message is displayed.

    @return
        None
    """
    try:
        print("\nView Logs in Terminal:")

        records = SHEET.get_all_records()
        if not records:
            print("No logs available to view.")
            return

        table = PrettyTable()
        table.field_names = records[0].keys()
        for record in records:
            table.add_row(record.values())
        print(table)

    except gspread.exceptions.APIError as e:
        print(f"Error viewing logs due to API error: {e}")
    except gspread.exceptions.SpreadsheetNotFound:
        print("Spreadsheet not found. Please check your spreadsheet ID.")
    except ValueError as e:
        print(f"Invalid data: {e}")


def filter_tasks_by_month(records):
    """
    Filter task records by the selected month.

    This function provides the user with a list of the last 12 months to choose
    from. It filters the task records based on the selected month and year.

    Args:
        records: A list of task records retrieved from the Google Sheet.

    @return
        tuple: A tuple containing:
            - filtered_records (list): Task records for the selected month.
            - selected_month_name (str): The name of the selected month,
            or None if no valid choice is made.
    """
    today = datetime.now()

    months = []
    for i in range(12):
        month = (today.month - i - 1) % 12 + 1  # Handle month rollover
        year = today.year if today.month - i > 0 else today.year - 1
        months.append((calendar.month_name[month], month, year))

    months = months[::-1]

    print("\nFilter by Month:")
    for idx, (month_name, _, _) in enumerate(months, start=1):
        print(f"{idx}. {month_name}")

    try:
        choice = int(input("Enter the number corresponding to your choice: ")) - 1
        if choice < 0 or choice >= len(months):
            print("Invalid choice.")
            return [], None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return [], None

    selected_month_name, selected_month, selected_year = months[choice]
    filtered_records = [
        record
        for record in records
        if datetime.strptime(record['Date'], "%d-%m-%Y").month == selected_month
        and datetime.strptime(record['Date'], "%d-%m-%Y").year == selected_year
    ]

    return filtered_records, selected_month_name


def display_statistics_table():
    """
    Display task statistics for the selected month.

    This function retrieves all task records from the Google Sheet and filters
    them by the selected month. It calculates:
        - Hours worked per task type.
        - Hours worked by each collaborator.
        - Total hours logged for the selected month.

    The statistics are displayed in a tabular format using the
    PrettyTable library. If no logs are found or no records match
    the selected month, appropriate messages are displayed.

    @return
        None
    """
    try:
        records = SHEET.get_all_records()

        if not records:
            print("No logs found. Please log a task first.")
            return

        while True:
            filtered_records, selected_month_name = filter_tasks_by_month(records)

            if filtered_records:
                print(f"\nRecords found for {selected_month_name}.\n")
                break
            if selected_month_name is None:
                print("Invalid choice. Please select a valid month.")
            else:
                print(f"No records found for {selected_month_name}. "
                    "Please select another month.")

        # Initialize data containers for statistics
        task_type_data = defaultdict(float)
        collaborator_data = defaultdict(float)
        selected_month_total_hours = 0

        # Calculate statistics for the selected month
        for record in filtered_records:
            task_type_data[record["Type"]] += float(record["Hours"])
            collaborator_data[record["Name"]] += float(record["Hours"])
            selected_month_total_hours += float(record["Hours"])

        # Helper function to generate and display tables
        def generate_table(data, title, headers):
            table = PrettyTable()
            table.title = title
            table.field_names = headers
            for key, value in data.items():
                table.add_row([key, f"{value:.2f}h"])
            print(table)

        # Generate and display tables
        generate_table(
            task_type_data,
            f"Hours per Task Type for {selected_month_name}",
            ["Task Type", "Hours"]
        )
        generate_table(
            collaborator_data,
            f"Hours by Collaborator for {selected_month_name}",
            ["Collaborator", "Hours"]
        )
        print(f"\nTotal Hours for {selected_month_name}: {selected_month_total_hours:.2f}h")

    except (ValueError, TypeError) as e:
        print(f"Error displaying statistics: {e}")


def main():
    """
    Main function to initialize the program and provide a menu-driven interface
    for the Task Logger program.

    The function offers the following options:
        1. Log Task: Allows the user to log a new task.
        2. View Logs: Displays all logged tasks in a tabular format.
        3. View Statistics: Displays task statistics for a selected month.
        4. Exit: Exits the program.

    The program initializes the Google Sheets connection and continues to
    display the menu until the user chooses to exit.

    @return
        None
    """
    # Initialize global variables and Google Sheets connection
    init()

    # Call the function to display the introduction
    welcome_message()

    # Call ensure_headers to make sure headers are in place
    ensure_headers()

    while True:
        print("\nOptions:")
        print("1. Log Task")
        print("2. View Logs")
        print("3. View Statistics")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            log_task()
        elif choice == '2':
            view_logs()
        elif choice == '3':
            display_statistics_table()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
