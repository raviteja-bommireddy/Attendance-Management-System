import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os

def send_email(recipient_email, subject, body, attachment_path):
    from_email = "your_email@example.com"  # Replace with your email
    from_password = "your_password"       # Replace with your email password or app-specific password
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # HTML content (can include activation/deactivation button as a link)
    msg.attach(MIMEText(body, 'html'))

    # Attach QR code image
    with open(attachment_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
        msg.attach(img)

    # Set up the server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, from_password)
            server.sendmail(from_email, recipient_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def create_email_body(qr_code_path):
    activation_url = "https://yourdomain.com/activate"  # Link to activate attendance
    deactivation_url = "https://yourdomain.com/deactivate"  # Link to deactivate attendance

    return f"""
    <html>
    <body>
        <p>Please find your attendance QR Code attached. To collect attendance, please use the links below:</p>
        <p><a href="{activation_url}">Activate Attendance</a></p>
        <p><a href="{deactivation_url}">Deactivate Attendance</a></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    recipient_email = "professor@example.com"  # Replace with the professor's email
    qr_code_path = "qr_codes/2025-01-16_08-00-00.png"  # Replace with the actual generated QR code file
    email_subject = "Daily Attendance QR Code"
    email_body = create_email_body(qr_code_path)

    send_email(recipient_email, email_subject, email_body, qr_code_path)
