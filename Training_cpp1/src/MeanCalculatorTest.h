/*
 * MeanCalculatorTest.h
 *
 *  Created on: Apr 5, 2015
 *      Author: manuel
 */

#ifndef MEANCALCULATORTEST_H_
#define MEANCALCULATORTEST_H_

#include <iostream>
#include "MeanCalculator.h"
using namespace std;

class MeanCalculatorTest
{
public:
	void TestResult(bool result, string testname);
	void TestAddValue();
	void TestGetCount();
	void TestGetReset();
	void TestGetMean();
};

#endif /* MEANCALCULATORTEST_H_ */
