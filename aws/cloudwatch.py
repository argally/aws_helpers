"""
Class to represent Cloudwatch resources
"""
from __future__ import print_function
from builtins import str
from builtins import object

class CloudWatchLogs(object):
	"""
	Working with Cloudwatch logs 
	"""

	def __init__(self, loggroup):
		"""
		EC2Eip Constructor which instanciates Connection class
		"""
		self.loggroup = loggroup
 
	def log_group_search(self, conn):
		next_token = None
		log_groups = conn.logs.describe_log_groups()
		print("LogGroupName: %s" % self.loggroup)