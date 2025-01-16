import qrcode
import os
from datetime import datetime

def generate_qr_code(data: str, output_path: str):
    # Create a QR code object
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    img.save(output_path)

def generate_daily_qr():
    # Use the current date and time to make the QR code unique
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    qr_data = f"attendance_link_{current_time}"
    output_path = f"qr_codes/{current_time}.png"
    
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")
    
    generate_qr_code(qr_data, output_path)
    return output_path

if __name__ == "__main__":
    qr_code_path = generate_daily_qr()
    print(f"QR Code generated and saved to: {qr_code_path}")
