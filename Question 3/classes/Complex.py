class Complex:
    def __init__(self,real,im):
        self.real=float(real)
        self.im=float(im)
    def add(self,n):
        return self.real+n,self.im
    def sub(self,n):
        return self.real-n,self.im
    def div(self,n):
        return self.real/n,self.im/n
    def mul(self,n):
        return self.real*n,self.im*n
    def neg(self):
        return -self.real,-self.im
    def __str__(self):
        return "("+str(self.real)+","+str(self.im)+")"
if __name__=="__main__":
    p1=Complex(1,2)
    p2=3
    p3=p1.add(p2)
    print p3
