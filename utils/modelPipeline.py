import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine

conns = create_engine("sqlite:/// app/database/PreprocessData.db").connect()
data = pd.read_sql_table("hospitalData", conns)

print(data.head())
print(data.info())