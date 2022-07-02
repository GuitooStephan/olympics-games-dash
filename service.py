import pandas as pd
import numpy as np


def load_data(FILE_PATH):
    df = pd.read_csv(FILE_PATH)
    df = clean_data(df)
    return df


def clean_sex(row):
    sex = row['Sex']
    if sex in ['M', 'Male']:
        return 'Male'
    elif sex in ['F', 'Female']:
        return 'Female'
    else:
        return pd.NA


def clean_data(df: pd.DataFrame):
    """
    Clean Data
    """
    _df = df.copy()
    _df['Sex'] = df.apply(clean_sex, axis=1)
    return _df


def filter_by_medal_year(df: pd.DataFrame, medal: int, year: str) -> pd.DataFrame:
    """
    Filter dataframe by medal and year
        @param df Dataframe
    """
    filtered_df = df[
        np.logical_and(
            df['Medal'] == medal, df['Year'] == int(year)
        )
    ]
    result = filtered_df
    return result


def filter_by_gender_year(df: pd.DataFrame, gender: str, year: str) -> pd.DataFrame:
    """
    Filter dataframe by gender and year
        @param df Dataframe
        @param gender str
        @param year str
    """
    filtered_df = df[
        np.logical_and(
            df['Sex'] == gender, df['Year'] == int(year)
        )
    ]
    result = filtered_df
    return result


def filter_by_year(df: pd.DataFrame, year: str) -> pd.DataFrame:
    """
    Group dataframe by year
        @param df Dataframe
        @param year Year
    """
    filtered_df = df[df['Year'] == int(year)]
    result = filtered_df
    return result


def get_medals_by_team(df: pd.DataFrame, team: str) -> pd.DataFrame:
    """
    Filter dataframe by team and year
        @param df Dataframe
        @param team str
    """
    filtered_df = df[df['Team'] == team]
    result = filtered_df.groupby('Medal').size().sort_index(ascending=False)
    return result


def group_by_team_and_sex(df: pd.DataFrame, medal, year) -> pd.DataFrame:
    """
    Group dataframe by team
        @param df Dataframe
    """
    filtered_df = df[
        np.logical_and(
            df['Medal'] == medal, df['Year'] == int(year)
        )
    ]

    top_25_countries = filtered_df.groupby(['Team']).size(
    ).sort_values(ascending=False).head(25).index.to_list()

    top_countries_df = filtered_df[filtered_df['Team'].isin(top_25_countries)]

    grouped_df = top_countries_df.groupby(
        ['Team']).size().sort_values(ascending=False)

    return grouped_df


def group_by_sport_and_sex(df: pd.DataFrame, year) -> pd.DataFrame:
    """
    Group by sport and sex
    """
    filtered_df = df[df['Year'] == int(year)]
    grouped_df = filtered_df.groupby(
        ['Sport', 'Sex']).size().sort_values(ascending=False).unstack()
    print(grouped_df)
    return grouped_df
