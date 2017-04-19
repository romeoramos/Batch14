def DrawGrid():
    row = 3
    col = 3

    x = [i % col for i in range(row*col)]
    y = [i / col for i in range(row*col)]

    
