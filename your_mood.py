# mood_responses.py

def mood_response(mood):
    """Return a custom response based on the user's mood."""
    mood = mood.lower().strip()
    
    responses = {
        'happy': "That's great to hear! Keep smiling!",
        'sad': "I'm sorry you're feeling down. I hope things get better!",
        'excited': "Fantastic! Enjoy the excitement!",
        'angry': "Take a deep breath. It's important to stay calm.",
        'bored': "Maybe try something new or take a break!",
    }
    
    return responses.get(mood, "I'm not sure how to respond to that mood. Maybe try another one?")
