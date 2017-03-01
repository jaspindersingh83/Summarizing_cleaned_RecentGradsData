import pandas as pd
all_ages=pd.read_csv("all-ages.csv")
recent_grads=pd.read_csv("recent-grads.csv")
print(all_ages.head())
print(recent_grads.head())

## Create dictionary of each Major_Cat_Graduates
aa_cat_counts = dict()
rg_cat_counts = dict()
pivot_table_aa=all_ages.pivot_table(index="Major_category",values="Total",aggfunc=np.sum)
aa_cat_counts=pivot_table_aa.to_dict()
pivot_table_rg=recent_grads.pivot_table(index="Major_category",values="Total",aggfunc=np.sum)
rg_cat_counts=pivot_table_rg.to_dict()
### Calculate percent of low_wage_graduates from data
columns=list(recent_grads.columns)
low_wage_percent=(recent_grads['Low_wage_jobs'].sum())/(recent_grads['Total'].sum())

### Count of Majore for which recent_grads did better in terms of unemployment_rate

majors = recent_grads['Major'].unique()
  
rg_lower_count = 0
pivot_rg=recent_grads.pivot_table(index="Major",values="Unemployment_rate")
pivot_aa=all_ages.pivot_table(index="Major",values="Unemployment_rate")
dict1=pivot_rg.to_dict()
dict2=pivot_aa.to_dict()
for i in dict1:
    if dict1[i]<dict2[i]:
        rg_lower_count= rg_lower_count+1