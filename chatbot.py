while True:
    raw_input = input('You: ')
    clean_input = raw_input.lower().strip()
    if clean_input == "hello":
        print("Bot: Hi there! How can I help you today?")
    elif clean_input == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I'm sorry, I don't understand that.")