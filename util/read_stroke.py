import numpy as np


def read_stroke_data(data_path):
    
    stroke_info = np.load(data_path)
    return stroke_info



if __name__ == "__main__":

    dpath = "/Users/ashishperuri/Desktop/Acads/Sem3/Advanced Computer Vision/Project/dataset group/10002/d04-081/d04-0811_stroke.npy"

    sinfo = read_stroke_data(dpath)
    print(len(sinfo))
    print((sinfo).shape)
    print(type(sinfo))
    print(np.count_nonzero(sinfo))
