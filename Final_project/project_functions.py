# # from Mrinal  https://www.kaggle.com/mrinaal007/police-shootouts (defunct)
import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import missingno as msno
import openpyxl as opxl
import xlrd
import xlwt
import xlsxwriter


def create_usrus_dataframes(civilian_df, officer_df):
    """This function takes in two usrus dataframes and cleans the dataframes from the designated source,
    creates a list of  those dataframes, and then returns that list in a from more inline with the .

    Dataset Source: https://policescorecard.org/
    Dataset Sources for complementary datasets:
    The Guardian -
    https://www.theguardian.com/us-news/ng-interactive/2015/jun/01/the-counted-police-killings-us-database
    The Washington Post -
    https://www.washingtonpost.com/graphics/investigations/police-shootings-database/

    Adapted from or inspired by the following:
    Mrinal, https://www.kaggle.com/mrinaal007/police-shootouts (defunct)
    Dataquest Labs (2019),  https://www.dataquest.io/blog/excel-and-pandas/,
    Guan. Y (2020a),
    https://github.com/iSchool-590pr/Summer2020_examples/blob/master/week_08_pandas/pandas_intro.ipynb
    Guan. Y (2020b),
    https://github.com/iSchool-590pr/Summer2020_examples/blob/master/week_09_pandas2/pandas_pt2.ipyn
    The Pandas Development Team (2020),
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
    and Weible, J (2020)

    :return: list of dataFrames

    >>>
    >>> create_usrus_dataframes(civilian_df, officer_df)

    """
    import pandas as pd # redundant?
    import missingno as msno # redundant

    civilian_df.rename(
        columns={'Included in Police Scorecard Analysis (All Incidents where Civilians were Shot '
                 'At, '
                 'Killed or Seriously Injured)?': 'included_in_scorecard'})
    officer_df.rename(
        columns={'Included in Police Scorecard Analysis (All Incidents where Civilians were Shot '
                 'At, '
                 'Killed or Seriously Injured)?': 'included_in_scorecard'})

    # check values
    print(civilian_df.dtypes)
    print(officer_df.dtypes)
    print(civilian_df.shape)
    print(officer_df.shape)

    # check head & tail
    print(civilian_df.head())
    print(civilian_df.tail())
    print(officer_df.head())
    print(officer_df.tail())


    # check missing numbers


    # concat a third combined df of both civillian and officer data, grouped by incident number
    # Question:  this may be a memory hog


    df_list = [civilian_df, officer_df]



    return df_list

# Test
# -------------
usrus_xlsx_civ = pd.read_excel('URSUS Deadly Force Incident Data, 2016-2018.csv.xlsx',
                               sheet_name='Use of Force Incident Data (URS',
                               usecols="A:K, S:W,AC, AO",
                               dtype={"Injured": "bool",
                                      "DISCHARGE_OF_FIREARM_INDIVIDUAL": "bool",
                                      "DISCHARGE_OF_FIREARM_INDIVIDUAL": "bool",
                                      "CIVILIAN_Assaulted_Officer":
                                          "bool",
                                      "CIVILIAN_Resisted": "bool"},
                               na_filter=False)

usrus_xlsx_off = pd.read_excel('URSUS Deadly Force Incident Data, 2016-2018.csv.xlsx',
                               sheet_name='Officers Involved',
                               usecols="A:K, S:W,AC, AO",
                               dtype={"Injured": "bool",
                                      "DISCHARGE_OF_FIREARM_INDIVIDUAL": "bool",
                                      "DISCHARGE_OF_FIREARM_INDIVIDUAL": "bool",
                                      "CIVILIAN_Assaulted_Officer":
                                          "bool",
                                      "CIVILIAN_Resisted": "bool"},
                               na_filter=False)

create_usrus_dataframes(usrus_xlsx_civ, usrus_xlsx_off)

