# create class
class stu_manage():
    def __init__(self):
        self.stu = []

    # 1.Adding Student
    def adding_stu(self,student_id,student_name,Sex,birth_date,average):
        students = {
            'id': student_id,
            'name' : student_name,
            'sex' : Sex,
            'birth-date' : birth_date,
            'average' : average
        }
        self.stu.append(students)
        print("Student added successful.")
        print(self.stu)
    # 2.Search student
    def search_stu(self,stu_id):
        for students in self.stu:
            if students['id'] == stu_id:
                print(f"Result: \nID: {students['id']}\nName:{students['name']}\nSex:{students['sex']}\nBirth Date:{students['birth-date']}\nAverage:{students['average']}")
                return
        print("ID not found!")
    # 3.Delete student
    def delete_stu(self,stu_id):
        for students in self.stu:
            if students['id'] == stu_id:
                self.stu.remove(students)
                print(f"Student with ID: {stu_id} deleted.")
                return
        print("ID not found!")

student = stu_manage()
while True:
    print("===> Student Management System <===")
    print("1.Add New Student.")   
    print("2.View Student.") 
    print("3.Search Student.") 
    print("4.Delet Student.") 
    print("5.Exit.")

    choice = input("\nChoose your option(1-5):") 

    if choice == '1':
        student_id = input("Enter ID of student:")
        student_name = input("Enter Name of student:")
        Sex = input("Enter Sex of student:")
        birth_date = input("Enter Birth Date of student:")
        average = input("Enter average of student:")
        student.adding_stu(student_id = student_id,student_name=student_name,Sex=Sex,birth_date=birth_date,average=average)
        