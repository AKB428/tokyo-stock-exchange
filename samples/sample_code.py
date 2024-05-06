from tokyo_stock_exchange import tse

csv_file_path = tse.csv_file_path
print(csv_file_path)

print(tse.get_file_date())

stock_name = tse.get_name_by_code("7832")
print(stock_name)

stock_code = tse.get_code_by_name("バンダイナムコホールディングス")
print(stock_code)

sotck_info = tse.get_stock_info("7203")
print(sotck_info[0], sotck_info[1])

sotck_info = tse.get_stock_info("トヨタ自動車")
print(sotck_info[0], sotck_info[1])


stock_name = tse.get_name_by_code("147A")
print(stock_name)

stock_code = tse.get_code_by_name("ソラコム")
print(stock_code)

sotck_info = tse.get_stock_info("147A")
print(sotck_info[0], sotck_info[1])

sotck_info = tse.get_stock_info("ソラコム")
print(sotck_info[0], sotck_info[1])

print("------------")
tse.print_category("規模区分", "TOPIX Core30")

print("------------")
tse.print_category_counts()

print("------------")
def category_task():
    matching_items = tse.category_find("規模区分=TOPIX Mid400", "33業種区分=陸運業")
    for code, name in matching_items:
        print(f"{name} ({code})")
        # 証券コードを用いて株価を取得してチャートを書いたり分析するコードを書く
        # getStockDataAndGenChart(code)
        
category_task()