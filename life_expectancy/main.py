import pandas as pd
import argparse
from pathlib import Path
from life_expectancy.loaders import load_data, save_data
from life_expectancy.cleaning import clean_data

# Determines the absolute path of the directory we are working on 
FILE_DIR = Path(__file__).parent
print("this is the FILE_DIR", FILE_DIR)

# Determines the relative path of the directory we are working on
data_dir = FILE_DIR / 'data'
print("this is the DATA_DIR", data_dir)

def main(region: str = "PT",
         file: str = 'eu_life_expectancy_raw.tsv',
         location: str = data_dir) -> pd.DataFrame:
    
    df = load_data(file)
    df_cleaned = clean_data(df, region = region)
    save_data(df_cleaned, f"{region}_life_expectancy.csv", location)
    return df_cleaned


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean life expectancy data")
    parser.add_argument("--region", default="PT", help="Region code to clean data for")
    args = parser.parse_args()
    main(region = args.region.upper(), location = data_dir)
