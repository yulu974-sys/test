# -*- coding: utf-8 -*-

def find_product(products: list, pid: int) -> dict:
    for p in products:
        if p.get("id") == pid:
            return {"success": True, "data": p}
    return {"success": False, "data": None}


def format_price(price: int) -> str:
    return f"${price:,}"


if __name__ == "__main__":
    products = [
        {"id": 1, "name": "Keyboard", "price": 1200},
        {"id": 2, "name": "Mouse", "price": 800},
        {"id": 3, "name": "Monitor", "price": 4500}
    ]

    # 查詢 ID: 1
    print("=== 查詢 ID: 1 ===")
    result = find_product(products, 1)
    if result["success"]:
        product = result["data"]
        print(f"找到產品: {product['name']}, 價格: {format_price(product['price'])}")
    else:
        print("=> 查無此產品")

    print()

    # 查詢 ID: 99
    print("=== 查詢 ID: 99 ===")
    result = find_product(products, 99)
    if result["success"]:
        product = result["data"]
        print(f"找到產品: {product['name']}, 價格: {format_price(product['price'])}")
    else:
        print("=> 查無此產品")
