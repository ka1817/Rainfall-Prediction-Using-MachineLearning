from data_ingestion import data_ingestion

def preprocess():
    # Load data
    df = data_ingestion()

    # Drop rows with missing values
    df.dropna(axis=0, inplace=True)

    # Strip leading/trailing whitespace from column names
    df.columns = df.columns.str.strip()

    # Map 'rainfall' column to binary values
    df['rainfall_binary'] = df['rainfall'].map({'no': 0, 'yes': 1})

    # Columns to drop (including original 'rainfall')
    features_to_drop = ['day', 'pressure', 'maxtemp', 'mintemp', 'winddirection', 'rainfall']
    df_cleaned = df.drop(columns=features_to_drop)

    return df_cleaned

# Run this only when executing the script directly
if __name__ == "__main__":
    df_cleaned = preprocess()
    print(df_cleaned.head())  # Preview the cleaned data
