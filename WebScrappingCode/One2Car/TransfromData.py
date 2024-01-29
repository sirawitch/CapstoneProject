import pandas as pd
from datetime import date, timedelta

today = date.today()

# define path
data_path = (f"/opt/airflow/WebScrapData/One2Car/{today.month}_{today.year}.csv",)

# init var
data_df = pd.read_csv(data_path)
dimension_column_names = ["webid", "name", "mile", "color", "gear", "web"]
transaction_column_names = ["webid", "status", "cost", "date"]

# tranform
# car_all_info = pd.DataFrame(
#         {
#             "name": [name],
#             "cost": [cost],
#             "mile": [mile],
#             "status": [status],
#             "color": [color],
#             "gear": [gear],
#             "web": ["one2car"],
#             "webid": [webid],
#             "date": [today],
#         }
#     )


print("Done")
