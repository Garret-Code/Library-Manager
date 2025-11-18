print("📚 Welcome to the Python Library Manager 📚")

library = [
    {"title": "Spider-Man", "category": "comic book",},
    {"title": "Bible", "category": "religious"},
    {"title": "Harry Potter", "category": "fiction"},
    {"title": "Self-Help-101", "category": "non-fiction"},
    {"title": "Star Wars", "category": "fiction"}
]

def View_all_books():
    print("\n--- View Books ---")
    for book in library:
        print(f"{book['title']:<20} {book['category']}")
    input("\nPress Enter to continue...")

def Add_a_book():
    print("\n--- Add Books ---")
    title = input("Title: ").strip()
    category = input("Category: ").strip()
    
    # Check for duplicate title
    for book in library:
        if book["title"].lower() == title.lower():
            print(f"Error: '{title}' already exists in the library.")
            input("\nPress Enter to continue...")
            return  # Stop function early
        
     # If no duplicate, add it
    library.append({"title": title, "category": category})
    print("Book added!")
    input("\nPress Enter to continue...")

    
def Search_for_book():
    print("\n--- Search ---")
    search = input("Enter title to search: ").lower().strip()
    found = False # Flag to check if any book was found
    for book in library:
        if search in book["title"].lower():
            print("Found:", book["title"], "-", book["category"])
            found = True
    if not found:
        print(f"'{search}' not found in the records.")

    input("\nPress Enter to continue...")


def Filter_by_category():
    print("\n--- Categories ---")
    cat = input("Category: ").lower().strip()
    found = False # Flag to check if any book was found
    for book in library:
        if book["category"].lower() == cat:
            found = True
            print(book["title"])
    if not found:
        print(f"'{cat}' not found in the records.")

    input("\nPress Enter to continue...")
            


def Remove_book():
    print("\n--- Remove ---")
    remove_title = input("Enter exact title to remove: ").strip()
    removed = False # Flag to check if any book was found
    for book in list(library):
        if book["title"].lower() == remove_title.lower():
            library.remove(book)
            removed = True
            print(f"'{remove_title}' removed!")

            # We can break here since we only remove the first matching book
            break

    if not removed:
        # This message only prints if the loop finishes without finding a match
        print(f"Error: '{remove_title}' not found in the library")

    input("\nPress Enter to continue...")
        


# menu selection through user input
while True:
    print(
""" 
1. View all books 
2. Add a book 
3. Search for a book
4. Filter by category
5. Remove a book
6. Exit
""")
    
    choice = input("Choose an option: ")
    print()

    if choice == "1":
        View_all_books()
    elif choice == "2":
        Add_a_book()
    elif choice == "3":
       Search_for_book()
    elif choice == "4":
        Filter_by_category()
    elif choice == "5":
        Remove_book()
    elif choice == "6":
        print("\n--- EXIT ---")
        print("Goodbye!\n")
        break
    else:
        print("Invalid option")

#After closing program this shows the number of books left in record
print("Number of books in the library:", len(library))