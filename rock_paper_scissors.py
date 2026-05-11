import pyttsx3                      # for text-to-speech
import random                       # for random computer choice

# Initialize engine only once (important fix)
engine = pyttsx3.init()

def speak(text):                    # Function to speak the given text
    engine = pyttsx3.init()                  
    engine.say(text)
    engine.runAndWait()

def rps():                          # Welcome function for the game
    speak("Welcome to Rock Paper Scissors!")
    print("Welcome to Rock, Paper, Scissors!")

rps()                               # call welcome function

youDict = {"rock": 1, "paper": 2, "scissors": 3}
reversedict = {1: "rock", 2: "paper", 3: "scissors"}

while True:                         # Infinite loop to keep game running

    computer = random.randint(1, 3)

    try:
        youstr = input("\nEnter your choice (rock, paper, scissors) or 'exit': ").lower()
    except KeyboardInterrupt:
        print("\nGame interrupted!")
        speak("Game interrupted")
        break

    if youstr == "exit":
        print("Good Game 👋")
        speak("Good Game")
        break

    if youstr not in youDict:
        print("Invalid input!")
        speak("Invalid input!")
        continue

    you = youDict[youstr]

    print("Computer chose:", reversedict[computer])

    if computer == you:
        print("Tie!")
        speak("Tie!")

    elif (computer == 1 and you == 2) or \
         (computer == 2 and you == 3) or \
         (computer == 3 and you == 1):
        print("You win!")
        speak("You win!")

    else:
        print("You lose!")
        speak("You lose!") 