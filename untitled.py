import requests
import pandas as pd

class assetanalysis:
    def __init__ (self, data):
        self.data = data   #assign data from yfinance to "self.data"
        self.get_data() #run get_data method
        self.get_corr()  #run get_corr method
        self.get_rf() #run get_rf method
        self.get_boll() #run get attribute method

    def get_data(self):
        self.data = yf.download(tickers=[*x], period = '90d', interval = '1d')
        df = data['Close'].dropna()
        return df

#     def get_attributes(self): # run functions for each attribute
#         self.num_sales = [x['num_sales'] for x in self.data['assets']]
#         self.token_id = [x['token_id'] for x in self.data['assets']]
#         self.name = [x['name'] for x in self.data['assets']]
#         self.last_sale = [x['last_sale'] for x in self.data['assets']]
#         self.project_des = self.data['assets'][0]['asset_contract']['description']
#         self.collection_name = self.data['assets'][0]['collection']['name']
        
#     def as_df(self): # cast attributes into df
#         return pd.DataFrame({'Token ID':self.token_id,'Name':self.name})
    

# class OpenSeaItem:
#     def __init__ (self, single_url):
#         self.single_url = single_url   #assign query url to "self.url"
#         self.get_single_data()  #run get_data method
#         self.get_single_attributes() #run get attribute method

#     def get_single_data(self):
#         self.single_data = requests.request("GET", self.single_url).json() #assign query json to "self.data"

#     def get_single_attributes(self):
#         self.asset_image = self.single_data['image_thumbnail_url']
#         self.currency_data = [x['symbol'] for x in self.single_data['collection']['payment_tokens']]
#         self.floor_price = self.single_data['collection']['stats']['floor_price']
#         self.total_supply = self.single_data['collection']['stats']['total_supply']
#         self.traits = [x['trait_type'] for x in self.single_data['traits']]
#         self.collection_name = self.single_data['collection']['name']
    
#     def price_plot(self):
#         price_plot_chart = self.data['hist_price'].hvplot.line()
#         return price_plot_chart
    
#     def as_df(self):
#         return pd.DataFrame({'Token ID':self.token_id,'Name':self.name})