from pathlib import Path


class StandardizedDirProtoMeta(type):
	def __new__(cls, className, parents, attrs, *args, **kwargs):
		attrsNew = type(attrs)()
		for k, v in attrs.items():
			if k[0] == "_":
				continue

			if isinstance(v, str):
				attrsNew[k] = v
			elif v is None:
				attrsNew[k] = k
			elif issubclass(v, StandardizedDirProto):
				attrsNew[k] = v
		return super().__new__(cls, className, parents, {"delayed": attrsNew}, *args, **kwargs)


class StandardizedDirProto(metaclass=StandardizedDirProtoMeta):
	pass


class StandardizedDirMeta(type):
	def __new__(cls, className, parents, attrs, *args, **kwargs):
		if "ROOT" in attrs:
			attrsNew = type(attrs)()
			root = attrs["ROOT"]
			attrsNew["__slots__"] = ()
			attrsNew["__root__"] = root
			attrsNew["__fspath__"] = attrsNew["__str__"] = lambda self: str(self.__root__)
			attrsNew["__truediv__"] = lambda self, other: self.__root__ / other
			attrsNew["__repr__"] = lambda self: repr(self.__root__)
			attrsNew["__eq__"] = lambda self, other: self.__root__ == other
			attrsNew["__ne__"] = lambda self, other: self.__root__ != other
			attrsNew["__hash__"] = lambda self: hash(self.__root__)

			attrs = type(attrs)(attrs)
			del attrs["ROOT"]

			delayedAssignRoot = []
			for k, v in attrs.items():
				if k[0] == "_":
					continue

				if isinstance(v, str):
					attrsNew[k] = root / v
				elif v is None:
					attrsNew[k] = root / k
				elif isinstance(v, type) and issubclass(v, StandardizedDirProto):
					v.delayed["ROOT"] = root / v.__name__
					attrsNew[k] = cls(v.__class__.__name__, parents, v.delayed, *args, **kwargs)

			res = super().__new__(cls, className, parents, attrsNew, *args, **kwargs)()
			return res
		else:
			return super().__new__(cls, className, parents, attrs, *args, **kwargs)


class StandardizedDir(metaclass=StandardizedDirMeta):
	def __getattr__(self, k):
		return getattr(self.__root__, k)


class FHS(StandardizedDir):
	ROOT = Path("/")

	boot = "boot"
	dev = "dev"

	class etc(StandardizedDirProto):
		sgml = "sgml"
		X11 = "X11"
		xml = "xml"
		opt = "opt"

	home = "home"
	media = "media"
	mnt = "mnt"

	opt = "opt"
	proc = "proc"
	root = "root"
	run = "run"
	srv = "srv"
	sys = "sys"
	tmp = "tmp"

	bin = "bin"
	lib = "lib"
	lib32 = "lib32"
	lib64 = "lib64"

	class usr(StandardizedDirProto):
		bin = "bin"
		lib = "lib"
		libexec = "libexec"
		lib32 = "lib32"
		lib64 = "lib64"
		sbin = "sbin"

		include = "include"
		src = "src"
		X11R6 = "X11R6"

		class share(StandardizedDirProto):
			man = "man"

			class misc(StandardizedDirProto):
				ascii = "ascii"
				termcap = "termcap"
				termcapDB = "termcap.db"

			class color(StandardizedDirProto):
				icc = "icc"

			class dict(StandardizedDirProto):
				words = "words"

			doc = "doc"
			games = "games"
			info = "info"
			locale = "locale"
			nls = "nls"
			ppd = "ppd"

			class sgml(StandardizedDirProto):
				docbook = "docbook"
				tei = "tei"
				html = "html"
				mathml = "mathml"

			class xml(StandardizedDirProto):
				docbook = "docbook"
				xhtml = "xhtml"
				mathml = "mathml"

			terminfo = "terminfo"
			tmactroff = "tmactroff"
			zoneinfo = "zoneinfo"

		class local(StandardizedDirProto):
			bin = "bin"
			etc = "etc"
			games = "games"
			include = "include"
			lib = "lib"
			libexec = "libexec"
			man = "man"
			sbin = "sbin"
			share = "share"
			src = "src"

	class var(StandardizedDirProto):
		class cache(StandardizedDirProto):
			fonts = "fonts"
			man = "man"
			www = "www"

		class lib(StandardizedDirProto):
			misc = "misc"
			color = "color"
			hwclock = "hwclock"
			xdm = "xdm"

		lock = "lock"

		class log(StandardizedDirProto):
			last = "last"
			messages = "messages"
			wtmp = "wtmp"

		mail = "mail"
		opt = "opt"

		class spool(StandardizedDirProto):
			mail = "mail"

			class lpd(StandardizedDirProto):
				printer = "printer"

			mqueue = "mqueue"
			news = "news"
			rwho = "rwho"
			uucp = "uucp"

		account = "account"
		crash = "crash"
		games = "games"
		mail = "mail"
		yp = "yp"


class Common:
	OpenCL = FHS.etc / "OpenCL"
	OpenCLVendors = OpenCL / "vendors"
	applications = FHS.usr.share / "applications"
	icons = FHS.usr.share / "icons"
	pkgConfig = FHS.usr.lib / "pkgconfig"
	aclocal = FHS.usr.share / "aclocal"
	mime = FHS.usr.share / "mime"
	systemdDir = FHS.usr / "systemd"
	systemdUnitsDir = systemdDir / "system"
