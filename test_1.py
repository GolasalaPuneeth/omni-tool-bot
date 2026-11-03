import time
import spacy

# 1. Load the English spaCy model
nlp = spacy.load("en_core_web_sm")

# 2. Generate 20 dummy data queries
dummy_queries = [
    "what is the time in london",
    "how is the weather in Tokyo today",
    "flights from Paris to New York",
    "best restaurants in Berlin",
    "what is the capital of Australia",
    "top tourist spots in Brazil",
    "is it raining in Mumbai right now",
    "hotel recommendations in Rome",
    "current population of Canada",
    "what time zone is Tokyo in",
    "cheap hotels in Madrid",
    "distance between Cairo and Dubai",
    "is Toronto safe for tourists",
    "best time to visit Iceland",
    "train schedule from Amsterdam to Brussels",
    "local traditions in Japan",
    "what language is spoken in Mexico",
    "visa requirements for South Korea",
    "museums to visit in Chicago",
    "what is the currency in South Africa"
]

# 3. Track start time
start_time = time.perf_counter()

# 4. Run loop over dummy data
print("--- Entity Recognition Results ---")
for i, text in enumerate(dummy_queries, start=1):
    doc = nlp(text)
    gpe_entities = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    
    print(f"[{i:02d}] Query: '{text}'")
    if gpe_entities:
        for ent_text in gpe_entities:
            print(f"     -> Found Location/Country/City: {ent_text} (Label: GPE)")
    else:
        print("     -> No GPE entity found")

# 5. Track end time & calculate durations
end_time = time.perf_counter()
total_time = end_time - start_time
num_queries = len(dummy_queries)
avg_time = total_time / num_queries

print("----------------------------------")
print(f"Total Execution Time:   {total_time:.4f} seconds")
print(f"Average Execution Time: {avg_time:.6f} seconds per query")
