from read_data import data_reader
from product_costs import calculate

df_boms, df_client_prices, df_procurement, df_sales = data_reader()

df_product_costs = calculate(df_procurement, df_boms)

