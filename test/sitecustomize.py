
'''Setup testing entry point for the following:
    * Set sys.path
    * Add gevent exception workaround'''

import os
import sys

# Set sys.path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)
sys.path.append(os.path.join(root_path, 'lib'))

# Prevent gevent monkeypatching used on lib/storage/s3 to throw KeyError
# exception. Should be loaded as early as posible:
#   http://stackoverflow.com/questions/8774958
import gevent.monkey
gevent.monkey.patch_thread()
