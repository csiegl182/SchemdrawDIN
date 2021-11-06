import schemdraw
from .elements import InductorDIN
from .elements import SourceUDIN

STYLE_DIN = schemdraw.elements.STYLE_IEC.copy()
STYLE_DIN.update({
    'Inductor': InductorDIN,
    'SourceV': SourceUDIN,
    })

#schemdraw.elements.style(STYLE_DIN)