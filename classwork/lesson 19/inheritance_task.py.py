class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    
    def office_location(self):
        print("The head office is located in Cap Town.")

class OOPCourse(Course):

    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(f"Description: {self.description}\nTrainer: {self.trainer}")

    def show_course_id(self):
        print("Course ID: #12345")        



# Example usage:
# Create an instance of the Course class
#course = Course()
course_1 = OOPCourse()

# Call the contact_details method to display contact information
#course.contact_details()

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()


