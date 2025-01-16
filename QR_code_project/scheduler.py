import schedule
import time
from generate_qr import generate_daily_qr
from send_email import send_email, create_email_body

def job():
    # Generate the QR code
    qr_code_path = generate_daily_qr()
    
    # Send the email to the professor
    recipient_email = "professor@example.com"  # Replace with the professor's email
    email_subject = "Daily Attendance QR Code"
    email_body = create_email_body(qr_code_path)
    send_email(recipient_email, email_subject, email_body, qr_code_path)

# Schedule the job to run every weekday at 8 AM
schedule.every().monday.at("08:00").do(job)
schedule.every().tuesday.at("08:00").do(job)
schedule.every().wednesday.at("08:00").do(job)
schedule.every().thursday.at("08:00").do(job)
schedule.every().friday.at("08:00").do(job)

if __name__ == "__main__":
    print("Scheduler started. Waiting for the time to run tasks...")
    while True:
        schedule.run_pending()
        time.sleep(1)
