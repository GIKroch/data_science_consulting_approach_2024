from bom_generator import BomGenerator
from procurement_generator import ProcurementGenerator

if __name__=='__main__':
    bom = BomGenerator().generate()
    procurement = ProcurementGenerator().generate()

