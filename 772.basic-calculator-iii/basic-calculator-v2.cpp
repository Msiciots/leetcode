#include <iostream>
#include <stack>
using namespace std;
int myPow(int base, int exp) {
  int res = 1, sign = 1;
  if (base < 0) {
    sign = -1;
    base *= -1;
  }
  for (int i = 0; i < exp; i++) res *= base;
  return res * sign;
}
class Solution {
 public:
  int calculate(string s) {
    s += "+";
    stack<int> stack;
    char sign = '+';
    int num = 0;
    int num_flag = 0;
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == ' ')  // space
        continue;
      else if ('0' <= s[i] && s[i] <= '9'){  // number
        num = 10 * num + (s[i] - '0');
        num_flag = 1;
      }
      else if (s[i] == '(') {
        int count = 1;
        for (int j = i+1; j <= s.length(); j++) {
          if (s[j] == '(') count++;
          else if (s[j] == ')') {
            count--;
            if (count == 0) {
              num = calculate(s.substr(i + 1, j - i - 1));
              i = j;
              num_flag = 1;
              break;
            }
          }
        }
      } else {  // operator
        if (num_flag) {
          if (sign == '+')
            stack.push(num);
          else if (sign == '-')
            stack.push(-num);
          else if (sign == '*') {
            int tmp = stack.top();
            stack.pop();
            stack.push(tmp * num);

          } else if (sign == '/') {
            int tmp = stack.top();
            stack.pop();
            stack.push(tmp / num);
          } else if (sign == '^') {
            int tmp = stack.top();
            stack.pop();
            stack.push(myPow(tmp, num));
          }
        }
        sign = s[i];
        num = 0;
        num_flag = 0;
      }
    }
    int res = 0;
    while (!stack.empty()) {
      res += stack.top();
      stack.pop();
    }
    return res;
  }
};
