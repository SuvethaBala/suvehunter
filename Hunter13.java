import java.util.*;
import java.lang.*;
import java.io.*;


class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner in=new Scanner(System.in);
        String inputString = in.nextLine();
        Stack stack = new Stack();

        for (int i = 0; i < inputString.length(); i++) {
            stack.push(inputString.charAt(i));
        }

        String reverseString = "";

        while (!stack.isEmpty()) {
            reverseString = reverseString+stack.pop();
        }

        if (inputString.equals(reverseString))
            System.out.println("YES");
        else
            System.out.println("NO");

	}
}
