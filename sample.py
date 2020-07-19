class Sample:
    def __getinput(self):
        a=raw_input("enter the number 1:")
        b=raw_input("Enter the number 2:")
        return a,b
    def sPrint(self):
        c=self.__getinput()
        print(int(c[0])+int(c[1]))

s1=Sample()
s1.sPrint()
