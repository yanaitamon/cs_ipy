using System;
using System.Collections;
using System.Collections.Generic;
//using System.Linq;
using System.Text;

namespace CsCalled
{
  /// <summary>
  /// サンプルクラス
  /// </summary>
  public class Class1 : IEnumerable
  {
    /// <summary>
    /// コンストラクタ
    /// </summary>
    /// <param name="nData"></param>
    public Class1(int nData) { }
    public Class1() { }

    /// <summary>
    /// Data 自動プロパティ
    /// </summary>
    public int myData { set; get; }

    public IEnumerator GetEnumerator()
    {
      for (int i = 0; i < myData; i++)
        yield return new Class1(i);
    }

    /// <summary>
    /// ToStringをオーバーライド
    /// </summary>
    /// <returns></returns>
    public override string ToString()
    {
//      return base.ToString();
      return String.Format("Class1<{0}>", myData);
    }

    /// <summary>
    /// + の operator
    /// </summary>
    /// <param name="a"></param>
    /// <param name="b"></param>
    /// <returns></returns>
    public static Class1 operator +(Class1 a, Class1 b)
    {
      return new Class1(a.myData + b.myData);
    }

    /// <summary>
    /// とりあえず数値を返すのみ
    /// </summary>
    /// <returns></returns>
    public int doSomething(int na)
    {
      int nRet = 0;
      try
      {
        ClassLibrary1.clsSample c = new ClassLibrary1.clsSample();

        c.doModal();

        nRet = c.return3multiple(na);
      }
      catch (Exception ex)
      {
        System.Diagnostics.Trace.WriteLine(ex.Message);
      }
      return nRet;
    }
  }
}
