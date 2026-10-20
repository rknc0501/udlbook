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
            age.append(int(row(0)))
            hg.append(int(row(1)))
            cls.append(int(row(2)))
    

    return age, hg, cls



if __name__ == "__main__":
    age, hg, cls = load_data("stroke_separable.csv")
    print(len(age), len(hg), len(cls))
    print(age[0], hg[0], cls[0])