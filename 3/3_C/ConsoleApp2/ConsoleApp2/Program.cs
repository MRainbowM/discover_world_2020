using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            int n = Convert.ToInt32(str);
            int i = 1;
            int z = 0;
            string answ = "1 ";
            while (i != n)
            {
                if(i * 3 <= n)
                {
                    i = i * 3;
                } else if(i * 2 <= n)
                {
                    i = i * 2;
                } 
                else
                {
                    i = i + 1;
                }
                z ++;
                answ = answ + Convert.ToString(i) + ' ';
                if (i == n) { break; }
            }
            answ = Convert.ToString(z) + '\n' + answ;
            Console.WriteLine(answ);

        }
    }
}
