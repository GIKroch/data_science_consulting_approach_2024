import random
import pandas as pd
from datetime import datetime
import numpy as np
from base_generator import BaseGenerator


def random_date(year):
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)
    return start + (end - start) * random.random()


class ProcurementGenerator(BaseGenerator):
    def __init__(self, year = 2023, num_orders = 100):
        self.year = year
        self.num_orders = num_orders
        self.base_prices = {
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

    def generate(self):
        procurement_data = []
        for _ in range(self.num_orders):
            order_timestamp = random_date(self.year)
            num_components = np.random.randint(
                1, 11
            )  # Random number of components (1-10)
            components = np.random.choice(
                list(self.base_prices.keys()), size=num_components, replace=False
            )

            for component in components:
                base_price = self.base_prices[component]
                price_variation = random.uniform(-0.5, 0.5) * base_price
                unit_price = round(base_price + price_variation, 2)

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

        return (
            pd.DataFrame(procurement_data)
            .sort_values(by="order_timestamp")
            .reset_index(drop=True)
        )
