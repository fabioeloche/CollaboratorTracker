# Collaborator Tracker

Collaborator Tracker is a Python program designed to help users efficiently log, view, and analyze tasks using a Google Sheets backend. The program integrates task management and data visualization features, offering a simple yet effective solution for individuals and teams.

![Collaborator Tracker](./assets/images/main.png)

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Live Application](#live-application)
3. [Features](#features)
4. [Setup](#setup)
   - [Dependencies](#dependencies)
   - [Google Sheets API Setup](#google-sheets-api-setup)
   - [Environment Variables](#environment-variables)
   - [Configurations](#configurations)
5. [Usage](#usage)
6. [Testing](#testing)
   - [Summary of Tests](#summary-of-tests)
   - [Unit Testing](#unit-testing)
   - [Integration Testing](#integration-testing)
   - [Error Handling](#error-handling)
   - [Performance Testing](#performance-testing)
   - [Browser Compatibility Testing](#browser-compatibility-testing)
7. [Project Structure](#project-structure)
8. [Deployment on Heroku](#Deployment-on-Heroku)
8. [Contributors](#contributors)
9. [License](#license)

## Project Overview

Collaborator Tracker aims to simplify task tracking and management by providing:
- A command-line interface for logging tasks.
- Google Sheets integration for real-time data storage and retrieval.
- Data filtering and statistical analysis for better task insights.

## Live Application

Access the live application here: [Collaborator Tracker](https://fabioapptest-71025b7099dc.herokuapp.com/)


---

## Features

- *Task Logging:* Easily log task details such as type, assignee, date, and hours worked.
- *Data Viewing:* Retrieve and display task logs in a tabular format.
- *Filtering by Month:* Filter tasks by specific months for focused reviews.
- *Statistical Analysis:* View detailed statistics, including total hours spent per task type and collaborator.
- *Google Sheets Integration:* Interact with Google Sheets for seamless data handling.

---

## Setup

### Dependencies
- *Python*
- *Libraries:*
  - gspread: For interacting with Google Sheets.
  - google-auth: For authenticating with Google APIs.
  - prettytable: For creating formatted tables.

### Google Sheets API Setup
1. Enable the *Google Sheets API* in the Google Cloud Console.
2. Create a service account and download the credentials as a JSON file.
3. Save the credentials in a secure location and ensure the path is accessible by your program.

### Environment Variables
Set up the following environment variable:
- CREDS: Path to your Google Sheets API JSON credentials.

### Configurations
Modify the script with your Google Sheets details:
- SPREADSHEET_ID: The ID of your spreadsheet.
- SHEET_NAME: The name of the worksheet to use.

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/fabioeloche/CollaboratorTracker.git
2. Navigate to the project directory:
   ```bash
   cd CollaboratorTracker
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the program:
   ```bash
   python run.py
5. Follow the interactive menu to log tasks, view logs, or analyze data.

---

## Testing

The project includes extensive testing to ensure reliability and performance. Below is an outline of the tests performed, their objectives, and outcomes.

### Summary of Tests

| Feature                 | Expected Outcome                                         | Testing Performed                           | Result                            | Pass/Fail |
|-------------------------|---------------------------------------------------------|--------------------------------------------|-----------------------------------|-----------|
| `get_current_datetime()`| Returns correctly formatted date and time               | Checked against different system times      | Correctly formatted date/time     | Pass      |
| `log_task()`            | Logs task details accurately in Google Sheets           | Logged various tasks with different details| Task logged successfully          | Pass      |
| `view_logs()`           | Displays all tasks in tabular format                    | Viewed logs after multiple task entries     | Logs displayed as expected        | Pass      |
| `filter_tasks_by_month()`| Filters tasks correctly by the selected month          | Filtered tasks for multiple months          | Tasks filtered accurately         | Pass      |
| `display_statistics_table()` | Aggregates and displays task statistics            | Viewed statistics after task entries        | Accurate statistics displayed     | Pass      |
| Error Handling          | Manages invalid inputs and API failures gracefully      | Entered invalid data, simulated API errors | Errors handled with messages      | Pass      |
| Performance             | Handles large datasets efficiently                      | Tested with 1000+ task entries              | System remains responsive         | Pass      |
| Browser Compatibility   | Works across major browsers (Chrome, Firefox, Edge, Safari) | Tested the app in various browsers        | Full functionality across all     | Pass      |

### Types of Tests

#### Unit Testing
- **Objective:** To validate individual functions independently.
- Examples:
  - `get_current_datetime()`: Validates date and time formatting.
  - `log_task()`: Ensures task data is logged accurately.

#### Integration Testing
- **Objective:** To validate the interaction between multiple features.
- Examples:
  - Ensured logging tasks, viewing logs, and displaying statistics work cohesively.
  - Validated Google Sheets integration for seamless data handling.

#### Error Handling
- **Objective:** To handle unexpected or invalid inputs and external errors gracefully.
- Examples:
  - Tested invalid dates or missing data fields.
  - Simulated Google Sheets API failures to check fallback mechanisms.

#### Performance Testing
- **Objective:** To ensure the application remains performant under heavy use.
- Example:
  - Tested with a dataset containing over 200 task entries, ensuring consistent responsiveness.

#### Browser Compatibility Testing
- **Objective:** To verify the app functions as expected on different web browsers.
- Browsers Tested:
  - **Google Chrome**
  - **Mozilla Firefox**
  - **Microsoft Edge**
  - **Safari**
- Results:
  - The app is fully functional and responsive across all tested browsers.

---

## Project Structure

### Key Files
- *task_logger.py*: Main program script.
- *requirements.txt*: Lists Python dependencies.
- *Google Sheets Credentials*: JSON file for API authentication.

### Screenshots
- *Task Logging Screen*:  
  ![Task Logging](./assets/images/img1)
- *View Logs Screen*:  
  ![View Logs](./assets/images/img2)
- *Statistics Screen*:  
  ![Statistics](./assets/images/img3)

---

## Deployment on Heroku

1. **Add Buildpacks:**
   - Go to the **Settings** tab of your Heroku app.
   - In the **Buildpacks** section, add:
     - `heroku/python`
     - `heroku/nodejs`
   - Ensure `heroku/python` is listed first.

2. **Set Environment Variables:**
   - In the **Config Vars** section under the **Settings** tab, add the following:
     - **`CREDS`**: Paste your Google Sheets API JSON credentials.
     - **`PORT`**: Set the value to `8000`.

3. **Connect to GitHub:**
   - Go to the **Deploy** tab in your Heroku app.
   - Under **Deployment Method**, select **GitHub** and link your repository.

4. **Select and Deploy Branch:**
   - Choose the branch you want to deploy (e.g., `main`).
   - Click **Deploy Branch** to build and deploy the app.

---

## Contributors

- [Fabio Loche](https://github.com/fabioeloche) - Project Author

---
