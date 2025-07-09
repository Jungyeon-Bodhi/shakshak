#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Jan 16 10:07:52 2025

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "Assessing the effectiveness and impact of Tearfund’s approaches to peacebuilding and sexual and gender based violence"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/24-TF-GLO-1 - Raw_dataset"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/24-TF-GLO-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

enumerator_name = ['Enumerator','4-2.Burkina','4-2.Mali', 'Enumerator Name1','Enumerator Name2']
# Original column name for enumerators' names (for anonymisation and duplicate removal)

identifiers = ['Enumerator','106', 'today', '_id', '_uuid']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = ['2025-01-06'] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['start', 'end', 'today', 'deviceid', 'audit', 'audit_URL', 'Consent1', 'Consent2','con_pic1', 'con_pic2',
 '1','2', '3', '4.Burundi', '4.Burkina_Faso', '4-1.Nord', '4-1.Plateau_Central', '4.Mali', '4-2.Burkina', '4-2.Mali',
 '5-1', '5-2', '5-3', '6', '7-0-1', '7-0-2', '7-1', '8', '9a', '9-1', '9-2', '9-3', '9-4', '9-5', '9-6', '9-7', '9-8', '9-o', '10',
 '11-1', '11-3', '11-3-o', '12', '12-1', '13', '14a', '14-1', '14-2', '14-3', '14-4', '14-5', '14-6', '14-7', '14-o',
 '15', '16', '17', '18', '19', '20', 'type_project','21', '22', '23', '24', '25',"26", '26-1', '27', '28', '29',
 '29-1', '30', '31', '32', '33', '34', '35', '36','37', '38', '39', '40', '41', '42', '43','44', '45', '46', '47',
 '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68',
 '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', "87", '88', '89', '90',
 '91', '92', '93', '94', '95', "96", "97", '98', '99', '100', '101','102', '103', '104', '105','106', 'Enumerator Name1', 
 'Enumerator Name2','old1', 'old2', 'old3','_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status', '_submitted_by', '__version__', '_tags', '_index']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['9a','14a','start','end','today','deviceid','Enumerator Name1','Enumerator Name2','Consent1', 'Consent2', 'con_pic1', 'con_pic2','old1', 'old2',
        'old3', '_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status', '_submitted_by', '__version__',
         '_tags', '_index','4-2.Burkina','4-2.Mali']
# Specify the columns to be excluded from the data analysis

miss_col = ['1', '2', '3', '6','10', '12', '15', '16','17', '18', '19', '20']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['7-1','9-o','11-3-o','12-1','14-o','26-1','28','29-1','30','32','36','38','106']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = '1'
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['15','16', '17', '18', '19', '20']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

shakshak = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, enumerator_name, identifiers, open_cols, cols_new, age_col, diss_cols, del_type = 0, file_type=file_type)
shakshak.processing()