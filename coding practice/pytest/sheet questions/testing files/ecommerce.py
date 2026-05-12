
def calculate_total(items,tax_rate):
        
    for item_price in items:
        if item_price<0:
            raise ValueError("Item price cannot be negative")
            
        if tax_rate<0 or tax_rate>1:
            raise ValueError("Invalid tax rate")
        

    total=sum(items)
    amount=total+(total*tax_rate)
    return amount
