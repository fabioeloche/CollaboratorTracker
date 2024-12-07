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
   bash
   git clone https://github.com/fabioeloche/CollaboratorTracker.git
   
2. Navigate to the project directory:
   bash
   cd CollaboratorTracker
   
3. Install the required Python dependencies:
   bash
   pip install -r requirements.txt
   
4. Run the program:
   bash
   python run.py
   
5. Follow the interactive menu to log tasks, view logs, or analyze data.

---