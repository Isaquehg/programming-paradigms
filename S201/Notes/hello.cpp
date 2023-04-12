#include <iostream>
#include "somefile.h"

extern int a;
int x = -1;

int main(){
    std::cout << a << std::endl;

    int x = 10;
    std::cout << ::x << std::endl;
    std::cout << x << std::endl;

    return 0;
}