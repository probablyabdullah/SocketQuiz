import socket
import threading
import time

# Define the quiz questions
quiz_questions = [
    "What is the capital of France?",
    "What is the largest country in the world?",
    "What is the currency of Japan?",
    "Who is the current President of the United States?",
    "What is the smallest planet in our solar system?"
]

# Define the quiz answers
quiz_answers = [
    "Paris",
    "Russia",
    "Yen",
    "Joe Biden",
    "Mercury",
    "paris",
    "russia",
    "yen",
    "joe biden",
    "mercury",
]

# Define a function to handle the client connections
def handle_client(conn, addr):
    # Send a welcome message to the client
    conn.send("Welcome to Quizaroo!\n".encode())
    # Initialize the client's score to 0
    score = 0
    # Loop through each question in the quiz
    for i in range(5):
        # Send the current question to the client
        conn.send(f"Question {i+1}: {quiz_questions[i]}\n".encode())
        # Start the timer for the client to answer the question
        start_time = time.time()
        # Receive the client's answer to the question
        answer = conn.recv(1024).decode().strip()
        # Cancel the timer
        end_time = time.time()
        # Check if the client's answer is correct
        if end_time-start_time <= 5.0 and (answer == quiz_answers[i] or answer == quiz_answers[i+5]):
            # Send a message indicating that the client answered correctly
            conn.send("Correct!\n".encode())
            # Update the client's score
            score += 1
        elif end_time-start_time > 5.0:
            # Send a message indicating that the time was up
            conn.send("Time's Up!\n".encode())
        else:
            # Send a message indicating that the client answered incorrectly
            conn.send("Incorrect.\n".encode())
    # Send the client's final score
    conn.send(f"Your final score is {score} out of 5.\n".encode())
    # Close the connection
    conn.close()

# Create a socket object and bind it to a port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.99.27', 1234))

# Listen for incoming connections
s.listen()

# Start the quiz
print("Quiz started!")
while True:
    # Accept a client connection
    conn, addr = s.accept()
    print(f"Connected to {addr}")
    # Create a new thread to handle the client connection
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
