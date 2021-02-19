#include <stdio.h>
#include <math.h>


int findMaxNumberOfOne(const int *A, int ASize, int K) {
    int left = 0, right = 0;
    int zeros = 0;
    int res = 0;
    while (right < ASize) {
        if ( A[right] == 0 ) {
            zeros++;
        }
        if ( zeros > K ){
            if ( A[left] == 0 ) {
                zeros--;
            }
            left++;
        }

        res = (int) fmax(res, right - left + 1);
        right++;
    }
    return res;
}

int main(void) {
    int A[] = {0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1};
    int K = 3;
    int ASize = sizeof(A)/sizeof(A[0]);
    int max_num;
    max_num = findMaxNumberOfOne(A, ASize, K);
    printf("findMaxNumberOfOne is %d" , max_num);
    return 0;
}