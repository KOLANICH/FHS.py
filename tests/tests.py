#!/usr/bin/env python3
import sys
from pathlib import Path
from collections import OrderedDict
import unittest

thisFile = Path(__file__).absolute()
thisDir = thisFile.parent.absolute()
repoMainDir = thisDir.parent.absolute()
sys.path.insert(0, str(repoMainDir))

dict = OrderedDict

from FHS.GNUDirs import getGNUDirs
from FHS import FHS, Common


class SimpleTests(unittest.TestCase):
	def testSimple(self):
		self.assertEqual(Path(FHS.usr.local.bin), Path("/usr/local/bin"))

	def testRoot(self):
		self.assertEqual(FHS, Path("/"))

	def testCommon(self):
		self.assertEqual(Common.OpenCL, Path("/etc/OpenCL"))
		self.assertEqual(Common.icons, Path("/usr/share/icons"))

	def testGNUDirs(self):
		gd = getGNUDirs(FHS.usr)
		self.assertEqual(gd.toGnuArgs(), {
			"prefix": Path("/usr"),
			"bindir": Path("/usr/bin"),
			"datarootdir": Path("/usr/share"),
			"datadir": Path("/usr/share"),
			"sharedstatedir": Path("/usr/com"),
			"includedir": Path("/usr/include"),
			"infodir": Path("/usr/share/info"),
			"libdir": Path("/usr/lib"),
			"libexecdir": Path("/usr/libexec"),
			"localedir": Path("/usr/share/locale"),
			"localstatedir": Path("/usr/var"),
			"sbindir": Path("/usr/sbin"),
			"sysconfdir": Path("/usr/etc"),
			"mandir": Path("/usr/share/man")
		})

if __name__ == "__main__":
	unittest.main()
