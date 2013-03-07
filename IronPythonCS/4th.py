# coding: utf-8

####################################
#RSSを取得する例
####################################
#.NET Frameworkのクラスライブラリを使う宣言
import clr

#XML関連の参照設定とインポート
clr.AddReference("System.Xml")
from System.Xml import *

#RSSを取得
doc = XmlDocument()
doc.Load("http://codezine.jp/rss/new/20/index.xml")

#データ関連の参照設定とインポート
clr.AddReference("System.Data")
from System.Data import *

#XMLを解析してデータテーブルへ保存（ループ）
items = doc.SelectNodes("/rss/channel/item")
for item in items:
	row = table.NewRow()
	row["title"] = item.SelectSingleNode("title").InnerText
	row["url"] = item.SelectSingleNode("link").InnerText
	row["desc"] = item.SelectSingleNode("description").InnerText
	table.Rows.Add(row)

