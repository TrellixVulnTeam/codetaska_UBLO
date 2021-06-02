import requests

headers = {
    'accept': 'application/json',
    'content-type': 'application/json',
    'api_key': 'special_key'
}


class Pet:
    def __init__(self):
        pass

    def create(self, data):
        response = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, data=data)
        return response.status_code

    def read(self):
        response = requests.get('https://petstore.swagger.io/v2/pet/1', headers=headers)
        return response.status_code

    def update(self, data):
        response = requests.put('https://petstore.swagger.io/v2/pet', headers=headers, data=data)
        return response.status_code

    def find_by_status(self):
        response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=available', headers=headers)
        return response.status_code

    def update_store(self, data):
        header = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        response = requests.post('https://petstore.swagger.io/v2/pet/1', headers=header, data=data)
        return response.status_code

    def delete(self):
        response = requests.delete('https://petstore.swagger.io/v2/pet/1', headers=headers)
        return response.status_code


class Store:

    def read_inventory(self):
        response = requests.get('https://petstore.swagger.io/v2/store/inventory', headers=headers)
        return response.status_code

    def create_order(self, data):
        response = requests.post('https://petstore.swagger.io/v2/store/order', headers=headers, data=data)
        return response.status_code

    def read_order(self):
        response = requests.get('https://petstore.swagger.io/v2/store/order/1', headers=headers)
        return response.status_code

    def delete_order(self):
        response = requests.delete('https://petstore.swagger.io/v2/store/order/1', headers=headers)
        return response.status_code


class User:
    def create(self, data):
        response = requests.post('https://petstore.swagger.io/v2/user', headers=headers, data=data)
        return response.status_code

    def read(self):
        response = requests.get('https://petstore.swagger.io/v2/store/order/1', headers=headers)
        return response.status_code

    def update(self, data):
        response = requests.put('https://petstore.swagger.io/v2/user/username', headers=headers, data=data)
        return response.status_code

    def delete(self):
        response = requests.delete('https://petstore.swagger.io/v2/user/username', headers=headers)
        return response.status_code

    def login(self):
        params = (
            ('username', 'username'),
            ('password', 'password'),
        )
        response = requests.get('https://petstore.swagger.io/v2/user/login', headers=headers, params=params)
        return response.status_code

    def logout(self):
        response = requests.get('https://petstore.swagger.io/v2/user/logout', headers=headers)
        return response.status_code
