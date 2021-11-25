# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:16:57 2021

@author: Mark

Using "wdir='*/Demographic_Migration_Analysis/src'"

Basic data processing and importing. A pyplot call is used, and one image is created.

"""

from src.MigrationData import MigrationData
import pandas as pd
import matplotlib.pyplot as plt

def correct_year(year):
    '''
    Function to check the correct year s.t. it is between 2010 and 2019
    
    Parameters
    ----------
    year: int
        the int to be checked for the domain [2010,2019]
    
    Returns
    -------
    None
    '''
    assert isinstance(year, int)
    assert year <= 2019
    assert 2010 <= year 

def get_age_group_data_allyrs(years, ispercent):
    '''
    Function to get age information for all years and return it as a dict of pandas.core.frame.DataFrame
    
    Parameters
    ----------
    ispercent: bool
        whether the return type should be in percent or not
    years: tuple
        contains a tuple of ints (years)
        
    Returns
    -------
    age_group_data: dict of pandas.core.frame.DataFrame 
        dataframes for the given years
    
    '''
    assert isinstance(ispercent, bool)
    assert isinstance(years, tuple)
    l_year_info = [MigrationData(2010)]*len(years)
    age_group_data = {}
    for year in years:
        correct_year(year)
        l_year_info[year-2010] = MigrationData(year)
        l_year_info[year-2010].load_dframe()
        age_group_data[year] = l_year_info[year-2010].get_age_group_data(ispercent)
    return age_group_data

def get_age_info_years_state(data, state, years):
    '''
    Function to get all years info for a certain state. This is assumed to come after the 
    get_age_group_data_allyrs.
    
    Parameters
    ----------
    Data: dict
        dict of years of type pd.core.frame.DataFrame
    state:str
        the string of the state to be used
    years: tuple
        contains the valid years for which to be analyzed
        
    Returns
    -------
    all_years_population_data_state: pandas.core.frame.DataFrame
        the years information by age and state; the columns will be the groupings of the age 
        and the index will be the years
    '''
    #Next 4 lines are for enforcing the data model
    assert isinstance(data,dict)
    for year in years: #check the years are correct!
        correct_year(year)
        assert (state in a[year].axes[0])
    cols = ('1 to 17 years', '18 to 24 years', '25 to 54 years', '55 years and over')
    all_years_population_data_state = []
    for year in years:
        all_years_population_data_state.append(data[year].loc[state])
    all_years_population_data_state = pd.DataFrame(all_years_population_data_state,columns = cols, index = years)
    return all_years_population_data_state
    
if  __name__ == '__main__':
    years = (2010,2011,2012,2013,2014,2015,2016,2017,2018, 2019)
    keys = ('1 to 17 years', '18 to 24 years', '25 to 54 years', '55 years and over')
    a = get_age_group_data_allyrs(years,False);
    
    california_info_by_age = get_age_info_years_state(a, 'California', years)
    california_info_by_age.plot(title="California's inflow migration by age group")
    plt.show()
    plt.close("all")
