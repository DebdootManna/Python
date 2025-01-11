# Sample data for events and participants
events = {
    "Coding Competition": [
        ("Alice", "1234567890", "CSE", "Not Attended"),
        ("Bob", "9876543210", "IT", "Not Attended"),
    ],
    "Quiz Competition": [
        ("Charlie", "1231231234", "ECE", "Not Attended"),
        ("Dave", "3213214321", "ME", "Not Attended"),
    ],
    "Hackathon": [
        ("Eve", "1112223334", "CSE", "Not Attended"),
        ("Frank", "5556667778", "IT", "Not Attended"),
    ],
}

# Function to display the list of participants for a specific event
def display_participants(event_name):
    if event_name in events:
        print(f"\nParticipants for '{event_name}':")
        for participant in events[event_name]:
            print(f"Name: {participant[0]}, Contact: {participant[1]}, Department: {participant[2]}, Status: {participant[3]}")
    else:
        print(f"\nEvent '{event_name}' not found!")

# Function to search for a participant by name and display their event details
def search_participant(participant_name):
    found = False
    for event_name, participants in events.items():
        for participant in participants:
            if participant[0].lower() == participant_name.lower():
                print(f"\nParticipant Found: {participant_name}")
                print(f"Event: {event_name}, Contact: {participant[1]}, Department: {participant[2]}, Status: {participant[3]}")
                found = True
    if not found:
        print(f"\nParticipant '{participant_name}' not found!")

# Function to mark a participant as "Attended" or "Not Attended"
def mark_attendance(event_name, participant_name, status):
    if event_name in events:
        participants = events[event_name]
        for i, participant in enumerate(participants):
            if participant[0].lower() == participant_name.lower():
                participants[i] = (participant[0], participant[1], participant[2], status)
                print(f"\nUpdated Status for {participant_name} in '{event_name}' to '{status}'.")
                return
        print(f"\nParticipant '{participant_name}' not found in '{event_name}'.")
    else:
        print(f"\nEvent '{event_name}' not found!")

# Function to generate a summary of total participants in each event
def generate_summary():
    print("\nEvent Summary:")
    for event_name, participants in events.items():
        print(f"{event_name}: {len(participants)} participants")

# Menu-driven program
while True:
    print("\n--- College Event Management System ---")
    print("1. Display Participants for an Event")
    print("2. Search for a Participant by Name")
    print("3. Mark Attendance for a Participant")
    print("4. Generate Event Summary")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        event_name = input("Enter event name: ")
        display_participants(event_name)
    elif choice == "2":
        participant_name = input("Enter participant name: ")
        search_participant(participant_name)
    elif choice == "3":
        event_name = input("Enter event name: ")
        participant_name = input("Enter participant name: ")
        status = input("Enter status ('Attended' or 'Not Attended'): ")
        mark_attendance(event_name, participant_name, status)
    elif choice == "4":
        generate_summary()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again!")