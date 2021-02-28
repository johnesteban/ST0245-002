class Recursion1{
public int bunnyEars(int bunnies) {
  if (bunnies==0){
    return 0;
  }
  else{
     return bunnyEars(bunnies-1)+2;
  }
}
public int fibonacci(int n) {
  if(n==0){
    return 0;
  }
  else if(n==1){
    return 1;
  }
  else{
    return fibonacci(n-1)+fibonacci(n-2);
  }
}
public int bunnyEars2(int bunnies) {
  if(bunnies==0){
    return 0;
  }
  else if(bunnies%2==0){
    return 3+bunnyEars2(bunnies-1);
  }
  else{
    return 2+bunnyEars2(bunnies-1);
  }
}
public int triangle(int rows) {
  if(rows==0){
    return 0;
  }
  else{
    return triangle(rows-1)+rows;
  }
}
public int sumDigits(int n) {
  if(n==0){
    return 0;
  }
  else{
    return sumDigits(n/10)+(n%10);
  }
}
public int count7(int n) {
if(n==0){
    return 0;
  }
  else if(n%10==7){
    return 1+count7(n/10);
  }
  return count7(n/10);
}
public int powerN(int base, int n) {
  if(n==1){
    return base;
  }
  else{
    return powerN(base,n-1)*base;
  }
}

}
