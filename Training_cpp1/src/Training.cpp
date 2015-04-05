//============================================================================
// Name        : Training.cpp
// Author      : Manuel
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "MeanCalculatorTest.h"
using namespace std;

int main() {

	MeanCalculatorTest test;

	test.TestAddValue();
	test.TestGetCount();
	test.TestGetReset();
	test.TestGetMean();

	return 0;
}
