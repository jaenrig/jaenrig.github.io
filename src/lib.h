
class library
{
    private:
        bool att_flag;
        int  att_num;
        int*  att_ptr;
        
    public:
        library();
        ~library();
        void functionA();
        void functionB(int arg);
        int  functionC(int& arg);
};