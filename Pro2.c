#include<stdio.h>
int main()
{
int num,n,k,i,j=0,s[10],sum=0,temp=1;
scanf("%d",&n);
scanf("%d",&num);
while(n!=0)
{
k=n%10;
n=n/10;
s[j]=k;
j++;
sum++;
}
for(i=sum-1;i>=0;i--,temp++)
{
	if(temp!=num)
	{
	printf("%d",s[i]);
}
}
return 0;
}
