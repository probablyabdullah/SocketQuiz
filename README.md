# socketquiz
**A short quiz application using python's socket-programming.**

This project encompasses the basic features of a quiz program implemented using socket programming, with the quiz program being entirely written in Python. The program uses a host of python modules such as threading, time and socket. This is a single-player game and the host contains a list of challenging questions and the correct answers to them. The players then have an opportunity to answer the question, and the client answers are string-matched with the host’s answers, and the answers aren’t case-sensitive. There is a timer implemented, and the client is supposed to answer the question before the time runs out. If the answer is correct, the client is awarded a point. The connection is made by specifying the IP Address of the server and a randomized port number is then matched.
The game has two phases. One is the client phase, and one is the server phase. The server waits for the client to connect before the game begins. The server broadcasts the questions to client system using the thread module from the list of questions pre-stored on the server, in a list format. It then waits for the client to broadcast their answers. The score is incremented as per the answers provided. 
The program/game continues till a client has entered an answer for all the questions, upon which he/she receives his final score.

**Sample Screenshot:**

![Screenshot 2023-04-12 143419](https://user-images.githubusercontent.com/79295754/232965443-4f041ae6-f8a1-46c9-b126-933bef922aa4.png)

