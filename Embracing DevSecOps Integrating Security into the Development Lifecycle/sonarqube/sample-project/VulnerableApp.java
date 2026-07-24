package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

public class VulnerableApp {
    
    // Hard-coded credentials (security vulnerability)
    private static final String DB_URL = "jdbc:mysql://localhost:3306/testdb";
    private static final String USERNAME = "admin";
    private static final String PASSWORD = "password123";
    
    public static void main(String[] args) {
        VulnerableApp app = new VulnerableApp();
        app.demonstrateVulnerabilities();
    }
    
    public void demonstrateVulnerabilities() {
        // SQL Injection vulnerability
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter user ID: ");
        String userId = scanner.nextLine();
        
        try {
            Connection conn = DriverManager.getConnection(DB_URL, USERNAME, PASSWORD);
            Statement stmt = conn.createStatement();
            
            // Vulnerable SQL query - direct string concatenation
            String query = "SELECT * FROM users WHERE id = '" + userId + "'";
            ResultSet rs = stmt.executeQuery(query);
            
            while (rs.next()) {
                System.out.println("User: " + rs.getString("username"));
            }
            
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        scanner.close();
    }
    
    // Method with potential null pointer exception
    public String processUserInput(String input) {
        return input.toUpperCase(); // No null check
    }
    
    // Unused private method (code smell)
    private void unusedMethod() {
        System.out.println("This method is never called");
    }
}
