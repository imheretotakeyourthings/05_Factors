# checks input is a number between 1 and 200
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter an integer between 1 and 200 (inclusive)"
        
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
            
            
# Main Routine
keep_going = ""
while keep_going == "":
    to_factor = num_check("What number should I factor? ")
    print("success!  You chose", to_factor)
    print()