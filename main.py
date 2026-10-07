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
student.adding_stu(1,"daleap","M","30-06-2002",50.5)
student.adding_stu(2,"pheaktra","F","21-08-2008",90.5)
student.adding_stu(3,"bona","M","30-06-2002",45.5)
student.delete_stu(3)
#student.search_stu(2)
print(student.stu)
