#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

///// ax^2+bx+c=0 /////

int main()
{
  cout << setiosflags(ios::scientific) << endl;
 
   double a = 1;
   double x1=1.e-12;
   double x2=1.e12;
   double b = -(x1+x2);
   double c = x1*x2;
   double delta = b*b - 4*a*c;
   double sqrtdelta = pow(delta, 0.5);
   double sol1, sol2;
 
 /////// metodo classico ///////
 
 
  sol1 = (-b - sqrtdelta)/(2*a);
  sol2 = (-b + sqrtdelta)/(2*a);
  cout << "con il metodo classico i dati sono; " << endl;
  cout << "il delta è " << delta << endl;;
  cout << "la radice del delta è " << sqrtdelta << endl;
  if(sol1 < sol2)
  cout << "la prima soluzione è : " << sol1 << endl;
  cout <<"la seconda soluzione è : " << sol2 << endl;
  
  cout << "con il metodo alternativo i dati sono : " << endl;

////// metodo alternativo ///////

 if(b>=0)
 {
  sol1 = (-b - sqrtdelta)/(2*a);
  sol2 = (2*c)/(-b - sqrtdelta);
    cout << "il delta è " << delta << endl;;
    cout << "la radice del delta è " << sqrtdelta << endl;
    cout << "la prima soluzione è : " << sol1 << endl;
    cout <<"la seconda soluzione è : " << sol2 << endl;
 }
 else if(b<0)
 {
  sol1= (2*c)/(-b + sqrtdelta);
  sol2 = (-b + sqrtdelta)/(2*a);
    cout << "il delta è " << delta << endl;;
    cout << "la radice del delta è " << sqrtdelta << endl;
    cout << "la prima soluzione è : " << sol1 << endl;
    cout << "la seconda soluzione è : " << sol2 << endl;
 }
 else  
      
return 0;
}









