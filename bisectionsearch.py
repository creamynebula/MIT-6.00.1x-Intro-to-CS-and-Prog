print("Please think of a number between 0 and 100!\nIs your secret number 50?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
ans = str(input())
low, high, guess = 0, 100, 50

while ans != 'c':
    if ans != ('h' or 'l' or 'c'):
        print("Sorry, I did not understand your input.\n" + "Is your secret number " + str(guess) + "?\n" +
              "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        ans = str(input())
    if ans == 'h':
        high = guess
    elif ans == 'l':  # ans = 'l'
        low = guess
    guess = int((high+low)/2.0)
    print("Is your secret number " + str(guess) +
          "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    ans = str(input())

print("Game over. Your secret number was:", str(guess))
