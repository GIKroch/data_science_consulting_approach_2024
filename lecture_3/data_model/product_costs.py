def calculate(df_procurement, df_boms):
    df_procurement_average = df_procurement.groupby('component')[['unit_price']].mean().reset_index()

    df_cost = df_boms.merge(df_procurement_average, how = 'left', left_on = 'Component', right_on='component')

    df_cost['unit_cost'] = df_cost['Quantity'] * df_cost['unit_price']

    df_product_cost = df_cost.groupby('Beverage')[['unit_price']].sum().reset_index()

    return df_product_cost