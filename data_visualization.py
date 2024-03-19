import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df):
    # set the style
    sns.set_style("whitegrid")

    # Histogram of company ratings
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rating'], bins=20, kde=True, color='lightgreen')
    plt.title('Distribution of Company Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.show()

    # Scatter plot of reviewers vs. ratings
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='reviewers', y='rating', data=df, color='purple', alpha=0.5)
    plt.title('Reviewers vs. Company Ratings')
    plt.xlabel('Number of Reviewers (in thousands)')
    plt.ylabel('Rating')
    plt.xscale('log')  # Using a logarithmic scale due to wide distribution of reviewer counts
    plt.show()

    # Scatter plot of age vs. reviewers
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='age', y='reviewers', data=df, color='orange', alpha=0.5)
    plt.title('Company Age vs. Number of Reviewers')
    plt.xlabel('Company Age')
    plt.ylabel('Number of Reviewers (in thousands)')
    plt.yscale('log')  # Using a logarithmic scale due to wide distribution of reviewer counts
    plt.show()
