### still needs to be edited

from datetime import datetime
from zoneinfo import ZoneInfo
from geonamescache import GeonamesCache
import spacy

# Load models into RAM once at startup
nlp = spacy.load("en_core_web_sm")
gc = GeonamesCache()

# Pre-build lookup map
CITY_MAP = {
    info["name"].lower(): (info["name"], info["timezone"])
    for info in gc.get_cities().values()
}


def get_time_spacy(sentence: str) -> str:
  doc = nlp(sentence)

  # Extract entities labeled GPE (Geopolitical Entity: cities, countries, states)
  locations = [
      ent.text.strip().lower() for ent in doc.ents if ent.label_ in ("GPE", "LOC")
  ]

  if not locations:
    return "No location detected."

  target_location = locations[0]

  if target_location in CITY_MAP:
    city_name, tz_str = CITY_MAP[target_location]
    local_time = datetime.now(ZoneInfo(tz_str))
    return f"Time in {city_name}: {local_time.strftime('%I:%M %p %Z')}"

  return f"Location '{target_location}' not found in city database."


# # --- Test Cases ---
# print(get_time_spacy("What's the time in London right now?"))
# # Output: Time in London: 11:37 AM GMT

# print(get_time_spacy("Is it late in chennai?"))
# # Output: Time in Hyderabad: 05:07 PM IST