class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def PrintList(self):
		temp = self.head
		while temp:
			print(f"DATA: {temp.data}	NEXT: {temp.next}")
			temp = temp.next

if __name__=='__main__':
	lklst = LinkedList() #initialize linked list
	
	lklst.head = Node(1) #set head and add data 1 to first node
	second = Node(2) #add data 2 to second node
	third = Node(3) #add data 3 to third node

	lklst.head.next = second #set head to point to second node
	second.next = third #set second to point to third node

	lklst.PrintList()