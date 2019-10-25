
#include <stdlib.h>
#include "lib.h"

library::library()
{
    this->att_flag = false;
    this->att_num  = 0;
    this->att_ptr  = NULL;
}

library::~library()
{}

void library::functionA()
{

}

void library::functionB(int arg)
{

}
int  library::functionC(int& arg)
{
    return 1;
}

int library::functionE(void)
{
    return 0;
}