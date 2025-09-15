class A:
    def display(self):
        print("from A")
class B(A):
    def display(self):
        print("from b")
class C(A):
    def display(self):
        print("from c")
class D(B,C):
    pass      

d1=D()
d1.display()