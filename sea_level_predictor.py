import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(12, 6))

    # Scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    # Line of best fit (1880 - 2050)
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years1 = pd.Series(range(1880, 2051))
    ax.plot(years1, slope1 * years1 + intercept1, color='red', label='Best Fit 1880-2050')

    # Line of best fit (2000 - 2050)
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years2 = pd.Series(range(2000, 2051))
    ax.plot(years2, slope2 * years2 + intercept2, color='green', label='Best Fit 2000-2050')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    plt.savefig('sea_level_plot.png')
    return ax
