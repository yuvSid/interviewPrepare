#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cassert>

#include <boost/json/src.hpp>

#include "solutions/reverse_string.cpp"

int main()
{
    std::vector<boost::json::value> in;

    std::ifstream f("./../OUTPUT/IN");
    assert(f.is_open());
    for (std::string line; std::getline(f, line);)
    {
        error_code ec;
        auto jv = boost::json::parse(line, ec);
        if( ec )
            std::cout << "Parsing failed: " << ec.message() << "\n";
        else
            in.push_back(jv);
    }
    for (auto& el:in)
        std::cout << el.as_string() << std::endl;
}
