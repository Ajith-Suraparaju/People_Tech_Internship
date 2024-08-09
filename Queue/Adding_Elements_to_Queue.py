class Queue:  

  def __init__(self):  
      self.queue = list()  

  def element_add_exm(self,data):  
# Using the insert method  

      if data not in self.queue:  
          self.queue.insert(0,data)  
          return True  
      return False   

  def leng(self):    
      return len(self.queue)   

Queue_add = Queue()  
Queue_add.element_add_exm("Mercedes Benz")  
Queue_add.element_add_exm("BMW")  
Queue_add.element_add_exm("Maserati")  
Queue_add.element_add_exm("Ferrari")
Queue_add.element_add_exm("Lamborghini")
print("Queue's Length: ",Queue_add.leng())  
