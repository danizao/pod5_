from pathlib import Path
import pandas as pd
import os
from abc import ABC, abstractmethod
from life_expectancy.enums import Country

BASE_DIR = Path(__file__).parent / "data"
FIXTURES_DIR = Path(__file__).parent / "tests" / "fixtures"

class TypeStrategy(ABC):
    """
    Abstract Class to define a strategy for the type of file to be used
    """
    @abstractmethod
    def load_type(self, file: str) -> pd.DataFrame:
        """returns a Dataframe depending on the type of the file that contains the data"""

class TSVStrategy(TypeStrategy):
    """
    strategy to handle TSV files
    """
    def load_type(self, file: str) -> pd.DataFrame:
        df = pd.read_csv(BASE_DIR / file, delimiter="\t")
        return df

class JSONStrategy(TypeStrategy):
    """
    strategy to handle JSON files
    """
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

def file_type(file) -> TypeStrategy:
    available_types= {
        ".tsv": TSVStrategy(),
        ".json": JSONStrategy()
    }
    """
    this function defines what kind of strategy to be used depending on the file type
    """
    filename, file_extension = os.path.splitext(file)
    try:
        return available_types.get(file_extension)
    except Exception as exc:
        raise Exception(f"for now Only TSV or JSON files are accepted. Got {file_extension}") from exc
