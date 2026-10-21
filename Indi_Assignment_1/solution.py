import numpy as np
import matplotlib.pyplot as plt
import csv

def load_data(filename):
    age = []
    hg  = []
    cls = []

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            age.append(int(row[0]))
            hg.append(int(row[1]))
            cls.append(int(row[2]))
    

    return age, hg, cls

def perceptron(age, hg, cls):
    random_seed = np.random.default_rng(100)
    point = []

    for i in range(len(age)):
        point.append(np.array([1, age[i], hg[i]]))

    w = random_seed.normal(size=3)

    N = 1000000

    for steps in range(N):
        i = random_seed.integers(len(age))         
        x = point[i]
        y = w[0] + w[1] * age[i] + w[2] * hg[i]

        if cls[i] == 0 and y >= 0:
            w = w - x

        if cls[i] == 1 and y < 0:
            w =  w + x

    return w[0], w[1], w[2]

if __name__ == "__main__":
    age, hg, cls = load_data("stroke_separable.csv")
    print(len(age), len(hg), len(cls))
    for x in range(len(age)):
        print(age[x], hg[x], cls[x])

    w0, w_age, w_hg = perceptron(age, hg, cls)

    print("weights:", w0, w_age, w_hg)

    mistakes = 0
    for j in range(len(age)):
        s = w0 + w_age * age[j] + w_hg * hg[j]
       
    print("mistakes:", mistakes)
