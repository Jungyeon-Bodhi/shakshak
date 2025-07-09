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
df = pd.read_excel('data/24-TF-GLO-1 - Clean_dataset.xlsx')
indicators = []

# Create indicators and provide additional details as needed (Evaluation)
def descriptive_statistics(df, indicators):
    s_region = bd.Indicator(df, "Country", 0, ['3'], i_cal=None, i_type='count', description= "Respondents' Country", period='endline', target = None)
    s_region.add_breakdown({'2':'Gender', 'Age Group':'Age group'})
    s_region.add_var_order(['Mali', 'Burundi', 'Burkina Faso'])
    indicators.append(s_region)
    
    s_age = bd.Indicator(df, "age group", 0, ['Age Group'], i_cal=None, i_type='count', description='Respondents Age distribution', period='endline', target = None)
    s_age.add_breakdown({'2':'Gender', '3':'Country'})
    s_age.add_var_order(['17 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Above 65 years'])
    indicators.append(s_age)
    
    s_gender = bd.Indicator(df, "gender", 0, ['2'], i_cal=None, i_type='count', description='Gender distribution', period='endline', target = None)
    s_gender.add_breakdown({'3':'Country', 'Age Group':'Age group'})
    s_gender.add_var_order(['Male', 'Female'])
    indicators.append(s_gender)
    
    s_intervention = bd.Indicator(df, "intervention", 0, ['5'], i_cal=None, i_type='count', description='Intervention distribution', period='endline', target = None, visual = False)
    s_intervention.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group'})
    indicators.append(s_intervention)
    
    s_ethnic = bd.Indicator(df, "Ethnic_Mali", 0, ['11-1'], i_cal=None, i_type='count', description='Respondents Ethnic Group (Mali)', period='endline', target = None, visual = False)
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
    
    s_ethnic2 = bd.Indicator(df, "Ethnic_Burkina", 0, ['11-3'], i_cal=None, i_type='count', description='Respondents Ethnic Group (Burkina Faso)', period='endline', target = None, visual = False)
    s_ethnic2.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group'})
    s_ethnic2.add_var_order(["Mossi",
                            "Peulh",
                            "Gurunsi",
                            "Senufo",
                            "Tuareg",
                            "Samo",
                            "Kouroumba",
                            "Other"])
    indicators.append(s_ethnic2)
    
    s_ethnic3 = bd.Indicator(df, "Ethnic", 0, ['11'], i_cal=None, i_type='count', description='Respondents Ethnic Group (Overall)', period='endline', target = None, visual = False)
    s_ethnic3.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group'})
    s_ethnic3.add_var_order(["Bambara",
                            "Fula",
                            "Soninke",
                            "Senufo/Malinké",
                            "Dogon",
                            "Bobo",
                            "Songhai",
                            "Tuareg/Maure",
                            "Kassoké",
                            "Maniaka",
                            "Mossi",
                            "Peulh",
                            "Gurunsi",
                            "Senufo",
                            "Tuareg",
                            "Samo",
                            "Kouroumba",
                            "Other",
                            "Other_Mali"])
    indicators.append(s_ethnic3)

    
    s_religion = bd.Indicator(df, "religion", 0, ['10'], i_cal=None, i_type='count', description='Respondents Religion', period='endline', target = None)
    s_religion.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group"})
    s_religion.add_var_order(['Christianity', 'Islam', 'Indigenous beliefs'])
    indicators.append(s_religion)
    
    s_disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='geopolitical zone', period='endline', target = None)
    s_disability.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group", '10':"Religion"})
    s_disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(s_disability)
    
    province = bd.Indicator(df, "Province", 0, ['4'], i_cal=None, i_type='count', description='Province', period='endline', target = None, visual = False)
    province.add_breakdown({'2':'Gender', 'Age Group':'Age group',  "Disability":"Disability"})
    province.add_var_order(['Kirundo', 'Mutaho', "Matana", "Rumonge"])
    indicators.append(province)
    
    province1 = bd.Indicator(df, "Province_Burundi", 0, ['4.Burundi'], i_cal=None, i_type='count', description='Province (Burundi)', period='endline', target = None)
    province1.add_breakdown({'2':'Gender', 'Age Group':'Age group',  "Disability":"Disability"})
    province1.add_var_order(['Kirundo', 'Mutaho', "Matana", "Rumonge"])
    indicators.append(province1)
    
    province2 = bd.Indicator(df, "Province_Mali", 0, ['4.Mali'], i_cal=None, i_type='count', description='Province (Mali)', period='endline', target = None)
    province2.add_breakdown({'2':'Gender', 'Age Group':'Age group',  "Disability":"Disability"})
    province2.add_var_order(["Kayes","Hawa Dembaya", "Khouloum"])
    indicators.append(province2)
    
    province3 = bd.Indicator(df, "Province_Burkina", 0, ['4.Burkina_Faso'], i_cal=None, i_type='count', description='Province (Burkina Faso)', period='endline', target = None)
    province3.add_breakdown({'2':'Gender', 'Age Group':'Age group',  "Disability":"Disability"})
    province3.add_var_order(["Nord","Plateau Central"])
    indicators.append(province3)
    
    intervention_group = bd.Indicator(df, "Invervention_group", 0, ['i_group'], i_cal=None, i_type='count', description='geopolitical zone', period='endline', target = None, visual = False)
    intervention_group.add_breakdown({'3':'Country', '2':'Gender', 'Age Group':'Age group', '11':"Ethnic Group", '10':"Religion", "Disability":"Disability"})
    indicators.append(intervention_group)
    
    intervention_type = bd.Indicator(df, "Invervention_type", 0, ['i_type'], i_cal=None, i_type='count', description='Intervention type', period='endline', target = None)
    intervention_type.add_breakdown({'2':'Gender', 'Age Group':'Age group',  "Disability":"Disability"})
    intervention_type.add_var_order(['Integration', 'Isolation'])
    indicators.append(intervention_type)
    return indicators
    

