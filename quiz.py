import random

# Placeholder quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    # Add more questions...
]

def get_random_question():
    return random.choice(quiz_data)

def present_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")

def start_quiz():
    question = get_random_question()
    present_question(question)
    user_choice = input("Select your answer (1, 2, 3, 4, ...): ")

    if user_choice.isdigit() and 1 <= int(user_choice) <= len(question["options"]):
        selected_option = question["options"][int(user_choice) - 1]
        if selected_option == question["correct_answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", question["correct_answer"])
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    start_quiz()
