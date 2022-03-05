#!/usr/bin/env python3
import sys
import subprocess
import os


print("Content-type: text/html\n\n")
print("<html>\n<body>")
print("<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">")

mailq_status,mailq = subprocess.getstatusoutput('mailq | grep -c "^[A-F0-9]"')
if int(mailq) >= 0:
	print(f"Total Mail Queue: {mailq}\n")
else:
	print("Unable to fetch mailq\n")

##### get Total sent mails
####Give permission to /var/log/maillog of apache chmod 640 , and chown apache
sent_status,sent_mails = subprocess.getstatusoutput("cat /var/log/maillog | grep -Ev 'relay=local|Saved' | grep sent | wc -l")
if int(sent_status) == 0:
	print(f"<div>Total Sent Mail: {sent_mails}</div>")
else:
	print("Unable to fetch sent mails")


############## total received mails

received_status,received_mails = subprocess.getstatusoutput("cat /var/log/maillog | grep -E 'Saved|private' | wc -l")
if int(received_status) == 0:
	print(f"<div>Total received Mails: {received_mails}</div>")
else:
	print("Enable to fetch received Mails")

print("</div>\n</body>\n</html>")

