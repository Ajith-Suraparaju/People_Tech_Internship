import queue  

queu = queue.Queue()  

queu.put(5)  

queu.put(24)  

queu.put(16)  

queu.put(33)  

queu.put(6)    

# Using bubble sort algorithm for sorting  

i =  queu.qsize()  

for x in range(i):  

    # Removing elements  

    n = queu.get()  

    for j in range(i-1):  

        # Removing elements  

        y = queu.get()  

        if n > y :  

            # putting smaller elements at beginning  

            queu.put(y)  

        else:  

            queu.put(n)  

            n = y

    queu.put(n)  

while (queu.empty() == False):   

    print(queu.queue[0], end = " ")    

    queu.get()