import random
import string
import nltk
from nltk.stem import WordNetLemmatizer

# Download only what you need
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# === Predefined responses ===
greetings = ['hi', 'hello', 'hey', 'greetings']
farewells = ['bye', 'goodbye', 'see you', 'farewell']

greeting_responses = ['Hello!', 'Hi there!', 'Hey!', 'Greetings!']
farewell_responses = ['Goodbye!', 'See you later!', 'Bye!', 'Take care!']
fallback_responses = [
    "I'm not sure I understand.",
    "Could you rephrase that?",
    "Interesting! Tell me more...",
    "Let's talk about something else."
]

# === Function to preprocess input ===
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = text.split()  # Split by space
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

# === Generate chatbot response ===
def generate_response(user_input):
    tokens = preprocess(user_input)
    
    if any(word in tokens for word in greetings):
        return random.choice(greeting_responses)
    elif any(word in tokens for word in farewells):
        return random.choice(farewell_responses)
    elif 'how' in tokens and 'you' in tokens:
        return "I'm just a bot, but I'm doing fine! How about you?"
    elif 'name' in tokens:
        return "I'm a simple chatbot created with Python!"
    else:
        return random.choice(fallback_responses)

# === Chat loop ===
print("Chatbot: Hi! Type 'bye' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
        print("Chatbot: Goodbye! 👋")
        break
    response = generate_response(user_input)
    print("Chatbot:", response)
