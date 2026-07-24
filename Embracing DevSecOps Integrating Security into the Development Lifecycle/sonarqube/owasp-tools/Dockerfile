FROM openjdk:11-jre-slim

COPY webgoat-server/target/webgoat-server-*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app.jar"]
