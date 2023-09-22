class Course:
    def __init__(self,course_name,course_duration,*books):
        self.course_name = course_name
        self.course_duration = course_duration
        self.books = [self.Book(b) for b in books]

    def show_details(self):
        print("Course Name : ",self.course_name)
        print("Course Duration : ",self.course_duration)
        print("Suggested Books : ")
        for b in self.books:
            print(b)

    class Book:
        def __init__(self,title):
            self.title = title

        def __str__(self):
            return self.title
    
c1 = Course('Python',10,'Learn Python','Crash Course','Master Python')
c1.show_details()