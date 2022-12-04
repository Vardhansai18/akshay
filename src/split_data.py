import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_data( config_path ):
    config = read_params(config_path)
    train_datapath = config["split_data"]["train_path"]
    test_datapath = config["split_data"]["test_path"]
    raw_datapath = config["load_data"]["raw_data"]
    splitratio = config["split_data"]["test_size"]
    df = pd.read_csv(raw_datapath)
    train , test = train_test_split(df ,test_size= splitratio ) 
    train.to_csv(train_datapath)
    test.to_csv(test_datapath)
if __name__ == "__main__" :
    args = argparse.ArgumentParser()
    args.add_argument('--vardhan',default='params.yaml')
    parsed = args.parse_args()
    # print(parsed)
    split_data(parsed.vardhan)
