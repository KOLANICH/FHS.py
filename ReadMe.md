FHS.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
======
[![GitLab Build Status](https://gitlab.com/KOLANICH/FHS.py/badges/master/pipeline.svg)](https://gitlab.com/KOLANICH/FHS.py/pipelines/master/latest)
![GitLab Coverage](https://gitlab.com/KOLANICH/FHS.py/badges/master/coverage.svg)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/FHS.py.svg)](https://libraries.io/github/KOLANICH/FHS.py)

Just stores some dirs
* from [Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/fhs.shtml)
* some not so standardized but commonly used too;
* allows you to generate a set of [GNU Dirs](https://www.gnu.org/prep/standards/html_node/Directory-Variables.html) given the prefix and ABI Triple.


Allows you to select the standardized dirs with just dot notation. IPython auto-completion is supported.


Requirements
------------
* [`Python >=3.4`](https://www.python.org/downloads/). [`Python 2` is dead, stop raping its corpse.](https://python3statement.org/) Use `2to3` with manual postprocessing to migrate incompatible code to `3`. It shouldn't take so much time. For unit-testing you need Python 3.6+ or PyPy3 because their `dict` is ordered and deterministic. Python 3 is also semi-dead, 3.7 is the last minor release in 3.
