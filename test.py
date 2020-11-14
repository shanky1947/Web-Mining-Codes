
class book:
#     def __init__(self, temp):
#         self.temp=temp
    def add(self):
        abc=input("Enter name")
        return abc

class magazine(book):
    # def __init__(self, temp):
    #     book.__init__(self, temp)

    def more(self):
        pqr=input("enter name 2")
        abc=book.add(self);
        dict1 = {abc: pqr}
        print(dict1)

x=magazine()
x.more()