import os
import sys

# We get the actual Path.
# Example: dir_path = C:\repositories\python-codewars\tests
dir_path = os.path.dirname(os.path.realpath(__file__))
# Removing last five characters (tests):
# Example: dir_path = C:\repositories\python-codewars\
dir_path = dir_path[:-5]
# Append the src to dir_path string.
dir_path = dir_path + "src"
# Add to system paths our src folder:
#sys.path.insert(0, '../src')
sys.path.append(dir_path)
# Print all paths of python system.
#print('\n'.join(sys.path))
