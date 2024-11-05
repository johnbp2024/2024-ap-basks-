#ask user for their name
username = input("what is your name? ")
#ask user for their favorate number (integer)
fav_num = int(input("what is your favorate number? "))
#doble halve and square the users favorate number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num
#greet the user
print(f"hi {username},your favorate number is {fav_num}" )
#output results of dobling halving and squaring their favorate integer
print (f"double {fav_num} is {double}" )
print (f"halve {fav_num} is {halve}")
print (f"{fav_num} squared is {square}")
print()
print("have a nice day")