#Ask the user to enter marks for these 5 courses
#Check if the student passed or failed the course.
Math= int (input("enter math mark "))
if Math >=50:
    print("pass")
else:
    print("fail")

Science= int (input("enter science mark "))
if Science>= 50:
    print("pass")
else:
    print("fail")

History= int (input("enter history mark "))
if History >= 50:
    print("pass")
else:
    print("fail")

Geography= int (input("enter geography mark "))
if Geography >=50:
    print("pass")
else:
    print("fail")

English= int (input("enter english mark "))
if English >=50:
    print("pass")
else:
    print("fail")
#Calculate the final average percentage.
total= Math+ Science+ History+ Geography+ English
average= (total/500)*100
print(average)
#Check the final grade:
if average>=85:
    print("Excellent")
if 75<=average<=84:
    print("Very Good")
if 65<=average<=74:
    print("Good")
if 50<=average<=64:
    print("Pass")
if average<50:
    print("Fail")
#The student can join the competition if:
join_competition= (average>=85 and Math>=80) or (average<85 and Math>=90)
if (average>=85 and Math>=80) or (average<85 and Math>=90):
    print("can_join")
else:
    print("can't join")