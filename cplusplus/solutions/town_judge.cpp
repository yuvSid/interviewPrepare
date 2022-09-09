#include <vector>

// 997. Find the Town Judge -  Easy
//
// In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
// If the town judge exists, then:
//     The town judge trusts nobody.
//     Everybody (except for the town judge) trusts the town judge.
//     There is exactly one person that satisfies properties 1 and 2.
// You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
// Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



class Solution {
public:

    struct TrustedData {
        bool trusts = false;
        int trusted = 0;
    };

    int findJudge(int n, std::vector<std::vector<int>>& trust) {
        std::vector<TrustedData> res(n);
        for (auto& el: trust) {
            res[el[0]-1].trusts = true;
            res[el[1]-1].trusted += 1;
        }

        for (auto el = res.begin(); el != res.end(); el++) {
            if (!(el->trusts) && el->trusted == n-1)
                return std::distance(res.begin(), el) + 1;
        }


        return -1; 
    }
};