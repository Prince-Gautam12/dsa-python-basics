# give list of all student from given city  => done
# give 3 list failed (<33%) passed (33-74.99) distiction (>=75) {"failed":[], "passed":[], "topper": []} => done


class Student:
    def __init__ (self,name,roll,city,percentage,number,course,age):
        self.name = name
        self.roll = roll
        self.city = city
        self.percentage = percentage
        self.number = number
        self.course = course
        self.age = age
    def __str__(self):
         return f"name: {self.name}, roll: {self.roll}, city: {self.city}, percentage: {self.percentage}, number: {self.number}, course: {self.course}, age: {self.age}"

class StudentManager:
    studentList = []    
    
    def saveStudent(self, student):
        self.studentList.append(student)
        
    def printAllStudents(self):
        # print(self.students)s
        # for student in self.students :
        #     print(student)
        ListHelper.print(self.studentList)
    
    def getStudentFromCity(self,givenCity) :
        filteredStudents = []
        for student in self.studentList:
            if student.city == givenCity:
                filteredStudents.append(student)
        return filteredStudents
    
    def splitStudentsBasedOnPercenatge(self):
        failedStudetns = []
        passedStudents = []
        topperStudents = []

        for student in self.studentList:
            if student.percentage < 33:
                failedStudetns.append(student)
            elif student.percentage >=33 and student.percentage<75:
                passedStudents.append(student)
            else:
                topperStudents.append(student)
        sagregatedStudents = {"failed" : failedStudetns, "passed" : passedStudents, "topwale" : topperStudents}
        return sagregatedStudents
    
class ListHelper :
    @staticmethod
    def print(list) :
        for item in list :
            print(item)


def insertAllStudentDatabase (studentmanager):

    studentDataBase =  [Student("Akshay", 77, "Delhi", 100, "100-123-4567", "Btech", 30),
    Student("Akshay", 77, "Delhi", 100, "100-123-4567", "Btech", 30),
    Student("Rohit", 88, "Mumbai", 78, "101-123-4567", "Btech", 22),
    Student("Priya", 99, "Bangalore", 85, "102-123-4567", "MBA", 25),
    Student("Sneha", 66, "Hyderabad", 90, "103-123-4567", "BSc", 21),
    Student("Amit", 55, "Chennai", 82, "104-123-4567", "MCA", 23),
    Student("Neha", 44, "Kolkata", 88, "105-123-4567", "BCom", 24),
    Student("Ravi", 33, "Pune", 75, "106-123-4567", "BA", 20),
    Student("Sonal", 22, "Ahmedabad", 89, "107-123-4567", "BBA", 26),
    Student("Arjun", 11, "Jaipur", 92, "108-123-4567", "MBBS", 27),
    Student("Megha", 101, "Mumbai", 86, "109-123-4567", "BArch", 28),
    Student("Kunal", 78, "Delhi", 81, "110-123-4567", "Btech", 21),
    Student("Riya", 89, "Mumbai", 77, "111-123-4567", "Btech", 22),
    Student("Nikhil", 100, "Bangalore", 84, "112-123-4567", "MBA", 25),
    Student("Tanya", 67, "Hyderabad", 91, "113-123-4567", "BSc", 22),
    Student("Vikas", 56, "Chennai", 83, "114-123-4567", "MCA", 24),
    Student("Ankita", 45, "Kolkata", 87, "115-123-4567", "BCom", 23),
    Student("Rahul", 34, "Pune", 76, "116-123-4567", "BA", 21),
    Student("Ritu", 23, "Ahmedabad", 90, "117-123-4567", "BBA", 27),
    Student("Deepak", 12, "Jaipur", 93, "118-123-4567", "MBBS", 28),
    Student("Pooja", 102, "Lucknow", 85, "119-123-4567", "BArch", 29),
    Student("Anil", 79, "Delhi", 80, "120-123-4567", "Btech", 23),
    Student("Nisha", 90, "Mumbai", 78, "121-123-4567", "Btech", 24),
    Student("Siddharth", 101, "Bangalore", 86, "122-123-4567", "MBA", 26),
    Student("Jyoti", 68, "Hyderabad", 90, "123-123-4567", "BSc", 23),
    Student("Raj", 57, "Chennai", 82, "124-123-4567", "MCA", 25),
    Student("Monika", 46, "Kolkata", 10, "125-123-4567", "BCom", 26),
    Student("Suresh", 35, "Pune", 74, "126-123-4567", "BA", 22),
    Student("Anjali", 24, "Ahmedabad", 88, "127-123-4567", "BBA", 28),
    Student("Karan", 13, "Jaipur", 9, "128-123-4567", "MBBS", 29),
    Student("Komal", 103, "Lucknow", 87, "129-123-4567","BArch",12)]

    for student in studentDataBase :
        studentmanager.saveStudent(student)


def start () :
    studentmanager = StudentManager()
    insertAllStudentDatabase(studentmanager)
    # studentmanager.printAllStudents()
    print("======= Filtered Test of Delhi=====")
    filteredStudents = studentmanager.getStudentFromCity("Delhi")
    # print(filteredStudents)
    # for student in filteredStudents:
    #     print(student)
    ListHelper.print(filteredStudents)
    # Puttu = Student("Akshay", 77, "Delhi", 80, 100, "Btech", 30)
    # print(Puttu)
    print("======= Filtered Test of Mumbai=====")
    filteredStudents = studentmanager.getStudentFromCity("Mumbai")
    # for student in filteredStudents:
    #     print(student)
    ListHelper.print(filteredStudents)
    print("======= Filtered Test of Pune=====")
    filteredStudents = studentmanager.getStudentFromCity("Pune")
    ListHelper.print(filteredStudents)
    # for student in filteredStudents:
    #     print(student)
    print("======= Filtered Test of Hyderabad=====")
    filteredStudents = studentmanager.getStudentFromCity("Hyderabad")
    ListHelper.print(filteredStudents)
    # for student in filteredStudents:
    #     print(student)
    print("======= Splitted Students=====")
    sagregatedStudents = studentmanager.splitStudentsBasedOnPercenatge()
    for key, studentList in sagregatedStudents.items():
        print(key)
    ListHelper.print(studentList)

print("Start code run")
start()
print("Code run complete")
