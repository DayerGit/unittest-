import unittest
from лаба_3 import app

class TestTrigonometryApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_correct_input_degrees(self):
        response = self.client.post("/", data={
            "angle": "45",
            "unit": "degrees",
            "precision": "4"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sin: 0.7071", response.data)
        self.assertIn(b"cos: 0.7071", response.data)
        self.assertIn(b"tan: 1.0", response.data)

    def test_correct_input_radians(self):
        response = self.client.post("/", data={
            "angle": "0.785398",
            "unit": "radians",
            "precision": "4"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sin: 0.7071", response.data)
        self.assertIn(b"cos: 0.7071", response.data)
        self.assertIn(b"tan: 1.0", response.data)

    def test_invalid_input(self):
        response = self.client.post("/", data={
            "angle": "abc",
            "unit": "degrees",
            "precision": "2"
        })
        self.assertEqual(response.status_code, 200)
        error_message = "Ошибка: введите корректные числовые значения.".encode("utf-8")
        self.assertIn(error_message, response.data)

    def test_missing_input(self):
        response = self.client.post("/", data={})
        self.assertEqual(response.status_code, 200)
        error_message = "Ошибка: заполните все поля формы.".encode("utf-8")
        self.assertIn(error_message, response.data)

if __name__ == "__main__":
    unittest.main()