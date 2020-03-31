# Java-Password-Cracker
A distributed password cracker implemented using Java

## Introduction
The objective of this project is to design a password cracker that implements the concept of multithreading to perform its operation faster. To this end, the given password cracker consists of worker clients and a server. The server accepts a password from the user and is responsible for dividing and allocating the work among the clients. The clients and server communicate using the sockets API to send UDP packets. MD5 hashing is used for the purpose of this password cracker.

## Summary
When run, the server will ask user for a password. The password entered must have the following properties:
- Must be of length 5-6 characters.
- Must contain only digits (0-9) and small case alphabets (a-z)

After accepting the password, the server combines the password and the system date and generates an MD5 hash of the same. Each time a new client requests the server for connection, the server establishes a new thread for communication with the client. After the connection between the worker client and server is established, the server sends a hashed password and a range to the client. The client tries to generate all passwords within the given range and compare them to the hashed password. If a generated password matches the hashed password sent by the server it means that the client has successfully cracked the password and it notifies the server about the same. If the client is unable to crack the password successfully, it terminates with a failure message.

## Additional Notes
This password cracker is written in Java hence it is essential to install a JDK to run it. It consists of two programs named server and client. The server has to be run first and kept alive for the password cracking to take place smoothly. Since this password cracker incorporates multithreading, multiple clients can be run simultaneously.
