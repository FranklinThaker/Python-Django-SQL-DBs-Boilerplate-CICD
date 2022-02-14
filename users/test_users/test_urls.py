from urllib import response
from wsgiref import headers
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from users.views import getAllUsers, addUser, deleteUser, updateUser
from users.models import User
from rest_framework.test import APIClient


class Check_If_URLs_Are_Valid_Or_Not(SimpleTestCase):
    def test_getAllUsers(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, getAllUsers)

    def test_addUser(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func, addUser)

    def test_updateUser(self):
        url = reverse('update', args=[1])
        self.assertEquals(resolve(url).func, updateUser)

    def test_deleteUser(self):
        url = reverse('delete', args=[1])
        self.assertEquals(resolve(url).func, deleteUser)


class Test_APIs_With_Actual_Data(TestCase):
    def setUp(self) -> None:
        self.testData = User.objects.create(
            username='testing_username',
            password='testing_password',
            name='test_name',
            age=25
        )

        self.getUsersURL = reverse('list')
        self.addUserURL = reverse('add')
        self.updateUserURL = reverse('update', args=[self.testData.pk])
        self.deleteUserURL = reverse('delete', args=[self.testData.pk])

        return super().setUp()

    def test_ListUsersAPI(self):
        client = Client()
        response = client.get(self.getUsersURL)
        self.assertEquals(response.status_code, 200)

    def test_AddUserAPI(self):
        response = self.client.post(self.addUserURL, {
            'username': 'admin',
            'password': 'admin',
            'name': 'Franklin',
            'age': 20,
        })
        self.assertEquals(response.status_code, 200)

    def test_UpdateUsersAPI(self):
        payload = {
            'username': 'admin',
            'password': 'admin',
            'name': 'Franklin',
            'age': 20,
        }
        # response = self.client.put(self.updateUserURL, payload) // will throw 415 error in only test cases
        url = '/user/updateUser/'+str(self.testData.pk)
        client = APIClient()
        response = client.put(url, format='json', data=payload)
        self.assertEquals(response.status_code, 200)

    def test_DeleteUserAPI(self):
        response = self.client.delete(self.deleteUserURL)
        self.assertEquals(response.status_code, 200)
