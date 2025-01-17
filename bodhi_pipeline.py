#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Jan 16 12:07:52 2025

@author: ijeong-yeon
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/test_cleaned.xlsx')
indicators = []

# Create indicators and provide additional details as needed (Evaluation)
def descriptive_statistics(df, indicators):
    s_region = bd.Indicator(df, "Country", 0, ['3'], i_cal=None, i_type='count', description='geopolitical zone', period='endline', target = None)
    s_region.add_breakdown({'2':'Gender', 'Age Group':'Age group'})
    s_region.add_var_order(['Mali', 'Burundi', 'DRC'])
    indicators.append(s_region)
    
    s_age = bd.Indicator(df, "age group", 0, ['Age Group'], i_cal=None, i_type='count', description='age distribution', period='endline', target = None)
    s_age.add_breakdown({'2':'Gender', '3':'Country'})
    s_age.add_var_order(['18 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Above 65 years'])
    indicators.append(s_age)
    
    s_gender = bd.Indicator(df, "gender", 0, ['2'], i_cal=None, i_type='count', description='gender distribution', period='endline', target = None)
    s_gender.add_breakdown({'3':'Country', 'Age Group':'Age group'})
    s_gender.add_var_order(['Male', 'Female', 'Other', 'Prefer not to say'])
    indicators.append(s_gender)
    
    s_intervention = bd.Indicator(df, "intervention", 0, ['5'], i_cal=None, i_type='count', description='geopolitical zone', period='endline', target = None)
    s_intervention.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group'})
    indicators.append(s_intervention)
    

    s_ethnic = bd.Indicator(df, "ethnic_group", 0, ['11'], i_cal=None, i_type='count', description='geopolitical zone', period='endline', target = None)
    s_ethnic.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group'})
    s_ethnic.add_var_order(['Bambara', 'Fula', 'Soninke', 'Senufo / Bwa / Malinke','Dogon','Bobo',
                            'Songhai','Tuareg','Bantu peoples','Central Sudanic','Nilotic peoples',
                            'Ubangian','Pygmy peoples','Other_DRC','Other_mali'])
    indicators.append(s_ethnic)

    
    s_religion = bd.Indicator(df, "religion", 0, ['10'], i_cal=None, i_type='count', description='geopolitical zone', period='endline', target = None)
    s_religion.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group"})
    s_religion.add_var_order(['Christianity', 'Islam', 'Indigenous beliefs', 'Other', 'None'])
    indicators.append(s_religion)

    
    s_disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='geopolitical zone', period='endline', target = None)
    s_disability.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group", '10':"Religion"})
    s_disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(s_disability)
    
    intervention_group = bd.Indicator(df, "Invervention_group", 0, ['i_group'], i_cal=None, i_type='count', description='geopolitical zone', period='endline', target = None)
    intervention_group.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group", '10':"Religion", "Disability":"Disability"})
    indicators.append(intervention_group)
    return indicators
    

def statistical_indicators(df, indicators):
    cctd_impacts = bd.Indicator(df, "CCTD_impacts_OLS", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - OLS Test', s_test = 'ols', s_group = {'2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group", '10':"Religion", "Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(cctd_impacts)
    
    cctd_impacts2 = bd.Indicator(df, "CCTD_impacts_ANOVA", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - ANOVA Test', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group", '10':"Religion", "Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(cctd_impacts2)
    
    cctd_comp = bd.Indicator(df, "CCTD_impacts_comparision", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - Comparison', s_test = 't-test', s_group = {'i_type':'Intervention Type',"i_group":"Intervention Combination"})
    indicators.append(cctd_comp)
    
    cctd_weight = bd.Indicator(df, "CCTD_impacts_weight", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - Weights', s_test = 'ols', s_group = {"CCTD":"CCTD", 'J2H':"J2H", "TM":"TM"})
    indicators.append(cctd_weight)
    
    df_cctd = df[df['i_group'].str.contains('C', na=False)]
    df_cctd = df_cctd[df_cctd['i_type'] == 'Integration'] 
    participation_livelihood = bd.Indicator(df_cctd, "Participation_livelihood", 0, ['6'], i_cal=None, i_type='count', description='Level of Participation (by livelihood)', s_test = 'anova', s_group = {"i_group":"Intervention Combination"})
    indicators.append(participation_livelihood)

    df_cctd = df_cctd[df_cctd['i_group'].str.contains('T', na=False)]
    participation_tm = bd.Indicator(df_cctd, "Participation_TM", 0, ['6'], i_cal=None, i_type='count', description='Level of Participation (by TM)', s_test = 't-test', s_group = {"i_group":"Intervention Combination"})
    indicators.append(participation_tm)
    
    wemweb_age = bd.Indicator(df, "WEMWEB_age", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Age Group', s_test = 'anova', s_group = {'Age Group':'Age group'})
    indicators.append(wemweb_age)
    
    qols_age = bd.Indicator(df, "QOLS_age", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Age Group', s_test = 'anova', s_group = {'Age Group':'Age group'})
    indicators.append(qols_age)
    
    wemweb_gender = bd.Indicator(df, "WEMWEB_gender", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Age Group', s_test = 'anova', s_group = {'2':'Gender'})
    indicators.append(wemweb_gender)
    
    qols_gender = bd.Indicator(df, "QOLS_gender", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Age Group', s_test = 'anova', s_group = {'2':'Gender'})
    indicators.append(qols_gender)
    
    df_gbv = df[~df['gbv'].isna()]
    knowledge_level = bd.Indicator(df_gbv, "GBV_knowledge", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge', s_test = 't-test', s_group = {"gbv":"GBV Intervention Type"})
    indicators.append(knowledge_level)
    return indicators


# Create the PMF class ('Project Title', 'Evaluation')
shakshak = pmf.PerformanceManagementFramework('Shakshak', 'Evaluation')

indicators = descriptive_statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
shakshak.add_indicators(indicators)


file_path1 = 'data/Descriptive Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Test Results.xlsx'  # File path to save the statistical tests
folder = 'visuals/' # File path for saving visuals
shakshak.PMF_generation(file_path1, file_path2, folder) # Run the PMF
