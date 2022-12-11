import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np
x = []
y = []

with open('python_object_files/all.obj', 'rb') as f:
# Deserialize the object and store it in a variable
    my_object = pickle.load(f)
    for i in range(len(my_object)):
        x.append(my_object[i][0])
        y.append(my_object[i][1])
    plt.scatter(x, y, color = 'b', s = 1)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), color = "r")
    plt.xlabel('Iteration number')
    plt.ylabel('Score')
    plt.title('No Pretrain', fontsize = 10)
    r2 = r2_score(x, y)
    plt.annotate('R2: ' + str(r2_score(y, p(x))), xy = (69, 750))
    plt.show()
    #print(p)

names = ["All Optimizations", "No Dueling", "No Double", "No PER", "No Pretraining"]
time = [68.9111111, 26.650556, 47.93, 67.9397222, 69.8283333]
plt.bar(names, time, color = 'b',width = 0.4)
plt.xlabel("Models")
plt.ylabel("Training time for 1500 iterations (in hrs)")
plt.title("Models vs. Training time")
plt.show()