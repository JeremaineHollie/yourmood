# main.py

import mood_responses

def main():
    """Main function to interact with the user."""
    mood = input("How are you feeling today? ")
    response = mood_responses.mood_response(mood)
    print(response)

if __name__ == "__main__":
    main()
