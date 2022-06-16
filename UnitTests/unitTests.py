import unittest
import requests

unittest.TestLoader.sortTestMethodsUsing = None

class TestCase(unittest.TestCase):
    def setUp(self):
        self.host = 'http://127.0.0.1:8000/frames'

    def test_apost(self):
        f = open('1.jpg', 'rb')
        files = [('files', f)]
        req = requests.post(url=self.host, files=files)
        f.close()
        self.assertEqual(req.status_code, 200)
        print('One file - ' + req.content.decode('UTF-8'))

        f = open('1.jpg', 'rb')
        files = [('files', f)]
        f2 = open('2.jpg', 'rb')
        files.append(('files', f2))
        req = requests.post(url=self.host, files=files)
        f.close(); f2.close()
        self.assertEqual(req.status_code, 200)
        print('Two file - ' + req.content.decode('UTF-8'))

        files = []
        ff = []
        tmp = None
        for i in range(1,17):
            tmp = open(f'{i}.jpg', 'rb')
            files.append(('files', tmp))
            ff.append(tmp)
        req = requests.post(url=self.host, files=files)
        self.assertEqual(req.status_code, 400)
        for i in ff:
            i.close()
        print('To much files - ' + req.content.decode('UTF-8'))

    def test_bget(self):
        url = self.host + '/111'
        req = requests.get(url=url)
        self.assertEqual(req.status_code, 200)
        print('Code 111 - ' + req.content.decode('UTF-8'))
        url = self.host + '/222'
        req = requests.get(url=url)
        self.assertEqual(req.status_code, 200)
        print('Code 222 - ' + req.content.decode('UTF-8'))
        url = self.host + '/333'
        req = requests.get(url=url)
        self.assertEqual(req.status_code, 200)
        print('Code 333 - ' + req.content.decode('UTF-8'))

    def test_cdel(self):
        url = self.host + '/111'
        req = requests.delete(url=url)
        self.assertEqual(req.status_code, 200)
        print(req.content.decode('UTF-8'))
        url = self.host + '/222'
        req = requests.delete(url=url)
        self.assertEqual(req.status_code, 200)
        print(req.content.decode('UTF-8'))
        url = self.host + '/333'
        req = requests.delete(url=url)
        self.assertEqual(req.status_code, 200)
        print(req.content.decode('UTF-8'))
        print('\nNow all must be clinner\n')
        self.test_bget()


if __name__ == "__main__":
  unittest.main()