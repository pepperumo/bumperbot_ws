import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pepperumo/bumperbot_ws/src/install/bumperbot_utils'