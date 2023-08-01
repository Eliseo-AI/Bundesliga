Table of Content
=====================
*  [Bundesliga](#Bundesliga)
   * [Description](#Description)
   * [Datasets](#Datasets)
   * [Installation requirements](#Installation-requirements)
   * [Licensing](#Licensing)
   * [Author](#Author)
    
# Bundesliga
It is a project to analyze the basic statistics of the Bundesliga, there is information on the participating teams from the 1999-2000 season to 2022-2023, for which there are two files: Bundesliga-2023.csv and DE-2023.csv [Bundesliga](https://www.bundesliga.com/en/bundesliga)

## Description 
A work of building an interactive dashboard to provide insights about Bundesliga Results by master of digital science from the [Digital Sciences Track of Université Paris Cité](https://u-paris.fr/en/master-aire-digital-sciences/). 

## Datasets
The Bundesliga-2023.csv file has 15 columns and 433 rows, with the following information per column:
Club: Name of Club.(German Language)
Season: Period of season.
Position: Season ending position.
Win: Victories achieved during the season.
Draw: Draws achieved during the season.
Loss: Losses achieved during the season.
GF: Goals for scored during the season.
GC: Goals against conceded during the season.
GD: Goals difference during the season.
Points: Ponts earned during the season.
Q or R: Qualification for international cup or team relegation zone.
State: State of the German federal republic to which the club belongs.(German Language)
Pokal: Champion and runner-up of the German Cup.
Location: Municipality in which the club's stadium is located.
Stadium: Name of the stadium where the club plays.

The Bundesliga-2023.csv file has 20 columns and 487 rows, with the following information per column:
city: city 
lat: latitude
lng: longitude 
country: country 
iso2: State of the German federal republic to which the city belongs.
admin_name: Name of the city 
capital = city type category ("primary" = country capital, "admin" = regional capital, "minor"= metropolitan city, "" = city) 
population= population of the city. 
population_ptroper: population of the city.

## Installation Requirements
- Download Zip
```
Code - Download ZIP
```

- Clone this repository with this command
```
git clone https://github.com/Eli-2020/Bundesliga.git
```
- Install the project dependencies run pip install -r requirements.txt
```
pip install -r requirements.txt
```
- Requirements includes:
```
pandas == 1.5.3
streamlit==1.19.0
plotly==5.0.0
```
To run the streamlit code
```
streamlit run Pj-Bundesliga.py
```
## Licensing
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Author:
* **Eliseo Baquero** [@Eli-2020](https://github.com/Eli-2020)
