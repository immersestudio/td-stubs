import typing as _T
from abc import ABC as _ABC

if False:
	from td import *
	import tdu

class COMP(OP):
	extensions: list
	extensionsReady: bool
	clones: _T.List['COMP']
	componentCloneImmune: bool
	vfs: 'VFS'
	dirty: bool
	externalTimeStamp: int
	currentChild: '_AnyOpT'
	selectedChildren: _T.List['_AnyOpT']
	pickable: bool
	isPrivate: bool
	isPrivacyActive: bool
	isPrivacyLicensed: bool
	privacyFirmCode: int
	privacyProductCode: int
	privacyDeveloperName: str
	privacyDeveloperEmail: str
	inputCOMPs: _T.List['_AnyCompT']
	outputCOMPs: _T.List['_AnyCompT']
	inputCOMPConnectors: _T.List['Connector']
	outputCOMPConnectors: _T.List['Connector']


	def destroyCustomPars(self): ...
	def sortCustomPages(self, *pages): ...
	def appendCustomPage(self, name: str) -> 'Page': ...
	# noinspection PyShadowingBuiltins
	def findChildren(
			self,
			type: _T.Type = None,
			path: str = None,
			depth: int = None,
			text: str = None,
			comment: str = None,
			maxDepth: int = 1,
			tags: _T.List[str] = None,
			allTags: _T.List[str] = None,
			parValue: str = None,
			parExpr: str = None,
			parName: str = None,
			onlyNonDefaults: bool = False,
			key: _T.Callable[['_AnyOpT'], bool] = None,
			includeUtility: bool = False,
	) -> '_T.List[_AnyOpT]': ...
	def copy(self, o: '_AnyOpT', name: str = None, includeDocked=True) -> 'op': ...
	def create(self, OPtype: _T.Union[str, _T.Type['_AnyOpT']], name: _T.Optional[str] = None, initialize=True) -> '_AnyOpT': ...
	def collapseSelected(self): ...
	def copyOPs(self, listOfOPs: _T.List['_AnyOpT']) -> _T.List['_AnyOpT']: ...
	def initializeExtensions(self, index: int = None) -> _T.Any: ...
	def loadTox(self, filepath: str, unwired=False, pattern: str = None, password: str = None) -> 'COMP': ...
	def resetNetworkView(self, recurse: bool = False): ...
	def save(self, filepath: str, createFolders: bool = False, password: str = None) -> 'str': ...
	def saveExternalTox(self, recruse: bool = False, password: str = None) -> int: ...
	def accessPrivateContents(self, key: str) -> bool: ...
	@_T.overload
	def addPrivacy(self, key: str, developerName: str = None): ...
	@_T.overload
	def addPrivacy(self, firmCode: int, productCode: int, developerName: str = None, developerEmail: str = None): ...
	def addPrivacy(self, *args, **kwargs): ...
	def blockPrivateContents(self, key: str): ...
	def removePrivacy(self, key: str) -> bool: ...
	def setVar(self, name: str, value): ...
	def unsetVar(self, name: str): ...
	def vars(self, *patterns: str) -> list: ...

class annotateCOMP(COMP):
	enclosedOPs: _T.List['_AnyOpT']
	height: float
	utility: bool
	width: float
	x: float
	y: float

class textCOMP(COMP):
	editText: str
	selectedText: str
	textHeight: float
	textWidth: float

	def evalTextSize(self) -> _T.Tuple[float, float]: ...
	def formatText(self, text: str, editing=False) -> str: ...
	def setCursorPosUV(self, u: float, v: float): ...
	def setKeyboardFocus(self, selectAll=False): ...

class PanelValue(_T.SupportsFloat, _T.SupportsInt, _ABC):
	name: str
	owner: OP
	val: _T.Union[float, int, str]
	valid: bool

