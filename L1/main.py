import pandas
import numpy as np
import matplotlib.pyplot as plt


df = pandas.read_csv('C:/Users\Domin\PycharmProjects\SeriesAna0\world-happiness-report-2021.csv')

def basic_ladder_statistics():
    """
    This function prints basic statistics of the ladder score column in the dataframe

    Args:
        None
    Returns:
        None
    """
    print(df.head())
    print(df.tail())
    print(df.describe())
    mean = df['Ladder score'].mean()
    median = df['Ladder score'].median()
    st_dev = df['Ladder score'].std()
    max = df['Ladder score'].max()
    country_with_highest_score = df.loc[df['Ladder score'].idxmax()]['Country name']
    min = df['Ladder score'].min()
    country_with_lowest_score = df.loc[df['Ladder score'].idxmin()]['Country name']
    print("***Basic statistics***")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {st_dev}")
    print(f"Highest score: {max}, country: {country_with_highest_score}")
    print(f"Lowst score: {min}, country: {country_with_lowest_score}")
    print()



def top_10_ladder_countries():
    """
    This function prints the top 10 countries by ladder score

    Args:
        None
    Returns:
        None
    """
    df_sorted = df.sort_values(by='Ladder score', ascending=False)

    df_top_ten = df_sorted[['Country name', 'Ladder score']].head(10)
    print("Top ten countries by ladder scores: ")
    print(df_top_ten)
    print()


def bottom_10_ladder_countries():
    """
    This function prints the bottom 10 countries by ladder score

    Args:
        None
    Returns:
         None
    """
    df_sorted = df.sort_values(by='Ladder score', ascending=True)

    df_bottom_ten = df_sorted[['Country name', 'Ladder score']].head(10)
    print("Bottom ten countries by ladder scores: ")
    print(df_bottom_ten)
    print()

def scatter_gdp_capita_ladder():
    """
    This function creates a scatter plot of ladder score vs GDP per capita

    Args:
        None
    Returns:
        None
    """
    x = df['Logged GDP per capita']
    y = df['Ladder score']

    coefficients = np.polyfit(x, y, 1)
    poly = np.poly1d(coefficients)
    x_line = np.linspace(min(x), max(x), 100)
    y_line = poly(x_line)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="green")
    plt.plot(x_line, y_line, color="darkgreen")
    plt.xlabel('GDP per Capita')
    plt.ylabel('Ladder Score')
    plt.title('Scatter Plot of Ladder Score vs GDP per Capita with Linear Regression Line')
    plt.show()

def scatter_socialsup_ladder():
    """
    This function creates a scatter plot of ladder score vs social support

    Args:
        None
    Returns:
        None
    """
    x = df['Social support']
    y = df['Ladder score']

    coefficients = np.polyfit(x, y, 1)
    poly = np.poly1d(coefficients)
    x_line = np.linspace(min(x), max(x), 100)
    y_line = poly(x_line)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="green")
    plt.plot(x_line, y_line, color="darkgreen")
    plt.xlabel('Social support')
    plt.ylabel('Ladder Score')
    plt.title('Scatter Plot of Ladder Score vs Social support with Linear Regression Line')
    plt.show()


def scatter_freedom_ladder():
    """
    This function creates a scatter plot of ladder score vs freedom to make life choices

    Args:
        None
    Returns:
        None
    """
    x = df['Social support']
    y = df['Ladder score']

    coefficients = np.polyfit(x, y, 1)
    poly = np.poly1d(coefficients)
    x_line = np.linspace(min(x), max(x), 100)
    y_line = poly(x_line)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="green")
    plt.plot(x_line, y_line, color="darkgreen")
    plt.xlabel('Freedom to make life choices')
    plt.ylabel('Ladder Score')
    plt.title('Scatter Plot of Ladder Score vs Freedom to make life choices with Linear Regression Line')
    plt.show()


def scatter_generosity_freedom():
    """
    This function creates a scatter plot of generosity vs freedom to make life choices

    Args:
        None
    Returns:
        None
    """

    x = df['Freedom to make life choices']
    y = df['Generosity']

    coefficients = np.polyfit(x, y, 1)
    poly = np.poly1d(coefficients)
    x_line = np.linspace(min(x), max(x), 100)
    y_line = poly(x_line)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="green")
    plt.plot(x_line, y_line, color="darkgreen")
    plt.xlabel('Freedom to make life choices')
    plt.ylabel('Generosity')
    plt.title('Scatter Plot of Generosity vs Freedom to make life choices with Linear Regression Line')
    plt.show()

def scatter_health_ladder():
    """
    This function creates a scatter plot of ladder score vs healthy life expectancy

    Args:
        None
    Returns:
        None
    """
    x = df['Healthy life expectancy']
    y = df['Ladder score']

    coefficients = np.polyfit(x, y, 1)
    poly = np.poly1d(coefficients)
    x_line = np.linspace(min(x), max(x), 100)
    y_line = poly(x_line)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="green")
    plt.plot(x_line, y_line, color="darkgreen")
    plt.xlabel('Healthy life expectancy')
    plt.ylabel('Ladder Score')
    plt.title('Scatter Plot of Ladder Score vs Healthy life expectancy with Linear Regression Line')
    plt.show()



def regional_comparison_ladder():
    """
    This function prints the highest ladder score by region

    Args:
        None
    Returns:
        None
    """
    idx = df.groupby(['Regional indicator'])['Ladder score'].idxmax()
    df_max_scores = df.loc[idx]
    df_sorted = df_max_scores.sort_values(by='Ladder score', ascending=False)

    print("Highest ladder scores by region: ")
    print(df_sorted[['Regional indicator', 'Country name', 'Ladder score']])
    print()


def main():
    basic_ladder_statistics()
    top_10_ladder_countries()
    bottom_10_ladder_countries()
    regional_comparison_ladder()
    scatter_gdp_capita_ladder()
    scatter_socialsup_ladder()
    scatter_generosity_freedom()
    scatter_freedom_ladder()
    scatter_health_ladder()


main()