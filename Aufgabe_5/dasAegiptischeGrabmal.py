listOfBlocks = []

userInput = -1
print("Bitte geben sie  Steinblock zeiten ein falls fertig geben sie fertig ein ")
while (userInput != "fertig"):
    userInput = input()
    if userInput.isdigit() == True:
        listOfBlocks.append(userInput)
print(listOfBlocks)