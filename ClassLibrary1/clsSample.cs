using System;
using System.Collections.Generic;
using System.ComponentModel;
//using System.Linq;
using System.Text;

namespace ClassLibrary1
{
  /// <summary>
  /// クラス
  /// </summary>
  public class clsSample
  {
    /// <summary>
    /// 9999かけて返す
    /// </summary>
    /// <param name="n"></param>
    /// <returns></returns>
    public int return3multiple(int n)
    {
      return n * 3;
    }

    public void doModal()
    {
      sampleForm.Form1 frm = new sampleForm.Form1();
      frm.ShowDialog();
    }
  }
}
