import pickle

with open("test1.pkl", "wb") as f:
    my_list = list(range(1, 11))
    print(pickle.dump(my_list, f))
