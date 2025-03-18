import pandas as pd
import numpy as np

data = {
    "Movie Title": ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5",
                    "Movie 6", "Movie 7", "Movie 8", "Movie 9", "Movie 10",
                    "Movie 11", "Movie 12", "Movie 13", "Movie 14", "Movie 15"],
    "Year": [2020, 2019, 2021, 2020, 2021, 2020, 2018, 2021, 2019, 2021, 2020, 2019, 2020, 2018, 2021],
    "Genre": ["Action", "Comedy", "Drama", "Action", "Thriller", "Drama", "Action", "Comedy", "Thriller", "Action", "Comedy", "Drama", "Thriller", "Action", "Comedy"],
    "Rating": [7.5, None, 8.2, 6.5, 7.0, 8.0, 7.8, 6.9, 7.3, 8.1, 6.8, 8.3, 7.4, 7.7, 7.2],
    "Budget": [100000, 50000, None, 120000, 80000, 150000, 200000, 120000, 95000, 180000, 110000, 130000, 105000, 150000, 100000],
    "Box Office": [2000000, 500000, 1500000, None, 1300000, 1000000, 3500000, 800000, 1100000, 2500000, 700000, 1800000, 1200000, 2200000, 950000]
}

df = pd.DataFrame(data)
print(df, "\n")

missing_data = df.isna().sum()
print(f"Missing data per column:\n{missing_data}\n")

df_cleaned = df.dropna()
print(f"Data after dropping missing rows:\n{df_cleaned}\n")

df['Rating'].fillna(df['Rating'].mean(), inplace=True)
df['Budget'].fillna(df['Budget'].mean(), inplace=True)
df['Box Office'].fillna(df['Box Office'].mean(), inplace=True)
print(f"Data after filling missing values:\n{df}\n")

movies_2020 = df.loc[df["Year"] == 2020]
print(f"Movies from 2020:\n{movies_2020}\n")

first_three_rows_first_two_cols = df.iloc[:3, :2]
print(f"First three rows and first two columns:\n{first_three_rows_first_two_cols}\n")

rating_array = np.array(df["Rating"])
budget_array = np.array(df["Budget"])
box_office_array = np.array(df["Box Office"])

average_rating = np.mean(rating_array)
print(f"Average Rating: {average_rating}\n")

total_box_office = np.sum(box_office_array)
print(f"Total Box Office: {total_box_office}\n")

movies_profit = box_office_array > budget_array
print(f"Movies with Box Office greater than Budget:\n{df['Movie Title'][movies_profit].tolist()}\n")

df['Profit'] = box_office_array - budget_array
print(f"Profits for each movie:\n{df[['Movie Title', 'Profit']]}\n")

sorted_by_rating = df.sort_values(by='Rating', ascending=False)
print(f"Movies sorted by Rating:\n{sorted_by_rating}\n")

average_rating_by_genre = df.groupby('Genre')['Rating'].mean()
print(f"Average Rating by Genre:\n{average_rating_by_genre}\n")

average_profit_by_genre = df.groupby('Genre')['Profit'].mean()
print(f"Average Profit by Genre:\n{average_profit_by_genre}\n")