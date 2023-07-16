import json
import random
#import re
#import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download NLTK data (if not already downloaded)
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')

# Load the intents JSON file
with open('intents.json') as file:
    intents = json.load(file)

# Create lists of patterns and responses for each intent
patterns = []
responses = []
tags = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize the pattern and remove stop words
        tokens = word_tokenize(pattern)
        tokens = [token.lower() for token in tokens if token not in stopwords.words('english')]
        # Lemmatize the tokens
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        # Add the pattern and tag to the lists
        patterns.append(tokens)
        tags.append(intent['tag'])
        responses.append(intent['responses'])


# Define a function to process user input and generate a response
def generate_response(input_text):
    # Tokenize the input and remove stop words
    tokens = word_tokenize(input_text)
    tokens = [token.lower() for token in tokens if token not in stopwords.words('english')]
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Find the best match for the user input
    best_match_tag = None
    best_match_score = 0
    for i in range(len(patterns)):
        pattern_tokens = patterns[i]
        score = sum([1 for token in tokens if token in pattern_tokens])
        if score > best_match_score:
            best_match_tag = tags[i]
            best_match_score = score

    # Select a random response for the best match tag
    if best_match_tag is not None:
        response = random.choice(responses[tags.index(best_match_tag)])
    else:
        response = "I'm sorry, I don't understand what you're saying."

    return response


# Start the chatbot
print("\nWELCOME TO OUR HOTEL!! \nI'm your A.I. Assistant let me know what can I do for you.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = generate_response(user_input)
    print("Bot: " + response)

# Ask for feedback
print("\nThank you for using our chatbot. Please provide your feedback:")
print("1. Worst")
print("2. Bad")
print("3. Average")
print("4. Good")
print("5. Very Good")
print("6. Outstanding")

feedback = input("Your Feedback (1/2/3/4/5/6): ")

# Process feedback and provide response
if feedback == "1":
    print("We apologize for your worst experience. Please let us know how we can improve.")
elif feedback == "2":
    print("We apologize for any inconvenience caused. Please let us know how we can improve.")
elif feedback == "3":
    print("Thank you for your feedback. We will work towards improving our services.")
elif feedback == "4":
    print("Thank you for your feedback. We are glad you had a good experience.")
elif feedback == "5":
    print("Thank you for your feedback. We are thrilled you had a very good experience.")
elif feedback == "6":
    print("Thank you for your feedback. We are delighted you had an outstanding experience.")
else:
    print("Invalid feedback. Thank you for using our chatbot.")