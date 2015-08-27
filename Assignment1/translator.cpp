/*
Name : Adhish Singla
Roll Number : 201403004
Translator Code to convert IA-32 assembly code to IA-64 Assembly Code
*/

#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream ip(argv[1]);
    ofstream op(argv[2]);
    string line;

    if(ip.is_open()){
        while(getline(ip, line)){
            if(line.find(" dd") != std::string::npos){
                line.replace(line.find(" dd"),3, " dq");
            }
            if(line.find("eax") != std::string::npos){
                line.replace(line.find("eax"),3, "rax");
            }
            if(line.find("edi") != std::string::npos){
                line.replace(line.find("edi"),3, "rdi");
            }
            if(line.find("esi") != std::string::npos){
                line.replace(line.find("esi"),3, "rsi");
            }
            if(line.find("edx") != std::string::npos){
                line.replace(line.find("edx"),3, "rdx");
            }
            op << line;
            op << "\n";
        }
        ip.close();
        op.close();
    }else{
        cout << "Unable to open file";
    }
    return 0;
}
