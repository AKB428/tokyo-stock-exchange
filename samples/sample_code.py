from tokyo_stock_exchange import tse

# ライブラリの関数を使用してみる
csv_file_path = tse.csv_file_path
print(csv_file_path)

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