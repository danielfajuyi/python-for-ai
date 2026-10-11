
def greet(): 
    print("Hello!")
    print("Hello again")
  

greet()

# Call it multiple times 
def say_goodbye():
    print("Goodbye!")

say_goodbye()

def check_weather():
    temperature = 30
    if temperature > 25:
        print("It's hot!")
    else: 
        print("!It's a nice weather")

check_weather()

#Functions with Parameters 

def greet_alice(): 
    print("Hello, Daniel!")

def greet(name):
   
    print (f"Hello, {name}")

greet(name="Daniel")
greet(name="Alice")

def greetings(first_name, last_name):
   
    print (f"Hello, {first_name} {last_name}")

greetings("Daniel", "Fajuyi")
greetings(first_name="Daniel", last_name="Fajuyi")

def calculate_total(price, tax_rate, discount): 
    tax = price * tax_rate 
    final_price = price + tax - discount 
    print(f"Total: ${final_price}")

# Order matters! 
calculate_total(price=100, tax_rate=0.08, discount=10)


#Order of Operation 
def calculator_total(price): 

    #Default value 
    tax = 0.08 
    discount = 10 

    # Calculation 
    tax = price * tax 
    final_price = price + tax - discount

    #Print the final price 
    print(f"Total: ${final_price}")

calculator_total(price=100)


# Functions can return 

#without return 
def add_print(a, b):
    print(a + b)


add_print(a=5, b=10)

#with return 
def add_return(a, b):
    return a + b 

add_return(a=5, b=10)


def calculate_area(width, height): 
    area = width * height 
    area = area * 1.05
    return area 

# Store the returned value 
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")



def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

f,l = simple_function()

print(f)
print(l)


#The difference between return and print 
def get_greeting_print(name): 
    print(f"Hello, {name}!") # Just displays 

def get_greeting_return(name): 
    return f"Hello, {name}!"  #Gives back value 

#We cant use print version outputs 
message = get_greeting_print("Alice") # Prints but returns None

#We can use return version outputs 
message = get_greeting_return("Daniel") # Returns the string
print(message.upper())




    
