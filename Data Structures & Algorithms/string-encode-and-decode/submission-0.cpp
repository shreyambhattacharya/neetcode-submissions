class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for (string str : strs) {
            encoded += str + '~';
        }

        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> decoded;

        string curr = "";
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != '~') curr += s[i];
            else {
                decoded.push_back(curr);
                curr = "";
            }
        }

        return decoded;
    }
};
