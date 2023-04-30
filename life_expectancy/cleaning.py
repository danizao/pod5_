import numpy as np
import pandas as pd
import argparse
import os
from pathlib import Path





# Determines the absolute path of the directory we are working on 
FILE_DIR = Path(__file__).parent

# Determines the relative path of the directory we are working on
data_dir = FILE_DIR / 'data'


def _split_column(df_: pd.DataFrame) -> pd.DataFrame:
    """splits a column into several, based on a comma separating diff values"""
    df = df_.copy()
    new_cols = df['unit,sex,age,geo\\time'].str.split(',', expand=True)
    new_cols.columns = ['unit', 'sex', 'age', 'region']
    df = pd.concat([df, new_cols], axis=1)
    df = df.drop(['unit,sex,age,geo\\time'], axis=1)
    return df


def extract_numeric_values_from_column(df_: pd.DataFrame, column: str) -> pd.DataFrame:
    """extracts numerical values from a string including several strange characteres"""
    df = df_.copy()
    df[column]= df[column].replace(to_replace=r'[^\d\.]+', value='', regex=True)
    df[column] = df[column].replace(to_replace='', value=np.nan)
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def load_data() -> pd.DataFrame:
    
    """ Load the raw data from a TSV file"""
    file_path = os.path.join(data_dir, 'eu_life_expectancy_raw.tsv')
    df = pd.read_csv(file_path, sep='\t')
    return df

def save_data(df_: pd.DataFrame, name_of_file: str) -> None:
    return df_.to_csv(os.path.join(data_dir, name_of_file), index=False)

def clean_data(df_: pd.DataFrame, region: str = "PT") -> None:
    """ receives a dataframe and do some cleaning"""

    df = df_.copy()
    df = split_column(df)
    df = df.melt(id_vars=["unit", "sex", "age", "region"], var_name="year", value_name="value")
    df = extract_numeric_values_from_column(df, "value")
    df = df.dropna(subset=["value"])
    df["year"] = df["year"].astype(int)
    df["value"] = df["value"].astype(float)
    df = df[df.region == region]
    return df

def main(region: str = "PT") -> None:
    
    df = load_data()
    df_cleaned = clean_data(df, region = region)
    save_data(df_cleaned, "pt_life_expectancy.csv")


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean life expectancy data")
    parser.add_argument("--region", default="PT", help="Region code to clean data for")
    args = parser.parse_args()
    main(region = args.region.upper())
