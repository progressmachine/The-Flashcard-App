import os

flashcard_file = "flashcards.txt"
flashcards = {}

# Function to ensure flashcards.txt exists and load it
def initialize_flashcards():
    if not os.path.exists(flashcard_file):
        open(flashcard_file, 'w', encoding='utf-8').close()  # Create the file

    with open(flashcard_file, 'r', encoding='utf-8') as f:
        for line in f:
            if "|||" in line:
                question, answer = line.strip().split("|||", 1)
                flashcards[question] = answer

# Save current flashcards dictionary to flashcards.txt
def save_flashcards_to_file():
    with open(flashcard_file, 'w', encoding='utf-8') as f:
        for question, answer in flashcards.items():
            f.write(f"{question}|||{answer}\n")

# Clear screen for cleanliness
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Add new flashcard
def add_flashcard():
    question = input("Enter the question: ").strip()
    if question in flashcards:
        print("This question already exists.")
    else:
        answer = input("Enter the answer: ").strip()
        flashcards[question] = answer
        save_flashcards_to_file()
        print("Flashcard added and saved.")

# Update existing flashcard
def update_flashcard():
    question = input("Enter the question to update: ").strip()
    if question in flashcards:
        new_answer = input("Enter the new answer: ").strip()
        flashcards[question] = new_answer
        save_flashcards_to_file()
        print("Flashcard updated and saved.")
    else:
        print("Flashcard not found.")

# Delete flashcard
def delete_flashcard():
    question = input("Enter the question to delete: ").strip()
    if question in flashcards:
        del flashcards[question]
        save_flashcards_to_file()
        print("Flashcard deleted and saved.")
    else:
        print("Flashcard not found.")

# View all flashcards
def view_flashcards():
    if not flashcards:
        print("No flashcards available.")
    else:
        print("\nAll Flashcards:")
        for i, (q, a) in enumerate(flashcards.items(), 1):
            print(f"{i}. Q: {q} | A: {a}")
        print()

# Export to user-defined file
def export_flashcards():
    filename = input("Enter filename to export (e.g., export.txt): ").strip()
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for question, answer in flashcards.items():
                f.write(f"{question}|||{answer}\n")
        print(f"Exported to {filename}.")
    except Exception as e:
        print(f"Error exporting flashcards: {e}")

# Import from external file and append to flashcards.txt
def import_flashcards():
    filename = input("Enter filename to import from (e.g., other.txt): ").strip()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            new_count = 0
            for line in f:
                if "|||" in line:
                    question, answer = line.strip().split("|||", 1)
                    if question not in flashcards:
                        flashcards[question] = answer
                        new_count += 1
        save_flashcards_to_file()
        print(f"Imported {new_count} new flashcards from {filename} and saved to {flashcard_file}.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error importing flashcards: {e}")

# Show menu
def main_menu():
    while True:
        print("\n=== Flashcard CLI App ===")
        print("1. Add Flashcard")
        print("2. Update Flashcard")
        print("3. Delete Flashcard")
        print("4. View Flashcards")
        print("5. Export Flashcards")
        print("6. Import Flashcards")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_flashcard()
        elif choice == "2":
            update_flashcard()
        elif choice == "3":
            delete_flashcard()
        elif choice == "4":
            view_flashcards()
        elif choice == "5":
            export_flashcards()
        elif choice == "6":
            import_flashcards()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Run app
if __name__ == "__main__":
    clear_screen()
    initialize_flashcards()
    main_menu()