def statistical_indicators(df, indicators):
    cctd = bd.Indicator(df, "CCTD_impacts", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', '3':"Country", 'Age Group':'Age group',  '10':"Religion","Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(cctd)
    
    wemweb = bd.Indicator(df, "WEMWBS_impacts", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', '3':"Country", 'Age Group':'Age group', '10':"Religion", "Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(wemweb)
    
    qols = bd.Indicator(df, "QOLS_impacts", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', '3':"Country", 'Age Group':'Age group', '10':"Religion", "Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(qols)
    
    df_gbv = df[~df['gbv'].isna()]
    gk = bd.Indicator(df_gbv, "GBV_knowledge_impacts", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge Impacts - Overall', s_test = 'stats', s_group = {'2':'Gender', '3':"Country",  'Age Group':'Age group', '10':"Religion", "Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(gk)
    
    cctd_impacts = bd.Indicator(df, "CCTD_impacts_OLS", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - OLS Test', s_test = 'ols', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion", "Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(cctd_impacts)
    
    cctd_impacts2 = bd.Indicator(df, "CCTD_impacts_ANOVA", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - ANOVA Test', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion", "Disability":"Disability", "i_group":"Intervention Combination", 'i_type':'Intervention Type'})
    indicators.append(cctd_impacts2)
    
    df_cctd = df[df['i_group'].str.contains('C', na=False)]
    cctd_comp = bd.Indicator(df_cctd, "CCTD_impacts_comparision", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - Comparison', s_test = 'anova', s_group = {'i_type':'Intervention Type',"i_group":"Intervention Combination"})
    indicators.append(cctd_comp)
    
    cctd_weight = bd.Indicator(df, "CCTD_impacts_weight", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - Weights', s_test = 'ols', s_group = {"CCTD":"CCTD", 'J2H':"J2H", "TM":"TM"})
    indicators.append(cctd_weight)
    
    df_j2h = df[df['i_group'].str.contains('J', na=False)]
    wemweb_j2h = bd.Indicator(df_j2h, "J2H_impacts_WEMWEB", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Intervention', s_test = 'anova', s_group = {'i_type':'Intervention Type',"i_group":"Intervention Combination"})
    indicators.append(wemweb_j2h)
    
    qols_j2h = bd.Indicator(df_j2h, "J2H_impacts_QOLS", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Intervention', s_test = 'anova', s_group = {'i_type':'Intervention Type',"i_group":"Intervention Combination"})
    indicators.append(qols_j2h)
    
    knowledge_j2h = bd.Indicator(df_j2h, "J2H_impacts_knowledge", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_Intervention', s_test = 'anova', s_group = {'i_type':'Intervention Type',"i_group":"Intervention Combination"})
    indicators.append(knowledge_j2h) 
    
    df2 = df[df['i_type'] == 'Integration']
    cctd_impacts_i = bd.Indicator(df2, "CCTD_impacts_integration", 0, ['CCTD_score'], i_cal=None, i_type='count', description='CCTD Impacts - ANOVA Test [Integration]', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion","Disability":"Disability"})
    indicators.append(cctd_impacts_i)
    
    df_integration2 = df2[df2['i_group'].str.contains('J', na=False)]
    j2h_impacts1_i = bd.Indicator(df_integration2, "J2H_impacts1_integration", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - ANOVA Test [Integration]', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion","Disability":"Disability"})
    indicators.append(j2h_impacts1_i)
    
    j2h_impacts2_i = bd.Indicator(df_integration2, "J2H_impacts2_integration", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS - ANOVA Test [Integration]', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion","Disability":"Disability"})
    indicators.append(j2h_impacts2_i) 
    
    j2h_impacts3_i = bd.Indicator(df_integration2, "J2H_impacts3_integration", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge - ANOVA Test [Integration]', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion","Disability":"Disability"})
    indicators.append(j2h_impacts3_i) 
    
    df_cctd = df[df['i_group'].str.contains('C', na=False)]
    participation_livelihood = bd.Indicator(df_cctd, "Participation_livelihood", 0, ['6'], i_cal=None, i_type='count', description='Level of Participation (by livelihood)', s_test = 't-test', s_group = {'2':'Gender', "participation_cctd":"CCTD impacts for the level of participation"})
    indicators.append(participation_livelihood)

    participation_j2h = bd.Indicator(df_j2h, "Participation_J2H", 0, ['6'], i_cal=None, i_type='count', description='Level of Participation (by J2H)', s_test = 't-test', s_group = {'2':'Gender', "participation_j2h":"J2H impacts for the level of participation"})
    indicators.append(participation_j2h)
    
    wemweb_age = bd.Indicator(df, "WEMWEB_age", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Age Group', s_test = 'anova', s_group = {'Age Group':'Age group'})
    indicators.append(wemweb_age)
    
    qols_age = bd.Indicator(df, "QOLS_age", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Age Group', s_test = 'anova', s_group = {'Age Group':'Age group'})
    indicators.append(qols_age)
    
    wemweb_gender = bd.Indicator(df, "WEMWEB_gender", 0, ['WEMWBS'], i_cal=None, i_type='count', description='WEMWBS - Gender', s_test = 't-test', s_group = {'2':'Gender'})
    indicators.append(wemweb_gender)
    
    qols_gender = bd.Indicator(df, "QOLS_gender", 0, ['QOLS'], i_cal=None, i_type='count', description='QOLS- Gender', s_test = 't-test', s_group = {'2':'Gender'})
    indicators.append(qols_gender)
    
    knowledge_level = bd.Indicator(df_gbv, "GBV_knowledge", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge', s_test = 't-test', s_group = {"gbv":"GBV Intervention Type", 'Knowledge_comp':"Participation in GBV components"})
    indicators.append(knowledge_level)
    
    knowledge_level2 = bd.Indicator(df_gbv, "GBV_knowledge2", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge2', s_test = 'anova', s_group = {'2':'Gender', 'Age Group':'Age group', '10':"Religion","Disability":"Disability"})
    indicators.append(knowledge_level2)
    
    df_gbv2 = df[~df['Knowledge_comp'].isna()]
    knowledge_level3 = bd.Indicator(df_gbv2, "GBV_knowledge3", 0, ['GBV_knowledge'], i_cal=None, i_type='count', description='GBV_knowledge: Comparison', s_test = 't-test', s_group = {'Knowledge_comp':"Participation in GBV components"})
    indicators.append(knowledge_level3)
    
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

indicators = descriptive_statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
shakshak.add_indicators(indicators)


file_path1 = 'data/24-TF-GLO-1 -Descriptive Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/24-TF-GLO-1 -Test Results.xlsx'  # File path to save the statistical tests
folder = 'visuals/' # File path for saving visuals
shakshak.PMF_generation(file_path1, file_path2, folder) # Run the PMF
