def fibonacci(n):
        
        if (n==0):          # F0=0,F1=F2=1,
            return 0
        elif(n==1):
            return 1
        else:
            # Fn=Fn−1+Fn−2
            # fibonacci_add formula
            return fibonacci(n-1)+fibonacci(n-2)
 

def fibonacci_sub(n):
    
        if(n==0):               #F0=0,F1=F2=1,
            return 0
        elif (n==1):
            return 1
        else:
                
            # Fn=Fn+2−Fn+1
            # fibonacci_sub formula
            return fibonacci_sub(n+2)-fibonacci_sub(n+1)    
    

while True:
    print("Press 1 Fibonacci-Add-number:")
    print("Press 2 Fibonacci-Subtract-number:")

    # Expectation Handling used
    try:
    
        press = int(input("Enter the press Button:"))
        print(f"Conversion successful: {press}")
        
    except ValueError as ve:
        print(f"ValueError occurred: {ve}")
        
        

    if press == 1:
        n = int(input("Enter a fibonacci-Addition-number: "))
        print(f"Result: {fibonacci(n)}")
    elif press == 2:
        n = int(input("Enter a fibonacci-subtract-number: "))
        print(f"Result: {fibonacci_sub(n)}")
    else:
        print("Invalid press button")

    continue_choice = input("Do you want to continue? yes/no => :").strip().lower()
 
        # The strip() function in Python is used to remove any leading and trailing whitespace
        # (spaces, tabs, newlines) from a string.
        # It can also be used to remove specific characters from both ends of the string
        # if a character or a set of characters is provided as an argument.
    
    if continue_choice != 'yes':
        break

print("Thank you for using!")