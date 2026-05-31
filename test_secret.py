import os

# 1. Fetch the key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# 2. Check if the key exists
if api_key:
    # Print only the first few characters to verify it exists safely
    print(f"✅ Success! API key found. Starts with: {api_key[:7]}...")
else:
    print("❌ Error: OPENAI_API_KEY environment variable is missing.")
