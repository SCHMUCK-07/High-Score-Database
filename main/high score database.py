def load_existing_data():
    usernames = set()
    try:
        with open("userinfo.txt", "r") as myFile:
            for line in myFile:
                # Extract the username from the line and add it to the set
                username = line.split(",")[0].split(":")[1].strip()
                usernames.add(username)
    except FileNotFoundError:
        pass  # If the file doesn't exist, we'll just return an empty set

    return usernames


def add_data(existing_usernames):
    try:
        with open("userinfo.txt", "r") as myFile:
            lines = myFile.readlines()

        if len(lines) >= 10:
            print("The file is full. You cannot add more than 10 usernames and scores.")
            return
    except FileNotFoundError:
        lines = []

    while True:
        username = input("What is your username: ").strip()

        # If the username already exists, update the score
        if username in existing_usernames:
            print(f"Username {username} already exists. Updating the score.")

            # Find the existing score and prompt for the new score
            new_score = int(input("Enter the new score: ").strip())

            updated_lines = []
            user_found = False

            # Loop through the lines and update the score if the username matches
            for line in lines:
                if f"username: {username}" in line:
                    current_score = int(line.split(", score: ")[1].strip())
                    # Only update if the new score is higher
                    if new_score > current_score:
                        updated_lines.append(f"username: {username}, score: {new_score}\n")
                        user_found = True
                    else:
                        updated_lines.append(line)  # Keep the old score if the new one is lower
                else:
                    updated_lines.append(line)

            if not user_found:
                updated_lines.append(f"username: {username}, score: {new_score}\n")

            with open("userinfo.txt", "w") as myFile:
                myFile.writelines(updated_lines)

            print(f"Score for {username} has been updated.")
            break

        # If the username doesn't exist, allow the user to add a new entry
        else:
            score = int(input("Please input your score: ").strip())

            # Add the new entry to the list
            lines.append(f"username: {username}, score: {score}\n")
            with open("userinfo.txt", "a") as myFile:
                myFile.write(f"username: {username}, score: {score}\n")

            existing_usernames.add(username)
            print(f"New user {username} added with score {score}.")
            break

        more = input("Do you want to add another user? (Yes/No): ").strip().lower()
        if more != "yes":
            break


def search_data():
    username_to_find = input("Enter the username to find the score: ").strip()
    found = False
    with open("userinfo.txt", "r") as myFile:
        for line in myFile:
            if f"username: {username_to_find}" in line:
                print(line.strip())
                found = True
                break
    if not found:
        print("Username not found.")


def delete_data():
    try:
        with open("userinfo.txt", "r"):
            pass  
    except FileNotFoundError:
        print("The file 'userinfo.txt' does not exist.")
        return

    confirm = input("Are you sure you want to clear 'userinfo.txt'? (Yes/No): ").strip().lower()
    if confirm == "yes":
        with open("userinfo.txt", "w") as file:
            file.write("")
        print("The file 'userinfo.txt' has been cleared.")
    else:
        print("File deletion canceled.")


def clear_all_data():
    confirm = input("Are you sure you want to clear all data? (Yes/No): ").strip().lower()
    if confirm == "yes":
        delete_data()
    else:
        print("All data clearing canceled.")


def clear_user_data():
    username_to_clear = input("Enter the username to clear their data: ").strip()
    
    try:
        with open("userinfo.txt", "r") as myFile:
            lines = myFile.readlines()
        
        with open("userinfo.txt", "w") as myFile:
            found = False
            for line in lines:
                if f"username: {username_to_clear}" in line:
                    found = True
                    print(f"Data for {username_to_clear} has been cleared.")
                    continue
                myFile.write(line)

            if not found:
                print(f"No data found for {username_to_clear}.")
    except FileNotFoundError:
        print("The file 'userinfo.txt' does not exist.")


def admin():
    username = input("Input username: ").strip()
    password = input("Input password: ").strip()
    
    if username == "tiago" and password == "superboot91":
        while True:
            print("\nADMIN Menu:")
            print("1. Clear all data")
            print("2. Clear data for a specific user")
            print("3. Exit")
            choice = input("Choose an option (1/2/3): ").strip()

            if choice == "1":
                clear_all_data()
            elif choice == "2":
                clear_user_data()
            elif choice == "3":
                break
            else:                print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        print("WOMP WOMP")


while True:
    existing_usernames = load_existing_data()

    print("\nMenu:")
    print("1. Add usernames and scores")
    print("2. Find a score by username")
    print("3. ADMIN")
    print("4. Exit")
    choice = input("Choose an option (1/2/3/4): ").strip()

    if choice == "1":
        add_data(existing_usernames)
    elif choice == "2":
        search_data()
    elif choice == "3":
        admin()
    elif choice == "4":
        print("bye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
