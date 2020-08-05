# Final_Projects_Su2020

IS590PR, Summer 2020 semester.

## Type III Project Background

Since 2015, The Washington Post ("The Post") has been building a database of fatal police shootings in the United States,
along with pertinent information relating to each incident (e.g., race of participants , gender, body-cams,
if the deceased was suffering a mental-health crisis, etc.).
According to The Post, their dataset is nearly twice the size as the official FBI dataset on the same subject, due in part to varied reporting
practices among policing agencies, as well as other factors, and notes, "5480 people have been shot and killed by police since Jan. 1, 2015" (Tate et al., 2015).

The Post recently released this dataset has recently become available for public use, and the kernel I will be reviewing and enhancing ~is~ was the top-rated kernel based
on the data. A legacy copy, as well as my annotated review copy, is included in this GitHUb Repo.  
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

## Project I will be reviewing and enhancing

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

Download a clone of the Git repository and run "👮🔫 Police Shootouts 👮🔫" from the local file location in Jupter Notebooks.

Alternatively, [the above notebook can be viewed in GitHub here](https://github.com/djmendoza/Final_Projects_Su2020/blob/master/Final_project/%F0%9F%91%AE%F0%9F%94%AB%20Police%20Shootouts%20%20%F0%9F%91%AE%F0%9F%94%AB.ipynb). (Recommended)

## Known Issues and Troubleshooting

Issue 1: The original project's plotted cells do not always post as expected when initially opening Jupyter Notebook.
- Solution: In the Jupyter Notebook dropdown menu: Select `Kernal > Restart & Run All`

Issue 2: 👮🔫 Police Shootouts 👮🔫_Original does not render correctly due when viewed through GitHub's Notebook 
- Solution: The original file contained a Table-of-Contents which does not render correctly given GitHub's lack of Extended Markup features. As such, the Table-of-Contents has been removed from the review copy for convient GitHub integration, with the lightly-altered original retained as legacy. If one needs to view the original, it should be loaded from a local clone. 

---

### References

- Bar Charts | Python | Plotly. (2020). Plotly. https://plotly.com/python/bar-charts/

- Gonzalez-Barrera, A., & Lopez, M. H. (2015, June 15). Is being Hispanic a matter of race, ethnicity or both? | Pew Research Center. Pew Research Center. https://www.pewresearch.org/fact-tank/2015/06/15/is-being-hispanic-a-matter-of-race-ethnicity-or-both/

- Guan, Y. (2020, July 7). Summer2020_examples/pandas_intro.ipynb at master · iSchool-590pr/Summer2020_examples. GitHub. https://github.com/iSchool-590pr/Summer2020_examples/blob/master/week_08_pandas/pandas_intro.ipynb

- Hunter, J., Dale, D., Droettboom, M., & Matplot Development Team. (2020, July 17). Pyplot tutorial — Matplotlib 3.3.0 documentation. https://matplotlib.org/tutorials/introductory/pyplot.html

- Jenkins, J., Rich, S., Tate, J., Muyskens, J., Fox, J., Fallis, D., & Rindler, D. (2020, July 8). Police shootings database 2015-2020 - Washington Post. Washington Post. https://www.washingtonpost.com/graphics/investigations/police-shootings-database/

- Mathieu, O. (2017). Image in markdown do not display in jupyter notebooks (#33995) · Issues · GitLab.org / GitLab FOSS · GitLab. GitLab.Org. https://gitlab.com/gitlab-org/gitlab-foss/-/issues/33995

- NetworkX Developers. (2019, October 17). Tutorial — NetworkX 2.4 documentation. NetworkX. https://networkx.github.io/documentation/stable/tutorial.html#edges

- Sierra, H. (2019, October 3). Five myths about Hispanics - The Washington Post. Washington Post. https://www.washingtonpost.com/

- Tate, J., Jenkins, J., Rich, S., Muyskens, J., Kennedy Elliott, & Mellnik, T. (2015). GitHub - washingtonpost/data-police-shootings: The Washington Post is compiling a database of every fatal shooting in the United States by a police officer in the line of duty in 2015 and 2016. The Washington Post. https://github.com/washingtonpost/data-police-shootings

- The Constitution of the United States and The Declaration of Independence. (2016). Racehorse Publishing.

- Weible, J. (2020). Program Quality and Code Reviews. https://learn.illinois.edu/pluginfile.php/6279486/mod_resource/content/2/Program Quality and Code Reviews.pdf





