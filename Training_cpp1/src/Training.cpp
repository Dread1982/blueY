//============================================================================
// Name        : Training.cpp
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
	m.AddValue(4);
	m.AddValue(5);
	m.AddValue(6);

	cout << "count:" << m.GetCount() << endl;
	cout << "mean:" << m.GetMean() << endl;

	return 0;
}
