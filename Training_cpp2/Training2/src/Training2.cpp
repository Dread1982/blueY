//============================================================================
// Name        : Training2.cpp
// Author      : Manuel
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "MeanCalculator.h"
using namespace std;

int main() {
	MeanCalculator m;
	m.AddValue(4.3);
	m.AddValue(5.7);
	m.AddValue(6.1);

	cout << "count:" << m.GetCount() << endl;
	cout << "mean:" << m.GetMean() << endl;

	vector<double> v;
	v.push_back(2.0);
	v.push_back(3.0);
	v.push_back(4.3);

	cout << m.GetMean(v) << endl;

	list<double> l;
	l.push_back(3.0);
	l.push_back(3.0);
	l.push_back(4.3);
	cout << m.GetMean(l) << endl;

	return 0;
}
