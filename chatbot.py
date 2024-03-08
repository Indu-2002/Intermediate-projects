import random

def get_response(user_input):
    patterns = {
        "hi": ["Hello!", "Hi there!", "Hey!"],
        "how are you": ["I'm good, thank you!", "I'm doing well, how about you?"],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "name": ["I'm just a chatbot, but you can call me ChatGPT.", "I don't have a name, but you can call me ChatBot!"],
        "weather": ["I'm afraid I don't have real-time weather information.", "You can check a weather website for the current conditions."],
        "age": ["I don't have an age. I'm just a computer program.", "I was created recently, so I'm quite young!"],
        "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm still learning!"],
    }

    # Check if any pattern is present in the user's input
    for pattern, responses in patterns.items():
        if pattern in user_input.lower():
            return random.choice(responses)

    # If no specific pattern matches, use a default response
    return random.choice(patterns["default"])

# Now the chatbot is ready to respond to user input
print("Bot: Hi! I'm your chatbot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ").lower()
    
    if user_input == 'exit':
        print("Bot: Goodbye! Have a great day.")
        break
    
    response = get_response(user_input)
    print(f"Bot: {response}")
