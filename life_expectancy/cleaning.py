import numpy as np
import pandas as pd
from pathlib import Path
from life_expectancy.loaders import load_data, save_data, TypeStrategy, TSVStrategy, JSONStrategy


# Determines the absolute path of the directory we are working on 
FILE_DIR = Path(__file__).parent

# Determines the relative path of the directory we are working on
data_dir = FILE_DIR / 'data'


def _split_column(df_: pd.DataFrame, type_strategy: TypeStrategy) -> pd.DataFrame:
    """splits a column into several, based on a comma separating diff values"""
    df = df_.copy()
    new_cols = df['unit,sex,age,geo\\time'].str.split(',', expand=True)
    new_cols.columns = ['unit', 'sex', 'age', 'region']
    df = pd.concat([df, new_cols], axis=1)
    df = df.drop(['unit,sex,age,geo\\time'], axis=1)
    df = df.melt(id_vars=["unit", "sex", "age", "region"], var_name="year", value_name="value")
    return df


def extract_numeric_values_from_column(df_: pd.DataFrame, column: str) -> pd.DataFrame:
    """extracts numerical values from a string including several strange characteres"""
    df = df_.copy()
    df[column]= df[column].replace(to_replace=r'[^\d\.]+', value='', regex=True)
    df[column] = df[column].replace(to_replace='', value=np.nan)
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df


def clean_data(df_: pd.DataFrame, region: str = "PT", type_strategy: TypeStrategy = JSONStrategy) -> None:
    """ receives a dataframe and do some cleaning"""

    df = df_.copy()
    print(df)
    if isinstance(type_strategy, TSVStrategy):
        print(f"I will be using TSVStrategy with {df}")
        df = _split_column(df, type_strategy)
    elif isinstance(type_strategy, JSONStrategy):
        print("I will be using JSONStrategy")
        df.drop(['flag', 'flag_detail'], axis=1 ,inplace=True)
        df.columns = ['unit', 'sex', 'age', 'region', 'year', 'value']
    df = extract_numeric_values_from_column(df, "value")
    df = df.dropna(subset=["value"])
    print(f"after droping i have {df}")
    df["year"] = df["year"].astype(int)
    df["value"] = df["value"].astype(float)
    print(f"before region i have {df}")
    df = df[df.region == region.value]
    print(region.value)
    print(f"after region i have {df}")
    print("before finishing clean_data, this is the dataframe", df)
    return df