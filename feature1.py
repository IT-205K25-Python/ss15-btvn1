def conver_user_input_to_int(content:str) -> int:
    while True:
        try:
            user_input = int(input(f"{content}"))

        except ValueError:
            print("Không hợp lệ, vui lòng nhập lại")
        
        else: 
            return user_input

inventory_stock = 100

def add_stock(amount):
    '''
    Add product quantity into inventory stock.

    Args:
        - amount: int
            Quantity of products added to inventory.

    Returns:
        - None
    '''
 
    if(amount <= 0):
        print("Dữ liệu nhập vào phải lớn hơn 0.") 
        return

    global inventory_stock
    inventory_stock += amount
    
    print(f"Đã thêm thành công {amount} sản phẩm")
    print(f"Tồn kho hiện tại: {inventory_stock}")


amount = None
while True:
    try: 
        amount = int(input("Nhập số lượng sản phẩm cần mua: "))

    except ValueError:
        print("Không hợp lệ. Vui lòng nhập lại")

    else:
        if amount > 0:
            break
        print("Số lượng phải lớn hơn 0")

add_stock(amount)
