# 📧 Email Bot Sender (Python)

A Python-based command-line utility that lets you send emails (with or without attachments) to single or multiple recipients via Gmail SMTP. Great for sending quick updates, project files, or even automated notifications directly from your terminal.

## 🚀 Features

- ✅ Send plain text emails via Gmail SMTP  
- ✅ Send to one or multiple recipients (comma-separated input)  
- ✅ Optionally attach any file type (PDF, images, DOCX, ZIP, etc.)  
- ✅ Automatically detects file MIME type for compatibility  
- ✅ Secure connection using TLS  
- ✅ Interactive CLI input — no need to edit the code

## 🧠 How It Works

The script:
1. Prompts you for your Gmail credentials.
2. Asks for recipient email(s), subject, body, and attachment (optional).
3. Connects securely to Gmail SMTP (via TLS).
4. Sends the email(s) and prints status updates.

## ⚙️ Setup

### 🔧 Requirements

Install Python dependencies:

```bash
pip install -r requirements.txt
