
class Array2{
//"---COUNT EVENS---"
public int countEvens(int[] nums) {
  int j=0;
  for(int i=0;i<nums.length;i++){
    if(nums[i]%2==0){
      j++;
    }
  }
  return j;
}

//"---FIZZ ARRAY---"
public int[] fizzArray(int n) {
  int nums[]=new int[n];
  for(int i=0;i<n;i++){
    nums[i]=i;
  }
  return nums;
}

//"---LUCKY 13---"
public boolean lucky13(int[] nums) {
  for(int i=0;i<nums.length;i++){
    if(nums[i]==1 || nums[i]==3){
      return false;
    }
  }
  return true;
}

//---SUM28---"
public boolean sum28(int[] nums) {
  int suma=0;
  for(int i=0;i<nums.length;i++){
    if(nums[i]==2){
      suma=suma+nums[i];
    }
  }
  if(suma==8){
    return true;
  }
  return false;
}

//---BIGDIFF---
public int bigDiff(int[] nums) {
  int mayor=nums[0];
  int menor=nums[0];
  for(int x=1;x<nums.length;x++){
    if(nums[x]>mayor){
      mayor=nums[x];
    }
    if(nums[x]<menor){
      menor=nums[x];
    }
  }
 
  return mayor-menor;
}

//--ISEVERYWHERE--
public boolean isEverywhere(int[] nums, int val) {
  boolean ans=true;
  for(int i=1;i<nums.length;i++){
    if(nums[i-1]!=val && nums[i]!=val){
      ans=false;
      break;
    }
  }
  return ans;
}

//--TRIPLEUP--
public boolean tripleUp(int[] nums) {
  for(int i=0;i<nums.length-2;i++){
    if(nums[i]==nums[i] && nums[i+1]==nums[i]+1 && nums[i+2]==nums[i]+2){
      return true;
    }
  }
  return false;
}
}

