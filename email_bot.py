import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import mimetypes

sender_email = input("Enter your email : ")
sender_password = input("Enter your Password : ")  # Use an App Password if 2FA is enabled

receiver_emails = input("Enter receiver Email 'if multiple receiver pls use (,) : ").split(',')  # Can be one or more
subject = input("Enter Subject of Email : ")
body = input("Enter the body of Email : ")

attach_file = False
attachment_path = ""
attachment_part = None  # Store prepared attachment to use later

while True:
    attachment_choice= input("You want to send any attachment (Yes/NO) : ").lower()
    if attachment_choice == "yes":
        attachement_path= input("Enter File full Path : ")
        try:
            file_name = os.path.basename(attachement_path)
            # Guess the MIME type (e.g., for .docx, .jpg, etc.)
            mime_type, _ = mimetypes.guess_type(attachement_path)
            if mime_type is None:
                mime_type = "application/octet-stream"  # Fallback

            main_type, sub_type = mime_type.split("/", 1)

            with open (attachement_path,"rb")as attachment:
                part = MIMEBase(main_type, sub_type)
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f'attachment; filename="{file_name}"')

            attachment_part = part
            attach_file = True
            print(f"Attached file{file_name}")
        except Exception as e:
            print("Failed to attach file : ", str(e))
            exit()
        break
    elif attachment_choice == "no":
        print("No attachment  will be send.")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

try:
    # Create SMTP session for sending the mail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)

    for receiver in receiver_emails:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] =  receiver
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))
        if attach_file and attachment_part:
            message.attach(attachment_part)  # Attach the file here

        # Send the email
        server.sendmail(sender_email, receiver, message.as_string())
        print("Email sent to receiver : ",receiver)

    server.quit()
    print("All Email Send SUCESSFULLY")

except Exception as e:
    print("Error:", e)
