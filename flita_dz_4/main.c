#include<stdio.h>
int main()
{
    int n,i,j;
    printf("Enter a number: ");
    scanf("%d",&n);
    int a[n];

    for(i=2;i<=n;i++) // ������������� �������
    {
        a[i]=1;
    }

    for(i=2;i<=n;i++) // ���������� ��������� ����������
    {
        if(a[i])
        {
            for(j = i*i;j<=n;j+=i)
            {
                a[j]=0;
            }
        }
    }

    printf("Prime numbers are: ");
    for(i=2;i<=n;i++) // ����� ������� �����
    {
        if(a[i])
        {
            printf("%d ",i);
        }
    }

    return 0;
    }
