class Student:
    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num
        self.mark = {}

    def Add_Marks(self, subjects, mark):
        self.mark[subjects] = mark

    def calculate_average(self):
        if not self.mark:
            return 0
        total_mark = sum(self.mark.values())
        num_mark = len(self.mark)
        return total_mark / num_mark

    def total_mark(self):
        return sum(self.mark.values()) if self.mark else 0

    def Display_Details(self):
        print(f"Student: {self.name}")
        for subjects, mark in self.mark.items():
            print(f"Subject: {subjects}")
            print(f"Marks: {mark}")
        total = self.total_mark()
        print(f"Total Marks: {total}")
        print(f"Average Marks: {self.calculate_average():.2f}")

    def update_student(self, roll_num=None, name=None, subject=None, mark=None):
        if name:
            self.name = name
            print(f"Updated name to: {self.name}")
        if roll_num:
            self.roll_num = roll_num
            print(f"Updated roll number to: {self.roll_num}")
        if subject and mark is not None:
            self.Add_Marks(subject, mark)
            print(f"Updated marks for subject {subject} to {mark}")
        else:
            print("No subject or mark data found.")

    def Delete_Data(self, subject=None):
        if subject:
            if subject in self.mark:
                del self.mark[subject]
                print(f"Deleted marks for subject: {subject}")
            else:
                print(f"No data found for subject: {subject}")
        else:
            self.mark.clear()
            print(f"Deleted all data for student {self.name}.")
            
            
            
            #<<-----------------------Main-function-------------------------------------
            # -------------------------------------------------------------------------- >>

def main():
    students = []

    while True:
        print("\nMenu")
        print("1. Add a student")
        print("2. Add subjects and marks")
        print("3. View student details")
        print("4. Update student data")
        print("5. Delete student data")
        print("6. Exit")
        
        #<<-------------------Menu----------------------->>

        try:
            choice = int(input("Enter a choice number: "))
            print(f"\nSuccessfully completed choice: {choice}")
        except ValueError as ve:
            print(f"ValueError occurred: {ve}. Please enter a valid choice.")
            continue
        
        #<<---------------- 1) . Add-student------------------------>>
        
        if choice == 1:
            try:
                name = input("\nEnter the student's name: ")
                roll_num = int(input("Enter the roll number: "))
                new_student = Student(name, roll_num)
                students.append(new_student)
                print("\nStudent added successfully!")
            except ValueError as ve:
                print(f"Invalid data: {ve}. Please enter valid information.")
                
        #<<----------- 2) .Add subject and marks--------------------------->>

        elif choice == 2:
            if not students:
                print("No students added yet. Please add a student first.")
            else:
                found_student = students[-1]  # Get the last added student
                if found_student:
                    print(f"Student name: {found_student.name}")
                    try:
                        num_subjects = int(input("Enter the number of subjects: "))
                        for i in range(num_subjects):
                            subject = input(f"Enter subject {i + 1}: ")
                            marks = float(input(f"Enter marks for {subject}: "))
                            found_student.Add_Marks(subject, marks)
                            print("Marks added successfully!")
                    except ValueError as ve:
                        print(f"Invalid data: {ve}. Please enter valid information.")

        #<<----------- 3). View Details --------------------------->>
        
        elif choice == 3:
            if not students:
                print("No students added yet. Please add a student first.")
            else:
                new_roll = int(input("Enter the roll number to view details: "))
                found = False
                for student in students:
                    if student.roll_num == new_roll:
                        student.Display_Details()
                        found = True
                        break
                if not found:
                    print("No student found with that roll number.")

        #<<----------- 4). UpDate student Data --------------------------->>
        
        elif choice == 4:
            if not students:
                print("No students added yet. Please add a student first.")
            else:
                roll_num = int(input("Enter the roll number: "))
                found_student = next((s for s in students if s.roll_num == roll_num), None)

                if found_student:
                    update_choice = input("Do you want to update (name, subject, marks, or roll_num)? ").strip().lower()
                    
                    

                    #--------update Name---------------
                    
                    if update_choice == "name":
                        update_name = input("Enter a new name: ")
                        found_student.name = update_name
                        print(f"Name successfully updated to: {update_name}")
                    
                    #-----------Roll_num----------------

                    elif update_choice == "roll_num":
                        new_roll = int(input("Enter a new roll number: "))
                        found_student.roll_num = new_roll
                        print("Roll number successfully updated.")
                    
                    #-------------subject-----------------

                    elif update_choice == "subject":
                        old_subject = input("Enter the subject to update: ")
                        if old_subject in found_student.mark:
                            new_subject = input(f"Enter the new subject name for {old_subject}: ")
                            marks = found_student.mark[old_subject]
                            found_student.Add_Marks(new_subject, marks)
                            del found_student.mark[old_subject]
                            print(f"Subject updated from {old_subject} to {new_subject}")
                        else:
                            print(f"Subject '{old_subject}' not found.")
                            
                    #-------------marks--------------------

                    elif update_choice == "marks":
                        subject = input("Enter the subject to Old-marks: ")
                        if subject in found_student.mark:
                            new_marks = float(input("Enter new marks: "))
                            found_student.mark[subject] = new_marks
                            print(f"Marks for {subject} updated to {new_marks}")
                        else:
                            print(f"Subject '{subject}' not found.")
                            
                            
                            
        #<<----------- 5). Delete student Data --------------------------->>                    

        elif choice == 5:
            if not students:
                print("No students added yet. Please add a student first.")
            else:
                roll_num = int(input("Enter the roll number: "))
                found_student = next((s for s in students if s.roll_num == roll_num), None)

                if found_student:
                    del_choice = input("Do you want to delete a specific subject or all data? (subject/all): ").strip().lower()
                    if del_choice == "subject":
                        del_subject = input("Enter the subject name to delete: ")
                        found_student.Delete_Data(subject=del_subject)
                    elif del_choice == "all":
                        students.remove(found_student)
                        print(f"Deleted all data for student: {found_student.name}")
                    else:
                        print("Invalid choice. Please enter 'subject' or 'all'.")
                else:
                    print("Student not found.")

        #<<----------- 3). Exit Data --------------------------->>
        elif choice == 6:
            print("Exit successfully completed.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
