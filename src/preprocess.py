from data_ingestion import data_ingestion

def preprocess():
    
    df = data_ingestion()

    
    df.dropna(axis=0, inplace=True)

    
    df.columns = df.columns.str.strip()

    
    df['rainfall_binary'] = df['rainfall'].map({'no': 0, 'yes': 1})

    
    features_to_drop = ['day', 'pressure', 'maxtemp', 'mintemp', 'winddirection', 'rainfall']
    df_cleaned = df.drop(columns=features_to_drop)

    return df_cleaned

if __name__ == "__main__":
    df_cleaned = preprocess()
    print(df_cleaned.head())  
