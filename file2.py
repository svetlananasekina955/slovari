
import random
def get_random_letter(n):
    return random.choices([chr(i) for i in range(ord("а"), ord("я"))], k=n)


first_letters = get_random_letter(10)
second_letters = get_random_letter(10)
print(first_letters)
print(second_letters)

first_dictionary = dict(enumerate(first_letters))
second_dictionary = dict(enumerate(second_letters))
print(first_dictionary)
print(second_dictionary)