import java.io.*;
import java.net.*;
import java.security.*;
import java.text.*;
import java.util.logging.Logger;
import java.util.logging.Level;
import java.util.Calendar;
import java.util.Scanner;

public class Client
{
	static final int portNumber=8003;
	static final String serverIP="127.0.0.1";
	static int clientTrialNumber=0;
	static String date, actualHashPassword;
	static Scanner sc;
	static PrintStream psOUT;
	static Socket clientSocket;
	static MessageDigest md;
	static String messageToServer;
	static int range;
	public static void main(String args[]) throws IOException
	{
		System.out.println("Welcome to the Password Cracker");
		try
		{
			md=MessageDigest.getInstance("MD5");
		}
		catch(NoSuchAlgorithmException ex)
		{
			Logger.getLogger(Client.class.getName()).log(Level.SEVERE,null,ex);
		}
		date=getSystemDate();
		ConnectToServer();
		clientTrialNumber++;
		while(clientTrialNumber<=100){
			range=getRange();
			printIntoStream(clientTrialNumber);
			messageToServer=crackPassword();
			if(messageToServer.equals("fail"))
			{
				System.out.println("\nCan't find Password");
				if(clientTrialNumber!=100) System.out.println("requesting another packet....");
				psOUT.println(messageToServer);
				clientTrialNumber++;
			}
			else
			{
				System.out.println("Got password. It is: "+messageToServer);
				psOUT.println("Success");
				getDisconnectedFromServer();
				System.exit(0);
			}
		}
		getDisconnectedFromServer();
	}

	public static String crackPassword()
	{
		String value, temp, generatedHash;
		long lower_limit, upper_limit;
		lower_limit = 1000000 * range; //1,000,000
        	upper_limit = lower_limit + (1000000-1);
		for(long i=lower_limit;i<=upper_limit;i++)
		{
			value=Long.toString(i,36);
			temp=value;
			generatedHash=generateHash(temp);
			if(compareHash(actualHashPassword,generatedHash))
			{
				return temp;
			}
		}
		return "fail";
	}

	public static String getSystemDate()
	{
		DateFormat dateFormat=new SimpleDateFormat("dd-MM-yyyy");
		Calendar cal=Calendar.getInstance();
		String date=(dateFormat.format(cal.getTime())).toString();
		return date;
	}

	public static String generateHash(String password)
	{
		byte[] byteDate;
		StringBuffer sb = new StringBuffer();
		md.update((password+date).getBytes());
		byteDate=md.digest();
		for(int i=0;i<byteDate.length;i++)
		{
			sb.append(Integer.toString((byteDate[i]&0xff)+0x100,16).substring(1));
		}
		return new String(sb);
	}

	public static boolean compareHash(String hashFound, String generatedHash)
	{
		if(hashFound.equals(generatedHash))
			return true;
		else
			return false;
	}

	public static void ConnectToServer()
	{
		try
		{
			clientSocket = new Socket(serverIP,portNumber);
			System.out.println("Server connection established");
			sc=new Scanner(clientSocket.getInputStream());
			psOUT=new PrintStream(clientSocket.getOutputStream());
		}
		catch (IOException ex) {ex.printStackTrace();}
	}

	public static void getDisconnectedFromServer()
	{
		try
		{
			clientSocket.close();
			sc.close();
			psOUT.close();
			System.out.println("Connection lost from server");
		}
		catch(IOException ex) {ex.printStackTrace();}
	}

	public static int getRange()
	{
		String sendMessage="",receiveRange="";
		receiveRange=sc.nextLine();
		actualHashPassword=sc.nextLine();
		return Integer.parseInt(receiveRange);
	}

	public static void printIntoStream(int dataReceiveNo)
	{
		long lower_limit=1000000*range;
		long upper_limit=lower_limit+(1000000-1);
		String Lower_limit=Long.toString(lower_limit,36);
		String Upper_limit=Long.toString(upper_limit,36);    
		System.out.println("\nGet data packet_"+dataReceiveNo+" from server");
		System.out.println("Start cracking password Range: "+Lower_limit+" to "+Upper_limit);
	}

} 