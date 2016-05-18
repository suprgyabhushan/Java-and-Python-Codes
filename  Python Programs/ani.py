#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int Row(char *file)
	{
	FILE *data=fopen(file,"r");
	int value;	
	int x=getc(data),row=0;
    	while(x!=EOF)
	    	{
        	x=getc(data);
		if(x==10)
        	    	{
			row=row+1;
			}
    		}
	return row;
	fclose(data);
	}
int Col(char *file)
	{
	FILE *data=fopen(file,"r");
        int x=getc(data),col=0;
	while(x!='\n')
	    	{
        	x=getc(data);		
		col=col+1;	
            	}
	return col;
	fclose(data);
	}
int main(int argc,char *argv[])
	{
	FILE *file=fopen(argv[1],"r");
	FILE *file1=fopen(argv[2],"r");
	int rows,columns;
	char a;
	int i,j;
	rows=Row(file);
	columns=Col(file);
	char **array;
	array=(char**)malloc(sizeof(char*)*rows)
	for(i=0;i<rows;i++)
		{
		array[i]=(char*)malloc(sizeof(char)*columns);
		}
	for(i=0;i<rows;i++)
		{
		for(j=0;j<columns;j++)
			{
			fscanf(in,"%c\n",&a);
			array[i][j]=a;
			printf("%c",array[i][j]);
			}
		printf("\n");
		}
	}
	fclose(in);
	return 0;
