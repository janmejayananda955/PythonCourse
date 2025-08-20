# wap to create a dict add book deatails (like Book_name,Author_name,price,)
#   1> Based on book_name delete book
#   2> Based on book_name update book(like price)
#   3> Based on book_name search book and display book info
#   4> Based on price Range(min to max) search book (like filter)


bookDb = {}

# what you want to do
while True:
    #ask to choose
    print(
        " 1. Add book details \n 2. Delete book \n 3. Update book \n 4. Search book \n 5. Filter books by price range \n 6. Exit"
    )
    choice = int(input("Enter your choice: "))
    if choice == 1:
        i = 1
    # while loop with infinite iteration
        while True:
            bookDetails = {}
            print("-------Add New Book Details-------")
            bookName = input("Enter Book_Name : ")
            bookDetails["book_name"] = bookName
            bookDetails["Author_name"] = input("Enter Author_name : ")
            bookDetails["book_price"] = float(input("Enter Price : "))

            # add to store all books (i = i+1 increase by one like store one bookdetails)
            bookDb[i] = bookDetails
            print(f"Book {bookName} added successfully!")

            choose = input("Do you want to add more Books[y/n] : ").lower()
            if choose == "n":
                break
            i = i + 1
    #delete book details
    elif choice == 2:
        print("Delete Book")
        bookName = input("Enter Book Name to delete:")
        findBook = False
        for key, value in bookDb.items():
            if value["book_name"] == bookName:
                findBook = True
                del bookDb.key
                print(f"Book {bookName} deleted successfully!")
                break
        if findBook == False:
            print(f"Book {bookName} not found in the database.")
    #update book details
    elif choice == 3:
        print("Update book")
        bookName = input("Enter book name: ")
        findBook = False
        for key, value in bookDb.items():
            if value['book_name'] == bookName:
                findBook = True
                newValue = float(input("Enter new price of Book: "))
                value['book_price'] = newValue
                print(f'Your book {bookName} Old price {value['book_price']} changed to {newValue}successfully ....')
        if findBook == False:
            print(f'Your Book {bookName} not found')
        #update price of book
    #search book
    elif choice == 4:
        findBook = False
        bookName = input("Enter book Name: ")
        for key, value in bookDb.items():
            if value['book_name'] == bookName:
                print(f"Book found and Book details are \n{value.items()}")
        if findBook == False:
            print(f'Your Book {bookName} not found')
    #Filter book according to range
    elif choice == 5:
        print(" 1. Range between ₹500 to ₹999 \n 2. Range between ₹100 to ₹499 \n 3. Below 100")
        choice = int(input("Enter your Filter choice : "))
        if choice == 1:
            print("Books in the range ₹500 to ₹999:")
            for key, value in bookDb.items():
                if 500 <= value['book_price'] <= 999:
                    print(value)
        elif choice == 2:
            print("Books in the range ₹100 to ₹499 : ")
            for key, value in bookDb.items():
                if 100 <= value['book_price'] < 500:
                    print(value)
        elif choice == 3:
            print("Books below ₹100 : ")
            for key, value in bookDb.items():
                if value['book_price'] < 100:
                    print(value)
        else:
            print("Invalid choice for filtering .")
    #Exit loop
    elif choice == 6:
        break
    else:
        print("Invalid choice")


print(bookDb)
