import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int c1=sc.nextInt();
		int b1=sc.nextInt();
		int c2=sc.nextInt();
		int b2=sc.nextInt();
		int c3=sc.nextInt();
		int b3=sc.nextInt();
		int c4=sc.nextInt();
		int b4=sc.nextInt();
		if(c1==c2&&c3==c4&&b1==b4&&b2==b3)
		{
			System.out.println("yes");
		}
		else
		{
			System.out.println("no");
		}
	}
}
