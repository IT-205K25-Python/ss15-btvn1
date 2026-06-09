# (1) Phân tích và thiết kế:
#
# Phân định rõ biến nào là Local, biến nào là Global trong luồng chạy. 
# Biến global:
# - inventory_stock
# - total_revenue
# Biến local:
# - temp_price
# - discount
# - vat
# - amount
# - quantity
# - price
# - quantity_input
# - price_input
# - bill
# - final_total
# - choice
# - user_input

# (2) Triển khai code:
#
# Tối thiểu phải có 4 hàm: add_stock(), calculate_final_price(), process_sale(), và print_report(), cùng 1 hàm main() để chạy vòng lặp while.
# Bắt buộc phải sử dụng Docstring cho ít nhất 2 hàm để giải thích tham số đầu vào và giá trị trả về.
# Toàn bộ tên biến, tên hàm viết chuẩn snake_case bằng tiếng Anh.

inventory_stock = 100
total_revenue = 0.0

def accept_user_input(content, notice):
    '''
    Validate and accept positive integer input from user.

    Args:
        - content: str
            Message displayed when asking for input.

        - notice: str
            Error message shown when input is invalid.

    Returns:
        - int
            Valid positive integer entered by user.
    '''
    while True:
        try:
            user_input = int(input(f"{content}:"))

        except ValueError:
            print("Không hợp lệ, vui lòng nhập lại")
        
        else:
            if user_input > 0:
                return user_input
            print(f"{notice}")

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

def print_report():
    '''
    Display inventory and revenue report.

    Args:
        - None

    Returns:
        - None
    '''

    global inventory_stock
    global total_revenue

    print(f"Tồn kho hiện tại: {inventory_stock}")
    print(f"Tổng doanh thu: {total_revenue}")

while True:
    print('''
========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
          ''')

    choice = input("Nhập lựa chọn của bạn: ")

    match choice:
        case '1':
            amount = accept_user_input(
                "Nhập số lượng cần thêm vào", 
                "Số lượng phải lớn hơn 0. Vui lòng nhập lại"
            )

            add_stock(amount)
        case '2':
            quantity_input = accept_user_input(
                "Nhập số lượng cần mua",
                "Số lượng phải lớn hơn 0. Vui lòng nhập lại"
            )
            price_input = accept_user_input(
                "Nhập giá sản phẩm",
                "Giá phải lớn hơn 0. Vui lòng nhập lại"
            )

            bill = process_sale(quantity_input, price_input)
            if bill is not None:
                temp_price, discount, vat = bill
                final_total = temp_price * (1 - discount) + vat

                inventory_stock -= quantity_input
                total_revenue += final_total

                print("-> Hóa đơn chi tiết:")
                print(f"Số lượng: {quantity_input} | Đơn giá: ${float(price_input)}")
                print(f"Tạm tính: ${float(temp_price)}")
                print(f"Giảm giá ({int(discount * 100)}%): ${temp_price * discount}")
                print(f"Thuế VAT (8%): ${temp_price * (1 - discount) * 0.08}")
                print(f"Tổng thanh toán: ${final_total}")
                print("Đã bán thành công !")
        case '3':
            print_report()
        case '4':
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ")
