import numpy as np
import pandas as pd
import argparse
import os
from pathlib import Path

# Determines the absolute path of the directory we are working on 
FILE_DIR = Path(__file__).parent

# Determines the relative path of the directory we are working on
data_dir = FILE_DIR / 'data'

other_stuff = data_dir / "pt_life_expectancy.csv"

print(f"FILE_DIR is {FILE_DIR}")
print(f"DATA_DIR is {data_dir}")
print(f"other_stuff is {other_stuff}")
