import pandas as pd 

def data_ingestion():
    df = pd.read_csv("../Data/Rainfall.csv")
    return df

# Call the function and print the result
data_ingestion()
