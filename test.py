import time
from sentence_transformers import SentenceTransformer, util

# 1. Load the lightweight and highly accurate transformer model
# Run `pip install sentence-transformers` in your terminal first if you haven't.
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Define prototype/anchor sentences for each category as raw strings
category_anchors = {
    "time": "what time is it clock schedule hours duration",
    "weather": "what is the weather climate temperature rain forecast hot cold",
    "currency": "money currency exchange rate dollars rupees price cost convert",
    "logical": "why how reason logic explanation cause proof",
    "math": "calculate add multiply solve equation mathematics numbers arithmetic compute algebra geometry",
    "ai": "artificial intelligence machine learning llm gpt chatbot neural network deep learning model",
    "music": "song track playlist artist album singer concert audio melody sound",
    "dbpedia": "wikipedia info history biography definition fact encyclopedia summary details background knowledge"
}

categories = list(category_anchors.keys())
anchor_texts = list(category_anchors.values())

# Pre-encode anchor sentences once for optimal performance
anchor_embeddings = model.encode(anchor_texts, convert_to_tensor=True)

def classify_intent(text, threshold=0.40):
    # Encode the incoming user text query
    query_embedding = model.encode(text, convert_to_tensor=True)
    
    # Compute cosine similarity against all category anchor embeddings
    cos_scores = util.cos_sim(query_embedding, anchor_embeddings)[0]
    
    # Find the highest scoring category
    best_score_idx = cos_scores.argmax().item()
    highest_similarity = cos_scores[best_score_idx].item()
    
    # If the match is too weak, fallback to 'others'
    if highest_similarity < threshold:
        return "others"
        
    return categories[best_score_idx]

# --- Expanded Test Cases covering AI and Math ---
test_inputs = [
    "whats time in india",
    "whats climate in tirupathi",
    "how much is 100 dollars in rupees",
    "why is the sky blue",
    "what is 45 multiplied by 12 and solved for x",
    "calculate the square root of 144",
    "how do large language models and transformers work",
    "what is artificial intelligence and machine learning",
    "play some relaxing jazz songs",
    "tell me a brief history of Albert Einstein from wikipedia",
    "completely unrelated random sentence"
]

# --- Start Timer ---
start_time = time.perf_counter()

print("--- Dynamic Semantic Classification Results (SentenceTransformers) ---")
for i, user_input in enumerate(test_inputs, start=1):
    result = classify_intent(user_input)
    print(f"[{i:02d}] Input: '{user_input}' --> Output: {result}")

# --- End Timer & Convert to Milliseconds ---
end_time = time.perf_counter()
total_time_ms = (end_time - start_time) * 1000
avg_time_ms = total_time_ms / len(test_inputs)

print("-" * 60)
print(f"Total Execution Time:   {total_time_ms:.2f} ms")
print(f"Average Execution Time: {avg_time_ms:.2f} ms per query")
