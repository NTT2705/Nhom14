# Fill the Python code in this file
import unittest
from recursive_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
	'''test module to test search function in `recursive_json_search.py`'''
	def test_search_found(self):
		'''key should be found, return list should not be empty'''
		self.assertTrue([]!=json_search(key1,data))
	def test_search_not_found(self):
		'''key should not be found, should return an empty list'''
		self.assertTrue([]==json_search(key2,data))
	def test_is_a_list(self):
		'''Should return a list'''
		self.assertIsInstance(json_search(key1,data),list)

	#test case bo sung
	def test_wrong_role_cannot_read_secret(self):
		'''viewer should not be able to read apiKey'''
		result = json_search("apiKey", data, role="viewer")
		self.assertEqual([], result)
	def test_viewer_can_read_issue_summary(self):
		'''viewer should be able to read issueSummary'''
		result = json_search("issueSummary", data, role="viewer")
		self.assertNotEqual([], result)
	def test_operator_cannot_read_secret(self):
		'''operator should not be able to read apiKey'''
		result = json_search("apiKey", data, role="operator")
		self.assertEqual([], result)

if __name__ == '__main__':
	unittest.main()
