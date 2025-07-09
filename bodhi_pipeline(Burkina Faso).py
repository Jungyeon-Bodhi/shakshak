#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 3 15:52:03 2025

@author: ijeong-yeon
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/24-TF-GLO-1 - Clean_dataset.xlsx')
df = df[df['3'] == 'Burkina Faso']
indicators = []

# Create indicators and provide additional details as needed (Evaluation)
def descriptive_statistics(df, indicators):

    s_age = bd.Indicator(df, "age group", 0, ['Age Group'], i_cal=None, i_type='count', description='Age distribution', period='endline', target = None)
    s_age.add_breakdown({'2':'Gender'})
    s_age.add_var_order(['17 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Above 65 years'])
    indicators.append(s_age)
    
    s_gender = bd.Indicator(df, "gender", 0, ['2'], i_cal=None, i_type='count', description='Gender distribution', period='endline', target = None)
    s_gender.add_breakdown({'Age Group':'Age group'})
    s_gender.add_var_order(['Male', 'Female'])
    indicators.append(s_gender)
    
    s_intervention = bd.Indicator(df, "intervention", 0, ['5'], i_cal=None, i_type='count', description='Intervention List', period='endline', target = None, visual = False)
    s_intervention.add_breakdown({'2':'Gender', 'Age Group':'Age group'})
    indicators.append(s_intervention)
    

    s_ethnic = bd.Indicator(df, "ethnic_group", 0, ['11-3'], i_cal=None, i_type='count', description='Respondents Ethnic Group', period='endline', target = None, visual = False)
    s_ethnic.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group'})
    s_ethnic.add_var_order(["Mossi",
                            "Peulh",
                            "Gurunsi",
                            "Senufo",
                            "Tuareg",
                            "Samo",
                            "Kouroumba",
                            "Other"])
    indicators.append(s_ethnic)

    
    s_religion = bd.Indicator(df, "religion", 0, ['10'], i_cal=None, i_type='count', description='Respondents Religion', period='endline', target = None)
    s_religion.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group"})
    s_religion.add_var_order(['Christianity', 'Islam', 'Indigenous beliefs', 'Other', 'None'])
    indicators.append(s_religion)

    
    s_disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='Disability Status (WG-SS)', period='endline', target = None)
    s_disability.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group'})
    s_disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(s_disability)
    
    province = bd.Indicator(df, "Province", 0, ['4.Burkina_Faso'], i_cal=None, i_type='count', description='Province', period='endline', target = None)
    province.add_breakdown({'2':'Gender', 'Age Group':'Age group',  "Disability":"Disability"})
    province.add_var_order(["Nord","Plateau Central"])
    indicators.append(province)
    
    intervention_group = bd.Indicator(df, "Invervention_group", 0, ['i_group'], i_cal=None, i_type='count', description='Intervention group', period='endline', target = None)
    intervention_group.add_breakdown({'2':'Gender', 'Age Group':'Age group',  "Disability":"Disability"})
    indicators.append(intervention_group)
    
    intervention_type = bd.Indicator(df, "Invervention_type", 0, ['i_type'], i_cal=None, i_type='count', description='Intervention type', period='endline', target = None)
    intervention_type.add_breakdown({'2':'Gender', 'Age Group':'Age group',  "Disability":"Disability"})
    intervention_type.add_var_order(['Integration', 'Isolation'])
    indicators.append(intervention_type)
    return indicators
    

def statistical_indicators(df, indicators):
    
    cctd = bd.Indicator(df, "CCTD_impacts", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion","11-3":"Ethnic", "Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(cctd)
    
    wemweb = bd.Indicator(df, "WEMWBS_impacts", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', 'Age Group':'Age group',  "11-3":"Ethnic","Disability":"Disability", '10':"Religion","i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(wemweb)
    
    qols = bd.Indicator(df, "QOLS_impacts", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', 'Age Group':'Age group',  "11-3":"Ethnic","Disability":"Disability", '10':"Religion","i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(qols)
    
    gk = bd.Indicator(df, "GBV_knowledge_impacts", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', 'Age Group':'Age group',  "11-3":"Ethnic","Disability":"Disability", '10':"Religion","i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(gk)
    
    cctd_impacts = bd.Indicator(df, "CCTD_impacts_OLS", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - OLS Test', s_test = 'ols', s_group = {'2':'Gender', 'Age Group':'Age group',  "11-3":"Ethnic","Disability":"Disability", '10':"Religion","i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(cctd_impacts)
    
    cctd_impacts2 = bd.Indicator(df, "CCTD_impacts_ANOVA", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - ANOVA Test', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', "11-3":"Ethnic","Disability":"Disability", '10':"Religion","i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(cctd_impacts2)
    
    df_cctd = df[df['i_group'].str.contains('C', na=False)]
    cctd_comp = bd.Indicator(df_cctd, "CCTD_impacts_comparision", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - Comparison', s_test = 't-test', s_group = {'i_type':'Intervention Type',"i_group":"Intervention Combination"})
    indicators.append(cctd_comp)
    
    cctd_weight = bd.Indicator(df, "CCTD_impacts_weight", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - Weights', s_test = 'ols', s_group = {"CCTD":"CCTD", 'J2H':"J2H", "TM":"TM"})
    indicators.append(cctd_weight)
    
    df2 = df[df['i_type'] == 'Integration']
    cctd_impacts_i = bd.Indicator(df2, "CCTD_impacts_integration", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - ANOVA Test [Integration]', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', "11-3":"Ethnic",'10':"Religion","Disability":"Disability"})
    indicators.append(cctd_impacts_i)
    
    
    df_cctd = df[df['i_group'].str.contains('C', na=False)]
    participation_livelihood = bd.Indicator(df_cctd, "Participation_livelihood", 0, ['6'], i_cal=None, i_type='count', description='Level of Participation (by livelihood)', s_test = 't-test', s_group = {"participation_cctd":"CCTD impacts for the level of participation"})
    indicators.append(participation_livelihood)

    
    wemweb_age = bd.Indicator(df, "WEMWEB_age", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Age Group', s_test = 'anova', s_group = {'Age Group':'Age group'})
    indicators.append(wemweb_age)
    
    qols_age = bd.Indicator(df, "QOLS_age", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Age Group', s_test = 'anova', s_group = {'Age Group':'Age group'})
    indicators.append(qols_age)
    
    wemweb_gender = bd.Indicator(df, "WEMWEB_gender", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Gender', s_test = 't-test', s_group = {'2':'Gender'})
    indicators.append(wemweb_gender)
    
    qols_gender = bd.Indicator(df, "QOLS_gender", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Gender', s_test = 't-test', s_group = {'2':'Gender'})
    indicators.append(qols_gender)
    
    knowledge_level2 = bd.Indicator(df, "GBV_knowledge2", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge2', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', "11-3":"Ethnic", '10':"Religion","Disability":"Disability"})
    indicators.append(knowledge_level2)
    return indicators


# Create the PMF class ('Project Title', 'Evaluation')
shakshak = pmf.PerformanceManagementFramework('Shakshak', 'Evaluation')

#indicators = descriptive_statistics(df, indicators)
indicators = []
indicators = descriptive_statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
shakshak.add_indicators(indicators)


file_path1 = 'data/Descriptive Statistics_Burkina.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Test Results_Burkina.xlsx'  # File path to save the statistical tests
folder = 'visuals/' # File path for saving visuals
shakshak.PMF_generation(file_path1, file_path2, folder) # Run the PMF
