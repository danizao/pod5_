from pathlib import Path
import pandas as pd
import os
from abc import ABC, abstractmethod
from life_expectancy.enums import Country

BASE_DIR = Path(__file__).parent / "data"
FIXTURES_DIR = Path(__file__).parent / "tests" / "fixtures"

class TypeStrategy(ABC):
    @abstractmethod
    def load_type(self, file: str) -> pd.DataFrame:
        """returns a Dataframe depending on the type of the file that contains the data"""

class TSVStrategy(TypeStrategy):
    def load_type(self, file: str) -> pd.DataFrame:
        df = pd.read_csv(BASE_DIR / file, delimiter="\t")
        return df

class JSONStrategy(TypeStrategy):
    def load_type(self, file: str) -> pd.DataFrame:
        return pd.read_json(BASE_DIR / file)


def load_data(file: str) -> pd.DataFrame:
    """ load data from a file"""
    print('printing in load_data', BASE_DIR / file)
    return pd.read_csv(BASE_DIR / file, delimiter="\t")

def save_data(df: pd.DataFrame, file: str, dir: str = FIXTURES_DIR) -> None:
    """save a dataframe into a file in a directory"""
    print(os.path.join(dir, file))
    return df.to_csv(os.path.join(dir, file), index=False)

def file_type(country: Country, file) -> TypeStrategy:
    available_types= {
        ".tsv": TSVStrategy(),
        ".json": JSONStrategy()
    }
    filename, file_extension = os.path.splitext(file)
    try:
        print(file_extension)
        print(f"the strategy we will use is {available_types.get(file_extension)})")
        return available_types.get(file_extension)
    except:
        raise Exception(f"for now Only TSV or JSON files are accepted. Got {file_extension}")

