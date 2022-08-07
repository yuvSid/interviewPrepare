#include <iostream>
#include <vector>
#include <string>

#include "solutions/reverse_string.cpp"

int main()
{
    std::vector<std::string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
    std::string result;

    for (const std::string& word : msg)
    {
        result += word + " ";
    }
    std::cout << result << std::endl;
    reverseStringCustom(result);
    std::cout << result << std::endl;
}