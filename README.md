# Hotel-AI-Chatbot


In this project, I have developed a sophisticated chatbot using Python that leverages natural language processing techniques and deep learning with TensorFlow. The chatbot is designed to interact with users, understand their queries, and provide relevant responses in a conversational manner. The key components and functionalities of this project are outlined below:
Data Processing and Model Building:
The project begins with loading intents data from a JSON file and organizing it into lists for patterns and responses.
Data preprocessing steps include removing punctuation, converting text to lowercase, tokenizing, and padding the sequences for model input.
The model architecture consists of an embedding layer, LSTM layer for sequence processing, and dense layer for classification.
The model is compiled with appropriate loss and optimizer functions for training.
Training and Evaluation:
The model is trained on the preprocessed data for 200 epochs to learn patterns and associations between input text and corresponding tags.
Training progress is visualized through plots showing accuracy and loss metrics over epochs.
Chatbot Functionality:
The chatbot interface is implemented using Tkinter, providing a user-friendly GUI for interaction.
Users can input queries through a text entry field, and the chatbot responds with relevant answers based on the trained model.
The chat history is displayed in the GUI, allowing users to track the conversation flow.
User Experience and Feedback:
The chatbot greets users, prompts for their name, and engages in a personalized conversation.
Upon completion of the chat, users are prompted to provide feedback through a feedback form.
Feedback responses are recorded in a CSV file for further analysis and improvement of the chatbot experience.
