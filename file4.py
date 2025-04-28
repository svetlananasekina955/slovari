server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for tag, info in server_data.items():
    print(tag + ":", "\n")
    for key, value in info.items():
        print("\t" + key + ": " + value, "\n")
