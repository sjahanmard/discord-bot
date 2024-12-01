import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils.service_account_key import service_account_key


def handle_cancellation(id: str):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_dict(service_account_key, scope)
    client = gspread.authorize(credentials)

    sheet = client.open("wow_orders").sheet1 

    cell = sheet.find(id, in_column=1)
    if cell:
        sheet.update_cell(cell.row, 3, "Cancelled")
        print(f"Order with id {id} has been cancelled.")
        return True
    else:
        print(f"Order with id {id} not found.")
        return False