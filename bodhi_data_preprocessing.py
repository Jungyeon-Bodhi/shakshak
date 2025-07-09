#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Jan 16 09:07:52 2025

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please download following Python Libraries:
1. Pandas
2. Numpy
3. uuid
4. openpyxl
"""

import pandas as pd
import numpy as np
import uuid
from openpyxl import load_workbook

class Preprocessing:
    
    def __init__(self, name, file_path, file_path_others, list_del_cols, dates, miss_col, anon_col2, identifiers, opened_cols, cols_new, 
                 age_col = None, diss_cols = None, del_type = 0, file_type='xlsx'):
        """
        - Initialise the Performance Management Framework class

        name: str, Name of the project
        file_path: str, Directory of the raw dataset
        file_path_others: str, Directory of the opened-end questions' answers
        list_del_cols: list, Columns list for deleting
        dates: list, Dates on which the pilot test was conducted from the data
        miss_col: list, Columns list for checking missing values
        anon_col2: str, Column for anonymisation (Enumerator Name)
        identifiers: list, Columns for checking duplicates 
        opened_cols: list, Opened-end question columns
        cols_new: list, New names for the columns (for data analysis purpose)
        age_col: str, Column of age infromation (for age-grouping purpose)
        diss_cols: list, Column of WG-SS questions in the dataset (for disability-grouping purpose)
        del_type: int, [0 or 1]
        -> 0: Remove all missing values from the columns where missing values are detected
        -> 1: First, remove columns where missing values make up 10% or more of the total data points
              Then, remove all remaining missing values from the columns where they are detected
        file_type: str, filetype of the raw dataset
        """
        self.name = name
        self.file_path = file_path
        self.file_path_others = file_path_others
        self.file_type = file_type
        self.list_del_cols = list_del_cols
        self.dates = dates
        self.miss_col = miss_col
        self.anon_col2 = anon_col2
        self.identifiers = identifiers
        self.opened_cols = opened_cols
        self.cols_new = cols_new
        self.age_col = age_col
        self.diss_cols = diss_cols
        self.del_type = del_type
        self.df = None
    
    def data_load(self):
        """
        - To load a dataset
        """
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df = pd.read_excel(f"{file_path}.{file_type}")
            self.df = df
            return True
        elif file_type == 'csv':
            df = pd.read_csv(f"{file_path}.{file_type}")
            self.df = df
            return True
        else:
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        
    def delete_columns(self):
        """
        - To drop unnecessary columns
        """
        df = self.df
        list_cols = self.list_del_cols
        df = df.drop(columns = list_cols)
        df = df[~((df['4.Burkina_Faso'] == 'Plateau Central') & 
          (df['5-3'] == 'Peacebuilding project in Passoré Province for Conflict Transformation (4501, 6601, 6885)'))]
        print(f'Number of columns: {len(df.columns)} | After removing the columns that are not needed for the analysis')
        self.df = df
        return True

    def date_filter(self):
        """
        - To remove dates on which the pilot test was conducted from the dataset
        """
        df = self.df 
        dates = self.dates
        for date in dates:
            df = df[df['today'] != date]
        self.df = df
        return True
    
    def qc_checklist(self):
        """
        - To update several data points where errors occurred during the data collection process
        """     
        df = self.df
        update_condition = df['today'].isin(['2025-1-8', '2025-1-9'])
        update_value = "Improved living conditions of people living in Kirundo province by 2022 (2846) (Kirundo I)"
        df.loc[update_condition, '5-2. Which program have you participated in? (Burundi)'] = update_value
        df.loc[(df['today'] == '2025-01-13') & (df['4. Which locality do you live in? (Burundi)'] == 'Mutaho'), '4. Which locality do you live in? (Burundi)'] = 'Matana'
        df.loc[(df['today'] == '2025-01-15') & (df['4. Which locality do you live in? (Burundi)'] == 'Matana'), '4. Which locality do you live in? (Burundi)'] = 'Rumonge'
        self.df = df
        return True
        
    def missing_value_clean(self):
        """
        - To detect and remove missing values
        """
        miss_col = self.miss_col
        df = self.df
        del_type = self.del_type
        initial_data_points = len(df)
        num_missing_cols = {}
        print("")
        for col in miss_col:
            missing_count = df[col].isnull().sum()
            num_missing_cols[col] = missing_count
            print(f'Column {col} has {missing_count} missing values')
    
        if del_type == 0:
            df_cleaned = df.dropna(subset=miss_col)

        elif del_type == 1:
            threshold = 0.1 * initial_data_points
            cols_to_drop = [col for col, missing_count in num_missing_cols.items() if missing_count > threshold]
            df_cleaned = df.drop(columns=cols_to_drop)
            print("")
            print(f'Number of columns: {len(df.columns)} | After removing the columns that contained missing values more than 10% of data points')
            print(f'Dropped columns = {cols_to_drop}')
            df_cleaned = df_cleaned.dropna(subset=miss_col)
        
        remaind_data_points = len(df_cleaned)
        print("")
        print(f'Number of deleted missing values: {initial_data_points - remaind_data_points}')
        print(f"Number of data points after missing value handling: {remaind_data_points}")
        print("")
        self.df = df_cleaned
        return True
    
    def save_data(self):
        """
        - To save the new dataframe
        """
        df = self.df
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        if file_type == 'xlsx':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx' or 'csv' file")
            return False
        
    def data_anonymisation(self):
        """
        - To implement a dataframe anonymisation
        """
        df = self.df
        cols_to_anon = self.anon_col2
        file_path = self.file_path
        
        def generate_unique_strings(prefix, series):
            unique_values = series.unique()
            key_mapping = {value: f"{prefix}{uuid.uuid4()}" for value in unique_values}
            return series.map(key_mapping), key_mapping
        
        respondent_mappings = {}
        
        for col in cols_to_anon:
            df[col], mapping = generate_unique_strings(f'{col}_', df[col])
            respondent_mappings[col] = mapping
        
        original = self.file_path
        self.file_path = f'{file_path}_anonymised'
        self.save_data()
        self.file_path = original
        self.df = df
        
        print("The respondent names have been anonymised.")
        return True
    
    def duplicates(self):
        """
        - To detect and remove duplicates
        """
        df = self.df
        col = self.identifiers
        duplicates = df[df.duplicated(subset=col, keep=False)]
        print("")
        print(f"Number of duplicate based on '{col}': {len(duplicates)}")

        if not duplicates.empty:
            print("Duplicate rows:")
            print(duplicates)
    
        df_cleaned = df.drop_duplicates(subset=col, keep='first')
    
        print(f"Number of data points: {len(df_cleaned)} | After removing duplicates")
        print("")
        self.df = df_cleaned
        return True

    def open_ended_cols(self):
        """
        - To save opened-ended columns and remove these from the dataset
        """
        df = self.df
        cols = self.opened_cols
        file_path = self.file_path_others
        empty_df = pd.DataFrame()
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df.to_excel(writer, sheet_name='basic', index=False)
        
            max_length = 0
            unique_data = {}

            for col in cols:
                unique_values = df[col].dropna().unique()
                unique_data[col] = unique_values
                max_length = max(max_length, len(unique_values))
        
            combined_df = pd.DataFrame({col: pd.Series(unique_data[col]) for col in cols})
            combined_df.to_excel(writer, sheet_name='open_ended', index=False)
        
        print(f"Open-ended columns have been saved to '{file_path}': {cols} ")
        df = df.drop(columns=cols)
        print(f'Number of columns: {len(df.columns)} | After removing the open-ended columns')
        self.df = df
        return True

    def columns_redefine(self):
        """
        - To change column names for smoother data analysis
        """
        df = self.df
        new_cols = self.cols_new
        file_path = f'{self.file_path}_columns_book.xlsx'
        original_cols = list(df.columns)
        df.columns = new_cols
    
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df = pd.DataFrame()
            empty_df.to_excel(writer, sheet_name='basic', index=False)

            columns_df = pd.DataFrame({'Column Names': new_cols,'Original Names': original_cols})
        
            columns_df.to_excel(writer, sheet_name='Column_Info', index=False)

            workbook = writer.book
            worksheet = workbook['Column_Info']
        
            for col in worksheet.columns:
                max_length = max(len(str(cell.value)) for cell in col)
                adjusted_width = max(max_length, 12)
                worksheet.column_dimensions[col[0].column_letter].width = adjusted_width

        print(f"Column information has been saved: {file_path}")
        self.df = df
        return True

    def age_group(self):
        """
        - To create new age group variable
        """
        df = self.df
        col = self.age_col
        df = df[df['1'] >= 17]
        bins = [16, 24, 34, 44, 54, 64, float('inf')]
        labels = ['17 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Above 65 years']
        df[col] = df[col].astype(int)
        df['Age Group'] = pd.cut(df[col], bins=bins, labels=labels, right=True)
        print('New age group variable (Age Group) has been created in this dataset')
        self.df = df
        return True
    
    def disability_wgss(self):
        """
        - To create disability group (based on the WG-SS)
        """
        df = self.df
        cols = self.diss_cols
        try:
            df['WG-Disability'] = ''
            
            def wg_ss(row, cols):
                values = row[cols]
                some_difficulty_count = (values == 'Some difficulty').sum()
                a_lot_of_difficulty = (values == 'A lot of difficulty').any() or (values == 'Cannot do at all').any()
                cannot_do_at_all = (values == 'Cannot do at all').any()
                if cannot_do_at_all:
                    return 'DISABILITY4'
                elif a_lot_of_difficulty:
                    return 'DISABILITY3'
                elif some_difficulty_count >= 2:
                    return 'DISABILITY2'
                elif some_difficulty_count >= 1:
                    return 'DISABILITY1'
                else:
                    return 'No_disability'
            df['WG-Disability'] = df.apply(lambda row: wg_ss(row, cols), axis=1)
            df['Disability'] = df['WG-Disability'].apply(lambda x: 'Disability' if x in ['DISABILITY4', 'DISABILITY3'] else 'No Disability')
            print('New disability variable (Disability) has been created in this dataset (Based on WG-SS)')
            self.df = df
            return True
        except Exception as e:
               print('New disability variable has not been created in this dataset')

    def gbv_personal_beliefs(self):
        """
        - To create Social Norm and Beliefs about GBV Scale
        """
        df = self.df
        score_map = {'Agree with this statement':1,"I am not sure if I agree or disagree with this statement":2,'I disagree with the statement, but I am not ready to tell others':3,'I disagree with the statement, and I am telling others that this is wrong':4}
        try:
            df['b_response_sex_violence'] = 0
            df['b_husband_right_violence'] = 0
            df['b_protect_family_honour'] = 0
            
            def categorise_response(value):
                if 1 <= value < 2:
                    return 'Negative response'
                elif 2 <= value < 3:
                    return 'Moderate response'
                elif 3 <= value <= 4:
                    return 'Positive response'
                else:
                    return pd.NA
            
            def scoring_sv(row):
                score = 0
                count = 0
                columns = ['76', '77', '78', '79', '80', '81']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                        count += 1
                
                if count > 0:
                    return score / count
            
            def scoring_hr(row):
                score = 0
                count = 0
                columns = ['82', '83', '84', '85']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                        count += 1
                
                if count > 0:
                    return score / count
            
            def scoring_pf(row):
                score = 0
                count = 0
                columns = ['86', "87", '88', '89', '90']
                
                for col in columns:
                    # Check if the value exists in score_map and is not missing
                    if pd.notna(row[col]):  # Skip NaN values
                        score += score_map.get(row[col], 0)  # Add score based on score_map
                        count += 1  # Increment count of valid values
                
                # If there are any valid values, calculate the average, otherwise return 0
                if count > 0:
                    return score / count
            
            df['b_response_sex_violence'] = df.apply(scoring_sv, axis=1)
            df['b_husband_right_violence'] = df.apply(scoring_hr, axis=1)
            df['b_protect_family_honour'] = df.apply(scoring_pf, axis=1)
            df['group_b_sex_violence'] = df['b_response_sex_violence'].apply(categorise_response)
            df['group_b_husband_violence'] = df['b_husband_right_violence'].apply(categorise_response)
            df['group_b_protect_honour'] = df['b_protect_family_honour'].apply(categorise_response)
            print('New GBV Personal Beliefs variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('New GBV Attitude variable has not been created in this dataset')
               
    def gbv_social_norm(self):
        """
        - To create Social Norm and Beliefs about GBV Scale
        """
        df = self.df
        score_map = {'None of them':1,"A few of them":2,'About half of them':3,'Most of them':4, 'All of them':5}
        try:
            df['s_response_sex_violence'] = 0
            df['s_husband_right_violence'] = 0
            df['s_protect_family_honour'] = 0
            
            def categorise_response(value):
                if 1 <= value < 2.5:
                    return 'Positive response'
                elif 2.5 <= value < 3.5:
                    return 'Moderate response'
                elif 3.5 <= value <= 5:
                    return 'Negative response'
                else:
                    return pd.NA
            
            def scoring_sv(row):
                score = 0
                count = 0
                columns = ['91', '92', '93', '94', '95']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                        count += 1
                
                if count > 0:
                    return score / count
            
            def scoring_hr(row):
                score = 0
                count = 0
                columns = ["96", "97", '98', '99', '100', '101']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                        count += 1
                
                if count > 0:
                    return score / count
            
            def scoring_pf(row):
                score = 0
                count = 0
                columns = ['102', '103', '104', '105']
                
                for col in columns:
                    # Check if the value exists in score_map and is not missing
                    if pd.notna(row[col]):  # Skip NaN values
                        score += score_map.get(row[col], 0)  # Add score based on score_map
                        count += 1  # Increment count of valid values
                
                # If there are any valid values, calculate the average, otherwise return 0
                if count > 0:
                    return score / count
            
            df['s_response_sex_violence'] = df.apply(scoring_sv, axis=1)
            df['s_husband_right_violence'] = df.apply(scoring_hr, axis=1)
            df['s_protect_family_honour'] = df.apply(scoring_pf, axis=1)
            df['group_s_sex_violence'] = df['s_response_sex_violence'].apply(categorise_response)
            df['group_s_husband_violence'] = df['s_husband_right_violence'].apply(categorise_response)
            df['group_s_protect_honour'] = df['s_protect_family_honour'].apply(categorise_response)
            print('New GBV Personal Beliefs variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('New GBV Attitude variable has not been created in this dataset')

    def GBV_knowledge(self):
        """
        - To create GBV Knowledge Scale
        """
        df = self.df
        score_map = {'Strongly disagree  (I have very limited or no understanding)':1,
                     "Disagree (I have some understanding but need more clarity)":2,
                     'Neutral (I have a moderate understanding)':3,
                     'Agree (I have a good understanding)':4, 
                     'Strongly agree (I am highly knowledgeable)':5}
        try:
            df['GBV_knowledge'] = 0
            
            def scoring(row):
                score = 0
                columns = ['69', '70', '71', '72', '73', '74', '75']  
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                return score
            df['GBV_knowledge'] = df.apply(scoring, axis=1)
            df['GBV_knowledge'] = df['GBV_knowledge'].replace(0, pd.NA)
            print('New GBV knowledge Scale variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('New GBV knowledge Scale variable has not been created in this dataset')
                
    def qols(self):
        """
        - To create Quality of Life Scale
        """
        df = self.df
        score_map = {'Terrible':1,
                     "Unhappy":2,
                     'Mostly dissatisfied':3,
                     'Moderate':4, 
                     'Mostly satisfied':5,
                     'Pleased':6,
                     'Delighted':7}
        try:
            df['QOLS'] = 0
            
            def scoring(row):
                score = 0
                columns = ['53', '54', '55', '56', '57', '58', '59', '60', 
                           '61', '62', '63', '64', '65', '66', '67', '68']  
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                return score
                
            df['QOLS'] = df.apply(scoring, axis=1)
            df['QOLS'] = df['QOLS'].replace(0, pd.NA)
            print('New Quality of Life Scale variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('New Quality of Life Scale variable has not been created in this dataset')
                
    def wemwbs(self):
        """
        - To create Mental health and well-being Scale
        """
        df = self.df
        score_map = {'None of the time':1,
                     "Rarely":2,
                     'Some of the time':3,
                     'Often':4, 
                     'All of the time':5}
        try:
            df['WEMWBS'] = 0
            
            def scoring(row):
                score = 0
                columns = ['39', '40', '41', '42', '43','44', '45', '46', '47','48', '49', '50', '51', '52']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map.get(row[col], 0)
                return score
            
            df['WEMWBS'] = df.apply(scoring, axis=1)
            df['WEMWBS'] = df['WEMWBS'].replace(0, pd.NA)
            print('New Mental Well-being Scale variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('New Mental Well-being Scale variable has not been created in this dataset')

    def cctd(self):
         """
        - To calcualte the impact of CCTD intervention
         """
        
         df = self.df
         score_map1 = {'Not at all':1,
                      "Slightly increased (willing to attend joint meetings with other groups)":2,
                      'Somewhat increased (willing to communicate with other groups)':3,
                      'Increased (understand and respect to other groups)':4, 
                      'Significantly increased (able to collaborate with other groups)':5}

         score_map2 = {'Not at all':1,
                      "Slightly increased (willing to attend joint discussions with other groups)":2,
                      'Somewhat increased (willing to engage in open dialogue with other groups)':3,
                      "Increased (showing understanding and respect for other groups’ opinions)":4, 
                      'Significantly increased (collaborating effectively with other groups on common goals)':5}
         
         score_map3 = {'Yes': 2, 'No': pd.NA}
         score_map4 = {'Yes': pd.NA, 'No': 2}
                  
         try:
             df['CCTD_score'] = 0
             df['CCTD1'] = 0
             df['CCTD2'] = 0
             df['CCTD3'] = pd.NA
             df['CCTD4'] = pd.NA
             
             def scoring1(row):
                 score1 = 0
                 columns = ['22']  
                 for col in columns:
                     if pd.notna(row[col]):
                         score1 += score_map1.get(row[col], 0)
                 return score1
                 
             def scoring2(row):
                 score2 = 0
                 columns = ['23']  
                 for col in columns:
                     if pd.notna(row[col]):
                         score2 += score_map2.get(row[col], 0)
                 return score2
                 
             def scoring3(row):
                 score3 = 0
                 columns = ['33','35']  
                 for col in columns:
                     if pd.notna(row[col]):
                         score3 += score_map3.get(row[col], 0)
                 return score3
                 
             def scoring4(row):
                 score4 = 0
                 columns = ['24']  
                 for col in columns:
                     if pd.notna(row[col]):
                         score4 += score_map4.get(row[col], 0)
                 return score4
                 
             df['CCTD1'] = df.apply(scoring1, axis=1)
             df['CCTD2'] = df.apply(scoring2, axis=1)
             df['CCTD3'] = df.apply(scoring3, axis=1)
             df['CCTD4'] = df.apply(scoring4, axis=1)
             df['CCTD_score'] = df['CCTD1'] + df['CCTD2'] + df['CCTD3'] + df['CCTD4']
             df['CCTD_score'] = df['CCTD_score'].replace(0, pd.NA)
             df.drop(columns = ['CCTD1', 'CCTD2', 'CCTD3', 'CCTD4'], inplace = True)
             print('New CCTD outcome variable has been created in this dataset')
             self.df = df
             return True
         except Exception as e:
                print('New CCTD outcome variable has not been created in this dataset')

    def grouping(self):
        df = self.df
        df['4'] = df[['4.Burundi','4.Burkina_Faso', '4.Mali']].bfill(axis=1).iloc[:, 0]
        df['Enumerator'] = df[['4-2.Burkina','4-2.Mali', 'Enumerator Name1','Enumerator Name2']].bfill(axis=1).iloc[:, 0]
        df['5'] = df[['5-1', '5-2', '5-3']].bfill(axis=1).iloc[:, 0]
        df['7'] = df[['7-0-1', '7-0-2']].bfill(axis=1).iloc[:, 0]
        df['11'] = df[['11-1', '11-3']].bfill(axis=1).iloc[:, 0]
        self.df = df
        
    def project_update(self):
        df = self.df
    
        col = '5-3'
    
        replacements = {
            r'^Year [12] - Peacebuilding project in Passoré Province for Conflict Transformation \(4501, 6601, 6885\)$':
                'Peacebuilding project in Passoré Province for Conflict Transformation (4501, 6601, 6885)',
            r'^Year [123] - Food and Nutritional Resilience Project Year 1 \(4402, 6184, 6882\)$':
                'Food and Nutritional Resilience Project (4402, 6184, 6882)',}
    
        for pattern, replacement in replacements.items():
            df[col] = df[col].str.replace(pattern, replacement, regex=True)
    
        self.df = df
        return True

    def interventions(self):
        """
        - To assgin each intervention to data points
        """
        df = self.df
        df['CCTD'] = 0
        df['J2H'] = 0
        df['TM'] = 0
        cctd = ["WA STAY Project - Mali (4192)","Peacebuilding project (2428) (Matana)",
                "Improved living conditions of people living in Kirundo province by 2022 (2846) (Kirundo I)",
                "Integrated Sexual and gender Based Violence Project (3394) (Rumonge I)",
                "Integrated Fragile States Programme in Burundi (4107) (All)",
                "Environment Restoration for Innovative Community Entrepreneurship(ERICEP) (2705) (Mutaho I)",
                "Engaging the youth and faith leaders in peacebuilding; prevention and response to SGBV for peaceful coexistence (4535)",
                "Artisanes de Paix: Setting inclusive Peacebuilding Networks in Tanganyika and addressing land issues (4280)",
                "Commitment of young people and religious leaders for peaceful cohabitation and transformation (6205)",
                "Peacebuilding project in Passoré Province for Conflict Transformation (4501, 6601, 6885)",
                "Food and Nutritional Resilience Project (4402, 6184, 6882)",
                "Souter Project for the promotion of peace and gender positive norms in Zorgho and Boudry communities (6423)"]
     
        j2h = ["Diocese de Matana, Development Programme (2695) (Matana II)",
                "Integrated Sexual and gender Based Violence Project (3391)",
                "Integrated Sexual and gender Based Violence Project (3394) (Rumonge I)",
                "Integrated Fragile States Programme in Burundi (4107) (All)",
                "Environment Restoration for Innovative Community Entrepreneurship(ERICEP) (2705) (Mutaho I)",
                "Projet Multisectoriel pour l’amélioration des conditions de vie et la promotion de la santé de la femme, de la jeune fille et de l’enfant à Kayes",
                "Projet de renforcement et d'amélioration des conditions de vie sociale et de santé des populations les plus vulnérables à Kayes",
                "Project for the Reduction of SGBV/FGM/MP and the Strengthening of Gender Relations"]
        
        tm = ["WA STAY Project - Mali (4192)",
              "Integrated Sexual and gender Based Violence Project (3391)",
                "Integrated Sexual and gender Based Violence Project (3394) (Rumonge I)",
                "Integrated Fragile States Programme in Burundi (4107) (All)",
                "Environment Restoration for Innovative Community Entrepreneurship(ERICEP) (2705) (Mutaho I)",
                "Engaging the youth and faith leaders in peacebuilding; prevention and response to SGBV for peaceful coexistence (4535)",
                "Artisanes de Paix: Setting inclusive Peacebuilding Networks in Tanganyika and addressing land issues (4280)",
                "Commitment of young people and religious leaders for peaceful cohabitation and transformation (6205)",
                "Souter Project for the promotion of peace and gender positive norms in Zorgho and Boudry communities (6423)",
                "Project for the Reduction of SGBV/FGM/MP and the Strengthening of Gender Relations"]

        df['CCTD'] = df['5'].apply(lambda row: 1 if any(project in row for project in cctd) else 0)
        df['J2H'] = df['5'].apply(lambda row: 1 if any(project in row for project in j2h) else 0)
        df['TM'] = df['5'].apply(lambda row: 1 if any(project in row for project in tm) else 0)                         
        df = self.df
        
    def intervention_group(self):
        """
        - To group the interventions
        """
        df = self.df
        df['i_group'] = ""
        df['i_group'] = df.apply(lambda row: f"{('C' if row['CCTD'] == 1 else '')}" +
                        f"{('J' if row['J2H'] == 1 else '')}" +
                        f"{('T' if row['TM'] == 1 else '')}",axis=1)
        
        df['i_type'] = df['i_group'].apply(lambda x: 'Isolation' if len(x) == 1 else 'Integration')
        df['gbv'] = np.where((df['TM'] == 1) & (df['J2H'] == 1), 'Together', np.where((df['TM'] == 0) & (df['J2H'] == 1), 'Alone', pd.NA))
        df.loc[(df['i_group'].str.contains('C', na=False)) & (df['i_type'] == 'Integration'),'participation_cctd'] = "C with Integration"
        df.loc[(df['i_group'].str.contains('C', na=False)) & (df['i_type'] == 'Isolation'),'participation_cctd'] = "C (Isolation)"
        df.loc[(df['i_group'].str.contains('J', na=False)) & (df['i_type'] == 'Integration'),'participation_j2h'] = "J with Integration"
        df.loc[(df['i_group'].str.contains('J', na=False)) & (df['i_type'] == 'Isolation'),'participation_j2h'] = "J (Isolation)"
        self.df = df
        
    def knowledge_comp(self):
        df = self.df
        conditions_participation = ['CJ', 'CJT', 'JT', 'J']
        conditions_non_participation = ['C', 'CT']
        def classify(row):
            if pd.notna(row['GBV_knowledge']):
                if row['i_group'] in conditions_participation:
                    return 'Participation'
                elif row['i_group'] in conditions_non_participation:
                    return 'Non-participation'
            return np.nan
        
        df['Knowledge_comp'] = df.apply(classify, axis=1)
        self.df = df
        
    def processing(self):
        """
        - To conduct data pre-processing
        1. Load the raw dataset
        2. Adjust the dataset based on the results of QC
        3. Re-define variable names
        4. Handle duplicates
        5. Anonymise data (Respondents' names)
        6. Remove pilot test data points
        7. Drop unnecessary columns
        8. Handle missing values
        9. Extract answers from open-ended questions
        10. Create age and disability groups
        11. Group some variables
        12. Create several variables for statistical tests
        13. Save the cleaned dataset
        """
        self.data_load()
        self.qc_checklist() 
        self.columns_redefine()
        self.project_update()
        self.grouping()
        print(f'Initial data points: {len(self.df)}')
        self.data_anonymisation()
        self.duplicates()
        if len(self.dates) != 0:
            self.date_filter()
        print(f'Initial number of columns: {len(self.df.columns)}')
        self.delete_columns()
        self.missing_value_clean()
        self.open_ended_cols()
        if self.age_col != None:
            self.age_group()
        if self.diss_cols != None:
            self.disability_wgss()
        self.interventions()
        self.intervention_group()
        self.cctd()
        self.wemwbs()
        self.qols()
        self.GBV_knowledge()
        self.gbv_social_norm()
        self.gbv_personal_beliefs()
        self.knowledge_comp()
        original = self.file_path
        self.file_path = f'{self.file_path}_cleaned'
        self.save_data()
        self.file_path = original
        print("")
        print(f'Final number of data points: {len(self.df)}')
        print(f"Cleaned dataframe has been saved: {self.file_path}_cleaned.{self.file_type}")
        return True