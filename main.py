import pandas as pd
import statsmodels.api as sm
from pathlib import Path
# Constants

Q = 100
c = 5

# Data
data_path = Path(r'data.txt')

df = pd.read_csv(data_path, sep="\t")    
print(df)

# Demand



