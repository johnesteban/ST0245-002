class Array3{
    //---MAXSPAN---
    public int maxSpan(int[] nums) {
  int temporal=0;
  int max=0;
  for(int i=0;i<nums.length;i++){
    for(int j=0;j<nums.length;j++){
      if(nums[i]==nums[j]){
        temporal=j-i+1;
        max=Math.max(temporal,max);
        
      }
    }
  }
  return max;
}

//--FIX34--
public int[] fix34(int[] nums) {
  for(int i=0;i<nums.length;i++){
  for(int j=0;j<nums.length;j++){
    if (nums[i]==4 && nums[j]==3){
      int temporal=nums[j+1];
      nums[j+1]=nums[i];
      nums[i]=temporal;
      }
  }
}
return nums;
}

//--FIX45--
public int[] fix45(int[] nums) {
  for(int i=0;i<nums.length;i++){
  for(int j=0;j<nums.length;j++){
    if (nums[i]==5 && nums[j]==4){
      int temporal=nums[j+1];
      nums[j+1]=nums[i];
      nums[i]=temporal;
      }
  }
}
return nums;
}

//--CANBALANCE--
public boolean canBalance(int[] nums) {
  int suma1=0;
  int suma2=0;
  
  for(int i=0;i<nums.length-1;i++)
    suma1=suma1+nums[i];
    suma2=nums[nums.length-1];
    
    for(int i=nums.length-2;i>0;i--){
      if(suma1==suma2){
        return true;
      }
      else{
        suma1=suma1-nums[i];
        suma2=suma2+nums[i];
      }
    }
  return suma1==suma2;
}

//--LINEARIN--
public boolean linearIn(int[] outer, int[] inner) {
  int contador=0;
  for(int i=0;i<inner.length;i++){
    for(int j=0;j<outer.length;j++){
      if (inner[i]==outer[j]){
        contador++;
        break;
      }
    }
  }
  if (contador==inner.length){
    return true;
  }
  return false;
}

}