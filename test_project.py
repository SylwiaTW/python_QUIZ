from project import print_score, print_prize, check_answer, calculate_percentage, update_incorrect_lectures
import emoji

def main():
    test_check_answer()
    test_calculate_percentage()
    test_update_incorrect_lectures()
    test_print_score()
    test_print_prize()

def test_check_answer():
    assert check_answer('A', 'A') == True
    assert check_answer('B', 'A') == False

def test_calculate_percentage():
    assert calculate_percentage(5, 10) == 50
    assert calculate_percentage(9, 10) == 90

def test_update_incorrect_lectures():
    lectures = {}
    updated_lectures = update_incorrect_lectures(lectures, 'Lecture 1')
    assert updated_lectures['Lecture 1'] == 1

    updated_lectures = update_incorrect_lectures(updated_lectures, 'Lecture 1')
    assert updated_lectures['Lecture 1'] == 2

def test_print_score():
    assert print_score(80, {}) == None

def test_print_prize():
    assert print_prize(91) == None
