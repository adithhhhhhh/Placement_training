class india:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("{} is good player".format(self.name))

a1=india("SACHIN")
a2=india("Virat")
a1.display()
a2.display()