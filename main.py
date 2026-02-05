import pandas as pd
from sqlalchemy import create_engine

def main():
    # Database connection
    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

    # Load taxi zone lookup
    print("Loading taxi zone lookup...")
    df_zones = pd.read_csv('taxi_zone_lookup.csv')
    df_zones.to_sql(name='taxi_zones', con=engine, if_exists='replace', index=False)
    print(f"Loaded {len(df_zones)} zones into taxi_zones table.")

    # Load green taxi data
    print("Loading green taxi data...")
    df_green = pd.read_parquet('green_tripdata_2025-11.parquet')
    print(f"Data shape: {df_green.shape}")
    print(df_green.head())

    # Create table and insert data in chunks to handle large data
    df_green.head(0).to_sql(name='green_taxi_trips', con=engine, if_exists='replace', index=False)
    print("Table green_taxi_trips created.")

    # Insert in chunks
    chunk_size = 100000
    for i in range(0, len(df_green), chunk_size):
        chunk = df_green.iloc[i:i+chunk_size]
        chunk.to_sql(name='green_taxi_trips', con=engine, if_exists='append', index=False)
        print(f"Inserted chunk {i//chunk_size + 1}: {len(chunk)} rows")

    print("All data loaded successfully.")

if __name__ == "__main__":
    main()
