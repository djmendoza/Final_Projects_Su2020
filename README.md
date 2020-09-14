# Final_Projects_Su2020
**IS590PR** : Summer 2020 

**Author**: David Mendoza
**GitHub ID**: djmendoza
**Fork URL**: https://github.com/djmendoza/Final_Projects_Su2020

## Type III Project Background

Since 2015, The Washington Post ("The Post") has been building a database of fatal police shootings in the United States,
along with pertinent information relating to each incident (e.g., race of participants , gender, body-cams,
if the deceased was suffering a mental-health crisis, etc.).
According to The Post, their dataset is nearly twice the size as the official FBI dataset on the same subject, due in part to varied reporting
practices among policing agencies, as well as other factors, and notes, "5480 people have been shot and killed by police since Jan. 1, 2015" (Tate et al., 2015).

The Post recently released this dataset has recently become available for public use, and the kernel I will be reviewing and enhancing ~is~ was the top-rated kernel based
on the data. A legacy copy, as well as my annotated review copy, is included in this GitHub Repo.  
Mrinaal007's kernel uses Numpy and Pandas, as well as visualization/plotting modules (e.g., matplotlib, seaborn).

## Initial Project Hypotheses

My initial hypotheses is that there are a number of areas for analysis as that could be cleaned up as they hurt credibility.
Likewise, initial overview of the kernel seems to indicate competent use of pandas, but these are initial trouble spots for analysis or enhancement.
It looks at age, race, body-cam use, as well as other scenarios. There is a congruence with the scenario presented by The Post
(i.e., "Black Americans are killed at a much higher rate than white Americans") (Tate et al., 2020), but I suspect the other areas need review.

The Type III review will cover 3 areas relating to the project:

1. Project Code Review: A detailed review of user Mrinaal007's kernal notebook based on John Weible's *Program Quality and Code Reviews* (Weible, 2020) featuring some analysis.
2. Kaggel Project Analysis Review: An detailed analysis of one of the sections of the project, featuring an enhancement.
3. Fatal Force Database Analysis: A brief analysis of racial categories in the Washington Post's *Fatal Force* database. 

## The team member name and UID

David Mendoza

GitHub ID: djmendoza

Fork URL: https://github.com/djmendoza/Final_Projects_Su2020

## Project I have be reviewed and enhanced

Mrinaal007 (alias). (2020, July 11). 👮🔫 Police Shootouts 👮🔫. Retrieved July 27, 2020, from https://www.kaggle.com/mrinaal007/police-shootouts (now defunct)

