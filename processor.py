import pandas as pd

df = pd.read_csv('Partial_data_Test.csv')

rc = pd.read_csv('watersheds_supergrid_rc.csv')
rc = rc.sort_values('HYDROID')

# read date
df['date'] = pd.to_datetime((df.Year*10000+df.Mo*100+df.Da).apply(str), format='%Y/%m/%d')

date_list = sorted(df['date'])

result = pd.DataFrame(date_list, columns=['HYDROID'])
result.head(10)

# Main process part
prev_hydroid = ''
column_name_list = []
for index, row in rc.iterrows():
    r = row['Row']
    c = row['Col']
    
    if row['HYDROID'] != prev_hydroid:
        if prev_hydroid != '':
            value_df_mean = df[column_name_list].mean(axis=1)
            # print(prev_hydroid, column_name_list)
            # print(value_df_mean.head(5))
            result[prev_hydroid] = value_df_mean;
            
        column_name_list = []
        prev_hydroid = row['HYDROID']
    
    column_name = '({:02d},{:02d})'.format(r, c)
    column_name_list.append(column_name)
    
if prev_hydroid != '':
    value_df_mean = df[column_name_list].mean(axis=1)
    # print(prev_hydroid, column_name_list)
    # print(value_df_mean.head(5))
    result[prev_hydroid] = value_df_mean;
    
result.to_csv("Final_Result.csv", index=False)