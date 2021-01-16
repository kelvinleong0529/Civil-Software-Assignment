import cx_Freeze
import sys
import matplotlib

base = None
if sys.platform == 'win32':
	base = 'Win32GUI'

executables = [cx_Freeze.Executable("Civil_Software.py",base=base)]

cx_Freeze.setup(
	name = "CivilSoftwareAssignment",
	options = {"build_exe":{"packages":["tkinter","matplotlib"]}},
	version = "1.0",
	description = "Civil Software Course Final Assignment",
	executables = executables
)