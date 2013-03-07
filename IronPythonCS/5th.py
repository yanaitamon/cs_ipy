# coding: utf-8

####################################
#C#のDLLのAPIをIronPythonから呼び出して結果をC#に返す例
####################################
#.NET Frameworkのクラスライブラリを使う宣言

# まだどの場合にどの程度ベースなライブラリをインポートすれば
# 足りるのか良く分かっていないので、とりあえず色々追加している
import System
import clr
import sys

# DLLのフルパス指定は、スクリプト実行する場合は
# 一度、sys.path.appendでパスを移動してから参照追加する
# clr.AddReferenceToFile('C:/test/samples/IronPython/CS/IronPythonCS/bin/Debug/CsCalled.dll')
# clr.AddReferenceToFile("C:/test/samples/IronPython/CS/IronPythonCS/bin/Debug/ClassLibrary1.dll")
sys.path.append(r'C:\test\samples\IronPython\CS\IronPythonCS\bin\Debug')
clr.AddReference('CsCalled')
# clr.AddReferenceToFile('CsCalled') # こちらでも行ける
# clr.AddReference('ClassLibrary1')

# DLLをインポート
import CsCalled
# import ClassLibrary1

a = CsCalled.Class1()
# 下記の value は、C#側からipyグローバル変数として追加されたもの
# 下記の ret は、ipy側で指定したもの C#側で型を合わせてipy側から取得できる
ret = CsCalled.Class1.doSomething(a, value)


# クラスの関数を呼ぶときは、どうも第1引数に
# そのクラスオブジェクトを渡さないといけないらしい
# IronPython2.0.2 をインストールしたのだが、
# いつ頃かまでのバージョンのPythonでは、第1引数に self を
# 渡さなくてはいけなかったらしく、その名残っぽい？

# 第1引数にクラスオブジェクトを渡さないと↓のようなエラーが出る
# TypeError: 関数名 takes exactly n argument (0 given)
