#Project - How the differing age froup populations within a country effect economic growth and the diversity in the job market
#Description - The thought I started with was that I believed that countries with a large young population are the ones
#              we should be investing in. That they will experience huge economic growth once the youth has established themselves
#              in the workplace. This project is me testng this hypothesis.
#How - The plan is to do some analysis on the United States "baby boomer" generation and see how they affected the United States
#      economy (I chose them becasue data on the United States is probably the most prevalent). I also want to do analysis on
#      international countries. For these countries though, the data on their economic development will be more sparse, so I will
#      most likely have to compare things like population, the strength of different industries, and GDP between the past and
#      present (This is essentially what I'll do with the US, but the data may not be as available with the other countries).

import os   #used for changing the working directory
import numpy as np
import pandas as pd
#changing working directory
os.chdir('C:\\Users\\ToastyJay\\Documents\\Data Sci Projects\\population-master\\population-master\\data')
import seaborn as sns
import matplotlib.pyplot as plt

globalData = pd.read_csv("population.csv")    #Reads in data from file

print("Global Data shape: ", globalData.shape)
print(globalData.head()) #prints the first 5 rows of the dataset
#using this to determine the variance in the amount of data for each country(if some have more years shown or less)
print(globalData['Country Name'].value_counts())    #displays the number of times each specific value in the data frame is present in the specified column, descending order
print("------------------------------------------------------------------------")
#Observations
#West Bank and Gaza ended up starting in 1990 and finishing in 2016
#Kuwait started in 1960 and goes to 2016, but is missing years 1992,3,4,
#Eritrea started in 1960 but only goes to 2011
#Serbia started in 1990 and goes to 2016
#Sint Maarten (Dutch Part) starts at 1998 and goes to 2016
print(globalData[globalData['Country Name'] == 'Sint Maarten (Dutch part)'])

#----------------------------------------------------------------------------------
# This function will allow me to take a larger dataset and get a smaller dataset of just the countries in a specfic continent.
# Parameters - Dataset, List containing all the countries in a specific continent
# Output - A dataset containing only the countries from a specific continent

africanCountries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon",
                    "Central African Republic", "Chad", "Comoros", "Congo", "Democratic Republic of the Congo",
                    "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia",
                    "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya",
                    "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Mozambique","Namibia", "Niger",
                    "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia",
                    "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia",
                    "Zimbabwe"]
def continentCreator(dataset, countriesList):
    continent = pd.DataFrame()  #creating an empty dataframe
    for country in countriesList:   #looping through a list to get all the different countries
        continent.append(globalData['Country Name'] == country) #adding all the corresponding rows to the dataframe
        continent.columns = ['Country Name', 'Country Code', 'Year', 'Value']   #adding headers to the column

    #This part is just for testing. I need to make sure countries aren't left out because of spelling and stuff like that
    print("Number of countries in the list: ", len(countriesList))
    print("Number of Countries in the dataset continent: ", continent.shape())
    return continent    #returning the newly created dataframe









