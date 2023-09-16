import typing as _T
import numpy

if False:
	from td import *

class TOP(OP):
	width: int
	height: int
	aspect: float
	aspectWidth: float
	aspectHeight: float
	depth: int
	gpuMemory: int
	curPass: int

	def sample(self, x: int = None, y: int = None, u: float = None, v: float = None) -> _Color: ...
	def numpyArray(self, delayed=False, writable=False, neverNone=False) -> 'numpy.array': ...
	def save(self, filepath, asynchronous=False, createFolders=False) -> 'str': ...
	def saveByteArray(self, filetype) -> bytearray: ...
	def cudaMemory(self) -> 'CUDAMemory': ...

class CUDAMemory:
	ptr: _T.Any
	size: int
	shape: 'CUDAMemoryShape'

class CUDAMemoryShape:
	width: int
	height: int
	numComps: int
	dataType: _T.Any  # numpy data type e.g. numpy.uint8, numpy.float32

class glslTOP(TOP):
	compileResult: str

class glslmultiTOP(glslTOP):
	...

class webrenderTOP(TOP):
	def sendKey(self, char: _T.Union[str, int], shift=False, alt=False, ctrl=False, cmd=False): ...
	def interactMouse(
			self,
			u: float, v: float,
			leftClick=0, middleClick=0, rightClick=0,
			left=False, middle=False, right=False,
			wheel=0,
			pixels=False,
			aux=None,
	):
		"""
		:param u: pos
		:param v:
		:param leftClick: number of left clicks
		:param middleClick: number of middle clicks
		:param rightClick: number of right clicks
		:param left: left button state
		:param middle: middle button state
		:param right: right button state
		:param wheel: mouse wheel
		:param pixels: treat coords as pixel offsets instead of normalized
		:param aux: auxilliary data
		:return:
		"""
		...
	def executeJavaScript(self, script: str): ...
	def sendString(self, char: str): ...

class textTOP(TOP):
	curText: str
	cursorEnd: int
	cursorStart: int
	selectedText: str
	textHeight: int
	textWidth: int
	numLines: int
	ascender: float
	descender: float
	capHeight: float
	xHeight: float
	lineGap: float

	def fontSupportsCharts(self, s: str) -> bool: ...
	def evalTextSize(self, s: str) -> _T.Tuple[float, float]: ...
	def lines(self) -> _T.List['TextLine']: ...

class scriptTOP(TOP):
	def copyNumpyArray(self, arr: numpy.array) -> None: ...
	def copyCUDAMemory(self, address, size, shape: CUDAMemoryShape) -> None: ...
	def loadByteArray(self, fileType: str, byteArray: _T.Union[bytes, bytearray]) -> bool: ...
	def destroyCustomPars(self): ...
	def sortCustomPages(self, *pages): ...
	def appendCustomPage(self, name: str) -> 'Page': ...

AnyTopT = _T.Union[TOP, textTOP, scriptTOP, glslTOP, glslmultiTOP, webrenderTOP]
