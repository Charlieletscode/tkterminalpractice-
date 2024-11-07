import sys

def main():
    
    response = input("Enter 'y' to continue or 'n' to quit: ").strip().lower()
    if response == 'y':
        print("Continuing...")
    elif response == 'n':
        print("Exiting...")
    else:
        print("Invalid input.")
    # Check if sufficient arguments are passed
    if len(sys.argv) < 3:
        print("Username and password not provided.")
        return
    
    # Get the username and password from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Print the username and password information
    print(f"Username: {username}")
    print(f"Password: {password}")

    # Prompt for further action

if __name__ == "__main__":
    main()
