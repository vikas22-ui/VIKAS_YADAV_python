import time
import random

def quiz_game():
    questions = [
        {"question": "What is the capital of France?", "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"], "answer": "C"},
        {"question": "Which programming language is known as the language of AI?", "options": ["A. Python", "B. Java", "C. C++", "D. Ruby"], "answer": "A"},
        {"question": "What is 5 + 7?", "options": ["A. 10", "B. 12", "C. 14", "D. 15"], "answer": "B"},
        {"question": "What is the largest planet in our solar system?", "options": ["A. Mars", "B. Earth", "C. Jupiter", "D. Saturn"], "answer": "C"},
        {"question": "Who wrote 'Hamlet'?", "options": ["A. Charles Dickens", "B. William Shakespeare", "C. J.K. Rowling", "D. Mark Twain"], "answer": "B"}
    ]
    
    random.shuffle(questions)  
    score = 0
    time_limit = 10 
    
    print("Welcome to the Quiz Game!")
    
   
    predefined_answers = [q["answer"] for q in questions]
    
    for i, q in enumerate(questions):
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        start_time = time.time()
        user_answer = predefined_answers[i].upper()  
        end_time = time.time()
        
        print(f"Your answer: {user_answer}")
        
        if end_time - start_time > time_limit:
            print("Time's up! No points awarded.")
        elif user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")
    
    print(f"\nGame Over! Your score: {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent! You got all the answers correct!")
    elif score >= len(questions) // 2:
        print("Good job! You did well!")
    else:
        print("Better luck next time! Keep practicing!")

if __name__ == "__main__":
    quiz_game()
