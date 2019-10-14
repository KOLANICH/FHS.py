import typing
from pathlib import Path
from functools import lru_cache

# from TargetTriple import TargetTriple

from . import StandardizedDirProto


class GNUDirs_:
	"""The way to pass the info about the dirs to the build system"""

	prefix = None
	bin = None
	sbin = None
	libexec = None
	etc = None
	var = None
	run = None
	lib = None
	include = None
	share = None
	info = None
	locale = None
	com = None
	doc = None
	man = None

	@classmethod
	def toGnuArgs(cls) -> typing.Mapping[str, Path]:
		return {
			"prefix": cls.prefix,
			#"exec_prefix" : cls.prefix,
			"bindir": cls.bin,
			"datarootdir": cls.share,
			"datadir": cls.share,  # datarootdir
			"sharedstatedir": cls.com,
			"includedir": cls.include,
			"infodir": cls.info,
			"libdir": cls.lib,
			"libexecdir": cls.libexec,
			"localedir": cls.locale,
			"localstatedir": cls.var,
			"sbindir": cls.sbin,
			"sysconfdir": cls.etc,
			"mandir": cls.man,
		}


@lru_cache(maxsize=None, typed=True)
def getGNUDirs(prefix: Path, triple: "TargetTriple" = None) -> GNUDirs_:
	pfx = Path(prefix)

	class GNUDirs(GNUDirs_):
		prefix = pfx
		bin = pfx / "bin"
		sbin = pfx / "sbin"
		libexec = pfx / "libexec"
		etc = pfx / "etc"
		var = pfx / "var"
		com = pfx / "com"
		run = var / "run"
		lib = (pfx / "lib") if triple is None else (pfx / "lib" / str(triple))
		include = pfx / "include"
		share = pfx / "share"
		info = share / "info"
		locale = share / "locale"
		doc = share / "doc"
		man = share / "man"

	return GNUDirs
