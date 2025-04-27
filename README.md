# CS50P Quiz Project

#### Video Demo:  <https://youtu.be/LjUv8ENET5M>

#### Description:
This project is a quiz game designed for CS50P to test knowledge of the course content. The game is written in Python and consists of several functions that allow the user to load questions from a CSV file, answer them, and receive feedback on their performance.

### Project Structure:
- `project.py`: This is the main file of the project, and it contains the following functions:
  1. **main()**: The main function that starts the quiz by calling `load_questions()` and `load_number_of_questions()`.
  2. **load_number_of_questions()**: This function prompts the user to enter the number of questions they want to answer (between 1 and 130). It ensures that the input is a valid integer within the specified range.
  3. **load_questions()**: This function loads the quiz questions from a CSV file (`quiz.csv`) and prepares them for the quiz. It uses the `csv.DictReader` to read the questions, and handles new lines within questions properly.
  4. **question_drawing()**: This function randomly selects a subset of questions based on the number specified by the user and runs the quiz. It presents questions to the user, checks their answers, and keeps track of scores and incorrect answers by lecture.
  5. **print_score()**: This function calculates the user's performance in percentage and displays the result. It also shows which lectures the user should review based on incorrect answers.
  6. **print_prize()**: Based on the user's score, this function awards virtual medals using emojis.

- `quiz.csv`: This file contains the quiz questions in CSV format. Each row represents a question with its answer choices and the correct answer.

- `test_project.py`: This file will contain test cases for the project’s functions. For example, `test_load_number_of_questions()` can verify the input handling, while `test_question_drawing()` can verify correct scoring behavior.

- `requirements.txt`: This file lists the external libraries needed for the project:
