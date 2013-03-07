# coding: utf-8

####################################
#System.Windows.FormsのformをIronPythonで作ってC#に渡す例
####################################
#.NET Frameworkのクラスライブラリを使う宣言

# まだどの場合にどの程度ベースなライブラリをインポートすれば
# 足りるのか良く分かっていないので、とりあえず色々追加している
import System
import clr
import sys

# DLLのフルパス指定は、スクリプト実行する場合は
# 一度、sys.path.appendでパスを移動してから参照追加する
sys.path.append(r'C:\test\samples\IronPython\CS\IronPythonCS\bin\Debug')
clr.AddReference('CsCalled')

# DLLをインポート
import CsCalled

a = CsCalled.Class1()
ret = CsCalled.Class1.doSomething(a, value)

# クラスの関数を呼ぶときは、どうも第1引数に
# そのクラスオブジェクトを渡さないといけないらしい
# IronPython2.0.2 をインストールしたのだが、
# いつ頃かまでのバージョンのPythonでは、第1引数に self を
# 渡さなくてはいけなかったらしく、その名残っぽい？

# 第1引数にクラスオブジェクトを渡さないと↓のようなエラーが出る
# TypeError: 関数名 takes exactly n argument (0 given)
