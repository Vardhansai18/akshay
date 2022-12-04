import os
import yaml
import pandas as pd
import argparse

def read_params(config_path ):
    with open(config_path) as f :
        config = yaml.safe_load(f) 
    return config

def get_data(config_path):
    config = read_params(config_path)
   # print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path)
    # print(df.head())
    return df
if __name__ == "__main__" :
    args = argparse.ArgumentParser()
    args.add_argument('--vardhan',default='params.yaml')
    parsed = args.parse_args()
    # print(parsed)
    get_data(parsed.vardhan)