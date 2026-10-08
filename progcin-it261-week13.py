def initialize_game():
    """Sets up the initial game state, welcome message, and player name."""
    print("=" * 40)
    print("      WELCOME TO THE PYTHON TRIVIA GAME!      ")
    print("=" * 40)
    player_name = input("Enter your name to begin: ").strip()
    print(f"\nHello, {player_name}! Let's test your knowledge.\n")
    return player_name


def ask_questions():
    """Defines the questions and collects the user's answers."""
    # List of dictionaries holding questions, options, and the correct answer key
    questions = [
        {
            "prompt": "What is the extension of Python source files?",
            "options": ["A) .pt", "B) .py", "C) .pyt", "D) .python"],
            "answer": "b"
        },
        {
            "prompt": "Which keyword is used to define a function in Python?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "c"
        },
        {
            "prompt": "Which data type is immutable in Python?",
            "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
            "answer": "d"
        }
    ]
    
    user_answers = []
    
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['prompt']}")
        for option in q['options']:
            print(f"  {option}")
        
        answer = input("Your answer (A/B/C/D): ").strip().lower()
        user_answers.append(answer)
        print("-" * 30)
        
    return questions, user_answers


def check_answers(questions, user_answers):
    """Compares user answers against correct answers and calculates the score."""
    score = 0
    
    for i in range(len(questions)):
        correct_answer = questions[i]["answer"]
        if user_answers[i] == correct_answer:
            score += 1
            
    return score


def display_score(player_name, score, total_questions):
    """Outputs the final results and performance summary."""
    print("\n" + "=" * 40)
    print("              FINAL RESULTS               ")
    print("=" * 40)
    print(f"Player: {player_name}")
    print(f"You scored {score} out of {total_questions}.")
    
    percentage = (score / total_questions) * 100
    if percentage == 100:
        print("Rating: Excellent! Perfect score! 🌟")
    elif percentage >= 50:
        print("Rating: Good job! Well played! 👍")
    else:
        print("Rating: Keep practicing! You'll get them next time. 💪")
    print("=" * 40)


def main():
    """Driver function that controls the overall game loop."""
    # 1. Initialize the game
    name = initialize_game()
    
    # 2. Ask questions and get user answers
    questions, user_answers = ask_questions()
    
    # 3. Check answers and get the final score
    score = check_answers(questions, user_answers)
    
    # 4. Display the score
    display_score(name, score, len(questions))


# Program entry point
if __name__ == "__main__":
    main()
