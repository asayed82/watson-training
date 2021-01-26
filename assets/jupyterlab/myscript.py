
import pandas as pd

df_data_1 = pd.read_csv('/project_data/data_asset/customer_demochurn_activity_analyze.csv')
df_data_1.head()

from project_lib import Project
project = Project.access()
    
# let's assume you have the pandas DataFrame  pandas_df which contains the data
# you want to save as a csv file
project.save_data("file_name.csv", df_data_1.to_csv(index=False))