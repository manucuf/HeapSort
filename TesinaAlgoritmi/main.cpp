//
//  main.cpp
//  TesinaAlgoritmi
//
//  Created by Emanuele Cufino on 27/02/2020.
//  Copyright © 2020 Emanuele Cufino. All rights reserved.
//

#include <iostream>
#include <vector>

#include "Heap.h"
#include "TimeManager.h"

using namespace std;
using namespace chrono;

const int DefaultRunNumber = 1;
const int DefaultIterations = 2;
const int DefaultArrayMaxValue = 1000;
const string DefaultFileName = "./results";

const int DefaultIncrement = 50;

enum {
    PathIndex,
    RunIndex,
    IterationsIndex,
    MaxValueIndex,
    FileNameIndex,
    ArgCount
};


int main(int argc, const char * argv[]) {
    
    // Getting arguments
    const int runNumber = (argv[RunIndex] && argc == ArgCount) ? atoi(argv[RunIndex]) : DefaultRunNumber;
    const int repetitions = (argv[IterationsIndex] && argc == ArgCount) ? atoi(argv[IterationsIndex]) : DefaultIterations;
    const int maxArrayValue = (argv[MaxValueIndex] && argc == ArgCount) ? atoi(argv[MaxValueIndex]) : DefaultArrayMaxValue;
    const string fileName = (argv[FileNameIndex] && argc == ArgCount) ? argv[FileNameIndex] : DefaultFileName;
    
    // Size and sizeIncrement declarations
    int size = 10;
    int sizeIncrement = 100;
    
    TimeManager timeManager = TimeManager();
    
    // Declare vector A
    vector<int> A;
    
    // Declare vector of sizes to store
    vector<int> sizes;
    
    
    // MARK: Build Max Heap
    cout << "--\nHeapSort" << endl;

    // Open file to store results
    timeManager.openFile(fileName + "BuildMaxHeap" + to_string(runNumber) + ".csv");
    
    // Iterate <repetitions> times
    for (int i = 0; i < repetitions; i++) {
            
        // Increment size for each iteration
        size += sizeIncrement;
        sizes.push_back(size);
        
        cout << "Iteration " << i+1 << ", Size: " << size << endl;
        
        // Initialize srand from current time
        srand((unsigned)time(NULL));
        
        // Clear vector
        A.clear();

        // Populate vector with random values
        for (int i = 0; i < size; i++) {
            A.push_back(rand() % maxArrayValue);
        }

        // Uncomment to test with example sequence
    //    A.push_back(4);
    //    A.push_back(1);
    //    A.push_back(3);
    //    A.push_back(2);
    //    A.push_back(16);
    //    A.push_back(9);
    //    A.push_back(10);
    //    A.push_back(14);
    //    A.push_back(8);
    //    A.push_back(7);
        
        // Set start time in milliseconds
        timeManager.setStartTime();

        // Build Max Heap
        Heap heap = Heap();
//        Heap::buildMaxHeap<int>(A);
        heap.heapSort(A);
        
        // Calculate final time
        timeManager.setEndTime();
        timeManager.calculateElapsedTime();
                
        sizeIncrement += DefaultIncrement;
    }
    
    timeManager.storeOnFile(repetitions, sizes);
    timeManager.closeFile();
    
    
    // MARK: Insertion Sort
    
    cout << "\n--\nInsertion Sort" << endl;
    
    timeManager.openFile(fileName + "InsertionSort" + to_string(runNumber) + ".csv");

    for (int i = 0; i < repetitions; i++) {
        
        cout << "Iteration " << i+1 << ", Size: " << sizes[i] << endl;
        
        // Initialize srand from current time
        srand((unsigned)time(NULL));

        // Clear vector
        A.clear();

        // Populate vector with random values
        for (int j = 0; j < sizes[i]; j++) {
            A.push_back(rand() % maxArrayValue);
        }
        
        // Set start time
        timeManager.setStartTime();

        // Build Max Heap
        insertionSort<int>(A);

        // Calculate final time
        timeManager.setEndTime();
        timeManager.calculateElapsedTime();
        
    }
    
//    printVector(timeManager.elapsedTime);
    
    // Store on file
    timeManager.storeOnFile(repetitions, sizes);
    
    timeManager.closeFile();

    return 0;
}
