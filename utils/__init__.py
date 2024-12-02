import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_channel_id():
    return int(os.getenv("FORM_SUBMISSION_CHANNEL_ID"))



def add_to_sheet(service_account_key:str, sheet_name:str, rows: set):
    """
    Adds rows to a Google Sheet using service account credentials.

    Args:
        service_account_key (dict): Dictionary containing the service account credentials.
        sheet_name (str): Name of the Google Sheet.
        rows (list of lists): List of rows to add, each row being a list of values.
    
    Returns:
        None
    """
    # Define the scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Authorize using the credentials dictionary
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(service_account_key, scope)
    client = gspread.authorize(credentials)
    print(sheet_name)
    # Open the spreadsheet by name
    sheet = client.open(sheet_name).sheet1  # Access the first sheet


    # Append rows
    for row in rows:
        sheet.append_row(row)

    print(f"Successfully added {len(rows)} row(s) to the Google Sheet: {sheet_name}")
