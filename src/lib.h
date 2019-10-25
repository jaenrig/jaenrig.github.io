
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
        static void functionD(){};
        int functionE();
};

class something
{
    private:
        bool flag;
        int  number;
        int  another_number;

    public:
        something() {};
        something(bool flag, int number, int another_number) : flag(flag), number(number), another_number(another_number) {};
        void product(){ library::functionD(); return (number*another_number); };
};

class child: public library
{
    protected:
        something objS;
    
    public:
        child(){};
};