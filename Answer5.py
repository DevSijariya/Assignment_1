def calcTotalTime(path):
 
    # Stores total time
    time = 0
 
    # Initial position
    x = 0
    y = 0
 
    # Stores visited segments
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
 
        # Check whether segment
        # is present in the set
        if (p + x, q + y) not in s:
            # Increment the value
            # of time by 2
            time += 2
 
            # Insert segment into the set
            s.add((p + x, q + y))
 
        else:
            time += 1
 
    # Print the value
    # of time
    print(time)
 
 
# Driver Code
if __name__ == "__main__":
 
    path = "NSE"
 
    calcTotalTime(path)