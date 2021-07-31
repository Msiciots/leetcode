#include<iostream>
// #include "basic-calculator.cpp"
#include "basic-calculator-v2.cpp"
using namespace std;
 
// main function -
// where the execution of program begins
int main(int argc, char *argv[])
{
    // prints hello world
    Solution s; 
    int res = s.calculate(argv[1]);
    cout<<res<<endl;
     
    return 0;
}
