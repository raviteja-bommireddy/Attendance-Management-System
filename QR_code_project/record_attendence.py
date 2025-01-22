from googleapiclient.discovery import build

# Google Sheets ID and Range
SPREADSHEET_ID = 'your-google-sheet-id'
RANGE = 'Sheet1!A1:Z1000'  # Change to your range in the Google Sheet

# Function to record attendance
def record_attendance(roll_number, date, status):
    creds = authenticate()
    service = build('sheets', 'v4', credentials=creds)

    # Read the current sheet data
    sheet = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
    rows = sheet.get('values', [])

    # Check if the student already has a record for that date
    for row in rows:
        if row[0] == roll_number:
            # Update the attendance status for the student
            row[date] = status
            update_range = f'Sheet1!A{rows.index(row) + 1}:Z{rows.index(row) + 1}'
            values = [row]
            body = {'values': values}
            service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=update_range, valueInputOption="RAW", body=body).execute()
            print(f"Attendance for {roll_number} on {date} has been updated to {status}")
            return

    # If student doesn't exist, add a new row
    new_row = [roll_number] + [status if i == date else '' for i in range(1, len(rows[0]))]
    service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE, valueInputOption="RAW", body={'values': [new_row]}).execute()
    print(f"New attendance record created for {roll_number} on {date}")
