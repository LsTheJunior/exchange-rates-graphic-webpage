import requests
import  pandas as pd
import datetime

from controller.BussinessDates import Dates


class GetData:
    def rates(self):

       date = Dates() 
       _bussinessDays = date.getBussinesDates()
       dataset = pd.DataFrame()
       df = pd.DataFrame(columns=['USD','JPY','BRL'])

       i= 0
       while i < 5:
            import datetime as dt
            today = dt.date.today()
            data = today - dt.timedelta(days=i)
            data = data.strftime('%Y-%m-%d')
            url = f'https://api.vatcomply.com/rates?base=USD&date={_bussinessDays[i]}'
            payload = ""
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            res_json = response.json()
            resultado = res_json['rates']
            dateString = datetime.datetime.strptime(_bussinessDays[i], '%Y-%m-%d')
            dataset = dataset.append({'EUR':resultado['EUR'],'JPY':resultado['JPY'],'BRL':resultado['BRL'],'Data':str(_bussinessDays[i])},ignore_index=True)
            i+=1

       return dataset