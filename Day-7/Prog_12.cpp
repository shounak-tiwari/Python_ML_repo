#include<iostream>
using namespace std;

class Demo{
    public:
    void demomethod(){
        cout<<"Hello Main parent ";
    }
};
class DemoChild1:public Demo{
    public:
    void DemochildFun1(){
        cout<<"Hello Demochhild -1 ";
    }
};

class DemoChild2:public Demo{
    public:
    void DemochildFun2(){
        cout<<"Hello Demochhild - 2 ";
    }
};

class singlechidl :public DemoChild1,DemoChild2{
    public:
    void childfun(){
        cout<<"Hey CDGI";
    }
};
int main(){
    singlechidl s1;
    s1.DemoChild1::demomethod();   
    s1.DemoChild2::demomethod();   
}