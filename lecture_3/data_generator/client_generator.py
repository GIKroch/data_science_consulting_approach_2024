from config import CLIENTS
import random
import pandas as pd

def price_modifier(price, client_price_level):
    individual_price_rate = random.uniform(
        client_price_level - 0.05, client_price_level + 0.05
    )
    new_price = price + (price * individual_price_rate)
    return new_price

# Let's use prod costs as a input for the prices clients are paying
def generate_prod_costs(df_boms, df_procurement):
    component_prices = (
        df_procurement.groupby(["component"])[["unit_price"]].mean().reset_index()
    )

    df_boms_prices = df_boms.merge(
        component_prices, how="left", left_on="Component", right_on="component"
    )

    df_boms_prices["production_cost"] = (
        df_boms_prices["Quantity"] * df_boms_prices["unit_price"]
    )

    df_prod_costs = (
        df_boms_prices.groupby("Beverage")[["production_cost"]].sum().reset_index()
    )

    return df_prod_costs

def generate_client_prices(df_boms, df_procurement):
    df_client_prices = pd.DataFrame()
    df_prod_costs = generate_prod_costs(df_boms, df_procurement)

    for client in CLIENTS:
        # This is set on client level
        client_price_level = random.uniform(-0.3, 0.3)

        df_client = df_prod_costs.copy()
        df_client['client'] = client
        df_client['sales_price'] = df_client["production_cost"].apply(
            lambda x: price_modifier(x, client_price_level)
        )
        df_client = df_client.loc[:,['client', 'Beverage', 'sales_price']].copy()

        df_client_prices = pd.concat([df_client_prices, df_client])

    return df_client_prices
