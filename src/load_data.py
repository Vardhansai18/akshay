import os 
import argparse 
from get_data import read_params , get_data 

def load_save(config_path):
    config =  read_params(config_path)
    df = get_data(config_path)
    print( df.head() )
    raw = config["load_data"]["raw_data"]
    new_columns = [col.replace(" ",'_') for col in df.columns]
    print( new_columns )
    df.to_csv( raw )


if __name__ == "__main__" :
    args = argparse.ArgumentParser()
    args.add_argument('--vardhan',default='params.yaml')
    parsed = args.parse_args()
    # print(parsed)
    load_save(parsed.vardhan)