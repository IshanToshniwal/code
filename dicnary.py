# dict = {'name': 'ishan', 'place': 'india', 'age': 11}
# dict2 = {
#     'name': 'ishan',
#     'place': 'india',
#     'age': 11}
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get('name'))
# print('place' in dict)
# dict['name'] = 'ishan toshniwal'
# dict.update({'name': 'ishan t'})
# dict.update({'black': 'color'})
# dict['green'] = 'color'
# dict.pop('name')
# del dict['place']
# dict.clear()
# del dict
# print(dict)


# homework 1 dic
# mcq_data = {
#     "What is the capital of India?": (["A) Delhi", " B) Mumbai", "C) Kolkata", "D) Chennai"], "A"),
#     "Which planet is closest to the sun?": (["A) Venus", "B) Earth", "C) Mercury", "D) Mars"], "C"),
#     "What is the largest mammal in the world?": (["A) Rhino", "B) Elephant", "C) Whale", "D) Giraffe"], "C")
# }
#
#
# score = 0
# for question, (choices, answer) in mcq_data.items():
#     print(question)
#     for choice in choices:
#         print(choice)
#     user_answer = input("Enter your answer (A/B/C/D): ").upper()
#     if user_answer == answer:
#         print("Correct!")
#         score += 1
#     else:
#         print("Incorrect. The correct answer is", answer)
# print("Your final score is:", score, "/", len(mcq_data))