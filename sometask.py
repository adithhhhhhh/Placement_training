class col:
    def cal_bane(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.per = (self.a + self.b + self.c) / 3

stu = []
while True:
    print("------------------------main menu---------------")
    print("1. add a student")
    print("2. view a status")
    print("3. exit")
    k = int(input("Enter your choice: "))

    match k:
        case 1:
            name = input("Enter your name: ")
            a = int(input("Enter your OS marks: "))
            b = int(input("Enter your DS marks: "))
            c = int(input("Enter your Python marks: "))
            R = col()
            R.cal_bane(name, a, b, c)
            stu.append(R)

        case 2:
            if not stu:
                print("No student data available.")
                continue
            while True:
                print("1. View topper")
                print("2. View individual status")
                print("3. go back to main menu")
                o = int(input("Enter your choice: "))
                if o == 1:
                    topper = sorted(stu, key=lambda x: x.per, reverse=True)[0]
                    print("Rank 1")
                    print("Name:", topper.name)
                    print("Percentage:", topper.per )
                elif o == 2:
                    i = input("Enter the name of the student: ")
                    f = False
                    toppe = sorted(stu, key=lambda x: x.per, reverse=True)
                    index=0
                    for student in toppe:
                        index += 1
                        if student.name == i:
                            print("rank:", index)
                            print("Name:", student.name)
                            print("OS Marks:", student.a)
                            print("DS Marks:", student.b)
                            print("Python Marks:", student.c)
                            print("Percentage:", student.per)
                            f = True
                            break
                    if not f:
                        print("Student not found.")
                elif o == 3:
                    break
        case 3:
            break
