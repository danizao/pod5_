import numpy as np
import pandas as pd
import argparse
import os
from pathlib import Path


def load_data(location: str, file: str, sep: str = '\c') -> pd.DataFrame:
    
    """ Load the raw data from a TSV file"""
    file_path = os.path.join(location, file)
    df = pd.read_csv(file_path, sep)
    return df

def save_data(df_: pd.DataFrame, name_of_file: str, location: str) -> None:
    return df_.to_csv(os.path.join(location, name_of_file), index=False)
