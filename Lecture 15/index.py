def quiz_game():
    questions = {
        "What is the capital of France?": {
            "options": ["A) Paris", "B) London", "C) Berlin"],
            "answer": "A"
        },
        "What is 2 + 2?": {
            "options": ["A) 3", "B) 4", "C) 5"],
            "answer": "B"
        },
        "What is the color of the sky?": {
            "options": ["A) Blue", "B) Green", "C) Red"],
            "answer": "A"
        }
    }

    score = 0

    for question, data in questions.items():
        print(question)
        for option in data["options"]:
            print(option)
        answer = input("Your answer (A, B, C): ").strip().upper()

        if answer == data["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer was:", data["answer"])

    print(f"\nYour final score is {score}/{len(questions)}.")


if __name__ == "__main__":
    quiz_game()
