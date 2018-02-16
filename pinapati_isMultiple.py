import random

firstNumber=random.randint(1,10000)
print("Randomly generated number is:" +str(firstNumber))
secondNumber=int(input("give me the secondnumber:"))
if firstNumber % secondNumber==0:
    print("yes")
else:
        print("no")
        
