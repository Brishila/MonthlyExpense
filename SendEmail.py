import smtplib
import os
from email.message import EmailMessage
from email.utils import formataddr
from datetime import datetime
from ExcelReport import ExcelReport


class SendEmail:
    def __init__(self):
        self.EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
        self.EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

    def send_report(self):
        msg = EmailMessage()
        msg["Subject"] = "Check your monthly expense"
        msg["From"] = formataddr(("MonthlyExpense", self.EMAIL_ADDRESS))
        msg["To"] = "jrbrishila@gmail.com"
        msg.set_content("File Attached...")

        file_append = datetime.now().strftime("%b%Y")
        fname = "MonthlyExpenses-" + file_append + ".xlsx"
        excel = ExcelReport(fname)

        try:
            excel.create_report()
        except:
            pass

        files = [fname]
        for report in files:
            with open(report, "rb") as f:
                file_data = f.read()
                file_name = f.name

            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename=file_name,
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
            smtp.send_message(msg)
