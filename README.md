#****Understanding the Idea****

Students enroll in a course under a professor, triggering the setup for attendance management. Every day, Monday to Friday, a unique QR code is sent to the professor’s email at 8 AM, along with a button that allows the professor to activate or deactivate attendance collection for that day. If the professor activates the attendance collection, students can scan the QR code to access a Google Form. On the form, students must enter their roll numbers, which are validated against their registered email IDs. If the roll number and email ID match, the student is marked as present. Attendance is automatically recorded in a Google Sheet, where student roll numbers are listed as rows, and working days are tracked as columns. This process ensures an efficient and accurate attendance management system for both students and professors.

##**implementation brreak down:**

**Enrollment**: Students enroll in a course under a professor, triggering setup for attendance management.

**Daily QR Code**: A unique QR code is sent to the professor's email daily. (Monday to Friday)

**Professor's Control**: The email contains a button allowing the professor to activate or deactivate attendance collection for that day. (professor will get a mail at a fixed time everyday, let's say morning 8AM)

**QR Presentation**: Students scan the QR code (if activated) to access a Google Form.

**Google Form Validation**: Students fill in their roll numbers, validated by their registered email IDs.

**Attendance Record**: Google Sheets maintains a table with student roll numbers as rows and working days as columns.

![image](https://github.com/user-attachments/assets/74b74320-f4f1-4580-849e-62e2ca2ecda0)

##**Tools and Technologies:**

**Python**: Backend logic, QR code generation, and API integration.

**Google Apps Script**: Integration with Google Forms and Sheets for data handling.

**Gmail API**: Automated email delivery with embedded QR codes and control buttons.

**Flask/Django**: Optional backend framework for a web interface.

**Google Forms & Sheets**: Data collection and storage.

**OAuth2**: For authentication and data security

**GitHub**: Version control and collaboration.

##****Implementation Plan:****

**Setup Gmail API and OAuth2**: Authenticate and automate QR code email delivery.

**Add Control Button in Emails**: Use HTML templates to embed "Enable/Disable" attendance buttons.

**Generate QR Codes**: Use Python’s qrcode library for daily codes.

**Google Forms and Sheets**: Create and secure the form, validate responses, and record data.

**Professor Analytics Dashboard**: Provide basic attendance analytics. (not mandetory, just test it & make sure that every students attendance is compiled or not 

**Testing and Debugging**: Ensure edge cases and workflows function seamlessly.

**Deployment**: Host the system for production on a cloud service like AWS or Heroku. (**not now, until the complete project with no bugs & sucessful testing**)
