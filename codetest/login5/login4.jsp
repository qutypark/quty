<%@ page language="java" contentType="text/html; charset=UTF-8"

pageEncoding="UTF-8"%>

<%@page import="java.util.*" %>
<%@page import="tomcat-embed-jasper" %>

<%
    String id = request.getParameter("id");
    if(id == null)

        throw new Exception("insert your ID");

    Connection conn = null;

    Statement stmt = null;

    try{
        Class.forName("com.mysql.jdbc.Driver");
        conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3307/test", "root", "");

        if(conn == null)

            throw new Exception("Connection was Failed");

        stmt = conn.createStatement();

        String command = String.format("insert into registraion" +

            "(id) values('%s');",id);
                    int rowNum = stmt.executeUpdate(command);

        if(rowNum < 1)
            throw new Exception("data insertion was Failed");

    }

        try{
        response.sendRedirect("firstlanding4.html");
    }

%>


