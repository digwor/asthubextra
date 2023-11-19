users = []

def create_user(user: dict) -> None:
    users.append(user)
    print()
    print('User created!')
    input('Press any key to continue')

def get_user_by_email(email: str) -> dict | None:
    for user in users:
        if user.get('email') == email:
            return user


def delete_user_by_email(email: str) -> None:
    user = get_user_by_email(email)

    if user is None:
        input('User not found!')
        return None

    users.remove(user)
    print()
    print('User deleted!')
    input('Press any key to continue')

def show_list_of_users() -> None:
    if users != []:
        for user in users:
            for key, value in user.items():
                print(f'{key}: {value}')
            print()
        input('Press any key to continue')
    else:
        input('User not found!')

def authorization(email: str, password: str) -> dict | None:
    for user in users:
        if user.get('email') == email and user.get('password') == password:
            print('You have successfully logged in')
            print(user)

def menu():
    print()
    print('Choose one option:')
    print('1. Create user')
    print('2. Show list of Users')
    print('3. Delete user from list')
    print('4. Authorization')
    print('5. Exit')

while True:
    menu()
    action = int(input())
    if action == 1:
        name = input('Name: ')
        surname = input('Surname: ')
        age = input('Age: ')
        address = input('Address: ')
        email = input('email: ')
        password = input('Password: ')
        user = {
            'name': name,
            'surname': surname,
            'age': age,
            'address': address,
            'email': email,
            'password': password,
        }

        create_user(user)

    elif action == 2:
        show_list_of_users()

    elif action == 3:
        search_email = input('Insert users email: ')
        delete_user_by_email(search_email)

    elif action == 4:
        login = input('Insert your email: ')
        passwrd = input('Insert your password: ')
        authorization(login, passwrd)

    elif action == 5:
        print('Goodbye!')
        break
    else:
        print('Invalid choose')
        input('Press any key to continue')