"""
Enums to support multiple values for a single attribute"""
from enum import Enum, unique

@unique
class Country(Enum):
    """Country Class that represents the country code acceptable for running the application"""
    AT = "AT"
    BE = "BE"
    BG = "BG"
    CH = "CH"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    EE = "EE"
    EL = "EL"
    ES = "ES"
    EU27_2020 = "EU27_2020"
    FI = "FI"
    FR = "FR"
    HR = "HR"
    HU = "HU"
    IS = "IS"
    IT = "IT"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    MT = "MT"
    NL = "NL"
    NO = "NO"
    PL = "PL"
    PT = "PT"
    RO = "RO"
    SE = "SE"
    SI = "SI"
    SK = "SK"
    DE = "DE"
    DE_TOT = "DE_TOT"
    AL = "AL"
    EA18 = "EA18"
    EA19 = "EA19"
    EFTA = "EFTA"
    IE = "IE"
    ME = "ME"
    MK = "MK"
    RS = "RS"
    AM = "AM"
    AZ = "AZ"
    GE = "GE"
    TR = "TR"
    UA = "UA"
    BY = "BY"
    EEA30_2007 = "EEA30_2007"
    EEA31 = "EEA31"
    EU27_2007 = "EU27_2007"
    EU28 = "EU28"
    UK = "UK"
    XK = "XK"
    FX = "FX"
    MD = "MD"
    SM = "SM"
    RU = "RU"

    @classmethod
    def __actual_countries__(cls):
        return [country.value for country in cls if
                len(country.value)==2 and not country.value.startswith('EU')]