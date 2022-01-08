import numpy as np
import string
import matplotlib.pyplot as plt

def look_for_start(y):
    max_abs_val = np.max(np.abs(y))
    for i in range(len(y)):
        if abs(y[i]) == max_abs_val:
            przesuniecie = i
            
    return przesuniecie

def charts(przesuniecie,y):
    look_for_start(y)
    
    x = []
    for i in range(len(y)):
        x.append(string.ascii_lowercase[i])
    x[-1] = string.ascii_lowercase[0] + "'"
    
    x_przes = x[(przesuniecie-len(x))::] + x[1:przesuniecie] + [x[(przesuniecie-len(x))] + "'"] 
    
    y_przes = y[(przesuniecie-len(x))::] + y[1:przesuniecie+1]
    
    plt.plot(x,y)
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
    plt.title('Oryginalny')
    plt.grid()
    plt.show()
    
    plt.plot(x_przes,y_przes)
    for i_x_przes, i_y_przes in zip(x_przes, y_przes):
        plt.text(i_x_przes, i_y_przes, '({}, {})'.format(i_x_przes, i_y_przes))
    plt.title("Przesuniety")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    #Data
    y = [112,-236,560,-180,348,28,424,-300,340,-540,112]
    #Charts
    charts(look_for_start(y),y) 