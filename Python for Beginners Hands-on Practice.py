# Basics of Python

# Question: 01

# Installation

# Question: 2

name = "Eric"
print(f"Hello {name}, Would you like to learn some python today?")

# Question: 3

name = "John"
print(name.upper())               #It will print the uppercase of string 
print(name.lower())               #It will print the lowercase of string
print(name.capitalize())          #It will change starting character from Uppercase and print it the whole string as same as original string 

# Question: 4

print('Albert Einstein once said,"A person who never made a mistake never tried anything new."')

# Question: 5
famous_person = "Henry"
quote = 'once said,"A person who never made a mistake never tried anything new."'
message= f"{famous_person} {quote}"
print(message)

# Question: 6

name="\n\tJack\n\t"
print(name)                 #It will print in new line and give some spaces.
print(name.strip())         #It will remove spaces and print just in new line

# Question: 7 & 8

print(5+3)    # +              #Add two values
print(10-2)   # -              #Subtract two values
print(4*2)    # *              #Multiply two values
print(16//2)  # //            #Divide two values


# Question: 9

fav_number=7
print("My favourite number is",fav_number)


# Question: 10     

# How to use comments 

# Question: 11

names=["Jack","John","Henry","David"]                  #Accessing each elements from the list
print(names[0])                                       #Print each elements from the list
print(names[1])
print(names[2])
print(names[3])

# Question: 12

print(f"Hello {names[0]}, How was your day?")                    #Print each elements with some text
print(f"Hello {names[1]}, How was your day?")
print(f"Hello {names[2]}, How was your day?")
print(f"Hello {names[3]}, How was your day?")

# Question: 13

fav_transportation=["Honda Motorcycle","BMW Car"]               #Print each choice with some text
for fav_ in fav_transportation:
    print(f"I would like to own a {fav_}")
   

# Question: 14

guest_lst=["Yousuf","Ali Raza","Ahmed"]                         #Print a message to each person, inviting them to dinner
for guest in guest_lst:
    print(f"Dear {guest}, Join us for dinner?")
print("*" * 65)


# Question: 15                                                     #You heared one person is not coming you invite another person and ask for dinner

print(f"Ohh! {guest_lst[1]} is not coming")                     #One person is not coming     
print("*" * 65)
guest_lst[1]="Owais Zafar"                                      #replace it                                                     

for guest in guest_lst:
     print(f"Dear {guest} Dinner at mine? Join me!")            #send messages all of them
print("*" * 65)

# Question: 16

print("I'have found a bigger dinner table!!")                         #I have found a bigger dinner table
print("*" * 65)

guest_lst.insert(0,"Umar")                                            #Add more members in a list
guest_lst.insert(2,"Qambar")
guest_lst.append("Asad")
  
for guest_ in guest_lst:                                            
    print(f"Dear {guest_} Join me for a delightful dinner at my place soon!!")           #Messages all of them to invite a dinner
print("*" * 65)

# Question: 17 

print("Sorry I can invite only two people for dinner!!")                                 #I can invite only two members
print("*" * 65)
print(guest_lst[5],"Sorry i cant invite you to dinner")                                  #And inform everone 
guest_lst.pop()
print(guest_lst[4],"Sorry i cant invite you to dinner")
guest_lst.pop()
print(guest_lst[3],"Sorry i cant invite you to dinner")
guest_lst.pop()
print(guest_lst[2],"Sorry i cant invite you to dinner")                                 #Now we have two members on the list
guest_lst.pop()

print("*" * 65)
                                                                          

for guest in guest_lst:                                                                 #Inform two members you are still invited
    print(guest,"You are still invited")

guest_lst.remove("Umar")                                                                #Remove all elements from the list Now List is empty
guest_lst.remove("Yousuf")


# Question: 18 

fav_places=["Makkah","Madina","US","Germany","Australia"]                               #Store elements from an array but make sure its not alphabetical order
print(fav_places)

fav_places.sort()
print(fav_places)                                                                       #Sorting the elements

fav_places=["Makkah","Madina","US","Germany","Australia"]                               #reverse the elements
fav_places.reverse()
print(fav_places)

fav_places=["Makkah","Madina","US","Germany","Australia"]              
print(fav_places)

fav_places.reverse()                                                                    #reverse the elements
print(fav_places)

fav_places.sort()                                                                       #Sorting the elements
print(fav_places)

fav_places.sort(reverse=True)                                                           #Sorting the elements in reverse order
print(fav_places)


# Question: 19

print("6 members are invited initially")


# Question: 20

cities=["Karachi","Lahore","KPK","Multan","Islamabad"]

# Question: 21

objects=[5,8,5.0,3.0,"string",True,False]                                      #These all are objects string,float,string,boolean


# Question: 22
error=["Owais","Ahmed","Zain","Sooman"]
#error[5]                                                                       #It gives an error because in list we have only 4 elements,list out of range

print(error[0])                                                                #It gives Owais because Owais is in list and indexing at 0


# Question: 23
                                        
car="Subaru"                                                             
print(car == "Subaru")
print("Subaru" == car)

if car=="Subaru":
    print(True)
else:
     print(False)

print(car != "owais")
print(not car=="Suburu")


print(car == "car")                                                                                     
print(car != "Subaru")

if car == "car":
     print(True)
else:
     print(False)

print("Subaru" != car)
print(not car == "Subaru")

# Question: 24

a="Car"
b="Car"
print(a == b)
print(a.lower()== b.upper())                                  #logical Operators and Comparison Operators

a=5
b=10

print(a!=b)
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==5 and b==10)
print(a==5 or b==15)

