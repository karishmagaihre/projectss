import random 

easy_words = ['cat', 'dog', 'sun', 'book', 'tree']
medium_words = ['python', 'guitar', 'flower', 'mountain', 'ocean']
hard_words = ['xylophone', 'quizzical', 'juxtaposition', 'serendipity', 'antidisestablishmentarianism']
print("Welcome to the password Guessing Game!")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter difficulty level: ").lower()
if level == 'easy':
    secret = random.choice(easy_words)
elif level == 'medium': 
    secret = random.choice(medium_words)
elif level == 'hard':
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level.")    
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password") 

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You've guessed the password '{secret}' in {attempts} attempts!")
        break

    hint = []
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint.append(guess[i])
        else:
            hint.append('_')

    print("Hint: " + ' '.join(hint))
print("Game Over!\n")
