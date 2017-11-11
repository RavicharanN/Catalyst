# Catalyst
Peer to peer communication made easy

### Libraries and stacks used 
* Flask as the webFramework 
* flask_compress module to compress the static files during runtime
* socket library for p2p communication

### How does it work? 
1. Sender and the receiver should be on the same local network.
2. Sender runs the application and enters the path of the particular file or a directory which he wishes to send, ans then he waits for the receiver to receive the file <br>
Note: ``` pwd ``` command can be used to obtain the path of the directory.
3. The receive receives the file by entering the IP address of the sender.

### Follow these  steps to run the application on your local machine 
After you clone the repo. 
```
cd Catalyst
pip install -r requirements.txt
python app.py
```
And you're ready to go! 
<br>
Run the application in a virtual environment.
