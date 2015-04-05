/*
 * MeanCalculator.cpp
 *
 *  Created on: Apr 5, 2015
 *      Author: manuel
 */

#include "MeanCalculator.h"

void MeanCalculator::AddValue(double newValue)
{
	this->values.push_back(newValue);
}

double MeanCalculator::GetMean()
{
	if (this->values.size() == 0)
		return 0;

	double sum = 0;
	for (unsigned int i = 0; i < this->values.size(); i++)
	{
		sum += this->values[i];
	}
	return sum / this->values.size();
}

int MeanCalculator::GetCount()
{
	return this->values.size();
}

void MeanCalculator::Reset()
{
	this->values.clear();
}


