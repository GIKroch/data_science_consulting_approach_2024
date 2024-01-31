from faker import Faker
from base_generator import BaseGenerator
import numpy as np
import pandas as pd
from config import BEVERAGE_TYPES, WORDS, BEVERAGE_COMPONENTS

class BomGenerator(BaseGenerator):
    def __init__(self):
        # Initializing faker to generate fake data
        self.fake = Faker()

        self.beverage_types = BEVERAGE_TYPES
        # List of words or phrases
        self.words = WORDS
        # Detailed components for beverages
        self.beverage_components = BEVERAGE_COMPONENTS
        
    def generate(self):
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
