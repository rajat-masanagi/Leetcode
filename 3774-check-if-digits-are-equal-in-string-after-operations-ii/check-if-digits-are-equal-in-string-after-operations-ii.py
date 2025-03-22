class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return False  # According to problem constraints, input is valid, but handle edge case
        if n == 2:
            return s[0] == s[1]
        m = n - 2
        digits = [int(c) for c in s]
        
        # Compute mod 2 sums using subset generation
        set_bits = []
        temp = m
        bit_pos = 0
        while temp > 0:
            if temp & 1:
                set_bits.append(bit_pos)
            temp >>= 1
            bit_pos += 1
        sum_left_mod2 = 0
        sum_right_mod2 = 0
        num_bits = len(set_bits)
        for mask in range(1 << num_bits):
            i = 0
            for j in range(num_bits):
                if mask & (1 << j):
                    i += (1 << set_bits[j])
            if i > m:
                continue
            sum_left_mod2 = (sum_left_mod2 + digits[i]) % 2
            sum_right_mod2 = (sum_right_mod2 + digits[i + 1]) % 2
        
        # Compute mod 5 sums using Lucas's theorem
        comb_table = [
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 2, 1, 0, 0],
            [1, 3, 3, 1, 0],
            [1, 4, 1, 4, 1],
        ]
        sum_left_mod5 = 0
        sum_right_mod5 = 0
        for i in range(m + 1):
            res = 1
            mm, ii = m, i
            valid = True
            while mm > 0 or ii > 0:
                m_digit = mm % 5
                i_digit = ii % 5
                if i_digit > m_digit:
                    valid = False
                    break
                res = (res * comb_table[m_digit][i_digit]) % 5
                mm //= 5
                ii //= 5
            if not valid:
                res = 0
            sum_left_mod5 = (sum_left_mod5 + res * digits[i]) % 5
            sum_right_mod5 = (sum_right_mod5 + res * digits[i + 1]) % 5
        
        return (sum_left_mod2 == sum_right_mod2) and (sum_left_mod5 == sum_right_mod5)

