import smtplib
from secrets import sender_email, app_password

def test_smtp_connection():
    print(f"Testing SMTP connection for {sender_email}...")
    try:
        # Using SMTP_SSL for port 465
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            print("Connecting to gmail smtp server...")
            server.login(sender_email, app_password)
            print("Successfully authenticated!")
            
            # Optional: Send a test email to yourself
            subject = "SMTP Test"
            body = "This is a test email to verify SMTP credentials."
            msg = f"Subject: {subject}\n\n{body}"
            
            server.sendmail(sender_email, sender_email, msg)
            print(f"Test email sent to {sender_email}")
            
    except smtplib.SMTPAuthenticationError:
        print("\nERROR: Authentication Failed.")
        print("Please check:")
        print("1. 2-Step Verification is ENABLED on your Google account.")
        print("2. You are using an APP PASSWORD, not your regular password.")
        print("3. The App Password in secrets.py is correct and hasn't been revoked.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    test_smtp_connection()
