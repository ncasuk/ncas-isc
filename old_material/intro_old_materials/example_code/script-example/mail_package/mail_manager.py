print("Importing mail_manager...")

subject = "Really important message"
from_addr = "no-reply@stfc.com"

body = """
Hi, 

Here is a message.

Bye
"""


def send_mail(recipient, subject=subject, from_addr=from_addr, body=body):
    if "@" not in recipient:
        return False

    # import mailing library
    # set up message
    # send the message
    print(f"[INFO] Sent to {recipient}, from {from_addr}, with subject: {subject}")
    return True
