# Problem #1: List Practice (Console App)
def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    # Print the length of the list
    print(len(fruit_list))

    # Adding "mango" at the end of the list
    fruit_list.append('mango')

    # Printing the Updated list
    print(fruit_list)

    # Length of the Updated list
    print(len(fruit_list))
    
    # As an Innovation lets remove an elemnt too. Removing Banana.
    fruit_list.remove('banana')
    print(fruit_list)

if __name__ == "__main__":
    main()