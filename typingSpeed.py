from time import time
import random as r

def error_count(actual, user):
    error = 0
    min_len = min(len(actual), len(user))
    for i in range(min_len):
        if actual[i] != user[i]:
            error += 1
    error += abs(len(actual) - len(user))
    return error

def calculate_speed(start_time, end_time, user_input):
    time_taken = end_time - start_time
    speed = len(user_input) / time_taken
    return round(speed, 2)

if __name__ == '__main__':
    while True:
        ck = input("Ready to test? (yes/no): ")
        if ck == "yes":
            test_sentences = [
                "Hello this paragraph is a self-contained unit of discourse in writing with a particular point or idea.",
                "My name is Aditya Rai.",
                "Welcome to the Aditya world."
            ]
            test_sentence = r.choice(test_sentences)
            print("***** Typing Speed *****")
            print(test_sentence)
            print()
            start_time = time()
            user_input = input("Enter: ")
            end_time = time()
            print('Speed:', calculate_speed(start_time, end_time, user_input), "w/sec")
            print("Error:", error_count(test_sentence, user_input))
        elif ck == "no":
            print("Thank you.")
            break
        else:
            print("Wrong input.")
