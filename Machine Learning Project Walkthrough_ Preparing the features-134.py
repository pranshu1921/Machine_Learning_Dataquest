## 1. Recap ##

import pandas as pd

loans = pd.read_csv("filtered_loans_2007.csv")

null_counts = pd.Series(loans.isnull().sum())

print(null_counts)

## 2. Handling Missing Values ##

loans = loans.drop('pub_rec_bankruptcies', axis = 1)
loans = loans.dropna(axis = 0)
print(loans.dtypes.value_counts())

## 3. Text Columns ##

object_columns_df = loans.select_dtypes(include = ['object'])
print(object_columns_df.head(1))

## 5. First 5 Categorical Columns ##

cols = ['home_ownership', 'verification_status', 'emp_length', 'term', 'addr_state']

for col in cols:
    print(pd.Series(loans[col].value_counts()))

## 6. The Reason for The Loan ##

print(loans['title'].value_counts())
print(loans['purpose'].value_counts())

## 7. Categorical Columns ##

mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}
loans = loans.drop(["last_credit_pull_d", "earliest_cr_line", "addr_state", "title"], axis=1)
loans["int_rate"] = loans["int_rate"].str.rstrip("%").astype("float")
loans["revol_util"] = loans["revol_util"].str.rstrip("%").astype("float")
loans = loans.replace(mapping_dict)

## 8. Dummy Variables ##

dummy_df = pd.get_dummies(loans[cat_columns])
loans = pd.concat([loans, dummy_df], axis = 1)
loans = loans.drop(['home_ownership','verification_status', 'purpose', 'term'], axis = 1) 