check=[5,7,2,5.0] 
print(5 in check)
print(10 in check)


# Question: 25

alien_color=["green","yellow","red"]                              #Check green in list or not
if "green" in alien_color:
    print("Player just earned 5 points")


if "yellow" in alien_color:
    print("Player just earned 5 points")                         #If yellow in alien_color so it will be executed else it will not executed
else:
    print("Player just earned 10 points")

# Question: 26

if "green" in alien_color:                                       #If green in an array wo if statment will be executed
    print("Player just earned 5 points")


if "green" not in alien_color:
    print("Player just earned 10 points")


if "green" in alien_color:                                       #If green in an array wo if statment will be executed otherwise else will be executed          
    print("if statement will be executed")

else:
    print("if green not in alien_color so else will be executed")


if "orange" in alien_color:                     
    print("if statement will be executed")

else:
    print("if orange not in alien_color so else will be executed")


# Question: 27

if "green" in alien_color:                                                          
    print("Player earned just 5 points")
else:
    print("else in not executed because green is present in alien_color")

if "yellow" in alien_color:
    print("Player earned just 10 points")
else:
    print("else in not executed because yellow is present in alien_color")

if "red" in alien_color:
    print("Player earned 15 points")

else:
    print("else in not executed because red is present in alien_color")


# Question: 28

person = 25

if person < 2:
    print("The person is baby")

elif 2 <= person < 4:
    print("The person is a toodler")

elif 4 <= person < 13:
    print("The person is a kid")

elif 13 <= person < 20:
    print("The person is a teenager")

elif 20 <= person < 65:
    print("The person is a adult")

elif person >= 65:
    print("The person is an elder")

# Question: 29
    
favourite_fruits=["Apple","Banana","peach"] 

if "Apple" in favourite_fruits:
    print("I like Apple")

if "Banana" in favourite_fruits:
    print("I like Banana")

if "peach" in favourite_fruits:
    print("I like peach")

if "Watermelon" not in favourite_fruits:
    print("I like Watermelon")

if "lychee" not in favourite_fruits:
    print("I like Lychee")


# Question: 30
    
users=["Admins","Eric","Holand","David","Henry",]
for i in users:
    if i==users[0]:
        print(f"Hello {i},would you like to see a status report")       
    
    else:
        print(f"Heloo {i},thankyou for logging in again")


# Question: 31

check=[]                                                          #Check if list is empty or not
if check==[]:
    print('We need to fine some users!!')

# Question: 32

current_users=["Owais","Yousuf","Ahmed","Ali","Shariq"]           #Check if user  in current users list and new user list so print Enter a new username 
new_users=["Hashir","Hassin","Owais","Yousuf","Umar"]             #else print username is available
    
