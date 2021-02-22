#include <stdio.h>
#include <math.h>


int findShortestSubArray(int* nums, int numsSize){
    //哈希表，hash[n][0]为值n出现次数，hash[n][1]为值n在nums数组中首次出现位置
    unsigned short hash[65536][2] = {{0}};
    int res = 0;            //最短连续子数组长度
    int max_num_times = 0;  //在遍历中发现的nums数组中值的最大出现次数
    int tmp = 0;            //记录当前遍历到的nums[i]值，不要也无所谓

    for (int i = 0; i < numsSize; i++)
    {
        tmp = nums[i];
        hash[tmp][0]++;  //记录tmp值出现的次数
        if (hash[tmp][1] == 0)
        {
            hash[tmp][1] = i + 1;  //记录tmp值首次出现的位置,比实际下标大1,否则记录nums[0]有误
        }

        //更新条件:
        //1.当前遍历到的值出现次数大于max_num_times中记录的值
        //2.或者两者相等但是当前遍历到的值的子数组长度小于res记录的子数组长度
        if ((max_num_times < hash[tmp][0])
            || ((max_num_times == hash[tmp][0]) && (res > (i - hash[tmp][1] + 2))))
        {
            max_num_times = hash[tmp][0];   //更新同一值出现的最大次数
            res = i - hash[tmp][1] + 2;     //更新最短连续子数组长度
        }
    }

    return res;
}

int main(void) {
    int nums[] = {7,7,7, 8,8};
    int numsSize = sizeof(nums)/sizeof(nums[0]);
    int max_num;
    max_num = findShortestSubArray(nums, numsSize);
    printf("findMaxNumberOfOne is %d" , max_num);
    return 0;
}