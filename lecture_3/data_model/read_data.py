import pandas as pd 

def data_reader():
    """Module to read data

    Returns
    -------
    pd.DataFrame
        all dataframes
    """
    df_boms = pd.read_excel("generated_data\\boms.xlsx")
    df_client_prices = pd.read_excel("generated_data\\client_prices.xlsx")
    df_procurement = pd.read_excel("generated_data\\procurement.xlsx")
    df_sales = pd.read_excel("generated_data\\sales.xlsx")

    return df_boms, df_client_prices, df_procurement, df_sales

