import bluetooth
import uuid

# Create a new UUID for the service
service_uuid = str(uuid.uuid4())
print(service_uuid)

# Get the Bluetooth MAC address of the device
mac_address = ':'.join(bluetooth.read_local_bdaddr()[0].split(':'))

# Create a new server socket
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Bind the socket to a port
server_socket.bind(("", bluetooth.PORT_ANY))

# Start listening for incoming connections
server_socket.listen(1)

# Advertise the service
bluetooth.advertise_service(server_socket, "MyService", service_id=service_uuid,
                             service_classes=[service_uuid, bluetooth.SERIAL_PORT_CLASS],
                             profiles=[bluetooth.SERIAL_PORT_PROFILE])

# Wait for a connection
print('Waiting for connection on RFCOMM channel', port)
client_socket, client_info = server_socket.accept()
print('Accepted connection from', client_info)

# Receive data from the client
data = client_socket.recv(1024)
print('Received', data)

# Disconnect from the client
client_socket.close()
server_socket.close()
