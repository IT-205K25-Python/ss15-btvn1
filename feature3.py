inventory_stock = 100
total_revenue = 0.0 


def print_report():
    '''
    Chức năng: Hàm dùng để in ra báo cáo tồn kho và doanh thu

    Args: None

    Returns: None
    '''

    global inventory_stock
    global total_revenue

    print(f"Tồn kho hiện tại: {inventory_stock}")
    print(f"Tổng doanh thu: {total_revenue}")
