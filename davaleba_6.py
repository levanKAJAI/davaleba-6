
# **************  1  **************

# # გენერატორი
# def char_gen(text):
#     for ch in text:
#         yield ch
#
#
# # სიტყვა
# Word = "CODE"
#
# # შესრულება
# for c in char_gen(Word):
#     print(c)



# **************  2  **************

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# index = int(input("შეიყვანე ინდექსი ნომერი: "))
#
# try:
#     print("მონაცემი ინდექსზე", index, "არის:", arr[index])
# except ValueError:
#     print("უნდა შეიყვანო მხოლოდ რიცხვი!")
# except IndexError:
#     print("ასეთი ინდექსი არ არსებობს")



# **************  3  **************

# def counter(func):
#     count = 0
#
#     def deco():
#         nonlocal count
#         count += 1
#         print("გამოძახება:", count)
#         func()
#
#     return deco
#
#
# @counter
# def say():
#     print("Hi")
#
#
# say()
# say()
# say()



# **************  4  **************

# import logging
# import random
#
# # ლოგის ფაილი
# logging.basicConfig(filename="game.log", level=logging.INFO, filemode="a")
#
# operators = ["+", "-", "*", "/"]
# score = 0
#
# for i in range(5):
#     a = random.randint(1, 10)
#     b = random.randint(1, 10)
#     op = random.choice(operators)
#
#     # გაყოფის შემთხვევაში ნულზე გაყოფა არ მოხდეს
#     if op == "/":
#         while b == 0:
#             b = random.randint(1, 10)
#
#     expression = f"{a} {op} {b}"
#     correct = round(eval(expression), 2)
#
#     try:
#         answer = float(input(f"{i + 1}) გამოთვალეთ {expression} = "))
#     except ValueError:
#         print("გთხოვ მხოლოდ რიცხვი შეიყვანეთ.")
#         logging.info(f"{i + 1}) {expression} = araswori formati")
#         continue
#
#     if round(answer, 2) == correct:
#         print("სწორია")
#         score += 10
#         logging.info(f"{i + 1}) {expression} = {answer}  sworia (+10 qula)")
#     else:
#         print(f"არასწორია! სწორი პასუხი იყო {correct}")
#         logging.info(f"{i + 1}) {expression} = {answer} arasworia (swori iyo {correct})")
#
# # შედეგი
# print("\nთქვენი შედეგი:", score, "ქულა")
# logging.info(f"sabolo qula: {score}\n")
# print("ყველა მცდელობა და შედეგი შენახულია game.log ფაილში.")



# **************  5  **************

# import logging
#
# # ლოგის ფაილი
# logging.basicConfig(filename="quiz.log", level=logging.INFO, filemode="w")
#
# # გენერატორი კითხვებისთვის
# def question_gen():
#     questions = [
#         "რა ქვია საქართველოს დედაქალაქს?",
#         "რომელი კონტინენტზე მდებარეობს საქართველო?",
#         "ვინ არის საქრთველო პრეზიდენტი? (2025 წ.)",
#         "რამდენია 5 * 6 ?",
#         "რომელ წელს იყო დიდგორის ბრძოლა?"
#     ]
#     for q in questions:
#         yield q
#
# # დაწყება
# gen = question_gen()
#
# print("Quiz დაიწყო!\n")
# for i, q in enumerate(gen, start=1):
#     ans = input(f"{i}) {q} - ")
#     logging.info(f"Q{i}: {q} | A: {ans}")
#
# print("\nთქვენი პასუხები შენახულია quiz.log ფაილში")


# **************  6  **************

