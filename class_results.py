

print("X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X")
P = 4
c = 0
while P > 0:

    class Student:
        

        def __init__(self, name, age, section, maths, science, english):
            self.name = name
            self.age = age 
            self.section = section
            self.maths = maths
            self.science = science
            self.english = english
            


    class Results(Student):

        def result(self):
            self.total = self.maths + self.science + self.english
            self.percent = self.total/3
            if self.percent >=35:
                print("TEST PASSED!")
                print(f"{self.name} GOT {self.percent:.2f}%.")
            else:
                print("TEST FAILED!")
                print(f"{self.name} GOT {self.percent:.2f}%.")



    name = input("What's your name?: ")
    name = name.title()
    age = int(input("What's your age?: "))
    section = input("What's your section?: ")
    section = section.upper()

    print("ENTER MARKS: ")

    maths = int(input("Math: "))
    science = int(input("Science: "))
    english = int(input("English: "))


    x = Results(name, age, section, maths, science, english)
    x.result()
    c += 1
    print(f"--> {c} DATA STORED SUCCESSFULLY!")
    print("X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X^X")