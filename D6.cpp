#include<bits/stdc++.h>
using namespace std;
const double g = 9.8;
//v = velocity, h = high, x = position(x), P = Plane, T = Target

double hP, vP, xPi, xPf, xT, t, dist, jarak;

int main(){
	cout<<"Masukkan Ketinggian Pesawat (m): ";
	cin>>hP;
	cout<<"Masukkan Kecepatan Pesawat (m/s): ";
	cin>>vP;
	cout<<"Masukkan Posisi x Pesawat (m): ";
	cin>>xPi;
	cout<<"Masukkan Posisi x Target (m): ";
	cin>>xT;
	
	t = sqrt(2*hP/g);
	dist = vP*t;
	xPf = xT-dist;
	jarak = xPf - xPi;

	//case: ketika paket tidak mungkin mengenai target
	if(jarak<0){
		cout<<"Ets, ga kena";
	}
	
	//case: ketika pesawat langsung menjatuhkan paket
	else if(jarak==0){
		cout<<"Paket bisa langsung dijatuhkan";
	}
	
	//normal case
	else{
		cout<<"Paket harus dijatuhkan saat pesawat berada di posisi "<<jarak<<" meter.";
	}
}