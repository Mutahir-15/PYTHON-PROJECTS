# Problem #2: Index Practice (Console App)
def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Error: Index out of range. Please choose an index between 0 and " + str(len(lst) - 1) + "."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Element modified successfully!"
    else:
        return "Error: Index out of range. Please choose an index between 0 and " + str(len(lst) - 1) + "."

def slice_list(lst, start, end):
    # Adjust start and end to be within bounds
    start = max(0, min(start, len(lst)))
    end = max(0, min(end, len(lst)))
    
    if start > end:
        return "Error: Start index must be less than or equal to end index."
    return lst[start:end]

def main():
    game_list = ["apple", 42, "banana", 7, "orange"]
    
    print("Welcome to the Index Game!")
    print("Here's the initial list:", game_list)
    print("List length:", len(game_list))
    print("You can perform the following operations:")
    print("- 'access': Get an element at a specific index")
    print("- 'modify': Change an element at a specific index")
    print("- 'slice': Get a sublist between two indices")
    print("- 'quit': Exit the game")
    
    while True:
        print("\nCurrent list:", game_list)
        operation = input("Choose an operation (access/modify/slice/quit): ").lower()
        
        if operation == "quit":
            print("Thanks for playing!")
            break
        
        if operation == "access":
            try:
                index = int(input("Enter the index to access: "))
                result = access_element(game_list, index)
                print("Result:", result)
            except ValueError:
                print("Error: Please enter a valid integer for the index.")
        
        elif operation == "modify":
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                result = modify_element(game_list, index, new_value)
                print(result)
            except ValueError:
                print("Error: Please enter a valid integer for the index.")
        
        elif operation == "slice":
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(game_list, start, end)
                print("Sliced list:", result)
            except ValueError:
                print("Error: Please enter valid integers for the indices.")
        
        else:
            print("Invalid operation. Please choose 'access', 'modify', 'slice', or 'quit'.")

if __name__ == "__main__":
    main()