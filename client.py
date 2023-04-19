import socket

# Create a socket object and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.99.27', 1234))

# Receive a welcome message from the server
print(s.recv(1024).decode())

# Loop through each question in the quiz
for i in range(1, 6):
    # Receive the current question from the server
    question = s.recv(1024).decode()
    # Print the question and ask the user for their answer
    answer = input(question)
    # Send the user's answer to the server
    s.send(answer.encode())
    # Receive the server's response (correct/incorrect)
    response = s.recv(1024).decode()
    # Print the server's response
    print(response)

# Receive the user's final score from the server
score = s.recv(1024).decode()
# Print the user's final score
print(score)

# Close the connection
s.close()
