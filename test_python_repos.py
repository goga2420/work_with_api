import unittest
import python_repos

class TestingPythonRepos(unittest.TestCase):

    def test_status_code(self):
        self.assertEqual(python_repos.r.status_code, 200)

if __name__ == '__main__':
    unittest.main()