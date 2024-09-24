try:

    BookList = []
    infile = open("BooksList.txt","r")
    line = infile.readline()
    while line:
        BookList.append(line.rstrip("\n").split(","))
        line = infile.readline()
    infile.close()

except FileNotFoundError:
    print("The <BookList.txt> file not found.\n")
    print("Starting a new Books list.")
    BookList = []



def main():


    while True:

        print("*** BOOK MANAGER ***\n")
        print("1-> Add a book.\n")
        print("2-> Look up a book.\n")
        print("3-> Display books.\n")
        print("4-> Quit.")
        print("************************************\n")
        choice = int(input("Enter your choice: "))
        print("\n")
        if choice == 1:
            AddBook()
        elif choice == 2:
            search()
        elif choice == 3:
            display()
        else:
            print("Quitting the program....")
            print("Thank you.")
            exit(0)
        
        new_func()

def new_func():
    outfile = open("BooksList.txt","w")
    for books in BookList:
        outfile.write(",".join(books)+"\n")
    outfile.close()

def AddBook():
    while True:
        print("\nAdding a book......\n")
        nBook = input("Enter the name of the book: ")
        aBook = input("Enter the author of the book: ")
        pBook = input("Enter the pages of the book: ")
        BookList.append([nBook,aBook,pBook])
        print("\n")
        choice = input("Do you wand to add more books (y/n): ")
        if choice == "y":
            continue
        else:
            break


def search():
    print("Looking up for a book.......\n")
    keyword = input("Enter the name or the author of the book: ")
    print("\n")
    print("The books are >>>>\n")
    for key in BookList:
        if keyword in key:
            print("Name of the book >>>> ",key[0])
            print("Author of the book >>>> ",key[1])
            print("No. of pages >>>> ",key[2])
            print("\n")

def display():
    print("Displaying all books......\n")
    for i in range(len(BookList)):
        print(BookList[i])
        print("\n")



if __name__ == "__main__":
    main()
    



