clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client is already in the clients\' list')


def list_clients():
    global clients
    print(clients)


def update_client(client_name, new_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, new_name)
    else:
        print('This clients does not exist')


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')


def _get_client_name():
    return input('What\'s the client name?: ')


if __name__ == "__main__":
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        new_name = input('What is the new name?: ')
        update_client(client_name, new_name)
        list_clients()
    else:
        print('Invalid command!')