for i in new_users:
    if i in current_users:
        print("Enter a new username")
    else:
        print("Username is available")


# Question: 33

numbers = [1,2,3,4,5,6,7,8,9]                                     #Print 1st 2nd 3rd instead of numbers
for i in numbers:
    if i == numbers[0]:
        print("1st")
    if i == numbers[1]:
        print("2nd")
    if i == numbers[2]:
        print("3rd")
    if i == numbers[3]:
        print("4th")
    if i == numbers[4]:
        print("5th")
    if i == numbers[5]:
        print("6th")
    if i == numbers[6]:
        print("7th")
    if i == numbers[7]:
        print("8th")
    if i == numbers[8]:
        print("9th")

# Question: 34

pizza_name=["Chicken Tikka","Hot King","Showarma"]
for i in pizza_name:
    print(f"I like {i} Pizza!")

print("I really love Pizza!!")

# Question: 35

animals=["Tiger","Dog","Cat"]
for i in animals:
    print(f"A {i} would make a great pet")              

print("These animals are very dangerous for their enemies")


# Question: 36

def make_shirt(size,text):
    print(f"The size of your shirt is {size}. And the text printed on the shirt is {text}.")      

make_shirt("Large","SuperMan")


# Question: 37

def shirt(size="large", message="I love Python"):
    if size == "large":
        print(f"Making a large shirt with message: {message}")
    elif size == "Medium":
        print(f"Making a medium shirt with message: {message}")
    else:
        print(f"Making a {size} shirt with a message: {message}")

shirt()                                           # Large shirt with default message
shirt("Medium")                                   # Medium shirt with default message
shirt("Small", "I reaaly like Python")            # Small shirt with a different message

# Question: 38

def describe_city(city,country="Pakistan"):
    print(f"{city} is in {country}.")

describe_city("Karachi")
describe_city("Lahore")
describe_city("Sydney","Australia")

# Question: 39

def city_country(city,country):
    print(city,country)

city_country('"karachi,','Pakistan"')
city_country('"Sydney,','Australia"')
city_country('"Mumbai,','India"')


# Question: 40

#1st Method

def make_album(artist_name, album_title, num_tracks=None):
    album_info = {
        'artist': artist_name,
        'title': album_title
    }
    if num_tracks:
        album_info['tracks'] = num_tracks
    return album_info

#Create three dictionaries representing different albums

album1 = make_album('Taylor Swift', '1989')
album2 = make_album('The Beatles', 'Abbey Road', 17)            # An album with a specified number of tracks
album3 = make_album('Ed Sheeran', 'Divide')

#Print each album's information

print(album1)
print(album2)
print(album3)


#2nd Method

def make_album(**kwargs):
    print(kwargs)


make_album(artist = "Taylor swift",title = "1898")
make_album(artist = "The Beatles",title = "Abbey Road", tracks = 17)  
make_album(artist = "Ed Sheeran", title = "Divide")

# Question: 41

def show_magicians(array):
    for i in array:
        print(i)
    print("*" * 30)

#Original List
magician_names=["Ahmed","Yousuf","Asad"]

print("Your original list:")
print("*" * 30)                                             #easy to understand output
print(magician_names)
print("*" * 30)
show_magicians(magician_names)


# Question: 42

def make_great(array):
    for i in range(len(array)):
        magician_names[i] = "The Great " + magician_names[i]


make_great(magician_names)

print("Your updated list:")
print("*" * 30)
#Updated list
print(magician_names)
print("*" * 30)


# Question: 43

def great(array):
    for i in array:
        print(i)


great(magician_names)
print("*" * 30)


# Question: 44

def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)
    print("Sandwich is ready!\n")
    print("*" * 40)

#Call the function with different numbers of arguments
make_sandwich("Turkey", "Lettuce", "Tomato")
make_sandwich("Ham", "Cheese")
make_sandwich("Peanut Butter", "Jelly", "Banana", "Honey")


# Question: 45

def keyword(**kwargs):
    print("Your items:")
    
    print(kwargs)
    
keyword(Manufacturer="Toyota",Model="2022",Colour="White")











        
   
































