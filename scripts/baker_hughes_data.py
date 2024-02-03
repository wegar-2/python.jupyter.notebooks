import os.path
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import re


def get_rig_oil_count_data(b_load_from_file: bool = True):
    if b_load_from_file:
        str_rig_count_link = os.path.join(os.getcwd(), "data", "WorldwideRigCountAug2022.xlsx")
    else:
        str_rig_count_link = "https://rigcount.bakerhughes.com/static-files/e106a3e4-ddd8-4e7d-93a3-01c3de9e7ac0"
    df = pd.read_excel(str_rig_count_link, sheet_name="Worldwide_Rigcount", header=None, skiprows=6,
                       usecols=list(range(1, 11, 1)), na_values="nan")
    # drop redundant rows
    df = df.loc[~(df.loc[:, 1].isin(["Avg."]) | df.loc[:, 1].isna()), :]
    # add columns names
    df.columns = df.loc[0, :]
    # add column with years data
    l_years = [[el]*13 for el in np.arange(2022, 1974, -1)]
    df["which_year"] = [iter_val for iter_list in l_years for iter_val in iter_list]
    # drop rows with locations
    df = df.loc[df["Europe"] != "Europe", :]
    df.rename(columns={2022: "which_month"}, inplace=True)
    # drop further redundant rows
    df = df.loc[~df["Europe"].isna(), :]
    df["which_month"] = [dt.datetime.strptime(el, "%b").month for el in df["which_month"]]

    def make_period(x):
        return pd.Period(dt.date(year=x["which_year"], month=x["which_month"], day=1), freq="M")

    df["which_yearmonth"] = df.apply(func=make_period, axis=1)
    df.drop(columns=["Total Intl.", "which_year", "which_month"], inplace=True)
    df.sort_values("which_yearmonth", ascending=True, inplace=True)
    df.rename(columns={"U.S.": "US"}, inplace=True)
    return df


df_rigs = get_rig_oil_count_data()
df_rigs.rename(
    columns=dict(zip(
        df_rigs.columns,
        [re.sub(pattern=" ", repl="_", string=el.lower()) for el in list(df_rigs.columns)])),
    inplace=True
)


def df_load_spot_oil_prices():
    str_oil_prices = os.path.join(os.getcwd(), "data", "oil_prices_eia.csv")
    df = pd.read_csv(str_oil_prices, sep=";")
    df.rename(columns={"brent_spot": "brent", "wti_spot": "wti"}, inplace=True)
    df["quote_date"] = df.apply(func=lambda x: dt.datetime.strptime(x["quote_date"], "%Y-%m-%d").date(), axis=1)
    df = df.loc[df["quote_date"] >= dt.date(year=1991, month=1, day=1), :]
    df = df.sort_values("quote_date", ascending=True)
    df.reset_index(inplace=True, drop=True)
    df[["wti", "brent"]] = df[["wti", "brent"]].fillna(method="ffill")
    df.reset_index(inplace=True, drop=True)
    return df


# calculate monthly average oil prices
df = df_load_spot_oil_prices()
df = df.assign(quote_yearmonth=[pd.Period(el, freq="M") for el in df["quote_date"]])
df_oil = df.groupby("quote_yearmonth")[["wti", "brent"]].mean()
df_oil.reset_index(inplace=True, drop=False)

df_data = pd.merge(left=df_oil, right=df_rigs, left_on="quote_yearmonth", right_on="which_yearmonth")
df_data.drop(columns=["which_yearmonth"], inplace=True)



