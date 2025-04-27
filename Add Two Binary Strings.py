class Solution:
    def addBinary(self, s1, s2):
        # Dono strings ke last se start karenge
        i = len(s1) - 1
        j = len(s2) - 1
        carry = 0
        result = []

        # Jab tak dono strings ya carry mein kuch hai, tab tak loop chalega
        while i >= 0 or j >= 0 or carry:
            # Agar index valid hai toh digit lo, warna 0 lo
            bit1 = int(s1[i]) if i >= 0 else 0
            bit2 = int(s2[j]) if j >= 0 else 0

            # Dono bits aur carry ka sum nikalo
            total = bit1 + bit2 + carry

            # Naya carry calculate karo
            carry = total // 2

            # Current bit ko result mein add karo
            result.append(str(total % 2))

            # Index ek step piche le jao
            i -= 1
            j -= 1

        # Ab tak humne result reverse order mein banaya hai, toh usko sahi order mein reverse karenge
        result = ''.join(result[::-1])

        # Leading zeros hata do, aur agar pura result empty ho gaya toh "0" return karo
        return result.lstrip('0') or '0'
    

# Example driver code (for running and checking)
if __name__ == "__main__":
    s1 = input("Enter first binary string: ").strip()
    s2 = input("Enter second binary string: ").strip()

    ob = Solution()
    print("Sum of Binary Strings:", ob.addBinary(s1, s2))