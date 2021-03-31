import java.io.*;
import java.lang.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class ServletInsertingDataUsingHtml extends
HttpServlet{
  public void doPost(HttpServletRequest request, HttpServletResponse response)
  throws ServletException, IOException{
  response.setContentType("text/html");
  PrintWriter pw = response.getWriter();
  String connectionURL = "jdbc:mysql://localhost/test";
  Connection connection;
  try{
  String id = request.getParameter("id");
  pw.println(id);
  Class.forName("org.gjt.mm.mysql.Driver");
  connection = DriverManager.getConnection
  (connectionURL, "root", "");
  PreparedStatement pst = connection.prepareStatement
  ("insert into registration values(?)");
  pst.setString(1,id);
  int i = pst.executeUpdate();
  if(i!=0){
  pw.println("<br>Record has been inserted");
  }
  else{
  pw.println("failed to insert the data");
  }
  }
  catch (Exception e){
  pw.println(e);
  }
  }
}