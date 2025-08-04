import json
import os

class Colors:
    GREEN = "\033[92m"
    RESET = "\033[0m"
    
COMPLETED_FILE = "completed_items.json"
UNCOMPLETED_FILE = "items.json"

# Load and Save Completed items
def load_completed_items():
    if os.path.exists(COMPLETED_FILE):
        with open(COMPLETED_FILE, "r") as file:
            return json.load(file)
    return []

def save_completed_items(completed):
    with open(COMPLETED_FILE, "w") as file:
        json.dump(completed, file)

# Load and Save uncompleted items
def load_items():
    if os.path.exists(UNCOMPLETED_FILE):
        with open(UNCOMPLETED_FILE, "r") as file:
            return json.load(file)
    return[]

def save_items(uncompleted):
    with open(UNCOMPLETED_FILE, "w") as file:
        json.dump(uncompleted, file)

# Add remove items (task)
def add_item(item):
    items = load_items()
    items.append(item)
    save_items(items)
    
def remove_item(index):
    items = load_items()
    if 0 <= index < len(items):
        removed = items.pop(index)
        save_items(items)
        completed = load_completed_items()
        if removed in completed:
            completed.remove(removed)
            save_completed_items(completed)
        print(f"Removed item: {removed}")
    else:
        print("Invalid index!")

# Display items (tasks)
def display_items(items):
    completed = load_completed_items()
    print(f"\n---TODO LIST---")
    for i, item in enumerate(items, 1):
        if item in completed:
            print(f"{i}. {Colors.GREEN}✓ {item} (COMPLETED){Colors.RESET}")
        else:
            print(f"{i}. {item}")
            
todo_items = []
     
while True:
    print("---Welcome to yor TODO List---")
    print("\n")
    print("1. See TODO List")
    print("2. Add item to TODO List")
    print("3. Mark item as completed")
    print("4. Remove item from TODO List")
    print("\n5. Exit")
    
    try:
        option = int(input("\n Select an option: "))
        
        if option == 1:
            print("\n---TODO LIST---")
            display_items(todo_items)
            
        elif option == 2:
            # Add item
            
        elif option == 3:
            # Mark complete
            
        elif option == 4:
            # Remove item
            
        elif option == 5:
            print("Goodbye!")
            break
        
        else:
            print("Invalid option! Please input 1-5")
            
    except ValueError:
        print("Please enter a valid number!")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        
    input("\nPress Enter to continue...")

input("\nPress Enter to exit...")