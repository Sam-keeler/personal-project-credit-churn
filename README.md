# Personal Classification Project Credit Card Churn

## Description
- Project examining the drivers of churn for credit card owners
- Data was acquired from a kaggle database which can be found here: https://www.kaggle.com/sakshigoyal7/credit-card-customers

## Goals
- Find out which features were most closely associated with customer churn and make a model to predict whether a customer will churn or not

## Trello Board
https://trello.com/b/LB42SLDI/credit-card-churn

## Data Dictionary

|                            | type    | description                                                                       |
|:---------------------------|:--------|:----------------------------------------------------------------------------------|
| churn                      | int64   | Whether the customer is with the bank or not, 1 indicating that they have churned |
| age                        | int64   | The customer's age                                                                |
| gender                     | object  | The customer's gender                                                             |
| dependents                 | int64   | How many dependents the customer has                                              |
| education                  | object  | The customer's highest level of education                                         |
| marital_status             | object  | The customer's marital status                                                     |
| income                     | object  | The customer's income arranged into bins                                          |
| card_type                  | object  | The type of credit card the customer has                                          |
| tenure                     | int64   | The number of months the customer has been with the bank                          |
| products_used              | int64   | Total number of products held by the customer                                     |
| inactive_months_past_year  | int64   | The number of months the customer has been inactive in the last year              |
| contacted_past_year        | int64   | Number of contacts in the last year                                               |
| credit_limit               | float64 | The customers credit limit                                                        |
| revolving_bal_tot          | int64   | Total revolving balance on the credit card                                        |
| avg_open_to_buy            | float64 | Difference in credit used and credit available (Average of last 12 months)        |
| trans_amt_chng_q4_q1       | float64 | Change in transaction amount (Q4 over Q1)                                         |
| tot_trans_amt              | int64   | Total transaction amount (last 12 months)                                         |
| total_trans_ct             | int64   | Total transaction count (last 12 months)                                          |
| ct_chng_q4_q1              | float64 | Change in transaction count (Q4 over Q1)                                          |
| avg_card_utilization_ratio | float64 | Average of credit used divided by credit available                                |


## Project Takeaways
- Random forest model created was 95% accurate at predicting churn, an improvement of about 11% from baseline
- Personal information about the customer (age, gender, dependents, etc.) turned out to be irrelevant when it came to predicting churn, the trends in how a person uses their credit card was the best indicator of churn
- If more data were available, would like to see spending categories for each customer to see if that could assist with churn prediction
