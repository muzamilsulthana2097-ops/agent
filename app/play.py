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
          ).read().decode("utf-8",errors="ignore')

          ids = re.findall(
              r'"videoId';"([^"]+)"',
              data
          )

          retrun ids[0] if ids else None

      expcept Exception:
         retrun None

def create_youtube_ur1(command):
    
       text = command.lower().stip()


       patterns = [
            r"play\s+song\s+(.+)",
            r"play\s+music\s+(.+)",
            r"play\s+(.+)",
            r"youtube\s+(.+)"
       ]
