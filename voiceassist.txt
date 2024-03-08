def listen_for_command():
    """
    Listens for user input and converts it to text.
    """
    print("Listening... Speak your command:")
    command = input().lower()
    return command

def execute_command(command):
    """
    Executes the user's command based on preferences.
    """
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        # You can add more commands here (e.g., weather, reminders, etc.)
        speak("The current time is 10:30 AM.")
    else:
        speak("I'm sorry, I don't understand that command.")

def speak(text):
    """
    Converts text to speech and prints it.
    """
    print(text)

if __name__ == "__main__":
    while True:
        user_command = listen_for_command()
        if user_command:
            execute_command(user_command)



