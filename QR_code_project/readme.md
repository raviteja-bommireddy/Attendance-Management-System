**have to work on this for better presentation of all these files interconnection while deployment & their working process by testing with real mail id**
## re-check all these files one more time before getting into further part.

# Backend Logic & QR Code Generation

### Step 1: Install Required Libraries
  pip install requirements.txt

### Step 2: Python Code for Generating QR Codes and Sending Emails
  **All proper cheching & working of python files**

### Step 3: Google Form Setup
  Create a Google Form:<br>
      <pre><br> 'Go to Google Forms & Create a form where students input their Roll Number and Email ID.'</pre>
      <pre><br> 'Ensure that responses are linked to a Google Sheet (this will automatically be created).'</pre>
### Step 4: Google Sheets API for Attendance Record
We'll use the Google Sheets API to record the attendance based on the data submitted through Google Forms.

## How the System Works:
<br>1. QR Code Generation: Every day, the Python script generates a unique QR code linked to a Google Form.
<br>2. Sending Emails: The script sends an email to the professor at a fixed time (e.g., 8 AM), including the QR code and a control button to activate/deactivate attendance.
<br>3. Student Form Submission: Students scan the QR code and fill out their roll numbers and email IDs in the Google Form.
<br>4. Attendance Record: The attendance is recorded automatically in a Google Sheet.
