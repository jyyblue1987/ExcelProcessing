import pandas as pd

df = pd.read_csv('Partial_data_Test.csv')
# rc = pd.read_csv('watersheds_supergrid_rc.csv')
rc = pd.read_csv('supergrid_area_wcs.csv')

rc = rc.sort_values('HYDROID')

# read date
df['date'] = pd.to_datetime((df.Year*10000+df.Mo*100+df.Da).apply(str), format='%Y/%m/%d')

date_list = sorted(df['date'])

result = pd.DataFrame(date_list, columns=['HYDROID'])
sum_result = pd.DataFrame(date_list, columns=['HYDROID'])
result.head(10)

# Main process part
prev_hydroid = ''
column_name_list = []
weight_list = []
for index, row in rc.iterrows():
    r = row['Row']
    c = row['Col']
    
    if row['HYDROID'] != prev_hydroid:
        if prev_hydroid != '':
            sub_df = df[column_name_list].apply(pd.to_numeric, errors='coerce')
            value_df_mean = sub_df.mean(axis=1)
            value_df_sum = sub_df.dot(weight_list)
            
            # print(prev_hydroid, column_name_list)
            # print(value_df_mean.head(5))
            result[prev_hydroid] = value_df_mean;
            sum_result[prev_hydroid] = value_df_sum;
            
        column_name_list = []
        weight_list = []
        prev_hydroid = row['HYDROID']
    
    column_name = '({:02d},{:02d})'.format(r, c)
    column_name_list.append(column_name)
    weight_list.append(row['Area_Acre'])
    
if prev_hydroid != '':
    sub_df = df[column_name_list].apply(pd.to_numeric, errors='coerce')
    value_df_mean = sub_df.mean(axis=1)
    value_df_sum = sub_df.dot(weight_list)

    # print(prev_hydroid, column_name_list)
    # print(value_df_mean.head(5))
    result[prev_hydroid] = value_df_mean;
    sum_result[prev_hydroid] = value_df_sum;
    
result.to_csv("Final_Result.csv", index=False)
sum_result.to_csv("Final_Result_Sum.csv", index=False)