import random
letters=['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 
         'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't',
         'u', 'v','w', 'x','y', 'z','A', 'B', 'C', 'D', 'E', 
         'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5','6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '&', '*', '(',')','+','?',
         '/','<','>','~','-','_','=']
print("Welcome to password Generator")
t_letters=int(input("How many letters you want to Generate?\n"))
t_numbers=int(input("How many numbers you want to Generate?\n"))
t_symbol=int(input("How many symbol you want to Generate?\n"))
password_list=[]
for i in range(1,t_letters+1):   #1,2,3,4
    char=random.choice(letters)
    password_list+=char
for i in range(1,t_numbers+1):   #1,2,3,4
    char=random.choice(numbers)
    password_list+=char
for i in range(1,t_symbol+1):   #1,2,3,4
    char=random.choice(symbols)
    password_list+=char
if len(password_list) <8:
    print("password must be at least 8 characters long.")
print(password_list)

#random.shuffle(password_list)
#print(password_list)
#password=""
#for char in password_list:
#    password+=char
#print(password)