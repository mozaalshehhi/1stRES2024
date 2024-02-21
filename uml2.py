print("Are you smarter than a 3rd grader!")
play=input("Want to test it out? ").lower()
if play != "yes":
    quit()
print("okay let's start")
score=0

ans=input("4 + 2 + 3 = ")
if ans == "9":
    print("correct :)")
    score+=1
else:
    print("incorrect!")
ans=input("4 x 6 = ")
if ans == "24":
    print("correct :)")
    score += 1
else:
    print("incorrect!")
ans=input("10,000 - 1000 = ")
if ans == "9000":
    print("correct :)")
    score += 1
else:
    print("incorrect!")
ans=input("How many zeros in a million? ")
if ans == "6":
    print("correct :)")
    score += 1
else:
    print("incorrect!")
ans=input("500 + 100 - 100 = ")
if ans == "500":
    print("correct :)")
    score += 1
else:
    print("incorrect!")
ans=input("Rate Moza from 1 to 10 ")
if ans == "10":
    print("correct :)")
    score += 1
else:
    print("incorrect!")
ans=input("0.5 x 100 = ")
if ans == "50":
    print("correct :)")
    score += 1
else:
    print("incorrect!")
if score >=6:
    print("you are smarter than a 3rd graded!")
else:
    print("no you are not smarter than a 3rd grader :(")
print("Done!" + "you got " + str(score) + " as the score! out of 7")


