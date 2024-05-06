# Tokyo Stock Exchange Library

`tokyo-stock-exchange`は東京証券取引所の証券コードを扱うPythonライブラリです。株式のコードや名称、分類情報に基づいて詳細なデータを照会する機能を提供します。

## 特徴

- 株式コードと企業名の相互変換
- 特定の株式の詳細情報取得
- 株式市場のカテゴリーに基づくデータ抽出

## インストール

```bash
pip install tokyo-stock-exchange
```

## 使い方


### 証券コードデータの指定

東証証券コードデータに関しては毎月更新されるため自身でダウンロードしUTF8のCSV形式で配置し環境変数でパスを指定してください。データを指定しない場合はライブラリ内にある古いコード一覧が使用されます。
元データはSJISのエクセルのためGoogleスプレッドシートでUFT8のCSVにするのがおすすめです。

https://www.jpx.co.jp/markets/statistics-equities/misc/01.html

```python
export TSE_LIST_DATA_PATH=./tokyo_stock_exchange/tse20240229.csv
```



### 銘柄一覧データファイルの確認と指定

```python
from tokyo_stock_exchange import tse

# CSVファイルのパスを取得
csv_file_path = tse.csv_file_path
print(csv_file_path)

# CSVファイルの日付を取得
print(tse.get_file_date())
```



```
/home/penguin/.local/lib/python3.10/site-packages/tokyo_stock_exchange/tse.csv
20240329
```

### 使い方

```python
from tokyo_stock_exchange import tse

# 株式コードによる企業名の取得
stock_name = tse.get_name_by_code("7832")
print(stock_name) 
```

```
バンダイナムコホールディングス
```

```python
# 企業名による株式コードの取得
stock_code = tse.get_code_by_name("バンダイナムコホールディングス")
print(stock_code)
```

```
7832
```

```python
# 株式コードもしくは証券コードによる株式情報の取得
sotck_info = tse.get_stock_info("7203")
print(sotck_info[0], sotck_info[1])

sotck_info = tse.get_stock_info("トヨタ自動車")
print(sotck_info[0], sotck_info[1])
```

```
7203 トヨタ自動車
7203 トヨタ自動車
```

### 「証券コード英文字組入れ」にも対応

```
stock_name = tse.get_name_by_code("147A")
print(stock_name)

stock_code = tse.get_code_by_name("ソラコム")
print(stock_code)

sotck_info = tse.get_stock_info("147A")
print(sotck_info[0], sotck_info[1])

sotck_info = tse.get_stock_info("ソラコム")
print(sotck_info[0], sotck_info[1])
```

```
ソラコム
147A
147A ソラコム
147A ソラコム
```


### カテゴリーに基づくデータ抽出

```python
# カテゴリーの出現回数を表示
tse.print_category_counts()
```

```
[市場・商品区分]
プライム（内国株式） = 1652
ETF・ETN = 349
グロース（内国株式） = 573
PRO Market = 102
スタンダード（内国株式） = 1607
プライム（外国株式） = 1
REIT・ベンチャーファンド・カントリーファンド・インフラファンド = 63
スタンダード（外国株式） = 2
グロース（外国株式） = 3
出資証券 = 2

[33業種区分]
水産・農林業 = 12
- = 414
医薬品 = 78
情報・通信業 = 620
陸運業 = 63
サービス業 = 557
建設業 = 161
~~~略
[規模区分]
TOPIX Small 2 = 1152
- = 2208
TOPIX Mid400 = 398
TOPIX Small 1 = 497
TOPIX Large70 = 69
TOPIX Core30 = 30
```

### 単発クエリー

```python
# 条件を満たす企業を検索し、出力
def single_category_task():
    matching_items = tse.category_find("規模区分=TOPIX Core30")
    for code, name in matching_items:
        print(f"{name} ({code})")
        # code に対して株価データ取得してグラフ化する処理などを追加

single_category_task()
```

```
セブン＆アイ・ホールディングス (3382)
信越化学工業 (4063)
武田薬品工業 (4502)
アステラス製薬 (4503)
第一三共 (4568)
リクルートホールディングス (6098)
ＳＭＣ (6273)
ダイキン工業 (6367)
日立製作所 (6501)
ニデック (6594)
ソニーグループ (6758)
キーエンス (6861)
ファナック (6954)
村田製作所 (6981)
トヨタ自動車 (7203)
本田技研工業 (7267)
ＨＯＹＡ (7741)
任天堂 (7974)
伊藤忠商事 (8001)
三井物産 (8031)
東京エレクトロン (8035)
三菱商事 (8058)
三菱ＵＦＪフィナンシャル・グループ (8306)
三井住友フィナンシャルグループ (8316)
みずほフィナンシャルグループ (8411)
東京海上ホールディングス (8766)
日本電信電話 (9432)
ＫＤＤＩ (9433)
ソフトバンク (9434)
ソフトバンクグループ (9984)
```

### 複合クエリー

```python
# 複数の条件を満たす企業を検索し、出力
def category_task():
    matching_items = tse.category_find("規模区分=TOPIX Mid400", "33業種区分=陸運業")
    for code, name in matching_items:
        print(f"{name} ({code})")
        # code に対して株価データ取得してグラフ化する処理などを追加

category_task()
```

```
東武鉄道 (9001)
相鉄ホールディングス (9003)
東急 (9005)
京浜急行電鉄 (9006)
小田急電鉄 (9007)
京王電鉄 (9008)
京成電鉄 (9009)
西武ホールディングス (9024)
西日本鉄道 (9031)
近鉄グループホールディングス (9041)
阪急阪神ホールディングス (9042)
南海電気鉄道 (9044)
京阪ホールディングス (9045)
名古屋鉄道 (9048)
ヤマトホールディングス (9064)
山九 (9065)
ニッコンホールディングス (9072)
セイノーホールディングス (9076)
九州旅客鉄道 (9142)
ＳＧホールディングス (9143)
ＮＩＰＰＯＮ　ＥＸＰＲＥＳＳホールディングス (9147)
```


## ライセンス

このライブラリは[MITライセンス](LICENSE)のもとで公開されています。

