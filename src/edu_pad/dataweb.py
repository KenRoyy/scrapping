import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup



class DataWeb:
    def __init__(self):
        self.url = "https://es.finance.yahoo.com/quote/GOOG/history"
    
    def obtener_datos(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            respuesta = requests.get(self.url,headers=headers)
            if respuesta.status_code != 200:
                print("Error!!!!!!, Pailas!!!")
            soup = BeautifulSoup(respuesta.text,'html.parser')
            tabla = soup.select_one('div[data-testid="history-table"] table')
            nombre_columnas = [th.get_text(strip=True) for th in tabla.thead.find_all('th')]
            filas = []
            for tr in tabla.tbody.find_all('tr'):
                columnas = [ td.get_text(strip=True) for td in tr.find_all('td')]
                if len(columnas) == len(nombre_columnas):
                    filas.append(columnas)
            df = pd.DataFrame(filas,columns=nombre_columnas).rename(columns = {
                'Fecha': 'fecha',
                'Abrir': 'abrir',
                'Máx.': 'max',
                'Mín.': 'min',
                'CerrarPrecio de cierre ajustado para splits.': 'cerrar',
                'Cierre ajustadoPrecio de cierre ajustado para splits y distribuciones de dividendos o plusvalías.': 'cierre_ajustado',
                'Volumen':'volumen'
            })

            df = self.convertir_numericos(df)
            print("*******************************************************************")
            print("Datos Obtenidos ")
            print("*******************************************************************")
            print(df.head())

            return df
        except Exception as err:
            print("Error en la funcion obtener_datos")
            df = pd.DataFrame()


    def convertir_numericos(self,df=pd.DataFrame()):
        df= df.copy()
        if len(df)>0:
            for col in ('abrir',	'max',	'min',	'cerrar',	'cierre_ajustado',	'volumen'):
                df[col] = (df[col]
                           .str.replace(r"\.","",regex=True)
                           .str.replace(",",'.'))

        return df


