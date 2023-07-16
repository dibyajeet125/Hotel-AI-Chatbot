import json
import random
import tkinter as tk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download NLTK data (if not already downloaded)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

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


# Create a Tkinter-based GUI for the chatbot
class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hotel A.I. Assistant")
        self.window.geometry("800x500")
        self.create_widgets()
        self.show_welcome_message()

    def create_widgets(self):
        self.chat_history = tk.Text(self.window, height=20, width=90)
        self.chat_history.pack(pady=10)
        self.user_input = tk.Entry(self.window, width=80)
        self.user_input.pack(pady=10)
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack()
        self.quit_button = tk.Button(self.window, text="Quit", command=self.quit)
        self.quit_button.pack()

    def show_welcome_message(self):
        self.chat_history.insert(tk.END, "Bot: WELCOME TO OUR HOTEL!! I'm your A.I. Assistant let me know what can I do for you.\n")

    def send_message(self):
        user_input = self.user_input.get()
        self.chat_history.insert(tk.END, "You: " + user_input + "\n")
        self.chat_history.insert(tk.END, "Bot: " + generate_response(user_input) + "\n")
        self.user_input.delete(0, tk.END)

    def quit(self):
        self.window.destroy()
        self.show_feedback_form()

    def show_feedback_form(self):
        feedback_window = tk.Tk()
        feedback_window.title("Feedback Form")
        feedback_window.geometry("500x400")
        feedback_label = tk.Label(feedback_window, text="Thank you for using our chatbot. Please provide your feedback:")
        feedback_label.pack(pady=10)
        feedback_options = [("Worst", "1"), ("Bad", "2"), ("Average", "3"), ("Good", "4"), ("Very Good", "5"), ("Outstanding", "6")]
        feedback_var = tk.StringVar()
        for option_text, option_value in feedback_options:
            tk.Radiobutton(feedback_window, text=option_text, variable=feedback_var, value=option_value).pack()
        submit_button = tk.Button(feedback_window, text="Submit", command=lambda: self.submit_feedback(feedback_window, feedback_var.get()))
        submit_button.pack(pady=10)

    def submit_feedback(self, feedback_window, feedback):
        feedback_window.destroy()
        if feedback == "1":
            feedback_response = "We apologize for your worst experience. Please let us know how we can improve."
        elif feedback == "2":
            feedback_response = "We apologize for any inconvenience caused. Please let us know how we can improve."
        elif feedback == "3":
            feedback_response = "Thank you for your feedback. We will work towards improving our services."
        elif feedback == "4":
            feedback_response = "Thank you for your feedback. We are glad you had a good experience."
        elif feedback == "5":
            feedback_response = "Thank you for your feedback. We are thrilled you had a very good experience."
        elif feedback == "6":
            feedback_response = "Thank you for your feedback. We are delighted you had an outstanding experience."
        else:
            feedback_response = "Invalid feedback. Thank you for using our chatbot."
        self.show_feedback_response(feedback_response)

    def show_feedback_response(self, feedback_response):
        feedback_response_window = tk.Tk()
        feedback_response_window.title("Feedback Response")
        feedback_response_window.geometry("500x400")
        feedback_response_label = tk.Label(feedback_response_window, text=feedback_response)
        feedback_response_label.pack(pady=10)

    def run(self):
        self.window.mainloop()

# Start the chatbot GUI
chatbot_gui = ChatbotGUI()
chatbot_gui.run()
