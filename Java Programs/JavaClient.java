import java.io.*;
import java.net.*;

class JavaClient
{
	public static void main(String argv[]) throws Exeption
	{	
		String sentence;
		String modifiedSentence;
		BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
		Socket clientSocket = new Socket("localhost",6789);
		DataOutputStream outToServer = new dataOutputStream(clientSocket.getOutputStream());
		BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));   
		sentence = inFromUse.readLine();
		modifiedSentence =inFromServer.readLine();
		System.out.println("FROM SERVER: " + modifiedSentence);
		clientSocket.close();
	}
}