- It appears that the user Mrninaal007 has either deleted this project or made it private; the above link returns a 404 error. As such, I have included 2 copies in this repository.
  - One is essentially an untouched version of the original Kaggle kernal with only minor changes to accommodate loading the csv from a local file.
  - The second, [located here](https://github.com/djmendoza/Final_Projects_Su2020/blob/master/Final_project/%F0%9F%91%AE%F0%9F%94%AB%20Police%20Shootouts%20%20%F0%9F%91%AE%F0%9F%94%AB.ipynb), features my review and analysis in full. 

## Kaggle kernel from this dataset

Samoshin, A. (2020, June 17). Data Police shootings. Retrieved July 27, 2020, from https://www.kaggle.com/mrmorj/data-police-shootings

### Dataset originated from this Washington Post article (may contain a paywall)

Tate, J., Jenkins, J., Rich, S., Muyskens, J., & Fox, J. (2020, January 22). Fatal Force: Police shootings database (D. Fallis & D. Rindler, Eds.). Retrieved July 27, 2020, from https://www.washingtonpost.com/graphics/investigations/police-shootings-database/

### GitHub of the Washington Post's data (includes fatal-police-shootings-data.csv)

Tate, J., Jenkins, J., Rich, S., Muyskens, J., Elliott, K., & Mellnik, T. (2015). Washingtonpost/data-police-shootings. Retrieved July 27, 2020, from https://github.com/washingtonpost/data-police-shootings

## Installation and Setup

* Download a clone of the Git repository and run "👮🔫 Police Shootouts 👮🔫" from the local file location in Jupter Notebooks (Recommended).

* Alteratively, a limited version can be previewed here at:
  * (Not Reccomended)     [nbviewer> djmendoza >Final_Projects_Su2020>Final_project>👮🔫 Police Shootouts 👮🔫.ipynb](https://nbviewer.jupyter.org/)
  * (Not Reccomended)  [Direct link (may not be up-to-date)](https://nbviewer.jupyter.org/github/djmendoza/Final_Projects_Su2020/blob/master/Final_project/%F0%9F%91%AE%F0%9F%94%AB%20Police%20Shootouts%20%20%F0%9F%91%AE%F0%9F%94%AB.ipynb)
 (See Issue 2, Below)

## Known Issues and Troubleshooting

Issue 1: The original project's plotted cells do not always post as expected when initially opening Jupyter Notebook.
- Solution: In the Jupyter Notebook dropdown menu: Select `Kernal > Restart & Run All`, or `Run` each cell individually.

Issue 2: Error when rendering at `In [56]:`
    `hm = hm.unstack()`
    `hm.style.background_gradient(cmap='Blues')`
- Solution: removed from final version; may still appear in nbviewer version.


    
---

### References

- Bar Charts | Python | Plotly. (2020). Plotly. https://plotly.com/python/bar-charts/

- Data Wrangling with pandas Cheat Sheet. (n.d.). Retrieved August 7, 2020, from http://pandas.pydata.org

- Dataquest Labs, I. (2019, June 13). Excel Tutorial for Python and Pandas – Dataquest. Dataquest. https://www.dataquest.io/blog/excel-and-pandas/

- Generate a Heatmap in MatPlotLib using Pandas Data - PythonProgramming.in. (2017). Pythonprogamming.In. https://www.pythonprogramming.in/generate-a-heatmap-in-matplotlib-using-pandas-data.html

- Gonzalez-Barrera, A., & Lopez, M. H. (2015, June 15). Is being Hispanic a matter of race, ethnicity or both? | Pew Research Center. Pew Research Center. https://www.pewresearch.org/fact-tank/2015/06/15/is-being-hispanic-a-matter-of-race-ethnicity-or-both/

- Guan, Y. (2020a, July 7). pandas_intro.ipynb. GitHub. https://github.com/iSchool-590pr/Summer2020_examples/blob/master/week_08_pandas/pandas_intro.ipynb

- Guan, Y. (2020b, July 14). Week 8 - Pandas, part 2. GitHub. 
https://github.com/iSchool-590pr/Summer2020_examples/blob/master/week_09_pandas2/pandas_pt2.ipynb

- Hunter, J., Dale, D., Droettboom, M., & Matplot Development Team. (2020, July 17). Pyplot tutorial — Matplotlib 3.3.0 documentation. https://matplotlib.org/tutorials/introductory/pyplot.html

- Jenkins, J., Rich, S., Tate, J., Muyskens, J., Fox, J., Fallis, D., & Rindler, D. (2020, July 8). Police shootings database 2015-2020 - Washington 

- Post. Washington Post. https://www.washingtonpost.com/graphics/investigations/police-shootings-database/

- Kartikaybhutani (alias). (2018, July 12). Python | Pandas Series.nunique() .  GeeksforGeeks. https://www.geeksforgeeks.org/python-pandas-series-nunique/

- Kite.com. (n.d.). How to plot a 2D heatmap from a Pandas DataFrame in Python. Kite.Com. Retrieved August 8, 2020, from https://www.kite.com/python/answers/how-to-plot-a-2d-heatmap-from-a-pandas-dataframe-in-python

- Mathieu, O. (2017). Image in markdown do not display in jupyter notebooks (#33995) · Issues · GitLab.org / GitLab FOSS · GitLab. GitLab.Org. https://gitlab.com/gitlab-org/gitlab-foss/-/issues/33995

- mrinaal007 (alias). (2020). Police Shootouts. Kaggle. https://www.kaggle.com/mrinaal007

- NetworkX Developers. (2019, October 17). Tutorial — NetworkX 2.4 documentation. NetworkX. https://networkx.github.io/documentation/stable/tutorial.html#edges

- Pandey, P. (2019, October 22). Getting more value from the Pandas’ value_counts() . Towards Data Science. https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6

- Plotly. (2020). Pie Charts | Python | Plotly. Plotly. https://plotly.com/python/pie-charts/

- Samoshin, A. (2020, June). Data Police shootings | Kaggle. https://www.kaggle.com/mrmorj/data-police-shootings/notebooks?sortBy=hotness&group=everyone&pageSize=20&datasetId=723010

- Sierra, H. (2019, October 3). Five myths about Hispanics - The Washington Post. Washington Post. https://www.washingtonpost.com/

- Sinyangwe, S. (2019). California Police Scorecard. Campaign Zero. https://policescorecard.org/

- Tate, J., Jenkins, J., Rich, S., Muyskens, J., Kennedy Elliott, & Mellnik, T. (2015). GitHub - washingtonpost/data-police-shootings: The Washington Post is compiling a database of every fatal shooting in the United States by a police officer in the line of duty in 2015 and 2016. The Washington Post. https://github.com/washingtonpost/data-police-shootings

- The Constitution of the United States and The Declaration of Independence. (2016). Racehorse Publishing.

- The Pandas Development Team. (2020, July 28). pandas.read_excel — pandas 1.1.0 documentation. Pandas. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html

- Weible, J. (2020). Program Quality and Code Reviews. https://learn.illinois.edu/pluginfile.php/6279486/mod_resource/content/2/Program Quality and Code Reviews.pdf





