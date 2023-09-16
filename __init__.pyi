import enum as _E
import typing as _T



class JustifyType(_E.Enum):
	TOPLEFT = 0
	TOPCENTER = 0
	TOPRIGHT = 0
	CENTERLEFT = 0
	CENTER = 0
	CENTERRIGHT = 0
	BOTTOMLEFT = 0
	BOTTOMCENTER = 0
	BOTTOMRIGHT = 0

class ParMode(_E.Enum):
	CONSTANT = 0
	EXPRESSION = 1
	EXPORT = 2
	BIND = 3
