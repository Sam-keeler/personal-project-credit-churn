import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from datetime import date
import seaborn as sns
from sklearn.model_selection import train_test_split

# .csv file obtained from https://www.kaggle.com/sakshigoyal7/credit-card-customers
# This code reads the .csv into a pandas dataframe.

def acquire():
     return pd.read_csv("BankChurners.csv")

# prepare function drops last two columns (probability predictions using Naive-Bayes), fills 'Unknown' with 'NaN', fills null values with the mode
# of the respective column (nulls made up less than 16% of each column) in marital status, income, and education, drops client number, renames
# columns, converts churn values to integers, and creates new columns that bins large numeric columns.

def prepare(credit):
    credit.drop(columns = ['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1', 'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'], inplace = True)
    credit.replace({'Unknown': np.nan}, inplace = True)
    credit['Marital_Status'] = credit.Marital_Status.fillna('Married')
    credit['Income_Category'] = credit.Income_Category.fillna('Less than $40K')
    credit['Education_Level'] = credit.Education_Level.fillna('Graduate')
    credit.drop(columns = ['CLIENTNUM'], inplace= True)
    credit.rename(columns = {'Attrition_Flag': 'churn', 'Customer_Age': 'age', 'Gender': 'gender', 'Dependent_count': 'dependents',
                             'Education_Level': 'education', 'Marital_Status': 'marital_status', 'Income_Category': 'income',
                             'Card_Category': 'card_type', 'Months_on_book': 'tenure', 'Total_Relationship_Count': 'products_used',
                             'Months_Inactive_12_mon': 'inactive_months_past_year', 'Contacts_Count_12_mon': 'contacted_past_year',
                             'Credit_Limit': 'credit_limit', 'Total_Revolving_Bal': 'revolving_bal_tot', 'Avg_Open_To_Buy': 'avg_open_to_buy',
                             'Total_Amt_Chng_Q4_Q1': 'trans_amt_chng_q4_q1', 'Total_Trans_Amt': 'tot_trans_amt', 
                             'Total_Trans_Ct': 'total_trans_ct', 'Total_Ct_Chng_Q4_Q1': 'ct_chng_q4_q1', 
                             'Avg_Utilization_Ratio': 'avg_card_utilization_ratio'}, inplace = True)
    credit.churn.replace({'Existing Customer': 0, 'Attrited Customer': 1}, inplace = True)
    cut_labels_4 = ['0', '1 - 1000', '1000 - 2000', '2000+']
    cut_bins = [-1, 0.99, 1000, 2000, 3000]
    credit['revolving_bal_bin'] = pd.cut(credit['revolving_bal_tot'], bins=cut_bins, labels=cut_labels_4)
    cut_labels_3 = ['20-30', '30-40', '40-50', '50-60', '60+']
    cut_binz = [20, 30, 40, 50, 60, 100]
    credit['age_bin'] = pd.cut(credit['age'], bins=cut_binz, labels=cut_labels_3)
    cut_labels_2 = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
    cut_bin = [-1, 0.2, 0.4, 0.6, 0.8, 1.01]
    credit['card_util_bin'] = pd.cut(credit['avg_card_utilization_ratio'], bins=cut_bin, labels=cut_labels_2)
    return credit

# Split function splits the data into train, validate, and test.

def split(credit):
    train, test = train_test_split(credit, test_size=.2, random_state=123, stratify=credit['churn'])
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train['churn'])
    return train, validate, test

# Finds the weights of features from the model created.

def get_the_weights(rf, x_train):
    feat = rf.feature_importances_
    key = x_train.columns.tolist()
    val = feat.tolist()
    val = [round(num, 2) for num in val]
    res = {key[i]: val[i] for i in range(len(key))} 
    return res

# Finds the weights of features for logistic regression model.

def get_the_coef(logit2, x_train):
    feat = logit2.coef_[0]
    key = x_train.columns.tolist()
    val = feat.tolist()
    val = [round(num, 2) for num in val]
    res = {key[i]: val[i] for i in range(len(key))} 
    return res

# Prepare function for modeling, removes most personal information columns and binned columns. Additionally
# removes financial features rated irrelevant by feature weight functions.

def prep_model(credit):
    credit['gender'] = credit.gender.apply(lambda x: 1 if x == 'F' else 0)
    credit.rename(columns = {'gender': 'is_female'}, inplace = True)
    credit.drop(columns = ['revolving_bal_bin', 'age_bin', 'card_util_bin'], inplace = True)
    credit.drop(columns = ['education', 'marital_status', 'income', 'card_type', 'credit_limit',
                         'is_female', 'dependents', 'avg_open_to_buy', 'age', 'tenure'], inplace = True)
    return credit