class Panel:
	owner: OP

	# Container
	select: PanelValue
	lselect: PanelValue
	mselect: PanelValue
	rselect: PanelValue
	reposition: PanelValue
	resize: PanelValue
	dragout: PanelValue
	ldragout: PanelValue
	mdragout: PanelValue
	rdragout: PanelValue
	ctrl: PanelValue
	alt: PanelValue
	shift: PanelValue
	cmd: PanelValue
	u: PanelValue
	v: PanelValue
	trueu: PanelValue
	truev: PanelValue
	rollu: PanelValue
	rollv: PanelValue
	dragrollu: PanelValue
	dragrollv: PanelValue
	dragrollover: PanelValue
	rollover: PanelValue
	inside: PanelValue
	insideu: PanelValue
	insidev: PanelValue
	radio: PanelValue
	lradio: PanelValue
	mradio: PanelValue
	rradio: PanelValue
	radioname: PanelValue
	lradioname: PanelValue
	mradioname: PanelValue
	rradioname: PanelValue
	children: PanelValue
	display: PanelValue
	enable: PanelValue
	key: PanelValue
	character: PanelValue
	focusselect: PanelValue
	click: PanelValue
	winopen: PanelValue
	wheel: PanelValue
	drag: PanelValue
	drop: PanelValue
	screenw: PanelValue
	screenh: PanelValue
	screenwm: PanelValue
	screenhm: PanelValue
	# Button
	state: PanelValue
	lstate: PanelValue
	mstate: PanelValue
	rstate: PanelValue
	picked: PanelValue
	# Field
	field: PanelValue
	fieldediting: PanelValue
	invalidkey: PanelValue
	focus: PanelValue
	# List
	scrollu: PanelValue
	scrollv: PanelValue
	# Slider
	stateu: PanelValue
	statev: PanelValue
	# Table
	celloverid: PanelValue
	cellfocusid: PanelValue
	cellselectid: PanelValue
	celllselectid: PanelValue
	cellmselectid: PanelValue
	cellrselectid: PanelValue
	cellradioid: PanelValue
	celldragid: PanelValue
	celldropid: PanelValue

class PanelCOMP(COMP):
	panel: Panel
	panelRoot: '_AnyOpT'
	panelChildren: _T.List['_AnyCompT']
	x: int
	y: int
	width: int
	height: int
	marginX: int
	marginY: int
	marginWidth: int
	marginHeight: int

	def panelParent(self, n: int = 1) -> _T.Optional['PanelCOMP']: pass
	def interactMouse(
			self,
			u, v,
			leftClick: int = 0, middleClick: int = 0, rightClick: int = 0,
			left=False, middle=False, right=False,
			wheel: float = 0, pixels=False, screen=False, quiet=True
	) -> 'PanelCOMP':
		pass

	def interactTouch(
			self,
			u, v,
			hover='id', start='id', move='id', end='id',
			pixels=False, screen=False, quiet=True, aux='data') -> 'PanelCOMP':
		pass
	def interactClear(self): pass
	def interactStatus(self) -> _T.List[list]: pass
	def locateMouse(self) -> _T.Tuple[float, float]: pass
	def locateMouseUV(self) -> _T.Tuple[float, float]: pass
	def setFocus(self, moveMouse=False): pass

class fieldCOMP(PanelCOMP):
	def setKeyboardFocus(self, selectAll=False): pass

class buttonCOMP(PanelCOMP):
	def click(self, val, clickCount=1, force=False, left=False, middle=False, right=False): pass

class sliderCOMP(PanelCOMP):
	def click(self, uOrV, v, clickCount=1, force=False, left=False, middle=False, right=False, vOnly=False): pass

class containerCOMP(PanelCOMP):
	def click(self, u, v, clickCount=1, force=False, left=False, middle=False, right=False, group=None): pass
	def clickChild(self, childIndex, clickCount=1, force=False, left=False, middle=False, right=False, group=None): pass
widgetCOMP = containerCOMP

class listCOMP(PanelCOMP):
	attribs: 'ListAttributes'
	cellAttribs: '_ListAttributesGrid'
	colAttribs: '_ListAttributesList'
	focusCol: int
	focusRow: int
	radioCol: int
	radioRow: int
	rolloverCol: int
	rolloverRow: int
	rowAttribs: '_ListAttributesList'
	selectCol: int
	selectRow: int
	selectionBorderColor: 'tdu.Color'
	selectionColor: 'tdu.Color'
	selections: _T.List[_T.Tuple[int, int, int, int]]  # [(startrow, startcol, endrow, endcol), ...]

	def scroll(self, row, col): pass
	def setKeyboardFocus(self, row, col, selectAll=False): pass

