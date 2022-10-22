"""Automated Test Checker

This script allows the user to quickly correct school exams, giving them
fast acess to the results, including score, hit rate and
all the wrong answers with their respective options.

Made by DOUGZ ;)
"""

# imports
from sys import argv
from datetime import date
from utils import get_test_results, get_file_answers

# check for invalid usage
if len(argv) != 2:
    print(
        "\33[1;31mInvalid Usage!\33[3m \
        \nTry: python3 check.py [EXAM_NAME]\33[m"
    )
    exit(1)

# get data from the provided files
exam = get_file_answers(f"gabaritos/{argv[1]}.txt")
usr_data = get_file_answers("user_input.txt")

# exit if a file was not found
if (exam is None) or (usr_data is None):
    print("\33[1;33mError! File not found :/\33[m")
    exit(2)

# exit if the number of answers on both lists does not match
elif len(exam) != len(usr_data):
    print(
        "\33[1;33mWarning! \
        \nNumber of answers and questions does not match!\33[m"
    )
    exit(3)

# get the results of the exam
results = get_test_results(exam, usr_data)

# store results on text file
with open(f"results_{argv[1]}.txt", "w") as output:

    # write exam data into file
    output.write(
        f"<-- {argv[1].replace('.txt', '').upper()} --> \
        \nData: {date.today().strftime('%d/%m/%Y')} \
        \nAcertos: {results['correct']} de {len(exam)} questões \
        \nTaxa de acertos: {results['rate']:.2f}% das questões\n"
    )

    # writes wrong answers and correct options (if there are any)
    if results["wrong"]:
        output.write("=" * 22 + "\nVocê errou as questões:\n")

        for quest, answer in results["wrong"].items():
            output.write(f"{quest:0>2}º) {answer}\n")
