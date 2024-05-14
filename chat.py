from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ["I'm good, thank you!", "I'm doing well."]),
    (r'what is your name', ["You can call me Chatbot.", "I'm Chatbot!"]),
    (r'quit', ['Bye!', 'Goodbye!', 'See you later.']),
    # Additional patterns and responses
    (r'how can I help you', ["You can ask me about anything!", "I'm here to assist you."]),
    (r'weather', ["I'm just a chatbot and don't have weather information."]),
    (r'tell me about yourself', ["I'm a chatbot created using NLTK.", "I'm here to chat with you!"]),
    (r'favorite food', ["I don't eat, but I like data bytes!"]),
    (r'how old are you', ["I don't have an age. I'm a digital creation!"]),
    (r'thank you', ["You're welcome!", "Anytime!"]),
    (r'i need help', ["Sure, I'll do my best to assist you."]),
    (r'(.)(good|great|fine)(.)', ["That's good to hear!", "Awesome!"]),
    (r'(.)(bad|not good)(.)', ["I'm sorry to hear that.", "Hope things get better!"]),
    (r'what can you do', ["I can chat with you, answer questions, or tell jokes!"]),
    (r'who created you', ["I was created by an AI developer.", "My creator prefers to stay anonymous."]),
    (r'(.)(joke|funny)(.)', ["Why don't scientists trust atoms? Because they make up everything!", "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"]),
    (r'(.*)', ["I'm not sure I understand.", "Could you please rephrase that?", "Let's talk about something else."]),
     r'tell me a joke': ["Why don't scientists trust atoms? Because they make up everything!", 
                       "What do you get when you cross a snowman and a vampire? Frostbite!"],
    r'how old are you': ["I don't have an age. I'm a chatbot!", "I exist in the virtual world, so no age for me."],
    r'what is the time': ["I don't have access to real-time data like the current time."],
    r'thank you': ["You're welcome!", "No problem!"],
    r'': ["Hmm, I'm not sure what you mean.", "Could you ask me something else?"]]

# Create a chatbot with the patterns and reflections
chatbot = Chat(patterns, reflections)

# Start chatting with the user
print("Chatbot: Hi, I'm Chatbot. How can I help you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() == 'quit':
        break
