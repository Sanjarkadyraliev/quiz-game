from _ctypes_test import func

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]
def new_game():
    question_num = 1
    guesses = []
    correct_answer = 0
    for key in questions:
        print(key)
        print("_________")
        for el in options[question_num -1]:
            print(el)
        print("_________")
        guess = input("Please enter answer (A, B, C, D)").upper()
        if len(guess) > 1:
                print("You should enter one symbol")
                guess = input("Please enter answer (A, B, C, D)").upper()
        #elif type(guess) == int or float:
                #print(" Invalid entry, try again: ")
                #guess = input("Please enter answer (A, B, C, D)").upper()
        elif len(guess) == 1 and type(guess) == str:
                guess = input("Please enter answer (A, B, C, D)").upper()
        guesses.append(guess)
        correct_answer += check_answer(questions.get(key), guess)
        question_num +=1
        display_score(correct_answer, len(guesses))



def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
def display_score(correct_ans, guesses):
    total = (correct_ans / guesses) * 100
    print("Your total score is",total, "%" )
def play_again():
    response = input("Do you wanna play again:(yes or no) : ").upper()
    if response == "Yes":
        return True
    elif response == "No":
        return False
new_game()

def main():
    while play_again():
        new_game()
        print("Bye bye")







