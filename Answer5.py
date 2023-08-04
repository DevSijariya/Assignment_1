def calcTotalTime(path):
 
  
    time = 0
 

    x = 0
    y = 0
 
  
    s = set([])
 
    for i in range(len(path)):
 
        p = x
        q = y
 
        if (path[i] == 'N'):
            y += 1
 
        elif (path[i] == 'S'):
            y -= 1
 
        elif (path[i] == 'E'):
            x += 1
 
        elif (path[i] == 'W'):
            x -= 1
 
      
        if (p + x, q + y) not in s:
           
            time += 2
 
          
            s.add((p + x, q + y))
 
        else:
            time += 1
 
    
    print(time)
 
 

if __name__ == "__main__":
 
    path = "NSE"
 
    calcTotalTime(path)
