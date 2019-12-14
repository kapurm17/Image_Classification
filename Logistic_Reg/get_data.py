import numpy as p
import pandas as pd
import matplotlib.pyplot as plt
import h5py

def get_data():
    with h5py.File("train_catvnoncat.h5", "r") as f:
        print(f.keys())
        train_X = f["train_set_x"].value
        train_y = f["train_set_y"].value

    with h5py.File("test_catvnoncat.h5", "r") as f:
        print(f.keys())
        test_X = f["test_set_x"].value
        test_y = f["test_set_y"].value

    return (train_X, train_y), (test_X, test_y)
