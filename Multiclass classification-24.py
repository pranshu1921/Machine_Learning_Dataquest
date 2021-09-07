## 1. Introduction to the Data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars['origin'].unique()
print(unique_regions)

## 2. Dummy Variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years = pd.get_dummies(cars['year'], prefix = 'year')
cars = pd.concat([cars, dummy_years], axis = 1)
cars = cars.drop(['year', 'cylinders'], axis = 1)
print(cars.head())

## 3. Multiclass Classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
highest_train_row = int(cars.shape[0] * .70)
train = shuffled_cars.iloc[0:highest_train_row]
test = shuffled_cars.iloc[highest_train_row:]

## 4. Training a Multiclass Logistic Regression Model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}
features = [c for c in train.columns if c.startswith("cyl") or c.startswith("year")]

for origin in unique_origins:
    model = LogisticRegression()
    X_train = train[features]
    y_train = train['origin'] == origin
    
    model.fit(X_train, y_train)
    models[origin] = model

## 5. Testing the Models ##

testing_probs = pd.DataFrame(columns=unique_origins)

for origin in unique_origins:
    
    X_test = test[features]
    
    testing_probs[origin] = models[origin].predict_proba(X_test)[:,1]
    

## 6. Choose the Origin ##

predicted_origins = testing_probs.idxmax(axis = 1)
print(predicted_origins)