import random
import json
import nltk
import string
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

with open('intents.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def clean_text(text):
    from nltk.tokenize import wordpunct_tokenize
    tokens = wordpunct_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

def match_intent(user_input):
    cleaned_input = clean_text(user_input)
    best_match = {"intent": None, "score": 0}

    for intent in data['intents']:
        for pattern in intent['patterns']:
            cleaned_pattern = clean_text(pattern)
            score = len(set(cleaned_input) & set(cleaned_pattern))
            if score > best_match["score"]:
                best_match["intent"] = intent
                best_match["score"] = score

    if best_match["intent"]:
        return random.choice(best_match["intent"]['responses'])
    else:
        return "I'm not sure how to respond to that. Try asking something else."

def start_chatbot():
    print("\U0001F916 ChatBot: Hi! I'm your friendly chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Bye! Have a great day! \U0001F60A")
            break
        response = match_intent(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    start_chatbot()
