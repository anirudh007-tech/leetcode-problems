bool isPalindrome(int x) {
    int a=x;
    if(a<0)
    {
        return false;
       
    }
    int z=a;
    long rev=0;
    int i;
    while(z!=0)
    {
        i=z%10;
        rev=rev*10+i;
        z=z/10;
    }
    if(x==rev)
    {
        return true;
    
    }
    else
    {
        return false;
    }

    
}