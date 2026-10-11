
# This is a comment in python (simple and clean)
"""
This is a multi-line comment in python (simple and clean)
It goes on for multiple lines and can be used to provide more detailed explanation 
"""
first_name = "Alice" 
last_name = "Smith"
user_age = 25
is_student = True


#For numbers 
5 * 5
total = 10 - 7 

#For strings 
string = "My name is Dave"

my_long_string = """This is a long string that can span multiple lines.
It can be useful for writing long paragraphs of text or documentation."""
first_name = "Daniel"
last_name = "Fajuyi"

full_name = first_name + " " + last_name
long_dash = "-" * 30 


print(f"Hello, my name is {full_name} and I am {user_age} years old.")
print(long_dash)

print(len(long_dash))


#for Booleans 

is_logged_in = True 

is_True = True 
age = 12
can_vote = age >= 18 
print(can_vote)
print(is_logged_in)

#for Boolean ans Operators 
age = 24
has_license = True
drunk = False
can_drive = age >= 16 and has_license and not drunk 
option1 = "Can Drive" 
option2 = "Cannot Drive"
driverstat = option1 if can_drive else option2
# AND - both must be true 

driver = driverstat

print(driver)  # Output: Can Drive

#Assignment Operators 
score = 10 
#Write 
score = score + 5 

score += 5  # This is equivalent to score = score + 5

# String manipulations 

name = "Daniel"

string = f"Hi there, my name is {name}!"

print(string)  

#String Methods 
my_name = "Daniel"
name.lower()
name.upper()

sentence = f"hi my name is {my_name} and I am learning python"

sentence.title()

#finding and Replacing Strings 

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"


#If Statement 

temperature = 34 
if temperature > 30:
    print("It's very hot!")
if temperature > 25: 
    print("It's a hot day!")
else: 
    print("It's a cool day!")

score = 79
if score >= 90:
    print("A - Excellent work!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Satisfactory!")
else:
    print("F - You failed the test.")


#Multiple Conditions 
has_ticket = True 
age = 18

if has_ticket and age >= 18:
    print("You can enter the concert.")
elif has_ticket and age < 18:
    print("You can enter the concert with a guardian.")
else:
    print("You cannot enter the concert.") 


#interation 
for i in range(1, 8): 
    print(i)

# Count by 2s 
for i in range(0, 11, 2):
    print(i)


#Data Structures 
age = 25
has_license = True 
my_list = ["Alice", 25, age, True ]

name = my_list[0]
age = my_list[1]

has_license = my_list[3]

my_list[0] = "Dave"

my_list.append("Alice Smith")

my_list.remove(25)

my_list


#Creating Dictonaries 

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
}

person["name"] = "Dave"

person

#Tuple 

empty = ()
 
point = (3, 4)
color = ("red", "green", "blue")


