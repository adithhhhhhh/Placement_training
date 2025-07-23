class college:
    col="NITTE"
    def student(self,name,mark):
        self.name=name
        self.mark=mark
    def passfail(self):
        if(self,mark>40):
            print("Clear")
        else:
            print("fail")
    def modify(self,grace):
        self.mark=self.mark+grace
    def display(self):
        print("Name: ",self.name)
        print("Mark: ",self.mark)
        print("College: ",self.col)
s1=college()
s1.student("Adith",66)
s1.display()