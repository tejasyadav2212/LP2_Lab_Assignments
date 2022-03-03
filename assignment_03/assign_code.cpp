// assignment 03  
// greedy algorithm for selection sort...

#include <iostream>
using namespace std;

// to swap
void swap(int *a, int *b){
    int temp = *a;
    *a=*b;
    *b=temp;
}

// to print array
void printArray(int array[], int size){
    for(int i=0; i<size; i++){
        cout<<array[i]<<" ";
    }
    cout<<endl;
}

// selection sort 
void selectionSort(int array[], int size){
    for(int i=0; i<size-1; i++){
        int min = i;
        for(int j=i; j<size; j++){
            if(array[j]<array[min]){
                min = j;
            }

            swap(&array[min], &array[i]);
        }
    }
}

int main(){
    int data[] = {20,12,10,15,2};
    int size = sizeof(data)/sizeof(data[0]);  // to get length
    selectionSort(data, size);
    cout<<"Sorted array is: ";
    printArray(data, size);
}

