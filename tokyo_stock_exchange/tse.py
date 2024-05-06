import pandas as pd
import os
import re

CSV_FILE_NAME = 'tse.csv'

def print_category_counts():
    # 各カテゴリーごとに処理
    for category, subdict in category_code_hashes.items():
        print(f"[{category}]")
        
        # 各区分ごとに銘柄の数を数える
        for category_value, codes in subdict.items():
            count = len(codes)  # 銘柄の数
            print(f"{category_value} = {count}")
        
        print()  # カテゴリー間に空行を入れる

def get_file_date():
    data_csv = pd.read_csv(csv_file_path)
    
    return data_csv.iloc[0]['日付']

def create_category_code_hash(csv_file_path):
    # CSVファイルを読み込む
    data_csv = pd.read_csv(csv_file_path)
    
    # 各カテゴリーごとに「コード：銘柄名」の組のハッシュを作成
    categories = ['市場・商品区分', '33業種区分', '17業種区分', '規模区分']
    category_dicts = {category: {} for category in categories}
    
    for index, row in data_csv.iterrows():
        code = row['コード']
        name = row['銘柄名']
        
        for category in categories:
            category_value = row[category]
            if category_value not in category_dicts[category]:
                category_dicts[category][category_value] = {}
            category_dicts[category][category_value][code] = name
    
    return category_dicts

def print_category(category, category_value):
    if category in category_code_hashes and category_value in category_code_hashes[category]:
        for code, name in category_code_hashes[category][category_value].items():
            print(f"{code}\t{name}")

def print_category_find(*criteria):
    # 初期の銘柄リスト（すべての銘柄）を取得
    matching_items = None

    # 各条件に基づいてフィルタリング
    for criterion in criteria:
        category, value = criterion.split("=")
        value = value.strip()
        # 指定されたカテゴリでフィルタリング
        if matching_items is None:
            # 初回はマッチングアイテムをそのカテゴリのアイテムに設定
            matching_items = category_code_hashes.get(category, {}).get(value, {})
        else:
            # 2回目以降は、すでに見つかったマッチングアイテムを絞り込む
            matching_items = {
                code: name for code, name in matching_items.items()
                if code in category_code_hashes.get(category, {}).get(value, {})
            }

    # マッチングアイテムを出力
    for code, name in matching_items.items():
        print(f"{code}\t{name}")

    print(f"条件合致: {len(matching_items)}件")    
        
# ここから新しい関数を定義
def get_code_by_name(name):
    """銘柄名から証券コードを取得する関数"""
    for category, subdict in category_code_hashes.items():
        for category_value, codes in subdict.items():
            for code, stock_name in codes.items():
                if stock_name == name:
                    return code
    return None

def get_name_by_code(code):
    """証券コードから銘柄名を取得する関数"""
    for category, subdict in category_code_hashes.items():
        for category_value, codes in subdict.items():
            if code in codes:
                return codes[code]
    return None

def category_find(*criteria):
    # 初期の銘柄リスト（すべての銘柄）を取得
    matching_items = None

    # 各条件に基づいてフィルタリング
    for criterion in criteria:
        category, value = criterion.split("=")
        value = value.strip()
        # 指定されたカテゴリでフィルタリング
        if matching_items is None:
            # 初回はマッチングアイテムをそのカテゴリのアイテムに設定
            matching_items = category_code_hashes.get(category, {}).get(value, {})
        else:
            # 2回目以降は、すでに見つかったマッチングアイテムを絞り込む
            matching_items = {
                code: name for code, name in matching_items.items()
                if code in category_code_hashes.get(category, {}).get(value, {})
            }

    # マッチングアイテムのリストを返す
    return list(matching_items.items())

def get_stock_info(stock_name_or_code):
    """
    Given a stock name or code, returns the corresponding stock code and name.
    If the input is only digits, assumes it's a stock code and fetches the name.
    If the input is not digits, assumes it's a name and fetches the stock code.
    
    Args:
        stock_name_or_code (str): The stock name or code.
        
    Returns:
        tuple: A tuple containing the stock code and stock name.
        
    Raises:
        ValueError: If the stock name or code cannot be found.
    """
    # 正規表現パターンを定義
    # https://www.jpx.co.jp/sicc/code-pr/
    pattern = r"^\d{4}$|^\d{3}[A-Z]$|^\d[A-Z]\d{2}$"

    if re.match(pattern, stock_name_or_code):
        stock_code = stock_name_or_code
        stock_name = get_name_by_code(stock_code)  # This function should be defined in topixlib
        if stock_name is None:
            raise ValueError(f"Error: 銘柄名が見つかりませんでした。証券コード: {stock_code}")
    else:
        stock_code = get_code_by_name(stock_name_or_code)  # This function should be defined in topixlib
        stock_name = stock_name_or_code
        if stock_code is None:
            raise ValueError(f"Error: 証券コードが見つかりませんでした。銘柄名: {stock_name}")

    return stock_code, stock_name


# CSVファイルのパスを動的に設定する
# 実行中のスクリプトのディレクトリパスを取得する
script_dir = os.path.dirname(os.path.abspath(__file__))

# CSVファイルのパスを動的に設定する
csv_file_path = os.path.join(script_dir, CSV_FILE_NAME)
if 'TSE_LIST_DATA_PATH' in os.environ:
    csv_file_path = os.environ['TSE_LIST_DATA_PATH']
category_code_hashes = create_category_code_hash(csv_file_path)