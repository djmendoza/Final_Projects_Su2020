def generate_pie_plot(user_defined_df, title_str, values_str):
    """ This function takes in a pd.DataFrame, a user defined title str, a user defined values string,
    and then parses and produces a plotly express pie chart; it then appends a prefix of the title_str
    before it returns the dataframe.

    It is designed for use with the Washington Post dataset below:
    The Washington Post -
    https://www.washingtonpost.com/graphics/investigations/police-shootings-database/

    It is designed for queries in the following format in the main():

    px_title = 'armed'
    px_value ='race'
    px_df = df[(df.armed !='unarmed') & (df.armed !='undetermined')]

    armed_df = generate_pie_plot(px_df, px_title, px_value)


    Adapted from or inspired by the following:
    Mrinal, https://www.kaggle.com/mrinaal007/police-shootouts (defunct)
    Dataquest Labs (2019),  https://www.dataquest.io/blog/excel-and-pandas/,
    Guan. Y (2020a),
    https://github.com/iSchool-590pr/Summer2020_examples/blob/master/week_08_pandas/pandas_intro.ipynb
    Guan. Y (2020b),
    https://github.com/iSchool-590pr/Summer2020_examples/blob/master/week_09_pandas2/pandas_pt2.ipyn
    The Pandas Development Team (2020),
    https://pandas.pydata.org/pandas-docs/stable/index.html
    The Data Wrangling with pandas Cheat Sheet https://pandas.pydata.org/
    Weible, J (2020),
    and many others: (https://github.com/djmendoza/Final_Projects_Su2020#references)

    :param user_defined_df: pd.DataFrame
    :param title_str: str
    :param values_str: str
    :return: pf.DataFrame
    """
    import pandas as pd
    import plotly.express as px

    user_defined_df = user_defined_df[values_str].value_counts()
    user_defined_df = pd.DataFrame(user_defined_df)
    user_defined_df = user_defined_df.reset_index()
    fig = px.pie(user_defined_df, values=values_str, names='index',
                 title="\'" + title_str + "\'" + " distribution by race",
                 color_discrete_sequence=px.colors.sequential.RdBu)
    fig.show()

    # add prefix to px_value to better reflect the data
    title_prefix = title_str + "_"
    user_defined_df = user_defined_df.add_prefix(title_prefix)

    return user_defined_df


def create_usrus_dataframes(civilian_df, officer_df):
    """This function takes in two usrus dataframes and cleans the dataframes from the designated source,
    creates a list of those dataframes, and then returns that list.

    NOTE: This function does not yet function as intended!

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
    The Data Wrangling with pandas Cheat Sheet https://pandas.pydata.org/,
    Weible, J (2020)
    many others: (https://github.com/djmendoza/Final_Projects_Su2020#references)

    :return: list of dataFrames



    """
    import pandas as pd  # redundant?
    import missingno as msno  # redundant

    civilian_df.tale

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

    # check handle missing data
    civilian_df.fillna(False)
    officer_df.fillna(False)

    # a third combined df of both civilian and officer data, grouped by incident number
    # Question:  this may be a memory hog

    df_list = [civilian_df, officer_df]

    officer_df.tale()

    return df_list


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

list = create_usrus_dataframes(usrus_xlsx_civ, usrus_xlsx_off)
usrus_officer = list[0]
usrus_officer.tale()


# From Mapping Police Violence from here: https://mappingpoliceviolence.org/
# Additional references: (https://github.com/djmendoza/Final_Projects_Su2020#references)
mpv_state_df = pd.read_excel('MPVDatasetDownload.xlsx',
                             sheet_name='2013-2019 Killings by State')



