import unittest
import subprocess
import time
from websocket import create_connection


class TestSocket(unittest.TestCase):
    def setUp(self):
        self.p = subprocess.Popen(['python', 'example.py'])
        time.sleep(0.2)

    def test_from_client(self):
        ws = create_connection("ws://localhost:5000/echo")
        msg = "Hello, World"
        print("Sending %s...\n" % msg)
        ws.send(msg)
        print("Sent\nRecieving...\n")
        reply = ws.recv()
        print("Received '%s'" % reply)
        ws.close()
        self.assertEqual(msg, reply)

    def tearDown(self):
        self.p.kill()


if __name__ == "__main__":
    unittest.main()
