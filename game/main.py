
import random

print(''' Welcome to the Number Guessing Game !
       Chechk your Brain power. Engineer
      I have Selected A Number Abb Teri Baarri
      Try to guess it . Kamm sai kamm attempts mai !\n''')


random_guess=random.randint(1,100)
attempts =0

while True:
    guess=int(input("Thora soch or pheli chance mai done krr chal number daal : "))
    attempts +=1

    if guess<random_guess:
        print("Are yr Thora kamm ho gya ")
    elif guess>random_guess:
        print("bhai kyy krr rha hai jayada guess krr diya ")
    else:
        print(f"Sbhash tune to {attempts} mai guess krr diya ")
        break


        