import zmq

context = zmq.Context()

#  Socket to talk to server
print("starting hello world server…")
socket = context.socket(zmq.SUB)
socket.bind("tcp://127.0.0.1:4444")
socket.subscribe("")

#  Do 10 requests, waiting each time for a response
while True:
    msg = socket.recv_string()
    print("got message ", msg)
