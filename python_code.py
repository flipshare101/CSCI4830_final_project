import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import csv
import numpy as np
x = []
y = []
with open('python_object_files/all.obj', 'rb') as f:
# Deserialize the object and store it in a variable
    my_object = pickle.load(f)
    for i in range(len(my_object)):
        x.append(my_object[i][0])
        y.append(my_object[i][1])
        #writer.writerow([my_object[i][2]])
    ax = plt.subplots()
    plt.scatter(x, y, color = 'b', s = 1)
    #plt.xticks(rotation = 25)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), color = "r")
    plt.xlabel('Iteration number')
    plt.ylabel('Score')
    plt.title('all optimizations', fontsize = 10)
    r2 = r2_score(x, y)
    plt.annotate('R2: ' + str(r2_score(y, p(x))), xy = (69, 900))
    plt.show()