/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
        array = [...nums]
    nums.sort((a, b) => a - b);
    let i = 0;
    let j = nums.length - 1;
    while (i <= j){
        if (nums[i] + nums[j] == target){
            break;
        }
        else if(nums[i] + nums[j] > target){
            j--;
        }
        else if(nums[i] + nums[j] < target){
            i++;
        }
    }
    const res = []
    for (x = 0; x <= array.length; x++){
        if (nums[i] == array[x]) {
           res.push(x)
           continue
        }
        if (nums[j] == array[x]) {
           res.push(x)
        }
    }
    return res
};