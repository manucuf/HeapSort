//
//  Header.h
//  TesinaAlgoritmi
//
//  Created by Emanuele Cufino on 29/02/2020.
//  Copyright © 2020 Emanuele Cufino. All rights reserved.
//

#ifndef Heap_h
#define Heap_h

#include <vector>
#include <iostream>

using namespace std;


class Heap {

private:
    
    int heapSize;
    
    int parent(int i) {
        return (int) ((i-1)/2);
    }
    
    int left(int i) {
        return (2*i) + 1;
    }
        
    int right(int i) {
        return (2*i) + 2;
    }
        
    
    template <class T> void maxHeapify(vector<T> &A, int i) {
        
        int l = left(i);
        int r = right(i);
        int largest = i;
        
        if ((l < heapSize) && (A[l] > A[largest])) {
            largest = l;
        }
        
        if ((r < heapSize) && (A[r] > A[largest])) {
            largest = r;
        }
        
        if (largest != i) {
            swap(A[i], A[largest]);
            maxHeapify(A, largest);
        }
    }


    template <class T> void buildMaxHeap(vector<T> &A) {
        
        heapSize = (int)A.size();
        
        int length = ((int)A.size()/2) - 1;
        for (int i = length; i >= 0; i--) {
            maxHeapify(A, i);
        }
    }

public:
    
    template <class T> void heapSort(vector<T> &A) {
    
        buildMaxHeap(A);
        
        for (int i = (int)A.size()-1; i >= 1; i--) {
            swap(A[0], A[i]);
            heapSize--;
            maxHeapify(A, 0);
        }
    }

};


template <class T> void printVector(vector<T> A) {
    
    // Print array elements
    cout << "Array elements: " << endl;
    for (auto i : A) {
        cout << i << " ";
    }
    cout << endl;
    
    //    ITERATOR MODE
    //    vector<int>::iterator cursor;
    //    cursor = array.begin();
    //    for (cursor = array.begin(); cursor != array.end(); cursor++) {
    //
    //    }
    
}

template <class T> void insertionSort(vector<T> &A) {

    for (int j = 1; j < A.size(); j++) {
        
        T key = A[j];
        int i = j - 1;
        
        while (i >= 0 && A[i] > key) {
            A[i+1] = A[i];
            i--;
        }
        
        A[i+1] = key;
        
    }
    
}








#endif /* Heap_h */
