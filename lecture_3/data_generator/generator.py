import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random


def random_date(year):
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)
    return start + (end - start) * random.random()


class Generator:
    def __init__(self):
        # Initializing faker to generate fake data
        self.fake = Faker()

        self.beverage_types = [
            "Coke",
            "Juice",
            "Milkshake",
            "Tea",
            "Tonic",
            "Energy Drink",
            "Smoothie",
            "Coffee",
            "Lemonade",
            "Soda",
        ]
        # List of words or phrases
        self.words = [
            "Tempest",
            "Othello",
            "Midsummer",
            "Verona",
            "Prospero",
            "Cordelia",
            "Iago",
            "Titania",
            "Hamlet",
            "Macbeth",
        ]
        # Detailed components for beverages
        self.beverage_components = [
            "Water",
            "Sugar",
            "Natural Flavor",
            "Citric Acid",
            "Caffeine",
            "Color",
            "Preservative E202",
            "Vitamin C",
            "Milk",
            "Coffee Extract",
            "Tea Extract",
            "Fruit Juice Concentrate",
            "Carbon Dioxide",
            "E330 - Citric Acid",
            "E296 - Malic Acid",
        ]

    def generate(self, generator_type):
        if generator_type == "bom":
            return self._generate_boms()
        elif generator_type == "plant":
            return self._generate_plant()
        elif generator_type == "client":
            return self._generate_client()
        elif generator_type == "sales":
            return self._generate_sales()
        elif generator_type == "procurement":
            return self._generate_procurement()

    def _generate_boms(self):
        # Generating unique beverage names
        unique_beverage_names = []
        for beverage in self.beverage_types:
            for word in self.words:
                unique_name = f"{beverage} {word} {self.fake.word().capitalize()}"
                unique_beverage_names.append(unique_name)

        # Ensure names are unique
        unique_beverage_names = list(set(unique_beverage_names))

        # Creating combinations of beverages and components
        beverage_combinations = []
        for name in unique_beverage_names:
            components = np.random.choice(
                self.beverage_components, size=np.random.randint(3, 8), replace=False
            )
            for component in components:
                quantity = np.random.uniform(0.1, 5.0)
                beverage_combinations.append((name, component, quantity))

        # Creating a DataFrame for the Bill of Materials
        bill_of_materials_data = {
            "Beverage": [combo[0] for combo in beverage_combinations],
            "Component": [combo[1] for combo in beverage_combinations],
            "Quantity": [combo[2] for combo in beverage_combinations],
        }

        bill_of_materials_df = pd.DataFrame(bill_of_materials_data)
        return bill_of_materials_df

    def _generate_procurement(self):
        num_orders = 100
        current_year = 2023

        # Component base prices (approximations for 2023, in EUR)
        base_prices = {
            "Water": 0.20,
            "Sugar": 0.50,
            "Natural Flavor": 5.00,
            "Citric Acid": 3.00,
            "Caffeine": 15.00,
            "Color": 10.00,
            "Preservative E202": 7.00,
            "Vitamin C": 20.00,
            "Milk": 0.70,
            "Coffee Extract": 25.00,
            "Tea Extract": 30.00,
            "Fruit Juice Concentrate": 8.00,
            "Carbon Dioxide": 0.30,
            "E330 - Citric Acid": 3.50,
            "E296 - Malic Acid": 4.00,
        }

        procurement_data = []
        for _ in range(num_orders):
            order_timestamp = random_date(current_year)
            num_components = np.random.randint(
                1, 11
            )  # Random number of components (1-10)
            components = np.random.choice(
                list(base_prices.keys()), size=num_components, replace=False
            )

            for component in components:
                base_price = base_prices[component]

                # Generating price with variation up to 50%
                price_variation = random.uniform(-0.5, 0.5) * base_price
                unit_price = round(base_price + price_variation, 2)

                # Generating quantity with variation up to 50%
                quantity_variation = random.uniform(0.5, 1.5)
                quantity = round(np.random.uniform(1, 100) * quantity_variation, 0)

                procurement_data.append(
                    {
                        "order_timestamp": order_timestamp,
                        "component": component,
                        "quantity": quantity,
                        "unit_price": unit_price,
                    }
                )

        # Creating a DataFrame
        procurement_df = pd.DataFrame(procurement_data)

        # Sorting by order_timestamp
        procurement_df = procurement_df.sort_values(by="order_timestamp").reset_index(
            drop=True
        )

        return procurement_df


# Using the class
generator = Generator()
df_boms = generator.generate("bom")
df_procurement = generator.generate("procurement")

#
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

# Let's use prod costs as a input for the prices clients are paying

clients = ["FourCare", "WSP", "WWO", "Beetle", "Dila", "Froggie", "Mercato", "PremiumX"]


def price_modifier(price, client_price_level):
    individual_price_rate = random.uniform(
        client_price_level - 0.05, client_price_level + 0.05
    )
    new_price = price + (price * individual_price_rate)
    return new_price


df_client_prices = pd.DataFrame()

for client in clients:
    # This is set on client level
    client_price_level = random.uniform(-0.3, 0.3)

    df_client = df_prod_costs.copy()
    df_client['client'] = client
    df_client['sales_price'] = df_client["production_cost"].apply(
        lambda x: price_modifier(x, client_price_level)
    )
    df_client = df_client.loc[:,['client', 'Beverage', 'sales_price']].copy()

    df_client_prices = pd.concat([df_client_prices, df_client])

df_client_prices