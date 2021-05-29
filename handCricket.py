import random
import time
import pyttsx3
import speech_recognition as sr

# Initial score and toss (default = False (Computer Wins))
score = 0
toss = False

# Toss choices True - User Wins, False - Computer Wins
tossChoices = [True, False]

# Possible score (1 to 6 runs)
numbers = [1, 2, 3, 4, 5, 6]

# Dictionary for voice input
numbersChoices = {
    1: 1,
    "one": 1,
    "won": 1,
    "own": 1,
    "in": 1,
    2: 2,
    "two": 2,
    "too": 2,
    "to": 2,
    "tu": 2,
    "tow": 2,
    "twoo": 2,
    "true": 2,
    3: 3,
    "three": 3,
    "tree": 3,
    "try": 3,
    "tri": 3,
    "free": 3,
    4: 4,
    "four": 4,
    "for": 4,
    "floor": 4,
    "flour": 4,
    "flower": 4,
    "fow": 4,
    "flow": 4,
    "core": 4,
    5: 5,
    "five": 5,
    "fi": 5,
    "pi": 5,
    "why": 5,
    "my": 5,
    6: 6,
    "six": 6,
    "sex": 6,
    "sx": 6,
}

# Choice of batting or bowling by person who wins toss
battingOrBowling = ["bat", "bowl"]

# Default value of batsman
currentBatsman = ""

# Toss
toss = random.choice(tossChoices)

# Text to speech conversion
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# Voice recognition using microphone
def recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now!")
        speak("Speak Now!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        choice = r.recognize_google(audio)
        if choice:
            print("You said: " + choice)
            speak("You said: " + choice)
            return choice
        else:
            return False
    except sr.UnknownValueError:
        print("Sorry! I Could not understand.")
        speak("Sorry! I Could not understand.")
        return False
    except sr.RequestError as e:
        print("Error {0}".format(e))
        speak("Error {0} occured!".format(e))
        return False


def compare(computerGuess, userGuess):
    # print(int(computerGuess), int(userGuess))
    return int(computerGuess) == int(userGuess)


def play(currentBatsman):
    global score
    notOut = True
    while notOut:
        validGuess = False
        computerGuess = random.choice(numbers)
        # print(computerGuess)
        userGuess = recognition()

        # Check whether user's input is actually valid
        for key, value in numbersChoices.items():
            if key == userGuess.lower():
                userGuess = value
                validGuess = True
                # print(userGuess)
                break

        # If user's input is valid, check with computers guess
        # If same then out, otherwise add to batsman's score
        if validGuess:
            if compare(computerGuess, userGuess):
                print("Batsman is out")
                speak("Batsman is out")
                print(f"Final Score: {score} runs")
                speak(f"Final Score: {score} runs")
                score = 0
                notOut = False
                return notOut
            else:
                print(f"Batsman has hit {userGuess} run(s)")
                speak(f"Batsman has hit {userGuess} run(s)")
                score += int(userGuess)
                print(f"Score: {score}")
                speak(f"Score: {score}")


if toss == False:
    print("Toss is won by the Computer!")
    speak("Toss is won by the Computer!")
    print("Computer is deciding...")
    speak("Computer is deciding...")
    if random.choice(battingOrBowling) == "bat":
        print("Computer chose batting...")
        speak("Computer chose batting...")
        currentBatsman = "computer"
        play(currentBatsman)
    else:
        print("Computer chose bowling...")
        speak("Computer chose bowling...")
        currentBatsman = "user"
        play(currentBatsman)
else:
    print("Toss is won by the User!")
    speak("Toss is won by the User!")
    print("User has to decide...")
    speak("User has to decide...")
    print("Speak bat or bowl...")
    speak("Speak bat or bowl...")

    userChoice = recognition()
    if userChoice == "bat" or userChoice == "but":
        print("User chose batting...")
        speak("User chose batting...")
        currentBatsman = "computer"
        while True:
            if play(currentBatsman) == False:
                break
    else:
        print("User chose bowling...")
        speak("User chose bowling...")
        currentBatsman = "user"
        while True:
            if play(currentBatsman) == False:
                break