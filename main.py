import pandas as pd
from data_cleaning import clean_data
from data_visualization import create_visualizations
from word_cloud import create_word_clouds

def main():
    # Read the data
    try:
        df = pd.read_csv('1000 companies list and rating.csv')
    except FileNotFoundError:
        print("Error: Data file not found!")
        return
    
    # Clean the data
    df = clean_data(df)
    
    # Visualize the data
    create_visualizations(df)  # Pass appropriate arguments if needed
    
    # Create word clouds
    create_word_clouds(df)

if __name__ == '__main__':
    main()
