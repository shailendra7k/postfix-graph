#!/usr/bin/env python3
import sys
import subprocess
import os
import cgi
import cgitb; cgitb.enable()
import matplotlib
import pylab
import matplotlib
matplotlib.use('Agg')

os.environ['HOME'] = '/tmp'

import matplotlib.pyplot as plt

print("Content-type: text/html\n\n")
print("<html>\n<head><script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js'></script></head>\n<body><canvas id='bar-chart' width=300' height='150'></canvas>")
print("<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">")
os.environ[ 'HOME' ] = '/tmp/'
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

print("""<script> new Chart(document.getElementById('bar-chart'), { type: 'bar', data: { labels: ['Mail Queue', 'Sent Mails', 'Received Mails'], datasets: [ { label: 'Number of Mails', backgroundColor: ['red', 'blue','yellow'], data: ["""+ f"""{mailq}"""+""","""+ f"""{sent_mails}"""+""","""+ f"""{received_mails}"""+"""] } ] },  options: {     legend: { display: false },   title: {    display: true,  text: 'Mail Graph'  }, scales: { yAxes: [{  ticks: { beginAtZero:true              }            }]        }    }});    </script>""")
print("</div>\n</body>\n</html>")

