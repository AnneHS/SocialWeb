import pandas as pd
import pickle

data_csv_path = "raw data.csv"
csv_read = pd.read_csv(data_csv_path, sep='\t')

pickle.dump( csv_read, open( "raw_data.pkl" ), 'w')