# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:16:57 2021

@author: Mark

Using "wdir='*/Demographic_Migration_Analysis'"

Example data processing and importing. Haven't yet plotted.

"""

from src.MigrationData import MigrationData
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018, 2019]
l_year_info = [MigrationData(2010)]*len(years)

age_group_data = {}

for year in years:
    l_year_info[year-2010] = MigrationData(year)
    l_year_info[year-2010].load_dframe()
    age_group_data[year] = l_year_info[year-2010].get_age_group_data(True)
