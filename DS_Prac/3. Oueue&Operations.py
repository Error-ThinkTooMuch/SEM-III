#WAP to implement Queue and its operations
class Queue():
    def __init__(self,n):
        self.n=n
        self.queue=[None]*n
        self.head=self.tail=-1
    def Enqueue(self,data):
        if(self.tail==self.n-1):
            print("Queue is full")
        elif(self.head==-1):
            self.head=0
            self.tail=0
            self.queue[self.tail]=data
        else:
            self.tail+=1
            self.queue[self.tail]=data
    def Dequeue(self):
        if(self.head==-1):
            print("Queue is empty")
        elif(self.head==self.tail):
            temp=self.queue[self.head]
            self.head=-1
            self.tail=-1
            return temp
        else:
            temp=self.queue[self.head]
            self.head+=1
            return temp
    def Display(self):
        if(self.head==-1):
            print("Empty Queue")
        else:
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end="\t")
            print()

q=Queue(7)
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
q.Enqueue(6)
q.Enqueue(7)
print("Initial Queue:")
q.Display()
q.Dequeue()
q.Dequeue()
print("Updated Queue:")
q.Display()
