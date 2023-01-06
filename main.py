print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Write your code below this line 👇

you = name1.lower() 
them = name2.lower() 
couple = you + them

T = couple.count("t")
R = couple.count("r")
U = couple.count("u")
E = couple.count("e")

Total_True = T + R + U + E 

L = couple.count("l")
O = couple.count("o")
V = couple.count("v")
E = couple.count("e")

Total_love = L + O + V + E 

TT = str(Total_True)
TL = str(Total_love)

Love_Score = TT + TL

if int(Love_Score) < 10 or int(Love_Score) > 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif int(Love_Score) >= 40 and int(Love_Score) <= 50:
    print(f"Your score is {Love_Score}, you are alright together.") 
else:
    print(f"Your score is {Love_Score}.")



