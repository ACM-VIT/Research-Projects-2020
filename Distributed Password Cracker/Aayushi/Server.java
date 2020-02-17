import java.io.*;
import java.net.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Scanner;

public class Server 
{
	static final int portNumber = 8003;
	static int range = -1;
	static String hashPassword, actualPassword;
	public static void main(String args[]) throws IOException 
	{
        	System.out.println("**** Distributed Password Breaker ****");
        	System.out.println("**************** Server **************");
		System.out.println("Enter Password:");
		Scanner sc=new Scanner(System.in);
		actualPassword=sc.next();
		System.out.println("Actual Password: " + actualPassword);
		if(actualPassword.length()<5 || actualPassword.length()>6)
		{
			System.out.println("Password not within proper length range");
			System.exit(0);
		}
        	hashPassword = generateHash();
        	System.out.println("Hash password: " + hashPassword);
        	ServerSocket ss = new ServerSocket(portNumber);
        	System.out.println("\nWaiting for client response....");
        	int id = 0;
        	while (true) 
		{
            		Socket clientSocket = ss.accept();
            		ClientMultiThread multiThread = new ClientMultiThread(clientSocket, ++id);
            		multiThread.start();
            		System.out.println("\nClient_" + id + " connection established\n");
        	}
    	}

	public static String generateHash() 
	{
        	StringBuffer sb = new StringBuffer();
		String date = getSystemDate();
        	try
		{
            		MessageDigest md = MessageDigest.getInstance("MD5");
            		md.update((actualPassword + date).getBytes());
            		byte[] byteData = md.digest();
			for (int i = 0; i < byteData.length; i++) 
                		sb.append(Integer.toString((byteData[i] & 0xff) + 0x100, 16).substring(1));
        	} 
		catch(NoSuchAlgorithmException ex) 
		{
			ex.printStackTrace();
		}
        	return new String(sb);
    	}

	public static String getSystemDate() 
	{
        	DateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy");
        	Calendar cal = Calendar.getInstance();
        	String date = (dateFormat.format(cal.getTime())).toString();
        	return date;
    	}

    	public static class ClientMultiThread extends Thread
	{
        	int noOfPacketsSent = 1;
		int clientId = -1;
        	String sendMsg = "", receiveMsg = "";
        	Socket clientSocket;
        	ClientMultiThread(Socket socket, int id)
		{
            		clientSocket = socket;
            		clientId = id;
        	}
        	void printIntoStream(int noOfPacketsSent, int clientId) 
		{
            		long lower_limit = 1000000 * range; 
            		long upper_limit = lower_limit + (1000000 - 1);
			String Lower_limit = Long.toString(lower_limit, 36);
            		String Upper_limit = Long.toString(upper_limit, 36);
            		System.out.println("\nData packet_" + noOfPacketsSent +" sent to client_" + clientId);
            		System.out.println("Given Range: " + Lower_limit + " to " + Upper_limit);
        	}
        
        	public void run() 
		{
			try 
			{
                		Scanner sc = new Scanner(clientSocket.getInputStream());
                		PrintStream psOUT = new PrintStream(clientSocket.getOutputStream());   
                		while (noOfPacketsSent <= 100) 
				{
                    			sendMsg = (++range) + "\n" + hashPassword;
                    			psOUT.println(sendMsg);
                    			printIntoStream(noOfPacketsSent, clientId);
                    			receiveMsg = sc.nextLine();
                    			if (receiveMsg.equals("Success")) 
					{
                        			System.out.println("Client_" + clientId + " successfully crack the password");
						clientSocket.close();
                				sc.close();
                				psOUT.close();
                				System.out.println("Connection lost from client_" + clientId);
                        			System.exit(0);
                    			}
                    			noOfPacketsSent++;
                		}
            		} 
			catch (IOException ex) 
			{ 
				ex.printStackTrace();
            		}
        	}
    	}
}
