import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


# parameters

n_estimators=230
max_depth=10
min_samples_leaf=1
output_file = f'model_rf_{n_estimators}_{max_depth}_{min_samples_leaf}.bin'


# data preparation

df = pd.read_csv('water_potability.csv', delimiter=',')

df.columns = df.columns.str.lower().str.replace(' ', '_')

# Fill missing values
df['ph'] = df['ph'].fillna(
    df.groupby('potability')['ph'].transform('mean')
)

df['sulfate'] = df['sulfate'].fillna(
    df.groupby('potability')['sulfate'].transform('mean')
)

df['trihalomethanes'] = df['trihalomethanes'].fillna(
    df.groupby('potability')['trihalomethanes'].transform('mean')
)

df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=9)
df_train, df_val = train_test_split(df_train_full, test_size=0.25, random_state=9)


# training 

def train(df_train, y_train, n_estimators, max_depth, min_samples_leaf):
    
    X_train = df_train.drop('potability',axis=1)
    
    model = RandomForestClassifier(n_estimators=n_estimators,
                            max_depth=max_depth,
                            min_samples_leaf=min_samples_leaf,
                            random_state=9)
    model.fit(X_train, y_train)
    
    return model


def predict(df, model):
    
    X = df.drop('potability',axis=1)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred


# validation

print(f'doing validation with n_estimators={n_estimators}, max_depth={max_depth}, min_samples_leaf={min_samples_leaf}')

y_train = df_train.potability.values
y_val = df_val.potability.values

model = train(
    df_train, 
    y_train, 
    n_estimators=n_estimators,
    max_depth=max_depth,
    min_samples_leaf=min_samples_leaf)

y_pred = predict(df_val, model)
auc = roc_auc_score(y_val, y_pred)
print(f'auc is {auc}')


# training the final model

print('\ntraining the final model')

model = train(df_train_full, df_train_full.potability.values, n_estimators=n_estimators, max_depth=max_depth, min_samples_leaf=min_samples_leaf)
y_pred = predict(df_test, model)

y_test = df_test.potability.values
auc = roc_auc_score(y_test, y_pred)

print(f'auc={auc}')


# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump(model, f_out)

print(f'\nthe model is saved to {output_file}')