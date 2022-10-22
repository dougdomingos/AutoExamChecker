"""
This module contains all the utilitary functions used on "check.py" script.
All these functions are listed bellow:

- get_file_answers: Given a filename, opens said file and returns the
  answers within it

- get_test_results: Given two lists, compares each item of both and returns the
  results into a dictionary
"""


def get_file_answers(filename: str):
    """Extracts data from provided text file.

    Args:
        filename (string): Name of the file for data extraction

    Returns:
        list: a list containing all the answers within the file
        None: if no file is found, return will be None
    """

    # open file for reading
    try:
        with open(filename, "r") as data_file:

            data = list()

            # filters unnecessary characters
            for item in data_file:
                data.append(item.replace("\n", "").upper())

    except FileNotFoundError:
        return None

    else:
        return data


def get_test_results(buffer_exam: list, buffer_user: list):
    """Get test results by comparing the answers from both files.

    Args:
        buffer_exam (list): a list with the answers of the exam
        buffer_user (list): a list with the answers of the user

    Returns:
        results (dict): a dictionary containing three values:
        - "correct": number of correct answers
        - "rate": percentage of correct answers
        - "wrong": a dictionary with all the wrong answers and
          their correct options
    """

    results = {"correct": 0, "rate": 0.0, "wrong": dict()}

    # compares each answers from the lists
    for index in range(0, len(buffer_exam)):

        # if they are the same, increases points by 1
        if buffer_exam[index] == buffer_user[index]:
            results["correct"] += 1

        # otherwise, stores the question number and correct answer
        else:
            results["wrong"][str(index + 1)] = buffer_exam[index]

    # calculate the percentage of correct answers
    results["rate"] = results["correct"] / len(buffer_exam) * 100

    return results
