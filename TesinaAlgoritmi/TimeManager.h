//
//  DateTime.h
//  TesinaAlgoritmi
//
//  Created by Emanuele Cufino on 01/03/2020.
//  Copyright © 2020 Emanuele Cufino. All rights reserved.
//

#ifndef TimeManager_h
#define TimeManager_h

#include <vector>
#include <chrono>
#include <fstream>
#include <iostream>

using namespace std;
using namespace chrono;

//! TimeManager is an helper class which manages time intervals

class TimeManager {
    
private:
    
    high_resolution_clock::time_point startTime;
    high_resolution_clock::time_point endTime;
    
    string fileName;
    ofstream fileOutput;

public:
    vector<double> elapsedTime;

    void setStartTime();
    void setEndTime();
    long int getTimeinMilliseconds();
    void calculateElapsedTime();
    
    void openFile(string fileName);
    void closeFile();
    
    /** Stores elapsed time on csv file, where each elapsedTime element matches to relative size
     @param repetition number of elements to store on csv file
     @param sizes array where each element is a size for each repetition
    **/
    void storeOnFile(int repetition, vector<int> sizes);
    
};


#endif /* TimeManager_h */
