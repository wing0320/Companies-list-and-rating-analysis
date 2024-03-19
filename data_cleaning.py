import pandas as pd
import numpy as np

# import and inspect the dataset
df = pd.read_csv('file path/1000 companies list and rating.csv')
print(df.head())

def clean_data(df):

    # cleaning the data (mainly age and review section)
    # highlight the two positive and negative reviews columns
    df = df.drop(columns=['Unnamed: 0'])

    # reviews
    df['highly_ratedFOR'] = df['highly_ratedFOR'].fillna('')
    df['critically_ratedFOR'] = df['critically_ratedFOR'].fillna('')

    # clean up age format ('# years old')
    df['age'] = df['age'].astype(str)
    df['age'] = df['age'].str.extract('(\d+)').astype(float)

    # if missing, fill in median age
    df['age'].fillna(df['age'].median(), inplace=True)

    # convert revieers to numeric values
    df['reviewers'] = df['reviewers'].apply(convert_reviewers)

    return df

def convert_reviewers(value):
    if 'k' in value:
        # Remove 'k Reviews', multiply by 1000
        return float(value.replace('k Reviews', '')) * 1000
    else:
        # Just remove ' Reviews'
        return float(value.replace(' Reviews', ''))

if __name__ == "__main__":
    # Read the dataset
    df = pd.read_csv('/Users/xiliu/my_data_science_project/1000 companies list and rating.csv')
    
    # Clean the data
    cleaned_df = clean_data(df)
    
    # Print the cleaned DataFrame
    print(cleaned_df.head())
