# SchemdrawDIN
Provide element styles of _Deutsches Institut für Normung_ for [schemdraw](https://pypi.org/project/schemdraw/).

## Description

[Schemdraw](https://pypi.org/project/schemdraw/) is a Python library, which provides an easy-to-use interface to draw schematics with. Thanks a lot to Collin J. Delker for such an amazing library. The source code is available at [bitbucket](https://bitbucket.org/cdelker/schemdraw/).

## Installation

## Usage

````python
import schemdraw
import schemdraw.elements as elm
from SchemdrawDIN.style import STYLE_DIN

elm.style(STYLE_DIN)
````