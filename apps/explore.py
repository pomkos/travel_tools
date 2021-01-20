import streamlit as st
import pandas as pd
import requests as r
import numpy as np
import datetime as dt

# beautifulsoup, html5lib, lxml required to read with pandas table

# get weather info
class weatherAnalysis():
    def __init__(self, location, type_='future'):
        '''
        Initiates weather api
        
        input
        ----
        location: str
            Zip code, ip address, lat/lon, city name
        type_: str
            current or future or history
        '''
        api_key = "4216ca74f3d1478dbbd154714212001"

        params = {
            'key':api_key,
            'q':location
        }

        if type_ == 'current':
            url = 'https://api.weatherapi.com/v1/current.json'
        elif type_ == 'future':
            url = 'https://api.weatherapi.com/v1/forecast.json'
            params['days'] = 3 # max forecast for free account
        elif type_ == 'history':
            url = 'https://api.weatherapi.com/v1/history.json'
            self.history(url, params)
            return
            
        response = r.get(url = url, params = params)
        self.response = response.json()

        if type_ == 'future':
            self.forecast()
        
    def date_lister(self):
        '''
        Returns list of 7 properly formatted dates
        '''
        historic_dates = []
        
        for i in range(1,8):
            new_date = dt.datetime.now() - dt.timedelta(days=i) # max history for free account
            historic_dates.append(new_date.strftime('%Y-%m-%d'))
        
        return historic_dates
    
    def forecast(self):
        '''
        Gets the forecast, calculates mean temp
        '''
        temps = []
        all_forecast = self.response['forecast']['forecastday']
        for day in all_forecast:
            temp = day['day']['avgtemp_f'] # get avg temp for day
            temps.append(temp)
        
        self.all_temps = temps
        self.mean_temp = np.mean(temps)
        
    def history(self, url, params):
        '''
        Gets historic weather, calculates mean temp
        
        input
        -----
        url: str
            Api url
        params: dict
            Constructed params, without date
            
        output
        ------
        self.historic: pd.DataFrame
            Dataframe of dates and temp in F
        '''
        temps = []
        date_list = self.date_lister()
        
        all_responses = []
        for date in date_list:
            params['dt'] = date
            response = r.get(url=url, params=params)
            all_responses.append(response.json())
        
        extracted = {}
        for i in range(len(all_responses)):
            selected = all_responses[i]['forecast']['forecastday'][0] # all info for selected day
            day = selected['day'] # temp stats for the day    
            extracted[selected['date']] = [day['avgtemp_f'],day['mintemp_f'],day['maxtemp_f']]
            
        df = pd.DataFrame(extracted).T.reset_index()
        df.columns = ['date','avg_temp_f','min_temp_f','max_temp_f']
        self.historic = df 

def progress_bar():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    
def find_cities(df, cities):
    '''
    Returns df of cities selected
    '''
    locs = []
    for i, r in df.iterrows():
        for x in cities:
            if x in r['City']:
                locs.append(i)
    small_df = df.loc[locs]
    return small_df

    
def app():
    st.title('Exploration Station')
    df = pd.read_html('data/walkscore.html')[0]
    temp_col = '7 Day Avg Temp (F)' # i keep changing name
    cols = list(df.columns) + [temp_col]
    cities = st.multiselect("Select cities of interest", df['City'].unique())
    
    new_df = pd.DataFrame(columns=cols) # dynamically create smaller df
    if not st.button("Submit"):
        st.stop()
        
    p_bar = st.progress(0)
    
    new_df = find_cities(df, cities)
    weather_avg = {}
    import time
    for i in range(len(cities)):
        c = cities[i]
        w = weatherAnalysis(c, type_='history')
        weather_df = w.historic
        weather_avg[c] = round(weather_df.avg_temp_f.mean())
        
        # increment the progress bar
        # i+1 so that progress bar doesnt start at 0
        p_bar.progress(int((i+1)*100/len(cities)))
    
    new_df['7 Day Avg (F)'] = new_df['City'].map(weather_avg)
    st.table(new_df)
    st.success("Enjoy!")