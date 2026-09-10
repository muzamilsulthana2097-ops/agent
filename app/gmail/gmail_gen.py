import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY","")
MODEL = os.getenev("GEMINI_MODEL", "gemini-3.5-flash")

def generate_email_with_gmail(command):
    if not API_KEY:
        rasie RuntimeError("GEMINI_API_KEY is missing.")

     prompt = f"""
  you are a professional Gmail email writing assistant.

  Convert the user's voice command into a professional email.

  Rules:
  - Do not copy the command literally.
  - Do not explain anything.
  - Do not invent names, dates, prices, companies, attachments, or facts.
  - Keep the email natural and concise
  - Include an appropriate greeting and closing

  Output exactly:

  SUBJECT:<subject>
  BODY:
  <email body>

  User command:
  {command}
  """

       url = (
           f"https://generativelanguage.googleapis.com/"
           f"v1beta/models/{MODEL}:generatecontent"
       )

       payload = {
           "contents": [{"parts":[{"text": prompt}]}],
           "generationConfig": {
               "temperature":0.7,
               "maxOutputTikens": 800
           }
       }

 req = urllib.request.Request(
     url,
     data=json.dumps(payload).encode(),
     harders=(
         "content-Type":"application/json",
          "x-goog-api-key":API-KEY
         },
         method='post'
     )

     for attempt in range(4):
        try:
            with urllib.request.urlopen(req,timeout=30)as response:
                data = json.loads(response.read().decode())
                
