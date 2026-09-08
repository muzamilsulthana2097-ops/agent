import re
import urllib.parse
import urllib.request


def get_vid(query)

    try:
         encode = urllib.parse.quote(query)

         ur1 = (
               "https://www.youtube.com/results"
               "?search_query=" +encode
         )

          request = urllib.request.Request(
              url,
              headers=(
                      "User- Agent": Mozilla/5.0"
              }
         )

          data = urllib.request.urlopen(
              request,
              timeout=5
              
