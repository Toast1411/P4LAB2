#Caleb Laws
#4/5/2026
#P4LAB2 - Interactive Multiplication Table
run_again = "yes"

while run_again.lower() == "yes":
    
    try:
        user_input = int(input("Enter an integer: "))
        
        
        if user_input >= 0:
            print(f"Multiplication table for {user_input}:")
         
            for i in range(1, 13):
                result = user_input * i
                print(f"{user_input} x {i} = {result}")
        else:
         
            print("Error: The program cannot accept negative values.")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    run_again = input("Do you wish to run it again? (yes/no): ").strip().lower()

print("Program ended.")