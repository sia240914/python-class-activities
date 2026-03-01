# 1) Import the required modules:
#    a) Import `random` to generate a random number.
#    b) Import `time` to add delays using `sleep()`.

# 2) Generate a random integer between 1 and 100 using `random.randint(1, 100)`
#    and store it in `number`.
#    (This will be the secret number to guess.)

# 3) Define a function `intro()` to introduce the game:
#    a) Ask the user for their name.
#    b) Declare `name` as a global variable so it can be used outside the function.
#    c) Take the input and store it in `name`.
#    d) Print a welcome message and tell the user the number is between 1 and 100.
#    e) Check if the secret `number` is even or odd using `% 2`:
#       - If even, set `x = 'even'`
#       - Else, set `x = 'odd'`
#    f) Print whether the secret number is even or odd.
#    g) Add small delays using `time.sleep()` and then ask the user to start guessing.

# 4) Define a function `pick()` that runs the guessing process:
#    a) Initialize `guessesTaken = 0` to count how many guesses the player makes.

# 5) Use a `while` loop that runs until the user has taken 6 guesses:
#    a) Add a small delay using `time.sleep(.25)`.
#    b) Ask the user to enter a guess and store it in `enter`.

# 6) Validate the guess using a `try` block:
#    a) Convert `enter` into an integer and store it in `guess`.
#    b) Check if `guess` is within the range 1 to 100.

# 7) If the guess is in range (1 to 100):
#    a) Increase `guessesTaken` by 1.
#    b) If `guessesTaken < 6`, compare the guess with the secret number:
#       i) If `guess < number`, print "too low".
#       ii) If `guess > number`, print "too high".
#       iii) If `guess != number`, print "Try Again!" after a short delay.
#       iv) If `guess == number`, stop the loop using `break`.

# 8) If the guess is out of range:
#    a) Print a message saying the number is not in range.
#    b) Ask the user again to enter a number between 1 and 100.

# 9) Use an `except` block to handle invalid input (non-numeric):
#    a) Print a message saying the entered value is not a number.

# 10) After the guessing loop ends:
#     a) If `guess == number`, print a success message with the user's name
#        and the number of guesses taken.
#     b) If `guess != number`, print the correct secret number.

# 11) Create a variable `playagain = "yes"` to start the game loop.

# 12) Use a `while` loop to allow replaying the game:
#     a) Repeat while `playagain` is "yes", "y", or "Yes".
#     b) Call `intro()` to show game introduction.
#     c) Call `pick()` to run the guessing game.
#     d) Ask the user if they want to play again and store the response in `playagain`.