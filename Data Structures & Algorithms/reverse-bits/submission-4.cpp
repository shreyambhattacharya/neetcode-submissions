class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t num = 0;
        for (int i = 0; i < 32; i++) {
            num <<= 1u;
            num |= (n & 1u);
            n >>= 1u;
        }

        return num;
    }
};
