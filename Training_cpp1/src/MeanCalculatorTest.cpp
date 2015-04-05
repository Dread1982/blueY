/*
 * MeanCalculatorTest.cpp
 *
 *  Created on: Apr 5, 2015
 *      Author: manuel
 */

#include "MeanCalculatorTest.h"


void MeanCalculatorTest::TestResult(bool result, string testname)
{
	string stringResult = result ? "successful" : "failed";

	cout << "Test \""<< testname << "\" " << stringResult << "!" << endl;
}

void MeanCalculatorTest::TestGetCount()
{
	MeanCalculator *meanCalculator = new MeanCalculator();

	bool result0 = meanCalculator->GetCount() == 0;

	meanCalculator->AddValue(3);

	bool result1 = meanCalculator->GetCount() == 1;

	this->TestResult(result0 && result1, "TestGetCount");
}

void MeanCalculatorTest::TestGetReset()
{
	MeanCalculator *meanCalculator = new MeanCalculator();

	meanCalculator->AddValue(3);
	meanCalculator->AddValue(4);

	bool result0 = meanCalculator->GetCount() == 2;

	meanCalculator->Reset();

	bool result1 = meanCalculator->GetCount() == 0;

	this->TestResult(result0 && result1, "TestGetReset");
}

void MeanCalculatorTest::TestAddValue()
{
	MeanCalculator *meanCalculator = new MeanCalculator();

	bool result0 = meanCalculator->GetCount() == 0;

	meanCalculator->AddValue(3);

	bool result1 = meanCalculator->GetCount() == 1;

	meanCalculator->AddValue(4);

	bool result2 = meanCalculator->GetCount() == 2;

	this->TestResult(result0 && result1 && result2, "TestAddValue");
}

void MeanCalculatorTest::TestGetMean()
{
	MeanCalculator *meanCalculator = new MeanCalculator();

	bool result0 = meanCalculator->GetMean() == 0;

	meanCalculator->AddValue(3);

	bool result1 = meanCalculator->GetMean() == 3;

	meanCalculator->AddValue(5);

	bool result2 = meanCalculator->GetMean() == 4;

	meanCalculator->AddValue(2);

	bool result3 = meanCalculator->GetMean() == 3;

	this->TestResult(result0 && result1 && result2 && result3, "TestGetMean");
}
