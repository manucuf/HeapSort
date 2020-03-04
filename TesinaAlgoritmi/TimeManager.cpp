//
//  TimeManager.cpp
//  TesinaAlgoritmi
//
//  Created by Emanuele Cufino on 01/03/2020.
//  Copyright © 2020 Emanuele Cufino. All rights reserved.
//

#include "TimeManager.h"

void TimeManager::setStartTime() {
    this->startTime = high_resolution_clock::now();
}

void TimeManager::setEndTime() {
    this->endTime = high_resolution_clock::now();
}

long int TimeManager::getTimeinMilliseconds() {
    auto nowInMilliseconds = chrono::time_point_cast<chrono::milliseconds>(startTime);
    auto epoch = nowInMilliseconds.time_since_epoch();
    auto value = chrono::duration_cast<chrono::milliseconds>(epoch);
    long int millisecondsAtStart = value.count();
    return millisecondsAtStart;
}

void TimeManager::calculateElapsedTime() {
    duration<double> elapsedTime = duration_cast<duration<double>>(endTime - startTime);
    cout << "\tElapsed time: " << elapsedTime.count() << endl;
    this->elapsedTime.push_back(elapsedTime.count());
}

void TimeManager::openFile(string fileName) {
    this->fileName = fileName;
    this->elapsedTime.clear();
    fileOutput.open(fileName, ios_base::app);
}

void TimeManager::closeFile() {
    fileOutput.close();
}


void TimeManager::storeOnFile(int repetitions, vector<int> sizes) {
    
    for (int runIndex = 0; runIndex < repetitions; runIndex++) {
        if (runIndex == 0) {
            fileOutput << "Iteration,Time,Size" << endl;
        }
        fileOutput << runIndex+1 << "," << elapsedTime[runIndex] << "," << sizes[runIndex] << endl;
    }

    
}
