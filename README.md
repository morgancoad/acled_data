# Analysis using Armed Conflict Location & Event Data(ACLED) and Covid19 data.

This analysis aims to understand the quantitative change in protests on a global scale. Furthermore, with this research I look to identify a correlation, or lack there of in varialbles that impact the increase/decrease of protests occuring. My original hypothesis is that the increase/decrease of social media usage will correlate with the amount of protests occuring. From there I would have liked to have analyzed which social media platforms are most used in the countries with the most protests to identify a correlation between protests occuring and the socail media platform most used in a specific country. However, I could not obtain a dataset indicating global trends on social media. 

My second course of action was to determine if the increase/decrease of Covid-19 cases correlated with protest occurence per country. The data indicates that there is a relationship between the number of protests and the amount of covid-19 cases.


## Table of Contents 
1. [Data](#data)
2. [Exploratory Data Analysis](#exploratory-data-analysis)
    - [2019-2020](#2019-2020)
    - [2020-2021](#2020-2021)
    - [2021-2022](#2021-2022)

# Data

The following datasets were obtained from [ACLED](https://acleddata.com/) and [Covid19](https://ourworldindata.org/coronavirus). 

The armed conflict data collects real-time data on the locations, dates, actors, fatalities, and types of all reported political violence and protest events around the world. ACLED has historic data dating back to 1997, however the analysis in this research is focused on data from the last 3 years(Sep2019-Sep2022). ACLED catgorizes their data into six types of events and twenty-five sub-events. 

The Covid19 data works to understand the world's largest problems in order to make progress in identifying resolutions. The Covid19 data is from Jan2020-Sep2022. For continued research the source of the Covid19 dataset updates the data daily. 

# Exploratory Data Analysis

My first objective when analyzing this dataset was to identify the quanitative change of the amount of protests each year by country. This would identify the countries with the most protests during the 3 year time period. The result from the protests that occured over the last 3 years was to much to graph on a map and simultaneously gleam insights into what the data was saying, so I broke down the data by year. This left me with data to analyze for Sep19-Sep20, Sep20-Sep21, and Sep21-Sep22. I then flitered each year by country and idnetifed the top 20 countries with the most protests that occured over the year. 

<p align="center">
<img src="Images\Protests 2019-2022.png" width = 600>
</p>

I also looked at getting the countries with the least amount of protests each year but if ACLED researches can identify single organization that conducted the protest they document the organization. However, if the people protesting are from various organizations they become protesters of the country. - Protesters(UnitedStates) or - Police Forces of Iraq - 

<p align="center">
<img src="Images\Protests 2019-2022_one.png" width = 600>
</p>

Because of this I had organizations with 1 documented protest that indicated the organization but in some cases didnt indicate the country. I chose to graph the countries with the least amount of protests but "greater than 1 protest" to mitigate some of the sole organizations as the protesters.

<p align="center">
<img src="Images\Protests_least_2019_2022.png" width = 600>
</p>

As I said before I wanted to break the data down by year to analyze it and I wanted to research indicators of a relationship or lack there of between Covid19 cases and protests.

## 2019-2020

The map below indicates the location of a documented protest as a red dot.

<p align="center">
<img src="Images\Protests_map_2019_2020.png" width = 600>
</p>

<p align="center">                                                       
<img src="Images\Protest_bar_2019_2020.png" width = 308>    
<img src="Images\Covid_bar_2019_2020.png" width = 350>  
</p>

The maroon bars in the graph on the right indicate countries that were in the top twenty for both protests occuring and Covid19 cases from Sep19-Sep20

## 2020-2021

The map below indicates the location of a documented protest as a red dot.

<p align="center">
<img src="Images\Protests_map_2020_2021.png" width = 600>
</p>

<p align="center">                                                       
<img src="Images\Protests_bar_2020_2021.png" width = 308>    
<img src="Images\Covid_bar_2020_2021.png" width = 350>  
</p>

The maroon bars in the graph on the right indicate countries that were in the top twenty for both protests occuring and Covid19 cases from Sep20-Sep21

## 2021-2022

The map below indicates the location of a documented protest as a red dot.

<p align="center">
<img src="Images\Protest_map_2021_2022.png" width = 600>
</p>

<p align="center">                                                       
<img src="Images\Protests_bar_2021_2022.png" width = 308>    
<img src="Images\Covid_bar_2021_2022.png" width = 356>  
</p>

The maroon bars in the graph on the right indicate countries that were in the top twenty for both protests occuring and Covid19 cases from Sep21-Sep22

# Conclusion/ Continuing EDA

The above analysis is indicative of a positive correlation between Covd19 cases and protests that occured. To continue to explore this theory I will use the Pearson correlation to measure the relationship. I will also add a third variable, "population" from the Covid19 dataset. 