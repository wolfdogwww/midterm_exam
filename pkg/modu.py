import json 
def triangle_zhonxin(A,B,C):
    """
        計算一個三角形的重心
        Args: A(tuples) the coordinate of A point
              B(tuples) the coordinate of B point
              C(tuples) the coordinate of C point
        return重心座標
    """
    X=(int(A[0])+int(B[0])+int(C[0]))/3
    Y=(int(A[1])+int(B[1])+int(C[1]))/3
    return (int(X),int(Y))
def read_json(file_name: str) -> dict:
    """
    讀取json檔案回傳一個字典

    Args:
        file_name (str): Json檔案的名子

    Returns:
        dict: 包含json的檔案(字典的格式)
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)
def print_json(data: dict) -> None:
    """
    輸出一個jSON的格式的字典

    Args:
        data (dict): 要被輸出的字典
    """
    print(json.dumps(data, ensure_ascii=False, indent=4))
def process_data(data: dict, discount: float) -> None:
    """
    對字典中的菜單品項進行折扣處理

    Args:
        data (dict): 含菜單的字典。
        discount (float): 折扣率（介於 0.0 到 1.0 之間）。
    """
    for category in data["categories"]:
        for item in category["items"]:
            item["price"] = round(item["price"] * discount)

    
def write_json(data: dict, file_name: str) -> None:
    """
    將字典寫入 JSON 檔案。

    Args:
        data (dict): 要被寫入Json的字典
        file_name (str): 要被寫入json的json檔案名子
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)