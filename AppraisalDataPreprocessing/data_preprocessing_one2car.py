# Import Libraries
import pandas as pd
import numpy as np

# Read Data
df = pd.read_csv('./WebScrapData/One2Car/Data.csv')

# Change 'cost' col
df['cost'] = df['cost'].apply(lambda x : x.replace(',',''))
df['cost'] = df['cost'].astype('int64')

# Change 'mile' col
def change_mile_dtypes(mile_data):
    try:
        mile_data = mile_data.replace('km','')
        if '-' not in mile_data:    # First type
            return int(mile_data)
        else:                       # Second type
            mile_data = mile_data.replace('K','')
            mile_data = mile_data.split('-')
            return int((int(mile_data[0]) + int(mile_data[1]))/2*1000)
    except:
        return np.NaN
                
df['mile'] = df['mile'].apply(change_mile_dtypes)

# Fill missing with mean
mile_mean = int(df['mile'].mean())
df.fillna(value=mile_mean, inplace=True)
df['mile'] = df['mile'].astype('int64')

# Change 'date' col
df['date'] = pd.to_datetime(df['date'])

# Extract 'name' col

# Cut from name
def cut_from_name(new_serie, name_serie):
    new_names = []
    for i in range(len(new_serie)):
        name_serie_tokens = name_serie[i].split(' ')
        new_serie_tokens = str(new_serie[i]).split(' ')
        new_name = ''
        for token in name_serie_tokens:
            if token not in new_serie_tokens:
                new_name += token + ' '
        new_names.append(new_name)
    return pd.Series(new_names)

# car_year
df['car_year'] = df['name'].apply(lambda x : int(x[:4]))

# brand
df['brand'] = df['name'].apply(lambda x : 'Mazda' if 'Mazda' in x else 'Other')

# model
models = ['2', '3', '121', '323', 'BT-50', 'BT-50 PRO', 'CX-3', 'CX-5', 'CX-7', 'CX-8', 'CX-9', 'CX-30', 'Familia', 'Fighter', 'Magnum Thunder', 'MX-5', 'RX-7', 'RX-8', 'Savanna']
def check_model(name):
    name = name.split(' ')
    for i in range(len(name)):
        if name[i] == 'Mazda' and ((name[i+1]+' '+name[i+2]) in models):
            return name[i+1]+' '+name[i+2]
        elif name[i] == 'Mazda' and (name[i+1] in models):
            return name[i+1]
    return np.NaN
df['model'] = df['name'].apply(check_model)

# sub_model
sub_models = ['0.8', '1.1', '1.3', '1.4', '1.5', '1.6', '1.8', '1.9', '2.0', '2.2', '2.3', '2.5', '2.9', '3.2', '3.7']
def check_sub_model(name):
    name = name.split(' ')
    for i in range(len(name)):
        if name[i] in sub_models:
            return name[i]
    return np.NaN
df['sub_model'] = df['name'].apply(check_sub_model)

# car_type
car_types = ['Sedan', 'Pickup', 'Hatchback', 'SUV', 'Convertible', 'Coupe']
def check_car_type(name):
    name = name.split(' ')
    for i in range(len(name)):
        if name[i] in car_types:
            return name[i]
    return np.NaN
df['car_type'] = df['name'].apply(check_car_type)

# model_year
def check_model_year(name):
    if 'ปี' in name:
        model_year = name[name.find('(') : name.find(')')+1]
        return model_year
    return np.NaN
df['model_year'] = df['name'].apply(check_model_year)
df['model_year_start'] = df['model_year'].apply(lambda x : int(x[x.find('-')-2 : x.find('-')]) if not pd.isna(x) else np.NaN)
df['model_year_end'] = df['model_year'].apply(lambda x : int(x[x.find('-')+1 : x.find('-')+3]) if not pd.isna(x) else np.NaN)

# Cut transmission cause we already have data
df['name'] = df['name'].apply(lambda x : x.replace('AT',''))
df['name'] = df['name'].apply(lambda x : x.replace('MT',''))

# Cut extract data from name
df['name'] = cut_from_name(df['car_year'], df['name'])
df['name'] = cut_from_name(df['brand'], df['name'])
df['name'] = cut_from_name(df['model'], df['name'])
df['name'] = cut_from_name(df['sub_model'], df['name'])
df['name'] = cut_from_name(df['car_type'], df['name'])
df['name'] = cut_from_name(df['model_year'], df['name'])

# sub_model_name
# The rest of name is sub model name
df['name'] = df['name'].apply(lambda x: x.strip())
df.rename(columns={'name' : 'sub_model_name'}, inplace=True)

# Make columns easy to understand
# Change transmission col
df.rename(columns={'gear' : 'transmission'}, inplace=True)
df['transmission'] = df['transmission'].apply(lambda x : 'AT' if x == 'เกียร์อัตโนมัติ' else 'MT')

# Change color col
color_map = {
    'สีเขียว':'green',
    'สีเงิน':'silver',
    'สีเทา':'gray',
    'สีเหลือง':'yellow',
    'สีแดง':'red',
    'สีขาว':'white',
    'สีครีม':'cream',
    'สีดำ':'black',
    'สีทอง':'gold',
    'สีน้ำเงิน':'blue',
    'สีน้ำตาล':'brown',
    'สีฟ้า':'sky',
    'สีส้ม':'orange',
    'สีอื่นๆ':'other',
}
df['color'] = df['color'].map(color_map)

# Change status
status_map = {
    'รถมือสอง' : 'second_hand'
}
df['status'] = df['status'].map(status_map)

# Change webid
df['webid'] = df['webid'].apply(lambda x : x.strip())

# Reorder columns
cols = ['car_year', 'brand', 'model', 'sub_model', 'sub_model_name', 'car_type', 'transmission', 'model_year_start', 'model_year_end', 'color', 'mile', 'date', 'webid', 'cost']
df = df[cols]

# Save csv
df.to_csv('./AppraisalDataPreprocessing/data_one2car.csv')