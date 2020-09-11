#include <stdio.h>

#define MOD 1000003LL

long long my_mod (long long a, long long mod)
{
 return ( a % mod + mod ) % mod;
}

long long add_mod (long long a, long long b, long long mod)
{
 return my_mod ((my_mod (a, mod) + my_mod (b,mod)), mod);
}

long long sub_mod (long long a, long long b, long long mod)
{
 return my_mod ((my_mod (a,mod) - my_mod (b,mod)), mod);
}

long long mul_mod (long long a, long long b, long long mod)
{
 return my_mod ((my_mod (a,mod) * my_mod (b,mod)), mod);
}

long long pow_mod (long long a, long long n, long long mod)
{
 if (n==0LL) return 1LL;
 if (n % 2LL != 0LL)   
   return mul_mod (a, pow_mod (a,n-1,mod), mod);
 long long tmp=pow_mod (a, n/2, mod);
 return mul_mod (tmp, tmp, mod);
}

long long div_mod (long long a, long long b, long long mod)
{
 return mul_mod (a, pow_mod (b, mod-2LL,mod),mod);
}

long long _gcd_x1,_gcd_y1,_gcd_x2,_gcd_y2;

long long gcd (long long a, long long b)
{
 if (a < 0LL) return gcd (-a,b);
 if (b < 0LL) return gcd (a,-b);
 if (a < b) return gcd (b,a);

 if (b==0LL) return a;
 
 long long x = _gcd_x1-(a/b)*_gcd_x2;
 long long y = _gcd_y1-(a/b)*_gcd_y2;

 _gcd_x1=_gcd_x2;_gcd_y1=_gcd_y2; 
 _gcd_x2=x;_gcd_y2=y; 

 return gcd (b, a%b);
}

long long ext_gcd (long long a, long long b)
{
// _gcd_x1 и _gcd_y1 после вызова - решение для ax1+by1=(a,b)
 _gcd_x1=1LL;_gcd_y1=0LL;
 _gcd_x2=0LL;_gcd_y2=1LL;

 long long d=gcd(a,b);

 if (my_abs(a) < my_abs(b)) 
  {
    long long tmp=_gcd_x1;
    _gcd_x1=_gcd_y1;
    _gcd_y1=tmp;
  }

 if (a<0) _gcd_x1=-_gcd_x1;
 if (b<0) _gcd_y1=-_gcd_y1; 

 return d;
}

long long div_mod_any (long long a, long long b, long long m)
{
 long long d1=gcd(a,b);
 long long d2=gcd(d1,m); // gcd (a,b,m);

 a=a/d2;b=b/d2;m=m/d2;
 
 d1 = ext_gcd (b,m); // b*x1 + m*y1 = 1 => x1 - обратный
 if (d1 > 1LL) return -1;
 return mul_mod (_gcd_x1,a,m); // a/b=a*1/b=a*x1 (mod m)
}



int main()
{

 
 return 0;
}

