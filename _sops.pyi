import typing as _T

if False:
	from td import *
	import tdu



_AttributeDataElementT = _T.Union[float, int, str]
_AttributeDataTupleT = _T.Union[
	_T.Tuple[_AttributeDataElementT],
	_T.Tuple[_AttributeDataElementT, _AttributeDataElementT],
	_T.Tuple[_AttributeDataElementT, _AttributeDataElementT, _AttributeDataElementT],
	_T.Tuple[_AttributeDataElementT, _AttributeDataElementT, _AttributeDataElementT, _AttributeDataElementT],
]
_AttributeDataT = _T.Union[
	_AttributeDataElementT,
	_AttributeDataTupleT,
	'tdu.Vector',
	'tdu.Position'
]

class Attribute:
	owner: 'SOP'
	name: str
	size: int
	type: type
	default: _AttributeDataT

	def destroy(self): ...

class Attributes(_T.Collection[Attribute], _ABC):
	owner: 'SOP'

	def create(self, name: str, default: _AttributeDataT = None) -> Attribute: ...

class AttributeData(_AttributeDataTupleT):
	owner: 'SOP'
	val: _AttributeDataT

class Point:
	index: int
	owner: 'SOP'
	P: 'AttributeData'
	x: float
	y: float
	z: float

	def __getattr__(self, item) -> _T.Any: ...
	def __setattr__(self, key, value): ...
	def destroy(self): ...

class Points(_T.Sequence[Point], _ABC):
	owner: 'SOP'

class Vertex(_T.Any):
	index: int
	owner: 'SOP'
	point: Point
	prim: 'Prim'

class Prim(_T.Sized, _T.Sequence[Vertex], _T.Any, _ABC):
	center: 'tdu.Position'
	index: int
	normal: 'tdu.Vector'
	owner: 'SOP'
	weight: float
	direction: 'tdu.Vector'
	min: 'tdu.Position'
	max: 'tdu.Position'
	size: 'tdu.Position'

	def destroy(self, destroyPoints=True): ...
	def eval(self, u: float, v: float) -> 'tdu.Position': ...

	def __getitem__(self, item: _T.Union[int, _T.Tuple[int, int]]) -> Vertex: ...

class Poly(Prim, _ABC):
	...

class Bezier(Prim, _ABC):
	anchors: _T.List[Vertex]
	basis: _T.List[float]
	closed: bool
	order: float
	segments: _T.List[_T.List[Vertex]]
	tangents: _T.List[_T.Tuple[Vertex, Vertex]]

	def insertAnchor(self, u: float) -> Vertex: ...
	def updateAnchor(self, anchorIndex: int, targetPosition: 'tdu.Position', tangents=True) -> 'tdu.Position': ...
	def appendAnchor(self, targetPosition: 'tdu.Position', preserveShape=True) -> Vertex: ...
	def updateTangent(
			self, tangentIndex: int, targetPosition: 'tdu.Position',
			rotate=True, scale=True, rotateLock=True, scaleLock=True) -> 'tdu.Position': ...
	def deleteAnchor(self, anchorIndex: int): ...

class Mesh(Prim, _ABC):
	closedU: bool
	closedV: bool
	numRows: int
	numCols: int

_AnyPrimT = _T.Union[Prim, Poly, Bezier, Mesh]

class Prims(_T.Sequence[_AnyPrimT], _ABC):
	owner: 'SOP'

class Group(_T.Union[_T.Iterable[Point], _T.Iterable[_AnyPrimT]]):
	# default - tuple "the default values associated with this group" ?
	name: str
	owner: OP

	def add(self, item: _T.Union[Point, Prim]): ...
	def discard(self, item: _T.Union[Point, Prim]): ...
	def destroy(self): ...

class SOP(OP):
	compare: bool
	template: bool
	points: Points
	prims: Prims
	numPoints: int
	numPrims: int
	numVertices: int
	pointAttribs: Attributes
	primAttribs: Attributes
	vertexAttribs: Attributes
	pointGroups: _T.Dict[str, Group]
	primGroups: _T.Dict[str, Group]
	center: 'tdu.Position'
	min: 'tdu.Position'
	max: 'tdu.Position'
	size: 'tdu.Position'

	def save(self, filepath: str, createFolders=False) -> str: ...

class scriptSOP(SOP):
	def destroyCustomPars(self): ...
	def sortCustomPages(self, *pages): ...
	def appendCustomPage(self, name: str) -> 'Page': ...
	def clear(self): ...
	# noinspection PyMethodOverriding
	def copy(self, sop: 'SOP'): ...
	def appendPoint(self) -> Point: ...
	def appendPoly(self, numVertices: int, closed=True, addPoints=True) -> Poly: ...
	def appendBezier(self, numVertices: int, closed=True, order=4, addPoints=True) -> Bezier: ...
	def appendMesh(self, numROws: int, numCols: int, closedU=False, closedV=False, addPoints=True) -> Mesh: ...


class textSOP(SOP):
	numLines: int
	ascender: float
	descender: float
	capHeight: float
	xHeight: float
	lineGap: float
	numGlyphs: int

	def fontSupportsCharts(self, s: str) -> bool: ...
	def lines(self) -> _T.List['TextLine']: ...

AnySopT = _T.Union[SOP, scriptSOP, textSOP]
