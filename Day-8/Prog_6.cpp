#include<iostream>
using namespace std;

class A{
    public:
    virtual void Greet(){
        cout<<"Hello A";
    }
};

class B:public A{
    public:
    void Greet(){
        cout<<"Hello B";
    }
};

int main(){
    A *obj;
    B obj2;
    obj = &obj2;

    obj->Greet();
}