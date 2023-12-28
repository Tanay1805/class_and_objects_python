class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display(self):
        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self, user):
        print(f"Welcome to the {self.name} quiz, {user.name}!")
        score = 0

        for i, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}:")
            question.display()

            # Handle user input with error checking
            while True:
                try:
                    user_answer = int(input("Your answer (enter the corresponding number): "))
                    if 1 <= user_answer <= len(question.options):
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and", len(question.options))
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if question.check_answer(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print("Incorrect. The correct answer was:", question.correct_option, "\n")

        print(f"Quiz completed! Your score: {score}/{len(self.questions)}")
        user.add_score(self.name, score)

    def display_results(self, user):
        print(f"\nQuiz Results for {user.name}:")
        for quiz_name, score in user.scores.items():
            print(f"{quiz_name}: {score}/{len(self.questions)}")


class User:
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def add_score(self, quiz_name, score):
        self.scores[quiz_name] = score



if __name__ == "__main__":
    question1 = Question("What is the capital of France?", ["Paris", "Berlin", "London"], 1)
    question2 = Question("Which programming language is this program written in?", ["Python", "Java", "C++"], 1)
    question3 = Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe"], 2)

    quiz = Quiz("General Knowledge", [question1, question2, question3])

    user = User(input("Enter your name:"))

    quiz.take_quiz(user)

    quiz.display_results(user)
