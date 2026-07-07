class Cqueue:
    def __init__(self,k):
        self.k=k
        self.queu=[None]*k
        self.front=-1
        self.rear=-1
    def display(self):
        if(self.front==-1):
            print("queue is empty")
            return
        elif self.front<=self.rear:
            for i in range(self.front,self.rear+1):
              print(self.queu[i],"->")
            return
        

        for i in range(self.front,self.k):
              print(self.queu[i],"->")
        for i in range(0,self.rear+1):
              print(self.queu[i],"->")

    def enque(self,data):
        if(((self.rear+1)%self.k)==self.front):
            print("queu is full you can imorove lenght")
        elif self.front==-1 :
            self.rear=0
            self.front=0
            self.queu[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.k
            self.queu[self.rear]=data
    def dequeu(self):
        if self.front==-1:
            return "empty"
        elif self.front==self.rear:
            t=self.queu[self.front]
            self.front=-1
            self.rear=-1
            return t
        else:
            t=self.queu[self.front]
            self.front=(self.front+1)%self.k
            return t

ki=Cqueue(3)
ki.enque("a")
ki.enque("b")
ki.enque("c")
ki.dequeu()
ki.enque("d")


ki.display()
