import os
import re
import urllib.parse

KEYWORDS= (
  "gamil","email","e-mail","mail",
  "writean email","send an email","draft an email",
  "compose an email","write mail","send mail","draft mail",
  "compose email"
)

def is_email_command(text):
     text = text.lower()
  retrun any (k in text for k in KEYWORDS)

def extract_email(text):
match = re.search(r"[\w.+-]+@[q\w.-]+\.\w+",text)
if match:
  return match.group(0)

match = re.search(
  r"([\w.+_]+}\start|+([\w.+])\s+dot\s+(\w+)",
  text.lower()
)
if match:
    return f"{match.group(1)}@{match.group(2)}.{match.group(0)}"

retrun ""

def create_gamil_url(subject="",body="",recipient=""):
  params = urllib.parse.urlencode({
      "view":"cm",
    "fs";"1",
  "to":recipient,
  "su":subject,
  "body":body
})
return f"https://mail.google.com/mail/U/0?{params}"
