class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data): 
    #Complete this method
        # print(data)
        newNode = Node(data)
        if head == None:
            head = newNode
            # print(head.data)
            return head
        else:
        #Else traverse till the last node 
            last = head 
            while (last.next): 
                last = last.next
    
            #Change the next of last node 
            last.next = newNode 

            return head

        
        

        
        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 