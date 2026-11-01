# Portfolio fonts

Archivo is licensed under the included `archivo-OFL.txt`. Its WOFF2 retains all original characters and the variable weight axis. The unused width axis is pinned to its default (100), reducing the file from 189,340 to 73,456 bytes without changing the site's normal-width typography.

For a fresh upstream font, reproduce with FontTools:

```python
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
font = TTFont('upstream-archivo-variable.woff2')
font = instantiateVariableFont(font, {'wdth': 100}, inplace=True)
font.save('static/fonts/archivo-variable.woff2')
```

Do not subset characters without considering the writing archive. Other fonts and their licenses remain unchanged.
