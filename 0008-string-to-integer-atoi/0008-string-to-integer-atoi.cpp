class Solution {
public:
    int myAtoi(string s) {
        int n = s.length();
        int i = 0;

        // 1. Skip leading whitespace
        while (i < n && s[i] == ' ') {
            i++;
        }

        // 2. Check sign
        int sign = 1;

        if (i < n && s[i] == '-') {
            sign = -1;
            i++;
        } 
        else if (i < n && s[i] == '+') {
            i++;
        }

        // 3. Convert digits
        long long result = 0;

        while (i < n && s[i] >= '0' && s[i] <= '9') {
            int digit = s[i] - '0';

            result = result * 10 + digit;

            // 4. Handle overflow
            if (sign == 1 && result > INT_MAX) {
                return INT_MAX;
            }

            if (sign == -1 && -result < INT_MIN) {
                return INT_MIN;
            }

            i++;
        }

        return sign * result;
    }
};