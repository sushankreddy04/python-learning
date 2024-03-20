class node:
    def __init__(self,x):
        self.data=x
        self.next=None
class link:
    def __init__(self):
        self.head=None
    def _add_front_(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
        
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def _add_back_(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp= self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def _display_(self):
        if(self.head==None):
            print("empty list")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data,end="->")
                temp=temp.next
    def _addall_(self):
        if(self.head==None):
            print("empty list")
        else:
            temp=self.head
            s=0
            while(temp!=None):
                    s=s+temp.data
                    temp=temp.next
            print(s)
    def _mid_(self):
        if(self.head==None):
            print('zero')
        else:
            tempf=self.head
            temps=self.head
            while(tempf!=None  and tempf.next!=None):
                tempf=tempf.next.next
                temps=temps.next
            print(temps.data)










l1=link()
l1._add_back_(21)
l1._add_back_(30)
l1._add_front_(32)
l1._add_back_(3)
l1._display_()
l1._mid_()







