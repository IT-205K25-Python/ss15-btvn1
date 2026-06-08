inventory_stock = 100
total_revenue = 0.0

def process_sale(quantity, price):
    '''
    Process selling operation and validate inventory quantity.

    Args:
        - quantity: int
            Quantity customer wants to buy.

        - price: int
            Unit price of product.

    Returns:
        - tuple
            (temp_price, discount, vat)

        - None
            If inventory is not enough.
    '''
    global inventory_stock
    if(quantity > inventory_stock):
        print(f"Không đủ hàng trong kho hiện tại chỉ còn {inventory_stock}")
        return
    
    return calculate_final_price(quantity, price)

def calculate_final_price(quantity, price):
    '''
    Calculate subtotal, discount and VAT for customer invoice.

    Args:
        - quantity: int
            Quantity of products purchased.

        - price: int
            Product unit price.

    Returns:
        - tuple
            temp_price: float
            discount: float
            vat: float
    '''

    temp_price = quantity * price

    discount = 0.1 if temp_price >= 1000 else 0

    vat = temp_price * (1 - discount) * 0.08

    return temp_price, discount, vat

while True:
    try: 
        quanttiy_input = int(input("Nhập số lượng sản phẩm cần mua: "))

    except ValueError:
        print("Không hợp lệ. Vui lòng nhập lại")

    else:
        if quanttiy_input > 0:
            break
        print("Số lượng phải lớn hơn 0")


while True:
    try: 
        price_input = int(input("Nhập số lượng sản phẩm cần mua: "))

    except ValueError:
        print("Không hợp lệ. Vui lòng nhập lại")

    else:
        if quanttiy_input > 0:
            break
        print("Giá tiền phải lớn hơn 0")
