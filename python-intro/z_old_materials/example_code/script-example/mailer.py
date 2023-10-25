import sys

import mail_package.mail_manager as mm

from_addr = sys.argv[1]
recipients = sys.argv[2:]

print(f"People: {recipients}\n")


for person in recipients:
    print(f"Mailing: {person}")
    response = mm.send_mail(person, from_addr=from_addr)
    
    if response is False:
        print("[WARN] Failed to send.")

