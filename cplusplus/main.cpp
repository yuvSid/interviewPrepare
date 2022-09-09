#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cassert>

#include <boost/json/src.hpp>

#include "solutions/town_judge.cpp"

int main()
{
    std::vector<boost::json::value> in;

    std::ifstream f("./../OUTPUT/IN");
    assert(f.is_open());
    for (std::string line; std::getline(f, line);) {
        std::error_code ec;
        auto jv = boost::json::parse(line, ec);
        if( ec )
            std::cout << "Parsing failed: " << ec.message() << "\n";
        else
            in.push_back(jv);
    }

    // findJudge(int n, std::vector<std::vector<int>>& trust) {
    const int n_args = 2;
    int curr_arg = 0;
    std::vector<boost::json::value> vals(n_args);
    for (auto& el:in) {
        vals[curr_arg] = el;
        curr_arg++;
        if (curr_arg != n_args)
            continue;
        
        curr_arg = 0;
        Solution exec;
        auto val2 = boost::json::value_to<std::vector<std::vector<int>>>(vals[1]);
        auto res = exec.findJudge(boost::json::value_to<int>(vals[0]), 
                                  val2);
        std::cout << boost::json::value_from(res) << std::endl;
    }
}
