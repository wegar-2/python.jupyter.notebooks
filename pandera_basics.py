from datetime import datetime
import pandas as pd
from pathlib import Path
import pandera as pa
from pandera.typing import Series, DateTime

# -------- pandera --------
# pd.DataFrame schemas
#   1. DataFrame schema
#   2. DataFrame model


def get_data():
    data_path: Path = Path(__file__).parent / "data" / "oil_prices_eia.csv"
    data: pd.DataFrame = pd.read_csv(
        data_path, parse_dates=["quote_date"], date_format="%Y-%m-%d", index_col=False, sep=";")
    return data


# def make_indexed_df() -> pd.DataFrame:
#     return pd.DataFrame(data={
#
#     }, index=pd.date_range(
#         start=
#     ))


class OilPricesData(pa.DataFrameModel):
    quote_date: Series[pd.Timestamp] = pa.Field(ge=pd.Timestamp(1987, 1, 1))
    wti_spot: Series[float] = pa.Field(nullable=True)
    brent_spot: Series[float] = pa.Field(nullable=True)


if __name__ == "__main__":
    data: pd.DataFrame = get_data()
    OilPricesData.validate(data)
    print(data)
