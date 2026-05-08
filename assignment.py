#Question 1
coffee_price = 25
cake_price = 40
water_price = 10
coffee_count = 2
cake_count = 1
water_count = 3
# A customer bought 2 coffees, 1 cake, and 3 waters
total_bill=(coffee_price*coffee_count)+(cake_price*cake_count)+(water_price*water_count) 
print(total_bill)
# is_bill > 100
print(total_bill> 100)
print (total_bill==120)

#Increase coffee price by 5 using reassignment.
coffee_price +=5
print(coffee_price)

#Question 2
points= 40
points+=20   #40+20=60
print(points)
points-=10   #60-10=50
print(points)
points*=2     #50*2=100
print(points)
#whether customer is VIP (points >= 100)
is_vip= points>=100
print(is_vip)
#whether customer can get free delivery:
free_delivery= (total_bill>150)or (is_vip)
print(free_delivery)

#Question3
#part A
result= 10+5*2   #20 ضرب ثم جمع
print(result)
result= (10+5)*2  # 30 أقواس ثم ضرب
print(result)
#part B
#B1= True ( true or (false and false) ) الأولوية ل and
# true or false= true 
print(True or False and False)
#B2=  False ((true or false) and false) الاولوية للاقواس
# (true and false)= false  
print ((True or False) and False)
#part C
total_bill = 120
points = 20
premium_member = True
#C1= ( false and false or true) 
#false or true= true
print(total_bill > 150 and points > 50 or premium_member)
#C2 = ( false and ( false or true))
#( false and true)= false
print(total_bill > 150 and (points > 50 or premium_member))