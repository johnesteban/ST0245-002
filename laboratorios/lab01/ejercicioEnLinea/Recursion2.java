
class Recursion2{
public boolean groupSum6(int start, int[] nums, int target) {
  if(start>=nums.length){
    if (target==0){
      return true;
    }
    else{
      return false;
    }
  }
  if(nums[start]==6){
    return groupSum6(start+1,nums,target-nums[start]);
  } 
  else{
    return (groupSum6(start+1,nums,target) || groupSum6(start+1,nums,target-nums[start])) ;
  }
}

public boolean groupNoAdj(int start, int[] nums, int target) {
  if(start>=nums.length){
    if (target==0){
      return true;
    }
    else{
      return false;
    }
  }
    return (groupNoAdj(start+1,nums,target) || groupNoAdj(start+2,nums,target-nums[start])) ;
}

public boolean groupSum5(int start, int[] nums, int target) {
  if(start>=nums.length){
    if (target==0){
      return true;
    }
    else{
      return false;
    }
  }
  if(nums[start]==1 && start>0 && nums[start-1]%5==0){
      return groupSum5(start+1,nums,target);
    }
    else if(nums[start]%5==0){
    return groupSum5(start+1,nums,target-nums[start]);
    }
  else{
    return (groupSum5(start+1,nums,target) || groupSum5(start+1,nums,target-nums[start])) ;
  }
}

public boolean splitArray(int[] nums) {
  return auxiliar(0,0,0,nums);
}
public boolean auxiliar(int i, int a, int b, int[] nums){
  if(i>=nums.length){
    return a==b;
  }
  else{
    return auxiliar(i+1, a+nums[i],b,nums) || auxiliar(i+1,a,b+nums[i],nums);
  }
}

public boolean splitOdd10(int[] nums) {
  return auxiliar1(0,0,0,nums);
}
public boolean auxiliar1(int i, int a, int b, int[] nums){
  if(i>=nums.length){
    return ((a%10==0 && b%2==1) ||(b%10==0 && a%2==1));
  }
  else{
    return auxiliar1(i+1, a+nums[i],b,nums) || auxiliar(i+1,a,b+nums[i],nums);
  }
}
}