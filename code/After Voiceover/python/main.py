# main.py
from GetTitleClass import GetTitle

def main():
    title_getter = GetTitle()
    
    while True:  # simple console UI loop
        print("\n" + "-"*30)  # prints 30 dashes for separation and a new line above
        print("1. Enter video title")
        print("2. Get current title")
        print("3. Exit")
        print("-"*30 + "\n")  # prints 30 dashes for separation and a new line below
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title_getter.prompt_for_title()
        elif choice == '2':
            current_title = title_getter.get_current_title()
            print(f"\nCurrent title: {current_title}\n")  # adds new lines above and below the title output
        elif choice == '3':
            break
        else:
            print("\nInvalid choice. Please try again.\n")  # adds new lines above and below the error message

if __name__ == "__main__":
    main()