# import random
# import logging
#
# # ლოგის ფაილი
# logging.basicConfig(filename="game.log", level=logging.INFO, filemode="w")
#
# choices = ["ქვა", "მაკრატელი", "ბადე"]
# user_score = 0
# comp_score = 0
# round_num = 1
#
# print("თამაში - 'ქვა, მაკარტელი, ბადე' \nთამაში გრძელდება 3 ქულამდე\n")
#
# while user_score < 3 and comp_score < 3:
#     try:
#         user = input("აირჩიე (ქვა, მაკრატელი, ბადე): ").strip()
#         if user not in choices:
#             raise ValueError("არასწორი არჩევანი")
#     except ValueError as e:
#         print(e)
#         continue
#
#     comp = random.choice(choices)
#     print("კომპიუტერმა აირჩია:", comp)
#
#     if user == comp:
#         result = "ფრე!"
#     elif (user == "ქვა" and comp == "მაკრატელი") or (user == "მაკრატელი" and comp == "ბადე") or (
#             user == "ბადე" and comp == "ქვა"):
#         result = "შენ მოიგე ეს რაუნდი!"
#         user_score += 1
#     else:
#         result = "კომპიუტერმა მოიგო ეს რაუნდი!"
#         comp_score += 1
#
#     print(result)
#     print(f"მიმდინარე ანგარიში: თქვენი {user_score} - {comp_score} კომპიუტერი\n")



# **************  7  **************

# import random
#
# def roll_dice():
#      return random.randint(1, 6)
#
# print("კამათლის თამაში\n")
#
# while True:
#     # ორივე აგორებს კამათელს
#     g1 = roll_dice()
#     g2 = roll_dice()
#
#     print(f"Gamer 1 გააგორა: {g1}")
#     print(f"Gamer 2 გააგორა: {g2}")
#
#     # ფრე
#     if g1 == g2:
#         print("ფრეა! თავიდან ვაგორებთ!\n")
#         continue
#
#     # გამარჯვებული ვინ არის
#     if g1 > g2:
#         winner, loser = "Gamer 1", "Gamer 2"
#     else:
#         winner, loser = "Gamer 2", "Gamer 1"
#
#     print(f"გამარჯვებულია: {winner} ")
#
#     # კითხვა თამაშის გაგრძელებაზე
#     while True:
#         choice = input(f"{winner}, გინდა მისცე კიდევ შანსი {loser}-ს? (კი/არა): ").strip().lower()
#         if choice in ["კი", "არა"]:
#             break
#         else:
#             print("გთხოვთ უპასუხოთ მხოლოდ 'კი' ან 'არა'.")
#
#     if choice == "არა":
#         print("თამაში დასრულდა")
#         break
#     else:
#         print("თამაში გრძელდება...\n")



# **************  8  **************

# import random
#
# # 10 სიტყვა
# words = [
#     "კომპიუტერი", "ინტერნეტი", "პროგრამირება", "მონაცემები", "დედამიწა",
#     "ბიბლიოთეკა", "წიგნი", "ვეფხვისტყაოსანი", "პროგრამა", "ანბანი"
# ]
#
# # შემთხვევით ავიღოთ 2 სიტყვა
# chosen = random.sample(words, 2)
#
# masked = []
# for word in chosen:
#     if len(word) > 2:
#         # შემთხვევით 2 ასო ამოვაგდოთ
#         start = random.randint(0, len(word) - 2)
#         masked_word = word[:start] + "_" * 2 + word[start+2:]
#         masked.append(masked_word)
#     else:
#         masked.append(word)
#
# print("გამოიცანი ეს სიტყვები: ")
# for i, w in enumerate(masked, start=1):
#     print(f"სიტყვა {i}: {w}")
#
# # მომხმარებლის პასუხები
# guess1 = input("სიტყვა 1: ").strip()
# guess2 = input("სიტყვა 2: ").strip()
#
# # შედეგის შემოწმება
# correct = 0
# if guess1 == chosen[0]:
#     correct += 1
# if guess2 == chosen[1]:
#     correct += 1
#
# # საბოლოო შედეგი
# if correct == 2:
#     print("გამარჯვება!")
# elif correct == 1:
#     print("50%")
# else:
#     print("დამარცხდი")
