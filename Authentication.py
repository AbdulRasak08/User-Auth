import random

# Initialize an empty dictionary to store users (username: email, password_hash)
user_database = {}
failed_attempts = {}  # Track login attempts
todo_list = {}  # Store To-Do lists for each user

# --- User Authentication Section ---

# Function to register a user with email verification
def register_user():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in user_database:
        print("Username already exists! Try again.")
        return
    
    email = input("Enter your email: ")
    if not email_is_valid(email):
        print("Invalid email format! Try again.")
        return
    
    password = input("Enter a password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return
    
    # Simulate email verification
    if not email_verification(email):
        print("Email verification failed!")
        return
    
    user_database[username] = {'email': email, 'password': password}
    print("Registration successful! Please verify your email.")

# Simple function to validate email format
def email_is_valid(email):
    return "@" in email and "." in email

# Simulate email verification (50% chance of success)
def email_verification(email):
    return random.choice([True, False])

# Function to log in a user with login attempt tracking
def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in user_database:
        print("Username not found! Please register first.")
        return
    
    # Track failed attempts
    if failed_attempts.get(username, 0) >= 3:
        print("Too many failed login attempts. Please try again later.")
        return
    
    password = input("Enter your password: ")
    stored_password = user_database[username]['password']
    
    # Check if the entered password matches the stored password
    if password == stored_password:
        print(f"\nWelcome back, {username}!")
        user_dashboard(username)
        failed_attempts[username] = 0  # Reset failed attempts on successful login
    else:
        print("Incorrect password! Try again.")
        failed_attempts[username] = failed_attempts.get(username, 0) + 1  # Increment failed attempts

# Dashboard after successful login
def user_dashboard(username):
    while True:
        print(f"\n--- Dashboard: {username} ---")
        print("1. View Profile")
        print("2. Change Password")
        print("3. To-Do List")
        print("4. Logout")
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        if choice == "1":
            view_profile(username)
        elif choice == "2":
            change_password(username)
        elif choice == "3":
            todo_menu(username)
        elif choice == "4":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")

# View Profile
def view_profile(username):
    print(f"\n--- Profile ---")
    print(f"Username: {username}")
    print(f"Email: {user_database[username]['email']}")
    print("Welcome to your dashboard!")

# Change Password
def change_password(username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")
    stored_password = user_database[username]['password']
    
    if old_password != stored_password:
        print("Incorrect current password! Password not changed.")
        return
    
    new_password = input("Enter a new password: ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
        return
    
    # Update the password
    user_database[username]['password'] = new_password
    print("Password updated successfully!")

# --- To-Do List Section ---

# Menu for the To-Do list
def todo_menu(username):
    while True:
        print(f"\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Back to Dashboard")
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        
        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            remove_task(username)
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

# Add task to the To-Do list
def add_task(username):
    task = input("Enter the task description: ")
    if username not in todo_list:
        todo_list[username] = []
    todo_list[username].append(task)
    print(f"Task '{task}' added.")

# View all tasks
def view_tasks(username):
    if username not in todo_list or not todo_list[username]:
        print("No tasks to show.")
    else:
        print("\n--- Your To-Do List ---")
        for idx, task in enumerate(todo_list[username], 1):
            print(f"{idx}. {task}")

# Remove a task from the To-Do list
def remove_task(username):
    view_tasks(username)
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(todo_list[username]):
            removed_task = todo_list[username].pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# --- Main Program Loop ---
while True:
    print("\n--- User Dashboard Management System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
