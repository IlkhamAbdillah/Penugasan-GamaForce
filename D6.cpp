#include<bits/stdc++.h>
using namespace std;
const double g = 9.8;
//v = velocity, h = high, x = position(x), P = Plane, T = Target

double hP, vP, xP, xT, t, dist, tP;

double time(double h){
	return sqrt(2*h/g);
}

double distance(double t){
	return (vP*t);
}

int main(){
	cout<<"Masukkan Ketinggian Pesawat (m): ";
	cin>>hP;
	cout<<"Masukkan Kecepatan Pesawat (m/s): ";
	cin>>vP;
	cout<<"Masukkan Posisi x Pesawat (m): ";
	cin>>xP;
	cout<<"Masukkan Posisi x Target (m): ";
	cin>>xT;
	
	t = time(hP);
	dist = distance(t);
	//paket harus dijatuhkan saat posisi pesawat = (target - dist)
	//cout<<t<<" "<<dist;
	xP = xT-dist;
	tP = xP/vP;
	
	//case: ketika paket tidak mungkin mengenai target
	//target - dist = negatif
	if(xT-dist<0){
		cout<<"Ets, ga kena";
	}
	
	//case: ketika pesawat langsung menjatuhkan paket
	//target - dist = 0
	else if(xT-dist==0){
		cout<<"Paket bisa langsung dijatuhkan";
	}
	
	//normal case
	else{
		cout<<"Paket harus dijatuhkan saat pesawat berada di posisi "<<xP<<" , yaitu pada waktu "<<tP<<" detik";
	}
}