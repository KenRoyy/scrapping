from dataweb import DataWeb
from database import DataBase
import pandas as pd



def main():
    dataweb = DataWeb()
    database = DataBase()
    df = dataweb.obtener_datos()
    df = dataweb.convertir_numericos(df)
    df_db = database.guardar_df(df)
    df_db2 = database.obtener_datos()
    df_db2.to_csv("src/edu_pad/static/csv/data_webdb.csv", index=False)



if __name__ == "__main__":
    main()
