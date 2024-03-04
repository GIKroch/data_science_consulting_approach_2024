from config import CLIENTS
import random
import pandas as pd
from helpers import random_date

def generate_sales(bom):
    beverages = bom['Beverage'].unique()
    all_orders = []
    for client in CLIENTS: 

        number_of_orders = random.randint(1, 20)

        order_details = []
        for order_number in range(number_of_orders):
            order_timestamp = random_date(2023)
            number_of_beverages_ordered = random.randint(1, len(beverages))

            for i in range(number_of_beverages_ordered):
                beverage_index = random.randint(0, len(beverages))
                sold_beverage = beverages[i]
                quantity = random.randint(1, 200)

                order_details.append([order_timestamp, client, sold_beverage, quantity])

        all_orders.append(order_details)

    df_sales = pd.DataFrame([x for y in all_orders for x in y], columns = ['timestamp', 'client', 'product', 'quantity_sold'])

    return df_sales
