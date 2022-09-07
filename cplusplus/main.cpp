#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cassert>

#include <boost/json/src.hpp>

#include "solutions/water_flow.cpp"

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
    for (auto& el:in) {
        auto input = boost::json::value_to<std::vector<std::vector<int>>>(el);
        Solution exec;
        auto res = exec.pacificAtlantic(input);
        std::cout << boost::json::value_from(res) << std::endl;
    }
}
