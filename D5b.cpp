#include<bits/stdc++.h>
using namespace std;
const double g = 9.8;

int main(){
    double h;
    cout<<"Masukkan ketinggian benda (m) : ";
    cin>>h;
    cout<<"Benda akan menyentuh tanah setelah "<<sqrt(2*h/g)<<" detik";
}