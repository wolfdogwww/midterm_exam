from pkg import print_json, process_data, read_json, write_json
MENU_FILE = 'menu.json'       # 輸入檔案名稱
OUTPUT_FILE = 'output.json'   # 輸出檔案名稱
menu = read_json(MENU_FILE)
print_json(menu)
new_dish = {
    "name": "海鮮燉飯",
   "price": 239,
    "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    }
menu["categories"][1]["items"].append(new_dish)
print_json(menu)
discount = float(input("請輸入折扣率(0.0 ~ 1.0): "))
process_data(menu, discount)
print_json(menu)
write_json(menu, OUTPUT_FILE)
