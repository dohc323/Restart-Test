from dataclasses import dataclass

@dataclass
class ItemOrigin:
    country: str
    production_date: str
    
@dataclass
class InventoryItem:
    name: str
    quantity: int
    serial_num: str
    origin = ItemOrigin
    
def main():
    item_origin = ItemOrigin(country = "Ethiopia", production_date= "02/12/23")
    my_item1 = InventoryItem(name = "printer", 
                            quantity= 5, 
                            serial_num= "AAA000", 
                            origin = item_origin)
    my_serailized_object = my_item1.__dict__
    print(my_serailized_object)
    my_item2 = InventoryItem(**my_serailized_object)
    print(my_item2.__dict__)

if __name__ == "__main__":
    main()
    