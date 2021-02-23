#include <stdio.h>
#include <math.h>
#include <stdbool.h>

#define max(a,b) ((a)>(b)?(a):(b))

int maxSatisfied(const int* customers, int customersSize, const int* grumpy, int grumpySize, int X){
    // 计算原来应用的顾客数量
    int originCustomers = 0;
    for (int i = 0; i < grumpySize; i++) {
        if (grumpy[i] == 0) {
            originCustomers += customers[i];
        }
    }
    printf("originCustomers is %d\n", originCustomers);

    // 计算[0, k)区间可以挽留顾客数量
    int grumpyCustomers = 0;
    for (int i = 0; i < X; i++) {
        if (grumpy[i] == 1) {
            grumpyCustomers += customers[i];
        }
    }
    printf("grumpyCustomers is %d\n", grumpyCustomers);

    // 滑动窗口计算最大的
    int res = grumpyCustomers;
    int left = 0;
    int right = X;
    while (right < customersSize) {
        if (grumpy[left] == 1) {
            grumpyCustomers -= customers[left];
        }
        if (grumpy[right] == 1) {
            grumpyCustomers += customers[right];
        }
        left++;
        right++;
        res = max(res, grumpyCustomers);
    }

    return res + originCustomers;
}

int main(void) {
    int customer[] = {1, 0, 1, 2, 1, 1, 7, 5};
    int customerSize = sizeof(customer) / sizeof(customer[0]);
    int grumpy[] = {0, 1, 0, 1, 0, 1, 0, 1};
    int grumpySize = sizeof(grumpy) / sizeof(grumpy[0]);
    int X = 3;
    int res;
    res = maxSatisfied(customer, customerSize, grumpy, grumpySize, X);
    printf("Max customer number is %d", res);
}