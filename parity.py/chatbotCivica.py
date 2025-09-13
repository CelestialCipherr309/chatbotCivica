import random
import time

# A mock database to store complaint details.
# In a real application, this would be a connection to a proper database.
complaints_db = {}

def generate_complaint_id():
    """Generates a unique 6-digit complaint ID."""
    return random.randint(100000, 999999)

def report_new_issue():
    """Handles the logic for reporting a new civic issue."""
    print("\nThank you for reporting a new issue.")
    print("Let's get some details.")

    # Get issue type
    issue_type = input("What is the type of issue? (e.g., Pothole, Streetlight Out, Garbage Dump): ")
    while not issue_type:
        print("Issue type cannot be empty.")
        issue_type = input("What is the type of issue? ")

    # Get location
    location = input("Please provide the location of the issue (address or landmark): ")
    while not location:
        print("Location cannot be empty.")
        location = input("Please provide the location of the issue: ")

    # Get description
    description = input("Please provide a brief description of the issue: ")
    while not description:
        print("Description cannot be empty.")
        description = input("Please provide a brief description of the issue: ")

    # Generate a new complaint ID
    complaint_id = generate_complaint_id()
    
    # Ensure the generated ID is unique
    while complaint_id in complaints_db:
        complaint_id = generate_complaint_id()

    # Store the complaint in our mock database
    complaints_db[complaint_id] = {
        "type": issue_type,
        "location": location,
        "description": description,
        "status": "Submitted" # Initial status
    }

    print("\nThank you for your submission!")
    print("="*30)
    print(f"Your Complaint ID is: {complaint_id}")
    print("Please save this ID to check the progress of your complaint later.")
    print("="*30)
    time.sleep(2)

def check_complaint_status():
    """Handles the logic for checking the status of an existing complaint."""
    print("\nTo check the status of your complaint, please enter the Complaint ID.")
    
    try:
        complaint_id_str = input("Enter your Complaint ID: ")
        complaint_id = int(complaint_id_str)

        if complaint_id in complaints_db:
            complaint = complaints_db[complaint_id]
            print("\n--- Complaint Status ---")
            print(f"  ID: {complaint_id}")
            print(f"  Type: {complaint['type']}")
            print(f"  Location: {complaint['location']}")
            print(f"  Description: {complaint['description']}")
            print(f"  Status: {complaint['status']}")
            print("------------------------")
            
            # Simulate a status update for demonstration purposes
            if complaint['status'] == 'Submitted':
                complaints_db[complaint_id]['status'] = 'In Progress'
                print("(Note: The status has been updated to 'In Progress' for this check.)")

        else:
            print(f"\nSorry, no complaint found with the ID: {complaint_id}")

    except ValueError:
        print("\nInvalid input. Please enter a valid numeric Complaint ID.")
    
    time.sleep(2)


def chatbot():
    """The main function to run the interactive chatbot."""
    print("==========================================")
    print(" Welcome to the Civica Help Desk Chatbot! ")
    print("==========================================")
    
    while True:
        print("\nHow can I help you today?")
        print("1. Report a new civic issue")
        print("2. Check the progress of an existing complaint")
        print("3. Exit")
        
        choice = input("Please enter your choice (1, 2, or 3): ")

        if choice == '1':
            report_new_issue()
        elif choice == '2':
            check_complaint_status()
        elif choice == '3':
            print("\nThank you for using the Civica Help Desk. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option (1, 2, or 3).")
        
        print("\n------------------------------------------")

if __name__ == "__main__":
    # This block runs the chatbot when the script is executed
    chatbot()
