# Counting Cats that entered in the building
class CatCounter:
    def __init__(self):
        self.cat_count = 0

    def cat_entered(self):
        self.cat_count += 1
        if self.cat_count == 1:
            print(f"{self.cat_count} Cat enter in the building\n")
        else:
            print(f"{self.cat_count} Cats enter in the building\n")

def main():
    cat_counter = CatCounter()
    
    user_input = input("Press 'Enter' to enter a cat in the building")

    while True:
        
        if user_input.lower() == 'q':
            print('\nCounter Successfully Quit')
        
            break  # Quit the program

        cat_counter.cat_entered()
        user_input = input("'Enter'| 'Press' q to quit\n")

if __name__ == "__main__":
    main()
