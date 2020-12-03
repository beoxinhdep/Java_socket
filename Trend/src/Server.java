// Java implementation of  Server side 
// It contains two classes : Server and ClientHandler 
// Save file as Server.java 

import java.io.*;
import java.text.*;
import java.util.*;
import java.net.*;

// Server class 
public class Server {

    public static void main(String[] args) throws IOException {
        // server is listening on port 5056 
        ServerSocket ss = new ServerSocket(8080);

        // running infinite loop for getting 
        // client request 
        while (true) {
            Socket s = null;

            try {
                // socket object to receive incoming client requests 
                s = ss.accept();

                System.out.println("A new client is connected : " + s);

                // obtaining input and out streams 
                DataInputStream dis = new DataInputStream(s.getInputStream());
                DataOutputStream dos = new DataOutputStream(s.getOutputStream());

                System.out.println("Assigning new thread for this client");

                // getting localhost ip 
//                InetAddress ip = InetAddress.getByName("localhost");
                // establish the connection with server port 5056 
//                Socket s1 = new Socket(ip, 12345);
                // obtaining input and out streams 
//                DataInputStream dis1 = new DataInputStream(s1.getInputStream());
//                DataOutputStream dos1 = new DataOutputStream(s1.getOutputStream());
                // create a new thread object 
                Thread t = new ClientHandler(s, dis, dos);

                // Invoking the start() method 
                t.start();

            } catch (Exception e) {
                s.close();
                e.printStackTrace();
            }
        }
    }
}

// ClientHandler class 
class ClientHandler extends Thread {

    DateFormat fordate = new SimpleDateFormat("yyyy/MM/dd");
    DateFormat fortime = new SimpleDateFormat("hh:mm:ss");
    Scanner scn = new Scanner(System.in);
    final DataInputStream dis;
    final DataOutputStream dos;
    final Socket s;

    // Constructor 
    public ClientHandler(Socket s, DataInputStream dis, DataOutputStream dos) {
        this.s = s;
        this.dis = dis;
        this.dos = dos;
//        this.s1 = s1;
//        this.dis1 = dis1;
//        this.dos1 = dos1;
    }

    @Override
    public void run() {
        String received;
        String toreturn;

        try {
            Scanner scn = new Scanner(System.in);
            InetAddress ip = InetAddress.getByName("localhost");
            Socket s1 = new Socket(ip, 12345);
            DataInputStream dis1 = new DataInputStream(s1.getInputStream());
            DataOutputStream dos1 = new DataOutputStream(s1.getOutputStream());

            while (true) {
                // Ask user what he wants 
                dos.writeUTF("What do you want?[Date | Time]..\n"
                        + "Type Exit to terminate connection.");
                // receive the answer from client 
                received = dis.readUTF();
                System.out.println("Receive from Java Client:"+received);
                //System.out.println(dis.readUTF()); 
                String tosend = received;
                dos1.writeUTF(tosend);
                System.out.println("Send to Python Server:"+tosend);

                // If client sends exit,close this connection  
                // and then break from the while loop 
//                if (tosend.equals("Exit")) {
//                    System.out.println("Closing this connection : " + s);
//                    s.close();
//                    System.out.println("Connection closed");
//                    break;
//                }
//                if (received.equals("Exit")) {
//                        System.out.println("Client " + this.s + " sends exit...");
//                        System.out.println("Closing this connection.");
//                        this.s.close();
//                        System.out.println("Connection closed");
//                        break;
//                    }
                // printing date or time as requested by client 
                String received2 = dis1.readUTF();
                System.out.println("Receive from Python Server:"+received2);

                // creating Date object 
                Date date = new Date();

                // write on output stream based on the 
                // answer from the client 
                switch (received) {

                    case "Date":
                        toreturn = fordate.format(date);
                        dos.writeUTF(toreturn);

                        break;

                    case "Time":
                        toreturn = fortime.format(date);
                        dos.writeUTF(toreturn);

                        break;

                    default:
                        dos.writeUTF("Invalid input");
                        break;
                }
            }
            

        } catch (Exception e) {
            e.printStackTrace();
        }

        try {
            // closing resources 
            this.dos.flush();
            this.dis.close();
            this.dos.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}

//import java.io.*;  
//import java.net.*; 
//public class Server {
//  public static void main(String[] args) throws IOException {
//       ServerSocket serverSocket = new ServerSocket(8080);
//       Socket soc = serverSocket.accept();
//       while (true)  {
//      try{ 
//      
//      System.out.println("Receive new connection: " + soc.getInetAddress());
//      DataOutputStream dout=new DataOutputStream(soc.getOutputStream());  
//      DataInputStream in = new DataInputStream(soc.getInputStream());
//      dout.writeUTF("Thank You For Connecting.");
//      String msg=(String)in.readUTF();
//      System.out.println("Client: "+msg);
//      dout.flush();
//      dout.close();
//      }
//      catch(Exception e)
//      {
//               soc.close();
//                e.printStackTrace(); 
//  }
//       }
//  }
//  }
