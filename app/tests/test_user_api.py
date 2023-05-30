import csv
import unittest
import requests

# Assuming the test data CSV file is in the same directory as this script
TEST_DATA_FILE = 'test_data.csv'
BASE_URL = 'http://localhost:8080'  # Update the URL if needed


class UserApiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data = cls.load_test_data()

    @staticmethod
    def load_test_data():
        test_data = []
        with open(TEST_DATA_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                test_data.append(row)
        return test_data

    def test_a_post_users_from_csv(self):
        for user_data in self.test_data:
            response = requests.post(f'{BASE_URL}/users', json=user_data)
            self.assertEqual(response.status_code, 200)

    def test_b_get_all_users(self):
        response = requests.get(f'{BASE_URL}/users')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('users', data)
        self.assertEqual(len(data['users']), len(self.test_data))

    def test_c_get_user_by_id(self):
        for row in self.test_data:
            user_id = int(row['id'])
            response = requests.get(f'{BASE_URL}/users/{user_id}')
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertIn('user_name', data)
            user_data = {'id': data['user_name']['id'],
                         'user_name': data['user_name']['user_name']}
            self.assertEqual(
                user_data, {'id': user_id, 'user_name': row['user_name']})

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
