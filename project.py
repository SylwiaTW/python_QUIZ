import csv
import random
import emoji
from pyfiglet import Figlet

def main():
    num_questions = load_number_of_questions()
    questions = load_questions("quiz.csv")
    run_quiz(questions, num_questions)


def load_number_of_questions():
    f = Figlet(font="standard")
    print(f.renderText("CS50P quiz"))

    while True:
        try:
            k = int(input(f"\033[1mHow many questions would you like to answer?\033[0m\n"))
            if 1 <= k <= 130:
                return k
            else:
                print(f"You should type number from 1 to 130")
        except ValueError:
            print(f"You should type number from 1 to 130")


def load_questions(filename):
    questions = []
    with open(filename, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            row['Question'] = row['Question'].replace("\\n", "\n")
            questions.append(row)
    return questions


def run_quiz(questions, num_questions):
    score = 0
    sampled_questions = random.sample(questions, num_questions)
    incorrect_lectures = {}

    for i, question in enumerate(sampled_questions, 1):
        print_question(question, i)
        answer = get_valid_answer()

        if check_answer(answer, question['answer']):
            score += 1
            print(f"Correct answer {emoji.emojize(':OK_hand:')} Score: {score}\n")
        else:
            incorrect_lectures = update_incorrect_lectures(incorrect_lectures, question['Lecture'])
            print(f"Wrong answer {emoji.emojize(':disappointed_face:')} Score: {score}\n")

    percentage = calculate_percentage(score, num_questions)
    print_score(percentage, incorrect_lectures)
    print_prize(percentage)

def print_question(question, number):
    print(f"\033[1m{number}.{question['Question']}\033[0m\nA: {question['A']}\nB: {question['B']}\nC: {question['C']}\nD: {question['D']}\n")


def get_valid_answer():
    while True:
        answer = input("Your answer: ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("You should type A, B, C or D. Try again!")


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def update_incorrect_lectures(incorrect_lectures, lecture):
    if lecture in incorrect_lectures:
        incorrect_lectures[lecture] += 1
    else:
        incorrect_lectures[lecture] = 1
    return incorrect_lectures


def calculate_percentage(score, total_questions):
    return (score / total_questions) * 100


def print_score(percentage, incorrect_lectures):
    print(f"\033[1mTest result: {percentage}% \033[0m\nYou should review:")
    sorted_lectures = sorted(incorrect_lectures.items(), key=lambda item: item[1], reverse=True)

    for lecture, _ in sorted_lectures:
        print(lecture[3:])


def print_prize(percentage):
    if percentage > 90:
        print(f"Congratulations! 1st prize medal: {emoji.emojize(':1st_place_medal:')}\n")
    elif percentage > 80:
        print(f"Very good! 2nd prize medal: {emoji.emojize(':2nd_place_medal:')}\n")
    elif percentage > 70:
        print(f"Nicer! 3rd prize medal: {emoji.emojize(':3rd_place_medal:')}\n")
    else:
        print(f"You don't win any prize {emoji.emojize(':disappointed_face:')}")

if __name__ == "__main__":
    main()
