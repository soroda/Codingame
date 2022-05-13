while True:
    maxValue=0
    aEliminer = 0
    
    for i in range(8):
        mountain_h = int(input())
        
        if mountain_h > maxValue :
            maxValue = mountain_h
            aEliminer = i
    print(aEliminer)
