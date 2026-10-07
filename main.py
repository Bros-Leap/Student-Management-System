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
            
student = stu_manage()
student.adding_stu(1,"daleap","M","30-06-2002",50.5)
student.search_stu(1)
#print(student.stu)
