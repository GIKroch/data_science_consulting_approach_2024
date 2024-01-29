import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for generating random words
fake = Faker()

# List of basic beverage types
beverage_types = ['Coke', 'Juice', 'Milkshake', 'Tea', 'Tonic', 'Energy Drink', 'Smoothie', 'Coffee', 'Lemonade', 'Soda']

# List of Shakespearean-style words or phrases
shakespearean_words = ['Tempest', 'Othello', 'Midsummer', 'Verona', 'Prospero', 'Cordelia', 'Iago', 'Titania', 'Hamlet', 'Macbeth']

# Generating unique beverage names
unique_beverage_names = []
for beverage in beverage_types:
    for word in shakespearean_words:
        unique_name = f"{beverage} {word} {fake.word().capitalize()}"
        unique_beverage_names.append(unique_name)

# Ensure names are unique
unique_beverage_names = list(set(unique_beverage_names))

# Detailed components for beverages
beverage_components = [
    'Water', 'Sugar', 'Natural Flavor', 'Citric Acid', 'Caffeine', 'Color', 
    'Preservative E202', 'Vitamin C', 'Milk', 'Coffee Extract', 'Tea Extract', 
    'Fruit Juice Concentrate', 'Carbon Dioxide', 'E330 - Citric Acid', 'E296 - Malic Acid'
]

# Creating combinations of beverages and components
beverage_combinations = []
for name in unique_beverage_names:
    components = np.random.choice(beverage_components, size=np.random.randint(3, 8), replace=False)
    for component in components:
        quantity = np.random.uniform(0.1, 5.0)
        beverage_combinations.append((name, component, quantity))

# Creating a DataFrame for the Bill of Materials
bill_of_materials_data = {
    'Beverage': [combo[0] for combo in beverage_combinations],
    'Component': [combo[1] for combo in beverage_combinations],
    'Quantity': [combo[2] for combo in beverage_combinations]
}

bill_of_materials_df = pd.DataFrame(bill_of_materials_data)
bill_of_materials_df.head()

bill_of_materials_df
