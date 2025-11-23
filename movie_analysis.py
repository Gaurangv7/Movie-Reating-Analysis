import pandas as pd
import random

def create_dataset():
    # 1. Create a Synthetic Dataset of Movies
    data = {
        'Movie_ID': range(101, 121),
        'Title': [
            'The Galaxy Wars', 'Dark Knight Rises', 'Avengers: Endgame', 'Inception', 'Titanic',
            'The Matrix', 'Interstellar', 'Parasite', 'Joker', 'Lion King',
            'Frozen II', 'Spider-Man', 'Black Panther', 'Harry Potter', 'Jurassic World',
            'Avatar', 'Iron Man', 'Toy Story 4', 'Logan', 'Dune'
        ],
        'Genre': [
            'Sci-Fi', 'Action', 'Action', 'Sci-Fi', 'Romance',
            'Sci-Fi', 'Sci-Fi', 'Drama', 'Drama', 'Animation',
            'Animation', 'Action', 'Action', 'Fantasy', 'Adventure',
            'Sci-Fi', 'Action', 'Animation', 'Action', 'Sci-Fi'
        ],
        'IMDb_Rating': [8.8, 9.0, 8.4, 8.8, 7.8, 8.7, 8.6, 8.6, 8.4, 8.5, 7.2, 7.3, 7.3, 8.1, 7.0, 7.8, 7.9, 7.7, 8.1, 8.0],
        'Budget_Millions': [200, 250, 356, 160, 200, 63, 165, 11, 55, 45, 150, 160, 200, 125, 150, 237, 140, 200, 97, 165],
        'Box_Office_Millions': [1000, 1081, 2798, 836, 2201, 467, 701, 263, 1074, 968, 1450, 1131, 1347, 1342, 1671, 2923, 585, 1073, 619, 402]
    }

    df = pd.read_csv('movies.csv') if False else pd.DataFrame(data)
    
    # 2. Data Cleaning / Feature Engineering
    # Calculate Profit
    df['Profit_Millions'] = df['Box_Office_Millions'] - df['Budget_Millions']
    
    # ROI Calculation (Return on Investment)
    df['ROI_Percentage'] = (df['Profit_Millions'] / df['Budget_Millions']) * 100
    df['ROI_Percentage'] = df['ROI_Percentage'].round(2)

    # Categorize based on Rating
    def categorize(rating):
        if rating >= 8.5: return "Masterpiece"
        elif rating >= 7.5: return "Excellent"
        else: return "Good"
    
    df['Verdict'] = df['IMDb_Rating'].apply(categorize)

    print("Data Processing Complete...")
    print(df.head())
    
    # 3. Export to CSV for Power BI
    df.to_csv('processed_movie_data.csv', index=False)
    print("\nSUCCESS: 'processed_movie_data.csv' has been created!")

if __name__ == "__main__":
    # Run the function
    create_dataset()