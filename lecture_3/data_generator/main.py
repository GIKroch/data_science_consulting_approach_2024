from bom_generator import BomGenerator
from procurement_generator import ProcurementGenerator
from client_generator import generate_client_prices
from sales_generator import generate_sales
from helpers import data_saver

if __name__=='__main__':
    bom = BomGenerator().generate()
    procurement = ProcurementGenerator().generate()
    client_prices = generate_client_prices(bom, procurement)
    sales_data = generate_sales(bom)

    data_saver(bom, "boms.xlsx")
    data_saver(procurement, "procurement.xlsx")
    data_saver(client_prices, "client_prices.xlsx")
    data_saver(sales_data, "sales.xlsx")