#!/usr/bin/python3
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(category, answers_left, score, wrong_attempts, max_wrong_attempts):
    print("-" * 40)
    print(f"{'Category:':<15} {category}")
    print(f"{'Answers left:':<15} {answers_left}")
    print(f"{'Score:':<15} {score}")
    print(f"{'Attempts left:':<15} {max_wrong_attempts - wrong_attempts}")
    print("-" * 40)

def play_round(category, answers):
    score = 0
    guessed_answers = [""] * len(answers)
    wrong_attempts = 0
    max_wrong_attempts = 5
    answers_left = len(answers)
    revealed_answers = {}

    while wrong_attempts < max_wrong_attempts and answers_left > 0:
        clear_screen()
        display_header(category, answers_left, score, wrong_attempts, max_wrong_attempts)

        print("Correct Answers:")
        for i, answer in enumerate(guessed_answers):
            print(f"{i+1}. {answer or '_' * len(list(answers.keys())[i]) + ' '}")
        print("-" * 40)

        guess = input("Your guess (or 'reveal <number>' to reveal an answer): ")
        guess_lower = guess.lower()

        if guess_lower.startswith("reveal "):
            try:
                answer_number = int(guess_lower.split()[1]) - 1
                if 0 <= answer_number < len(answers):
                    if guessed_answers[answer_number] == "":
                        answer = list(answers.keys())[answer_number]
                        reveal_cost = len(answer.split()) * 5
                        if score >= reveal_cost:
                            score -= reveal_cost
                            guessed_answers[answer_number] = answer
                            answers_left -= 1
                            revealed_answers[answer] = reveal_cost
                            print(f"{answer} revealed (cost: {reveal_cost}).")
                        else:
                            print("Not enough points to reveal this answer.")
                    else:
                        print("That answer has already been revealed.")
                else:
                    print("Invalid answer number.")
            except (ValueError, IndexError):
                print("Invalid reveal command. Use 'reveal <number>'.")
            continue

        if guess_lower in [x.lower() for x in guessed_answers if x != ""]:
            print("Already guessed!\n")
            continue

        found_match = False
        for i, answer in enumerate(answers):
            answer_words = answer.lower().split()
            guess_words = guess_lower.split()

            correct_word_count = 0
            for word in guess_words:
              if word in answer_words:
                correct_word_count +=1
            
            if correct_word_count >= len(answer_words) * 0.5:
                print(f"Correct! {answer} is worth {answers[answer]} points.\n")
                score += answers[answer]
                guessed_answers[i] = answer
                answers_left -= 1
                found_match = True
                break

        if not found_match:
            print("Incorrect.\n")
            wrong_attempts += 1

    clear_screen()
    display_header(category, 0, score, wrong_attempts, max_wrong_attempts)

    print("Guessed Answers:")
    for i, answer in enumerate(guessed_answers):
        if answer:
            print(f"- {answer}")

    print("\nAnswers You Missed:")
    missed_answers = [answer for answer in answers if answer not in guessed_answers]
    for answer in missed_answers:
        print(f"- {answer}")

    print("-" * 40)
    print(f"{'Round score:':<15} {score}")

    if revealed_answers:
        print("\nRevealed Answers:")
        for answer, cost in revealed_answers.items():
            print(f"- {answer} (cost: {cost})")

    print("-" * 40)
    print("Bye!")
    return score


game_data = {
    "Things that are Red": {
        "Apple": 10,
        "Strawberry": 10,
        "Cherry": 10,
        "Tomato": 10,
        "Rose": 10,
        "Ruby": 10,
        "Firetruck": 10,
        "Stop Sign": 10,
        "Blood": 10,
        "Redwood": 10,
    },
    "Foods that Start with the Letter 'P'": {
        "Pizza": 10,
        "Pasta": 10,
        "Potato": 10,
        "Pancake": 10,
        "Pineapple": 10,
        "Pecan": 10,
        "Peanut": 10,
        "Pear": 10,
        "Pomegranate": 10,
        "Pumpkin": 10,
    },
    "Animals that Live in the Jungle": {
        "Tiger": 10,
        "Monkey": 10,
        "Elephant": 10,
        "Snake": 10,
        "Gorilla": 10,
        "Jaguar": 10,
        "Toucan": 10,
        "Sloth": 10,
        "Orangutan": 10,
        "Chimpanzee": 10,
    },
    "Ice Cream Flavors": {
        "Vanilla": 10,
        "Chocolate": 10,
        "Strawberry": 10,
        "Mint": 10,
        "Cookies and Cream": 10,
        "Rocky Road": 10,
        "Coffee": 10,
        "Chocolate Chip Cookie Dough": 10,
        "Pistachio": 10,
        "Butter Pecan": 10,
    },
    "Fruits": {
        "Apple": 10,
        "Banana": 10,
        "Orange": 10,
        "Grape": 10,
        "Strawberry": 10,
        "Watermelon": 10,
        "Mango": 10,
        "Pineapple": 10,
        "Blueberry": 10,
        "Raspberry": 10,
    },
}

while True:
    clear_screen()
    print("-" * 40)
    print("Choose a category:")
    for i, category in enumerate(game_data.keys()):
        print(f"{i + 1}. {category}")
    print("-" * 40)

    while True:
        try:
            choice = int(input("Enter your choice (1-{}): ".format(len(game_data))))
            if 1 <= choice <= len(game_data):
                break
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_category = list(game_data.keys())[choice - 1]
    total_score = 0
    total_score += play_round(selected_category, game_data[selected_category])

    clear_screen()
    display_header(selected_category, 0, total_score, 0, 0)
    print("-" * 40)
    print(f"{'Game over! Total score for':<25} {selected_category}: {total_score}")

    print("\nAll Answers:")  # New section for all answers
    for answer in game_data[selected_category]:
        print(f"- {answer}")

    print("-" * 40)  # Separator
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
