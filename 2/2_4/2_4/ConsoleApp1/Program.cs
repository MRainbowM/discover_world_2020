using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = Console.ReadLine();
            string[] str_arr = str.Split(' ');
            long n = Convert.ToInt64(str_arr[0]);
            long m = Convert.ToInt64(str_arr[1]);
            long z = mod(n, m);
           
            if (n == 0)
            {
                Console.WriteLine(1);
            } else
            {
                Console.WriteLine(z);
            }
        }
        public static long mod(long n, long m)
        {
            double k = Math.Pow(n, n);
            double x = (k % m + m) % m;
            long z = Convert.ToInt64(x);
            return z;
        }
    }
}
