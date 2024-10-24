#include<bits/stdc++.h>
using namespace std;
const long long R = 6371000;

double solve(double x1, double y1, double z1, double x2, double y2, double z2){
    x1 = x1*(M_PI/180.0);
    y1 = y1*(M_PI/180.0);
    z1 = z1*(M_PI/180.0);
    x2 = x2*(M_PI/180.0);
    y2 = y2*(M_PI/180.0);
    z2 = z2*(M_PI/180.0);

    double dx = x2-x1;
    double dy = y2-y1;

    double hav = pow(sin(dx/2),2) + cos(x1)*cos(x2)*pow(sin(dy/2),2);
    double teta_rad = 2*asin(sqrt(hav));
    return teta_rad*R;
}

int main(){
    double x1, y1, z1;
    double x2, y2, z2;
    cout<<"Masukkan Titik Pertama :"<<endl;
    cout<<"Latitude (m) : ";
    cin>>x1;
    cout<<"Longitude (m) : ";
    cin>>y1;
    cout<<"Altitude (m) : ";
    cin>>z1;
    cout<<endl;
    cout<<"Masukkan Titik Kedua :"<<endl;
    cout<<"Latitude (m) : ";
    cin>>x2;
    cout<<"Longitude (m) : ";
    cin>>y2;
    cout<<"Altitude (m) : ";
    cin>>z2;
    cout<<"Jaraknya adalah : "<<solve(x1, y1, z1, x2, y2, z2)<<" meter";
}