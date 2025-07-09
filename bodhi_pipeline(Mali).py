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
df = df[df['3'] == 'Mali']
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
    

    s_ethnic = bd.Indicator(df, "ethnic_group", 0, ['11-1'], i_cal=None, i_type='count', description='Respondents Ethnic Group', period='endline', target = None, visual = False)
    s_ethnic.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group'})
    s_ethnic.add_var_order(["Bambara",
                            "Fula",
                            "Soninke",
                            "Senufo/Malinké",
                            "Dogon",
                            "Bobo",
                            "Songhai",
                            "Tuareg/Maure",
                            "Kassoké",
                            "Maniaka",
                            "Other_Mali"])
    indicators.append(s_ethnic)

    
    s_religion = bd.Indicator(df, "religion", 0, ['10'], i_cal=None, i_type='count', description='Respondents Religion', period='endline', target = None)
    s_religion.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group"})
    s_religion.add_var_order(['Christianity', 'Islam', 'Indigenous beliefs', 'Other', 'None'])
    indicators.append(s_religion)

    
    s_disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='Disability Status (WG-SS)', period='endline', target = None)
    s_disability.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group'})
    s_disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(s_disability)
    
    province = bd.Indicator(df, "Province", 0, ['4.Mali'], i_cal=None, i_type='count', description='Province', period='endline', target = None)
    province.add_breakdown({'2':'Gender', 'Age Group':'Age group',  "Disability":"Disability"})
    province.add_var_order(["Kayes","Hawa Dembaya", "Khouloum"])
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
    
    wemweb = bd.Indicator(df, "WEMWBS_impacts", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', 'Age Group':'Age group',  '10':"Religion","11-1":"Ethnic","Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(wemweb)
    
    qols = bd.Indicator(df, "QOLS_impacts", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', 'Age Group':'Age group',  '10':"Religion","11-1":"Ethnic","Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(qols)
    
    df_gbv = df[~df['gbv'].isna()]
    gk = bd.Indicator(df_gbv, "GBV_knowledge_impacts", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', 'Age Group':'Age group',  '10':"Religion","11-1":"Ethnic","Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(gk)
    
    df_j2h = df[df['i_group'].str.contains('J', na=False)]
    wemweb_j2h = bd.Indicator(df_j2h, "J2H_impacts_WEMWEB", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Intervention', s_test = 't-test', s_group = {'i_type':'Intervention Type',"i_group":"Intervention Combination"})
    indicators.append(wemweb_j2h)
    
    qols_j2h = bd.Indicator(df_j2h, "J2H_impacts_QOLS", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Intervention', s_test = 't-test', s_group = {'i_type':'Intervention Type',"i_group":"Intervention Combination"})
    indicators.append(qols_j2h)
    
    knowledge_j2h = bd.Indicator(df_j2h, "J2H_impacts_knowledge", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_Intervention', s_test = 't-test', s_group = {'i_type':'Intervention Type',"i_group":"Intervention Combination"})
    indicators.append(knowledge_j2h) 
    
    df2 = df[df['i_type'] == 'Integration']
    
    df_integration2 = df2[df2['i_group'].str.contains('J', na=False)]
    j2h_impacts1_i = bd.Indicator(df_integration2, "J2H_impacts1_integration", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - ANOVA Test [Integration]', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group','10':"Religion","11-1":"Ethnic", "Disability":"Disability"})
    indicators.append(j2h_impacts1_i)
    
    j2h_impacts2_i = bd.Indicator(df_integration2, "J2H_impacts2_integration", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS - ANOVA Test [Integration]', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion","11-1":"Ethnic","Disability":"Disability"})
    indicators.append(j2h_impacts2_i) 
    
    j2h_impacts3_i = bd.Indicator(df_integration2, "J2H_impacts3_integration", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge - ANOVA Test [Integration]', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion","11-1":"Ethnic","Disability":"Disability"})
    indicators.append(j2h_impacts3_i) 
    

    participation_j2h = bd.Indicator(df_j2h, "Participation_J2H", 0, ['6'], i_cal=None, i_type='count', description='Level of Participation (by J2H)', s_test = 't-test', s_group = {"participation_j2h":"J2H impacts for the level of participation"})
    indicators.append(participation_j2h)
    
    wemweb_age = bd.Indicator(df, "WEMWEB_age", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Age Group', s_test = 'anova', s_group = {'Age Group':'Age group'})
    indicators.append(wemweb_age)
    
    qols_age = bd.Indicator(df, "QOLS_age", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Age Group', s_test = 'anova', s_group = {'Age Group':'Age group'})
    indicators.append(qols_age)
    
    wemweb_gender = bd.Indicator(df, "WEMWEB_gender", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Gender', s_test = 't-test', s_group = {'2':'Gender'})
    indicators.append(wemweb_gender)
    
    qols_gender = bd.Indicator(df, "QOLS_gender", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Gender', s_test = 't-test', s_group = {'2':'Gender'})
    indicators.append(qols_gender)
    
    knowledge_level = bd.Indicator(df_gbv, "GBV_knowledge", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge', s_test = 't-test', s_group = {"gbv":"GBV Intervention Type"})
    indicators.append(knowledge_level)
    
    knowledge_level2 = bd.Indicator(df_gbv, "GBV_knowledge2", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge2', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion","11-1":"Ethnic","Disability":"Disability"})
    indicators.append(knowledge_level2)
    
    norm_sv = bd.Indicator(df_gbv, "Norm_sviolence", 0, ['group_s_sex_violence'], i_cal=None, i_type='count', description='Social Norm: Sexual Violence', s_test = 'chi', s_group = {"gbv":"GBV Intervention Type"})
    indicators.append(norm_sv)
    
    norm_hv = bd.Indicator(df_gbv, "Norm_hviolence", 0, ['group_s_husband_violence'], i_cal=None, i_type='count', description='Social Norm: Husband Violence', s_test = 'chi', s_group = {"gbv":"GBV Intervention Type"})
    indicators.append(norm_hv)
    
    norm_phf = bd.Indicator(df_gbv, "Norm_phf", 0, ['group_s_protect_honour'], i_cal=None, i_type='count', description='Social Norm: Protecting Family Honour', s_test = 'chi', s_group = {"gbv":"GBV Intervention Type"})
    indicators.append(norm_phf)
    
    belief_sv = bd.Indicator(df_gbv, "Belief_sviolence", 0, ['group_b_sex_violence'], i_cal=None, i_type='count', description='Belief Norm: Sexual Violence', s_test = 'chi', s_group = {"gbv":"GBV Intervention Type"})
    indicators.append(belief_sv)
    
    belief_hv = bd.Indicator(df_gbv, "Belief_hviolence", 0, ['group_b_husband_violence'], i_cal=None, i_type='count', description='Belief Norm: Husband Violence', s_test = 'chi', s_group = {"gbv":"GBV Intervention Type"})
    indicators.append(belief_hv)
    
    belief_phf = bd.Indicator(df_gbv, "Belief_phf", 0, ['group_b_protect_honour'], i_cal=None, i_type='count', description='Belief Norm: Protecting Family Honour', s_test = 'chi', s_group = {"gbv":"GBV Intervention Type"})
    indicators.append(belief_phf)
    return indicators


# Create the PMF class ('Project Title', 'Evaluation')
shakshak = pmf.PerformanceManagementFramework('Shakshak', 'Evaluation')

#indicators = descriptive_statistics(df, indicators)
indicators = []
indicators = descriptive_statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
shakshak.add_indicators(indicators)


file_path1 = 'data/Descriptive Statistics_Mali.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Test Results_Mali.xlsx'  # File path to save the statistical tests
folder = 'visuals/' # File path for saving visuals
shakshak.PMF_generation(file_path1, file_path2, folder) # Run the PMF
