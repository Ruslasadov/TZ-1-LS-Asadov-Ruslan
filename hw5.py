directory = {'user1': 55, 'user2': 26, 'user3': 76, 'user4': 21, 'user5': 45,
             'user6': 23, 'user7': 97, 'user8': 54, 'user9': 29, 'user10': 2, 'user11': 9}
input_name = input('Username: ')

def conversation():
        return directory.get(input_name, 'undefined')

print('Iphone: ', conversation())