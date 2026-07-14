"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:

    #class variables, instance variable for a specific object from False to True.
    has_been_read = False

    # Initialise the instance variables for each email.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    
    # Create the 'mark_as_read()' method to change the 'has_been_read'
    def mark_read(self):
        self.has_been_read = True

    def __str__(self):
        return (f"\nFrom: {self.email_address}\nSubject: {self.subject_line}\nBody: {self.email_content}\n")    
    


# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    hyperion_dev = Email("hyperion@gmail.com", "welcome!", "welcome to the bootcamp.")
    youtube = Email("youtube@gmail.com", "New video for you!", "Here are some vides you might like")
    netflix = Email("netflix@gmail.com", "Time to renew!", "Your subscription needs to be renewed")
    return [hyperion_dev, youtube, netflix]
    

def list_emails(inbox):
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for i in range(len(inbox)):
        print(f"{i}\tFrom: {inbox[i].email_address}\n\tSubject: {inbox[i].subject_line}\n")
    return


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    print(index)
    index.mark_read()
    return 
    

def view_unread_emails(inbox):
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    unread_inbox = []
    for i in inbox:
        if i.has_been_read == False:
            unread_inbox.append(i)

        else:
            pass
    print("\nUnread emails: ")        
    list_emails(unread_inbox)


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
inbox = []

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
inbox = populate_inbox()

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    try:
        user_choice = 0    
        user_choice = int(
            input(
                """Would you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: """
            )
        )

        if user_choice == 1:
            list_emails(inbox)
            user_choice = int(input("Please select a email to read: "))
            read_email(inbox[user_choice])

        elif user_choice == 2:
            # Add logic here to view unread emails
            view_unread_emails(inbox)
            
        elif user_choice == 3:
            #logic here to quit application.
            break

        else:
            print("\nOops - incorrect input.")

    except Exception:
        print("\nOops - incorrect input.")
             
