package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.Properties;
import java.util.Scanner;

public class SecureApp {
    
    // Use configuration file instead of hard-coded credentials
    private Properties config;
    
    public SecureApp() {
        loadConfiguration();
    }
    
    private void loadConfiguration() {
        config = new Properties();
        // In real application, load from secure configuration
        config.setProperty("db.url", "jdbc:mysql://localhost:3306/testdb");
        config.setProperty("db.username", System.getenv("DB_USERNAME"));
        config.setProperty("db.password", System.getenv("DB_PASSWORD"));
    }
    
    public static void main(String[] args) {
        SecureApp app = new SecureApp();
        app.demonstrateSecurePractices();
    }
    
    public void demonstrateSecurePractices() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter user ID: ");
        String userId = scanner.nextLine();
        
        try {
            Connection conn = DriverManager.getConnection(
                config.getProperty("db.url"),
                config.getProperty("db.username"),
                config.getProperty("db.password")
            );
            
            // Use prepared statement to prevent SQL injection
            String query = "SELECT * FROM users WHERE id = ?";
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setString(1, userId);
            
            ResultSet rs = pstmt.executeQuery();
            
            while (rs.next()) {
                System.out.println("User: " + rs.getString("username"));
            }
            
            conn.close();
        } catch (Exception e) {
            // Log error securely without exposing sensitive information
            System.err.println("Database error occurred");
        }
        
        scanner.close();
    }
    
    // Method with proper null checking
    public String processUserInput(String input) {
        if (input == null) {
            throw new IllegalArgumentException("Input cannot be null");
        }
        return input.toUpperCase();
    }
}
EOF

# Update pom.xml to use secure dependency versions
cat > pom.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example</groupId>
    <artifactId>devsecops-demo</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>
    
    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <sonar.projectKey>devsecops-demo</sonar.projectKey>
        <sonar.projectName>DevSecOps Demo</sonar.projectName>
    </properties>
    
    <dependencies>
        <!-- Updated to secure versions -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-collections4</artifactId>
            <version>4.4</version>
        </dependency>
        
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.15.2</version>
        </dependency>
        
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.sonarsource.scanner.maven</groupId>
                <artifactId>sonar-maven-plugin</artifactId>
                <version>3.9.1.2184</version>
            </plugin>
        </plugins>
    </build>
</project>
