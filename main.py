import pandas as pd
from sqlalchemy import create_engine

def main():
    # Database connection
    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

    # Read a sample of the data
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)

    # Display first rows
    print(df.head())

    # Check data types
    print(df.dtypes)

    # Check data shape
    print(df.shape)

    # Create table using pandas (it will infer types)
    # But to match the specified types, we can define dtypes
    # For simplicity, let pandas handle it

    # Read the full data in chunks
    df_iter = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', iterator=True, chunksize=100000)

    first_chunk = next(df_iter)

    # Create table with first chunk (empty to define schema)
    first_chunk.head(0).to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="replace"
    )

    print("Table created")

    # Insert first chunk
    first_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )

    print("Inserted first chunk:", len(first_chunk))

    # Insert remaining chunks
    for df_chunk in df_iter:
        df_chunk.to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="append"
        )
        print("Inserted chunk:", len(df_chunk))

if __name__ == "__main__":
    main()
