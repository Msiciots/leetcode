#include <stack>
using namespace std;
typedef struct {
  string op;
  int pri_in;
  int pri_out;
} operator_t;
int myPow(int base, int exp) {
  int res = 1;
  for (int i = 0; i < exp; i++) res *= base;
  return res;
}
class Solution {
 public:
  int calculate(string s) {
    s += "+";
    stack<int> operand_stack;
    stack<operator_t> operator_stack;

    int num = 0;
    int flag_num = 0;
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == ' ')  // space
        continue;
      else if ('0' <= s[i] && s[i] <= '9') {  // number
        num = 10 * num + (s[i] - '0');
        flag_num = 1;
      } else {  // operator

        if (flag_num) {
          operand_stack.push(num);
          flag_num = 0;
        }

        operator_t tmp;
        tmp.op = s[i];
        // Set priority
        if (operand_stack.empty() && s[i] == '-')
          tmp.pri_out = tmp.pri_in = 1;
        else if (s[i] == ')')
          tmp.pri_out = 5;
        else if (s[i] == '(') {
          tmp.pri_out = 0;
          tmp.pri_in = 5;
        } else if (s[i] == '+' || s[i] == '-') {
          tmp.pri_out = tmp.pri_in = 4;
        } else if (s[i] == '*' || s[i] == '/')
          tmp.pri_out = tmp.pri_in = 3;
        else if (s[i] == '^')
          tmp.pri_out = tmp.pri_in = 2;

        // Adjust stack
        while (!operator_stack.empty() &&
               (operator_stack.top().pri_in <= tmp.pri_out)) {
          operator_t opt = operator_stack.top();
          operator_stack.pop();
          if (opt.pri_in == 5) break;
          if (opt.pri_in == 1) {
            int opr1 = operand_stack.top();
            operand_stack.pop();
            operand_stack.push(opr1 * (-1));
            continue;
          }

          int opr1 = operand_stack.top();
          operand_stack.pop();
          int opr2 = operand_stack.top();
          operand_stack.pop();
          int res;
          if (opt.pri_in == 4) {
            res = opt.op == "+" ? opr2 + opr1 : opr2 - opr1;
          } else if (opt.pri_in == 3) {
            res = opt.op == "*" ? opr2 * opr1 : opr2 / opr1;
          } else if (opt.pri_in == 2)
            res = myPow(opr2, opr1);
          operand_stack.push(res);
        }
        num = 0;
        if (tmp.op != ")") operator_stack.push(tmp);
      }
    }
    if (num) operand_stack.push(num);

    return operand_stack.top();
  }
};
