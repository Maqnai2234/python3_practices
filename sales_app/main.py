import sys
clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    
    print(clients)


def update_client(client_name, updated_client_name):
    _replace_client(client_name, updated_client_name) 


def delete_client(client_name):
    _replace_client(client_name, "") 


def search_client(client_name):
    global clients
    clients_list = clients.split(',')
    for client in clients_list:
        if client  != client_name:
            continue
        else:
            return True

def _replace_client(client_name, string_replace):
    global clients
     
    if client_name in clients:
        clients = clients.replace(client_name + ',' , string_replace) 
    else:
        print('Client is not clients list')


def _add_comma():
    global clients

    clients += ','


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')
        if client_name == 'exit':
            break
    
    if client_name == 'exit':
        sys.exit()
        
    return client_name


def _print_welcome():
    print('WELCOME TO SALES APP')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name ')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print(f"The client: {client_name} is not our client\'s list")
    else:
        print('Invalid command')
