# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:16:57 2021

@author: Mark

Using "wdir='*/Demographic_Migration_Analysis/src'"

Basic data processing and importing. A pyplot call is used, and one image is created.

"""

from src.MigrationData import MigrationData
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np

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
    if ispercent:
        for year in years:
            correct_year(year)
            l_year_info[year-2010] = MigrationData(year)
            l_year_info[year-2010].load_dframe()
            age_group_data[year] = l_year_info[year-2010].get_age_group_data(ispercent)
        return age_group_data
    else:
        for year in years:
            correct_year(year)
            l_year_info[year-2010] = MigrationData(year)
            l_year_info[year-2010].load_dframe()
            age_group_data[year] = l_year_info[year-2010].get_age_group_data(ispercent).astype('int32')
        return age_group_data

def get_sex_group_data_allyrs(years, ispercent):
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
    if ispercent:
        for year in years:
            correct_year(year)
            l_year_info[year-2010] = MigrationData(year)
            l_year_info[year-2010].load_dframe()
            age_group_data[year] = l_year_info[year-2010].get_sex_group_data(ispercent)
        return age_group_data
    else:
        for year in years:
            correct_year(year)
            l_year_info[year-2010] = MigrationData(year)
            l_year_info[year-2010].load_dframe()
            age_group_data[year] = l_year_info[year-2010].get_sex_group_data(ispercent).astype('int32')
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
        assert (state in data[year].axes[0])
    cols = ('1 to 17 years', '18 to 24 years', '25 to 54 years', '55 years and over')
    all_years_population_data_state = []
    for year in years:
        all_years_population_data_state.append(data[year].loc[state])
    all_years_population_data_state = pd.DataFrame(all_years_population_data_state,columns = cols, index = years)
    return all_years_population_data_state
    
if  __name__ == '__main__':
    years = (2010,2011,2012,2013,2014,2015,2016,2017,2018, 2019)
    age_keys = ('1 to 17 years', '18 to 24 years', '25 to 54 years', '55 years and over')
    
    #Plotting age info for California
    age_data_allyrs = get_age_group_data_allyrs(years,False);
    #Graphing of California_migration_pyplot.png
    #california_info_by_age = get_age_info_years_state(age_data_allyrs, 'California', years)
    #plot_cali = california_info_by_age.plot(title="California's inflow migration by age group")
    for year in years:
        age_data_allyrs[year] = age_data_allyrs[year].sum()
    #Break into under 24 and over 24
    age_data_df = pd.DataFrame(age_data_allyrs.values(), index = years, columns = age_keys)
    frame_young = {age_keys[0]: age_data_df[age_keys[0]], age_keys[1]: age_data_df[age_keys[1]]}
    y_pf=pd.DataFrame(frame_young) #youth pandas dataframe
    y_plot = y_pf.plot.bar(stacked=True, title = "Youth migration follows a roughly linear path", rot = 0); 
    #y_plot means youth's plot
    y_plot.legend(loc = 'lower center')
    #y_plot.grid(axis = 'y')
    y_plot.set_ylim((2800000,3400000))
    #y_plot.spines['top'].set_visible(False)
    y_plot.ticklabel_format(axis = 'y', useMathText = True)
    y_plot.set_ylabel("Youths migrating")
    y_plot.set_xlabel("Year")
    y_plot.plot()
    
    frame_worth = {age_keys[2]: age_data_df[age_keys[2]]}
    w_df = pd.DataFrame(frame_worth)
    w_plot = w_df.plot.bar(title = "~350k increase in working class migration", rot = 0)
    w_plot.ticklabel_format(axis = 'y', useMathText = True)
    w_plot.set_xlabel("Year")
    w_plot.legend(loc = 'lower right')
    w_plot.set_ylim((2800000,3400000))
    w_plot.plot()
    
    '''#Plotting sex data, specifically the difference in the male and female migrants
    sex_data = get_sex_group_data_allyrs(years,False)
    for year in years:
        sex_data[year] = sex_data[year].sum()
    sex_data_df = pd.DataFrame(sex_data.values(), index = years, columns = ['Male', 'Female'])
    #initial_sex_dif = sex_data_df['Male'][2010] - sex_data_df['Female'][2010]
    #fin_sex_dif = sex_data_df['Male'][2019] - sex_data_df['Female'][2019]
    sex_data_df['difference'] = sex_data_df['Male'] - sex_data_df['Female']
    ax = sex_data_df['difference'].plot.bar(rot = 0, title = "Closing gap between Male and Female migrations from 2010 to 2019 in the US.")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.get_legend().remove()
    ax.set_ylabel('Total male migrants - total female migrants')
    ax.ticklabel_format(useOffset=False, style='plain', axis='y')
    ax.plot()'''
