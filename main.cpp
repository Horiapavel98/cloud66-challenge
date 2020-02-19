#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {

    // Assume input is a single line for now.
    
    cout << "Input text now:" << endl;
    string text;
    getline(cin, text);

    cout << "Input subtext now:" << endl;
    string subtext;
    getline(cin, subtext);

    transform(text.begin(), text.end(), text.begin(),
    [](unsigned char c){ return std::tolower(c); });
    
    transform(subtext.begin(), subtext.end(), subtext.begin(),
    [](unsigned char c){ return std::tolower(c); });

    cout << text << endl << subtext;

    // Linear search.

    return 0;
}