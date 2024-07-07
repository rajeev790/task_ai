import openai
import nltk
from textblob import TextBlob
import matplotlib.pyplot as plt

openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to interact with GPT-3 model


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Adjust the engine based on your preference
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'positive'
    elif sentiment < 0:
        return 'negative'
    else:
        return 'neutral'
  
 # Function to generate visualization
def generate_visualization(sentiment_distribution):
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [sentiment_distribution['positive'], sentiment_distribution['negative'], sentiment_distribution['neutral']]
    colors = ['gold', 'lightcoral', 'lightskyblue']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Sentiment Distribution')
    plt.show()

# Main function to run the program
def main():
    conversation_history = []
    sentiment_distribution = {'positive': 0, 'negative': 0, 'neutral': 0}

    print("Welcome to the Conversation Generator!")

while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        # Generate response
        prompt = '\n'.join(conversation_history + [f"You: {user_input}"])
        response = generate_response(prompt)

        # Perform sentiment analysis
        sentiment = analyze_sentiment(response)
        sentiment_distribution[sentiment] += 1

        # Display response
        print("AI: ", response)

        # Update conversation history
        conversation_history.append(f"AI: {response}")
        conversation_history.append(f"You: {user_input}")

    # Generate visualization of sentiment distribution
    generate_visualization(sentiment_distribution)

if _name_ == "_main_":
    main()