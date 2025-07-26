import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "sulemansarwarr1@gmail.com"
sender_password = "umcq xoae cjnz ccyf"  # Use an App Password if 2FA is enabled

receiver_emails = ["qureshi.isb04@gmail.com", "qureshi.isb04@gmail.com"]  # Can be one or more
subject = "Daily Report"
body = "Hello,\n\nThis is your daily report.\n\nRegards,\nSuleman"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_emails)
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

try:
    # Create SMTP session for sending the mail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_emails, message.as_string())
    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()

