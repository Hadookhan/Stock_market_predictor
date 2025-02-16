from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df = pd.read_csv("api/GOOG.csv") # Reads csv

columns_to_scale = ["Open","High","Low","Close"] # Focuses on these columns
data_to_scale = df[columns_to_scale] # Filters dataframe to focused columns

scaler = MinMaxScaler(feature_range=(0,1)) # Normalization scaler
scaled_data = scaler.fit_transform(data_to_scale) # Apply scaler to data

df_scaled = pd.DataFrame(scaled_data, columns=columns_to_scale)
df_scaled.to_csv("api/scaled_data.csv", index=False)

