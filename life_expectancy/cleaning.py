import os
import numpy as np
import pandas as pd
import argparse
from pathlib import Path

cwd = Path(__file__).parent.parent / "data"
data_dir = os.path.join(cwd, 'data')


def split_column(df_: pd.DataFrame) -> pd.DataFrame:
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


def clean_data(region: str = "PT") -> None:
    df = pd.read_csv(os.path.join(data_dir, "eu_life_expectancy_raw.tsv"), sep="\t")
    df = split_column(df)
    df = df.melt(id_vars=["unit", "sex", "age", "region"], var_name="year", value_name="value")
    df = extract_numeric_values_from_column(df, "value")
    df = df.dropna(subset=["value"])
    df["year"] = df["year"].astype(int)
    df["value"] = df["value"].astype(float)
    df = df[df.region == region]
    df.to_csv(os.path.join(data_dir, "pt_life_expectancy.csv"), index=False)


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean life expectancy data")
    parser.add_argument("--region", default="PT", help="Region code to clean data for")
    args = parser.parse_args()
    clean_data(args.region.upper())
    clean_data()