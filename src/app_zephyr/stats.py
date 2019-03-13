# coding: utf-8

# In[1]:


def get_stat_data(BASE_DIR):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    # import seaborn as sns
    from sklearn.preprocessing import Imputer
    import warnings

    warnings.filterwarnings("ignore")

    # In[2]:

    df = pd.read_csv(BASE_DIR+"/app_zephyr/stats_data.csv")
    df = df.drop(['stn_code', 'agency'], axis=1)

    imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imputer = imputer.fit(df.iloc[:, 3:8].values)
    df.iloc[:, 3:8] = imputer.transform(df.iloc[:, 3:8].values)

    commonArea = 'Residential, Rural and other Areas'
    df['type'] = df['type'].fillna(commonArea)
    statewise_emission = df.groupby('state').mean()[['so2', 'no2', 'rspm', 'spm', 'pm2_5']]

    dik = {}
    list1 = list(statewise_emission.index.values)
    list2 = list(statewise_emission['so2'])
    list3 = list(statewise_emission['no2'])
    list4 = list(statewise_emission['rspm'])
    list5 = list(statewise_emission['spm'])
    l = [list1, list2, list3, list4, list5]
    dik['allstate_so2_no2_rspm_spm'] = l

    # In[20]:

    states_highest_no2 = statewise_emission.sort_values('no2', ascending=False).head(10)
    states_highest_no2 = states_highest_no2.loc[:, ['no2']]
    dik['state_high_no2'] = [list(states_highest_no2.index.values), list(states_highest_no2.no2)]

    # In[23]:

    states_highest_so2 = statewise_emission.sort_values('so2', ascending=False).head(10)
    states_highest_so2 = states_highest_so2.loc[:, ['so2']]
    dik['state_high_so2'] = [list(states_highest_so2.index.values), list(states_highest_so2.so2)]


    # In[24]:

    states_highest_rspm = statewise_emission.sort_values('rspm', ascending=False).head(10)
    states_highest_rspm = states_highest_rspm.loc[:, ['rspm']]
    dik['state_high_rspm'] = [list(states_highest_rspm.index.values), list(states_highest_rspm.rspm)]

    # In[25]:

    states_highest_spm = statewise_emission.sort_values('spm', ascending=False).head(10)
    states_highest_spm = states_highest_spm.loc[:, ['spm']]
    dik['state_high_spm'] = [list(states_highest_spm.index.values), list(states_highest_spm.spm)]

    # In[26]:

    locationwise_emission = df.groupby('location').mean()[['so2', 'no2', 'rspm', 'spm', 'pm2_5']]

    # In[27]:

    loc_highest_rspm = locationwise_emission.sort_values('rspm', ascending=False).head(10)
    loc_highest_rspm = loc_highest_rspm.loc[:, ['rspm']]
    dik['loc_high_rspm'] = [list(loc_highest_rspm.index.values), list(loc_highest_rspm.rspm)]

    # In[28]:

    loc_highest_spm = locationwise_emission.sort_values('spm', ascending=False).head(10)
    loc_highest_spm = loc_highest_spm.loc[:, ['spm']]
    dik['loc_high_spm'] = [list(loc_highest_spm.index.values), list(loc_highest_spm.spm)]

    # In[29]:

    loc_highest_so2 = locationwise_emission.sort_values('so2', ascending=False).head(10)
    loc_highest_so2 = loc_highest_so2.loc[:, ['so2']]
    dik['loc_high_so2'] = [list(loc_highest_so2.index.values), list(loc_highest_so2.so2)]

    # In[30]:

    loc_highest_no2 = locationwise_emission.sort_values('no2', ascending=False).head(10)
    loc_highest_no2 = loc_highest_no2.loc[:, ['no2']]
    dik['loc_high_no2'] = [list(loc_highest_no2.index.values), list(loc_highest_no2.no2)]
    # print(dik.keys())
    return dik

