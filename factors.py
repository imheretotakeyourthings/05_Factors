# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    
    # Make string with five characters 
    ends = decoration * 10
    
    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)
    
    print()
    print(statement)
    print()
    
    return ""
    
# displays instructions / information
def instructions():
    
    statement_generator("Instructions /  Information", "=")
    print()
    print("Please enter an number that is one or more(less then 200).  The program will show a list of the numbers factors.")
    print()
    print("it will also show you if the number is a prime number or a perfect square")
    
    print()
    print("Press <enter> to find the factors of another number or any key to quit")
    print()
    return ""     

# checks input is a number more than a given value
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter an number between 1 and 200"
        
        try:
        
            # ask user to enter a number
            response = int(input(question))
            
            # checks number is between 1 and 200
            if 1 <= response <= 200:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    
# gets factors, returns a sorted list
def get_factors(to_factor):
    
    # list to hold factors
    factors = []
        
    # Square root to_factor to find 'half way'
    limit = int(to_factor ** 0.5)
    
    # find factor pairs and add to list
    for num in range (1, limit + 1):
        
        # check factor is not 1 (unity)
        if to_factor == 1:
            break
        
        # check if number is a factor
        result = to_factor % num
        factor_1 = to_factor // num
               
        # add factor to list if it is not already in there
        if result == 0:
            
            # add numbers/items to list
            factors.append(num)
            
        if factor_1 != num and result == 0:
            factors.append(factor_1)
            
        # sort list...
    
    factors.sort()
        
    return factors

# Main Routine

# Heading
statement_generator("THE Factors Calculator", "*")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()
# Loop
keep_going = ""
while keep_going == "":
    
    comment = ""
    
    # ask user for number to be factored    
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:            
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is unity  It only has one factor...  Itself :)"
        
    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
        
    # output factors and comment
    
    # Generate heading...    
    if var_to_factor == 1:
        heading = "One is special..."
        
    else:
        heading = "Factors of {}".format(var_to_factor)
    
    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()