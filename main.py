#!/usr/bin/python3

def play_round(category, answers):
    print("-" * 30)
    print(f"Category: {category}")
    print(f"There are {len(answers)} answers.")
    print("-" * 30)

    score = 0
    guessed_answers = set()
    wrong_attempts = 0
    max_wrong_attempts = 5

    while wrong_attempts < max_wrong_attempts:
        guess = input(f"Wrong attempts: {wrong_attempts}/{max_wrong_attempts}. Your guess: ")
        guess_lower = guess.lower()

        if guess_lower in guessed_answers:
            print("Already guessed!")
            continue

        found_match = False
        for answer, points in answers.items():
            if guess_lower == answer.lower():
                print(f"Correct! {answer} is worth {points} points.")
                score += points
                guessed_answers.add(answer.lower())
                found_match = True
                break

        if not found_match:
            print("Incorrect.")
            wrong_attempts += 1

        if len(guessed_answers) == len(answers):
            print("-" * 30)
            print("You found all the answers!")
            break

    print("-" * 30)
    print(f"Round score: {score}")
    return score


# Game data (Multiple categories)
game_data = {
    "Top 10 Car Brands": {
        "Toyota": 25,
        "Honda": 22,
        "Ford": 20,
        "Chevrolet": 18,
        "BMW": 15,
        "Mercedes-Benz": 14,
        "Audi": 12,
        "Hyundai": 10,
        "Nissan": 9,
        "Kia": 8,
    },
    "Top 5 Phone Brands": {
        "Apple": 20,
        "Samsung": 18,
        "Google": 15,
        "OnePlus": 12,
        "Xiaomi": 10,
    },
    "Top 5 Places to Visit (India)": {
        "Taj Mahal": 20,
        "Goa": 18,
        "Kerala": 15,
        "Rajasthan": 12,
        "Varanasi": 10,
    },
}

while True: #Game loop
    print("-" * 30)
    print("Choose a category:")
    for i, category in enumerate(game_data.keys()):
        print(f"{i + 1}. {category}")
    print("-" * 30)

    while True: #Category input loop
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

    print("-" * 30)
    print(f"Game over! Total score for {selected_category}: {total_score}")
    print("-" * 30)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break #End the game loop