class opviewerCOMP(PanelCOMP):
	def isViewable(self, path: str) -> bool: pass

class parameterCOMP(PanelCOMP):
	minWidth: int

class selectCOMP(PanelCOMP):
	pass

# noinspection PyShadowingBuiltins
class tableCOMP(PanelCOMP):
	def getRowFromID(self, id) -> int: pass
	def getColFromID(self, id) -> int: pass
	def click(self, row, col, clickCount=1, force=False, left=False, middle=False, right=False): pass
	def clickID(self, id, clickCount=1, force=False, left=False, middle=False, right=False): pass
	def getCellID(self, row, col) -> int: pass
	def setKeyboardFocus(self, row, col, selectAll=False): pass

class ListAttributes:
	bgColor: 'tdu.Color'
	bottomBorderInColor: 'tdu.Color'
	bottomBorderOutColor: 'tdu.Color'
	colStretch: bool
	colWidth: float
	draggable: bool
	editable: bool
	focus: bool
	fontBold: bool
	fontFace: str
	fontItalic: bool
	fontSizeX: float
	fontSizeY: float
	sizeInPoints: bool
	help: str
	leftBorderInColor: 'tdu.Color'
	leftBorderOutColor: 'tdu.Color'
	radio: bool
	rightBorderInColor: 'tdu.Color'
	rightBorderOutColor: 'tdu.Color'
	rollover: bool
	rowHeight: float
	rowIndent: float
	rowStretch: bool
	select: bool
	text: str
	textColor: 'tdu.Color'
	textJustify: 'JustifyType'
	textOffsetX: float
	textOffsetY: float
	top: 'TOP'

	topBorderInColor: 'tdu.Color'
	topBorderOutColor: 'tdu.Color'
	wordWrap: bool

class ListAttributesList(_T.Sized, _ABC):
	def __getitem__(self, item: int) -> _T.Optional[ListAttributes]:
		pass
class ListAttributesGrid(_T.Sized, _ABC):
	def __getitem__(self, rowCol: _T.Tuple[int, int]) -> _T.Optional[ListAttributes]:
		pass

class windowCOMP(COMP):
	scalingMonitorIndex: int
	isBorders: bool
	isFill: bool
	isOpen: bool
	width: int
	height: int
	x: int
	y: int
	contentX: int
	contentY: int
	contentWidth: int
	contentHeight: int

	def setForeground(self) -> bool: pass

class timeCOMP(COMP):
	frame: float
	seconds: float
	rate: float
	play: bool
	timecode: str
	start: float
	end: float
	rangeStart: float
	rangeEnd: float
	loop: bool
	independent: bool
	tempo: float
	signature1: int
	signature2: int

class Body:
	index: int
	owner: OP
	rotate: 'tdu.Vector'
	translate: 'tdu.Position'
	angularVelocity: 'tdu.Vector'
	linearVelocity: 'tdu.Vector'

	def applyImpulseForce(self, force, relPos: '_T.Union[tdu.Position, tdu.Vector, _T.Tuple[float, float, float]]' = None): ...
	def applyTorque(self, torque): ...
	def applyImpulseTorque(self, torque): ...
	def applyForce(self, force, relPos: '_T.Union[tdu.Position, tdu.Vector, _T.Tuple[float, float, float]]' = None): ...

class Bodies(_T.List[Body]):
	...

class actorCOMP(COMP):
	bodies: Bodies

class Actors(_T.List[actorCOMP]):
	...

class bulletsolverCOMP(COMP):
	actors: Actors

class baseCOMP(COMP):
	pass

class animationCOMP(COMP):
	def setKeyframe(self, position, channel='*', value=None, function=None): ...
	def deleteKeyframe(self, position, channel='*', value=None, function=None): ...


AnyPanelCompT = _T.Union[
	PanelCOMP, fieldCOMP, buttonCOMP, sliderCOMP, containerCOMP, widgetCOMP, listCOMP,
	opviewerCOMP, parameterCOMP, selectCOMP, tableCOMP]

AnyCompT = _T.Union[
	COMP, AnyPanelCompT,
	timeCOMP, windowCOMP, textCOMP, annotateCOMP, animationCOMP,
	bulletsolverCOMP, actorCOMP
]
