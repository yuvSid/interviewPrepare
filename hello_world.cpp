#include <iostream>
#include <vector>
#include <string>

using namespace std;

void reverseString(string &toReverse)
{
    size_t i, j;
    char tmp;
    for (i = 0, j=toReverse.length()-1; i < j; ++i, --j) {
        tmp = toReverse[i];
        toReverse[i] = toReverse[j];
        toReverse[j] = tmp;  
    }
}

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
    string msgToReverse;

    for (const string& word : msg)
    {
        msgToReverse += word + " ";
    }
    cout << msgToReverse << endl;
    reverseString(msgToReverse);
    cout << msgToReverse << endl;
}