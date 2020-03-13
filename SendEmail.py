import smtplib
import os
from email.message import EmailMessage
from email.utils import formataddr

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'Check your monthly expense'
msg['From'] = formataddr(('Brishila', EMAIL_ADDRESS))
msg['To'] = 'manikumar06@gmail.com'
msg.set_content('File Attached...')

files = ['MonthlyExpenses.xlsx']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS,  EMAIL_PASSWORD)
    smtp.send_message(msg)