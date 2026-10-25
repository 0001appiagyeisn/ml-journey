import random

secret = random.randint(1,10)
tries = 0

while True:
    
    num = int(input("Guess the number (1-10): "))   
    tries +=1
    if num > secret:
        print("Lower")
    
    elif num < secret:
        print("Higher")
        

    else:
        if tries == 1:
            word ="try"
        else:
            word="tries"
        print(f"Correct you guessed right! Took {tries} {word}")
        
        break

