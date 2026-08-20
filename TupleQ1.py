# Server configuration tuple
server_config = ("192.168.1.1", 8080)

print("Original Configuration:", server_config)

# Port number update karne ki koshish
try:
    server_config[1] = 9090
except TypeError as e:
    print("Error:", e)