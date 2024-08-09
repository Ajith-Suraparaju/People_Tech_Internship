class Queue:  

  def __init__(self):  

      self.queue = list()  

  def element_add_exm(self,data):  

# Using the insert method  

      if data not in self.queue:  

          self.queue.insert(0,data)  

          return True  

      return False

# Removing elements  

  def element_remove_exm(self):  

      if len(self.queue)>0:  

          return self.queue.pop()  

      return ("Empty Queue")  

queu = Queue()  

queu.element_add_exm("A")  

queu.element_add_exm("B")  

queu.element_add_exm("C")  

queu.element_add_exm("D")  

print(queu) #To print the location of the Queue

print(queu.element_remove_exm())  

print(queu.element_remove_exm())