import datetime as _DT
import enum as _E
import typing as _T
import numpy

if False:
	from . import *
	import tdu

class _Expando:
	def __getattr__(self, item) -> _T.Any: ...

class MOD:
	def __call__(self, *args, **kwargs): ...
	def __getattr__(self, item) -> _T.Any: ...


ext: _Expando

class PaneType(_E.Enum):
	NETWORKEDITOR = 0
	PANEL = 0
	GEOMETRYVIEWER = 0
	TOPVIEWER = 0
	CHOPVIEWER = 0
	ANIMATIONEDITOR = 0
	PARAMETERS = 0
	TEXTPORT = 0

class UI:
	clipboard: str
	colors: 'Colors'
	dpiBiCubicFilter: bool
	masterVolume: float
	options: 'Options'
	panes: 'Panes'
	performMode: bool
	preferences: 'Preferences'
	redrawMainWindow: bool
	rolloverOp: 'OP'
	rolloverPar: 'Par'
	lastChopChannelSelected: 'Par'
	showPaletteBrowser: bool
	status: str
	undo: 'Undo'
	windowWidth: int
	windowHeight: int
	windowX: int
	windowY: int

	def copyOPs(self, listOfOPs: _T.List['_AnyOpT']): ...
	# noinspection PyShadowingNames
	def pasteOPs(self, comp: 'COMP', x: _T.Optional[int] = None, y: _T.Optional[int] = None): ...
	# noinspection PyDefaultArgument
	def messageBox(self, title: str, message: str, buttons: _T.List[str] = ['Ok']) -> int: ...
	def refresh(self): ...
	def chooseFile(self, load=True, start=None, fileTypes=None, title=None, asExpression=False) -> _T.Optional[str]: ...
	def chooseFolder(self, title='Select Folder', start=None, asExpression=False) -> _T.Optional[str]: ...
	def viewFile(self, url_or_path: str): ...
	def openAbletonControl(self): ...
	def openBeat(self): ...
	def openBookmarks(self): ...
	def openCOMPEditor(self, path): ...
	def openConsole(self): ...
	def openDialogHelp(self, title): ...
	def openErrors(self): ...
	def openExplorer(self): ...
	def openExportMovie(self, path=""): ...
	def openHelp(self): ...
	def openImportFile(self): ...
	def openKeyManager(self): ...
	def openMIDIDeviceMapper(self): ...
	def openNewProject(self): ...
	# noinspection PyShadowingBuiltins
	def openOperatorSnippets(self, family=None, type=None, example=None): ...
	def openPaletteBrowser(self): ...
	def openPerformanceMonitor(self): ...
	def openPreferences(self): ...
	def openSearch(self): ...
	def openTextport(self): ...
	def openVersion(self): ...
	def openWindowPlacement(self): ...
	def findEditDAT(self, filename: str) -> _T.Optional['DAT']: ...

	status: str

class Preferences(_T.Mapping[str, _T.Any]):
	defaults: _T.Dict[str, _T.Any]

	def save(self): ...
	def resetToDefaults(self): ...
	def load(self): ...

class Options(_T.Mapping[str, _T.Any]):
	def resetToDefaults(self): ...

_RgbTupletT = _T.Tuple[float, float, float]

class Colors(_T.Mapping[str, _RgbTupletT]):
	def resetToDefaults(self): ...

class Panes(_T.Iterable['_AnyPaneT'], _T.Iterator['_AnyPaneT'], _T.Sized):
	def __getitem__(self, key: _T.Union[int, str]) -> '_AnyPaneT': ...
	# noinspection PyShadowingBuiltins
	def createFloating(
			self,
			type=PaneType.NETWORKEDITOR,
			name=None,
			maxWidth=1920, maxHeight=1080,
			monitorSpanWidth=0.9, monitorSpanHeight=0.9,
	) -> 'Pane': ...

	current: '_AnyPaneT'

class Coords(_T.NamedTuple):
	x: int
	y: int
	u: float
	v: float

class Pane:
	def changeType(self, paneType: 'PaneType') -> '_AnyPaneT': ...
	def close(self): ...
	def floatingCopy(self) -> '_AnyPaneT': ...
	def splitBottom(self) -> '_AnyPaneT': ...
	def splitLeft(self) -> '_AnyPaneT': ...
	def splitRight(self) -> '_AnyPaneT': ...
	def splitTop(self) -> '_AnyPaneT': ...
	def tearAway(self) -> bool: ...

	bottomLeft: 'Coords'
	id: int
	link: int
	maximize: bool
	name: str
	owner: 'COMP'
	ratio: float
	topRight: 'Coords'
	type: 'PaneType'

class NetworkEditor(Pane):
	showBackdropCHOPs: bool
	showBackdropGeometry: bool
	showBackdropTOPs: bool
	showColorPalette: bool
	showDataLinks: bool
	showList: bool
	showNetworkOverview: bool
	showParameters: bool
	straightLinks: bool
	x: float
	y: float
	zoom: float

	def fitWidth(self, width) -> None: ...

	def fitHeight(self, height) -> None: ...

	# noinspection PyShadowingNames
	def home(self, zoom=True, op=None) -> None: ...

	def homeSelected(self, zoom=True) -> None: ...

	def placeOPs(self, listOfOPs, inputIndex=None, outputIndex=None, delOP=None, undoName='Operators') -> None: ...

_AnyPaneT = _T.Union['Pane', 'NetworkEditor']

class Undo:
	globalState: bool
	redoStack: list
	state: bool
	undoStack: list

	def startBlock(self, name, enable=True): ...
	def clear(self): ...
	def addCallback(self, callback: _T.Callable[[bool, _T.Any], None], info=None): ...
	def redo(self): ...
	def undo(self): ...
	def endBlock(self): ...

class WindowStartMode(_E.Enum):
	DEFAULT = 'DEFAULT'
	FULL = 'FULL'
	LEFT = 'LEFT'
	RIGHT = 'RIGHT'
	CUSTOM = 'CUSTOM'

class Project:
	name: str
	folder: str
	saveVersion: str
	saveBuild: str
	saveTime: str
	saveOsName: str
	saveOsVersion: str
	paths: _T.Dict[str, str]
	cookRate: float
	realTime: bool
	isPrivate: bool
	isPrivateKey: bool
	# cacheParameters: bool
	externalToxModifiedInProject: bool
	externalToxModifiedOnDisk: bool
	windowOnTop: bool
	windowStartMode: WindowStartMode
	windowDraw: bool
	windowStartCustomWidth: int
	windowStartCustomHeight: int
	windowStartCustomX: int
	windowStartCustomY: int
	performOnStart: bool
	performWindowPath: 'OP'

	def load(self, path: str) -> None: ...
	def save(self, path: str, saveExternalToxs=False) -> bool: ...
	def quit(self, force=False, crash=False) -> None: ...
	def addPrivacy(self, key) -> bool: ...
	def removePrivacy(self, key) -> bool: ...
	def accessPrivateContents(self, key) -> bool: ...
	def applyWindowSettings(self) -> None: ...
	def stack(self) -> str: ...
	def pythonStack(self) -> str: ...

class Monitor:
	index: int
	isPrimary = False
	isAffinity = False
	width: int
	height: int
	left: int
	right: int
	top: int
	bottom: int
	displayName: str
	description: str
	dpiScale: float
	scaledWidth: int
	scaledHeight: int
	scaledLeft: int
	scaledRight: int
	scaledTop: int
	scaledBottom: int
	refreshRate: float

class Monitors(_T.Sequence[Monitor]):
	primary: Monitor
	width: 0
	height: 0
	left: 0
	right: 0
	top: 0
	bottom: 0

	@staticmethod
	def locate(x, y) -> Monitor: ...

	@staticmethod
	def refresh(): ...

class SysInfo:
	numCPUs: int
	ram: float
	numMonitors: int
	xres: int
	yres: int
	tfs: str

class _Parent:
	def __call__(self, *args, **kwargs) -> '_AnyOpT': ...
	def __getattr__(self, item) -> '_AnyOpT': ...

parent: _Parent

_ValueT = _T.Union[float, int, str]

class Par:
	valid: bool
	val: _ValueT
	expr: str
	exportOP: _T.Optional['OP']
	exportSource: _T.Optional[_T.Union['Cell', 'Channel']]
	bindExpr: str
	bindMaster: _T.Optional[_T.Union['Channel', 'Cell', 'Par']]
	bindRange: bool
	bindReferences: list
	index: int
	vecIndex: int
	name: str
	label: str
	subLabel: str

	startSection: bool
	readOnly: bool
	displayOnly: bool
	tuplet: 'ParTupletT'
	tupletName: str
	min: _ValueT
	max: _ValueT
	clampMin: bool
	clampMax: bool
	default: _ValueT
	defaultExpr: str
	normMin: float
	normMax: float
	normVal: float
	enable: bool
	enableExpr: str
	order: int
	page: 'Page'
	password: bool
	help: str

	mode: 'ParMode'
	prevMode: 'ParMode'
	menuNames: _T.List[str]
	menuLabels: _T.List[str]
	menuIndex: int
	menuSource: str
	owner: '_AnyOpT'
	styleCloneImmune: bool
	lastScriptChange: _T.Optional['SetInfo']

	collapser: bool
	collapsable: bool
	sequence: _T.Set

	isDefault: bool
	isCustom: bool
	isPulse: bool
	isMomentary: bool
	isMenu: bool
	isNumber: bool
	isFloat: bool
	isInt: bool
	isOP: bool
	isPython: bool
	isString: bool
	isToggle: bool
	style: str

	collapser: bool
	collapsable: bool
	sequence: None

	def copy(self, par: 'Par') -> None: ...
	def eval(self) -> _T.Union[_ValueT, '_AnyOpT']: ...
	def evalNorm(self) -> _ValueT: ...
	def evalExpression(self) -> _ValueT: ...
	def evalExport(self) -> _ValueT: ...
	def evalOPs(self) -> '_T.List[_AnyOpT]': ...
	def pulse(self, value=None, frames=0, seconds=0) -> None: ...
	def destroy(self) -> None: ...

	def __int__(self) -> int: ...
	def __float__(self) -> float: ...
	def __str__(self) -> str: ...

class ParGroup(tuple):
	bindExpr: tuple
	bindMaster: tuple
	bindRange: bool
	bindReferences: _T.List[tuple]
	clampMin: tuple
	clampMax: tuple
	collapser: bool
	collapsable: bool
	default: tuple
	defaultExpr: tuple

class SetInfo(tuple):
	dat: _T.Optional['DAT']
	path: str
	function: _T.Optional[str]
	line: _T.Optional[int]
	frame: int
	timeStamp: int

class Sequence:
	owner: 'OP'
	numBlocks: int
	maxBlocks: int
	blocks: _T.List['ParTupletT']

ParTupletT = _T.Union[
	_T.Tuple['Par'], _T.Tuple['Par', 'Par'], _T.Tuple['Par', 'Par', 'Par'], _T.Tuple['Par', 'Par', 'Par', 'Par']]

class ParTuple(ParTupletT):
	bindRange: bool
	collapsable: bool
	collapser: bool
	enable: bool
	enableExpr: str
	help: str
	label: str
	name: str
	order: int
	page: 'Page'
	password: bool
	readOnly: bool
	sequence: '_T.Optional[set]'
	startSection: bool
	style: str
	valid: bool
	index: int

	isDefault: bool
	isCustom: bool
	isPulse: bool
	isMomentary: bool
	isMenu: bool
	isNumber: bool
	isFloat: bool
	isInt: bool
	isOP: bool
	isPython: bool
	isString: bool
	isToggle: bool

	def copy(self, parTuple: 'ParTuple') -> None: ...
	def destroy(self) -> None: ...
	def eval(self) -> _T.Any: ...

class ParCollection:
	owner: 'OP'

	def __getattr__(self, item) -> Par: ...
	def __setattr__(self, key, value: _T.Any): ...
	def __getitem__(self, item) -> Par: ...
	def __setitem__(self, key, value: _T.Any): ...

class ParTupleCollection:
	owner: 'OP'

	def __getattr__(self, item) -> ParTuple: ...
	def __setattr__(self, key, value: _T.Any): ...
	def __getitem__(self, item) -> ParTuple: ...
	def __setitem__(self, key, value: _T.Any): ...

class ParGroupCollection:
	owner: 'OP'

	def __getattr__(self, item) -> ParGroup: ...
	def __setattr__(self, key, value: _T.Any): ...
	def __getitem__(self, item) -> ParGroup: ...
	def __setitem__(self, key, value: _T.Any): ...

class Page:
	name: str
	owner: 'OP'
	parTuplets: _T.List[ParTupletT]
	parGroups: _T.List[ParGroup]
	pars: _T.List['Par']
	index: int
	isCustom: bool

	def appendInt(self, name, label=None, size=1, order=None, replace=True) -> ParGroup: ...
	def appendFloat(self, name, label=None, size=1, order=None, replace=True) -> ParGroup: ...

	def appendOP(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendCHOP(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendDAT(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendMAT(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendTOP(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendSOP(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendCOMP(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendOBJ(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendPanelCOMP(self, name, label=None, order=None, replace=True) -> ParGroup: ...

	def appendMenu(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendStr(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendStrMenu(self, name, label=None, order=None, replace=True) -> ParGroup: ...

	def appendWH(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendRGBA(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendRGB(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendXY(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendXYZ(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendUV(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendUVW(self, name, label=None, order=None, replace=True) -> ParGroup: ...

	def appendToggle(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendPython(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendFile(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendFolder(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendPulse(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendMomentary(self, name, label=None, order=None, replace=True) -> ParGroup: ...
	def appendHeader(self, name, label=None, order=None, replace=True) -> ParGroup: ...

	def appendPar(self, name: str, par: 'Par' = None, label=None, order=None, replace=True) -> ParGroup: ...

	def sort(self, *parameters: str): ...
	def destroy(self): ...

class OP:
	valid: bool
	id: int
	name: str
	path: str
	digits: int
	base: str
	passive: bool
	curPar: 'Par'
	time: 'timeCOMP'
	ext: _T.Any
	mod: _T.Any
	par: ParCollection
	parTuple: ParTupleCollection
	parGroup: ParGroupCollection
	pages: _T.List['Page']
	customParGroups: _T.List['ParGroup']
	customPars: _T.List['Par']
	customPages: _T.List['Page']
	customTuplets: _T.List[ParTupletT]
	builtinPars: _T.List['Par']
	replicator: _T.Optional['OP']
	storage: _T.Dict[str, _T.Any]
	tags: _T.Set[str]
	children: _T.List['_AnyOpT']
	numChildren: int
	numChildrenRecursive: int
	parent: '_Parent'
	iop: _T.Any
	ipar: _T.Any
	currentPage: 'Page'

	activeViewer: bool
	allowCooking: bool
	bypass: bool
	cloneImmune: bool
	current: bool
	display: bool
	expose: bool
	lock: bool
	selected: bool
	python: bool
	render: bool
	showCustomOnly: bool
	showDocked: bool
	viewer: bool

	color: _T.Tuple[float, float, float]
	comment: str
	nodeHeight: int
	nodeWidth: int
	nodeX: int
	nodeY: int
	nodeCenterX: int
	nodeCenterY: int
	dock: 'OP'
	docked: _T.List['_AnyOpT']

	inputs: _T.List['_AnyOpT']
	outputs: _T.List['_AnyOpT']
	inputConnectors: _T.List['Connector']
	outputConnectors: _T.List['Connector']

	cookFrame: float
	cookTime: float
	cpuCookTime: float
	cookAbsFrame: float
	cookStartTime: float
	cookEndTime: float
	cookedThisFrame: bool
	cookedPreviousFrame: bool
	childrenCookTime: float
	childrenCPUCookTime: float
	childrenCookAbsFrame: float
	childrenCPUCookAbsFrame: float
	gpuCookTime: float
	childrenGPUCookTime: float
	childrenGPUCookAbsFrame: float
	totalCooks: int
	cpuMemory: int
	gpuMemory: int

	type: str
	subType: str
	OPType: str
	label: str
	icon: str
	family: str
	isFilter: bool
	minInputs: int
	maxInputs: int
	isMultiInputs: bool
	visibleLevel: int
	isBase: bool
	isCHOP: bool
	isCOMP: bool
	isDAT: bool
	isMAT: bool
	isObject: bool
	isPanel: bool
	isSOP: bool
	isTOP: bool
	licenseType: str

	def __init__(self): ...

	def destroy(self): ...

	def op(self, path) -> '_AnyOpT': ...
	def ops(self, *args) -> _T.List['_AnyOpT']: ...
	def shortcutPath(self, o: '_AnyOpT', toParName=None) -> str: ...
	def relativePath(self, o: '_AnyOpT') -> str: ...
	def openMenu(self, x=None, y=None): ...
	def var(self, name, search=True) -> str: ...
	def evalExpression(self, expr) -> _T.Any: ...
	def dependenciesTo(self, o: '_AnyOpT') -> _T.List['_AnyOpT']: ...
	def changeType(self, optype: _T.Type) -> '_AnyOpT': ...
	def copyParameters(self, o: '_AnyOpT', custom=True, builtin=True): ...
	def cook(self, force=False, recurse=False): ...
	def pars(self, *pattern: str) -> _T.List['Par']: ...

	def openParameters(self): ...
	def openViewer(self, unique=False, borders=True): ...
	def closeViewer(self): ...

	def store(self, key, value): ...
	def unstore(self, keys1, *morekeys): ...
	def storeStartupValue(self, key, value): ...
	def unstoreStartupValue(self, *keys): ...
	def fetch(self, key, default=None, search=True, storeDefault=False): ...
	def fetchOwner(self, key) -> '_AnyOpT': ...

	def addScriptError(self, msg): ...
	def addError(self, msg): ...
	def addWarning(self, msg): ...
	def errors(self, recurse=False) -> str: ...
	def warnings(self, recurse=False) -> str: ...
	def scriptErrors(self, recurse=False) -> str: ...
	def clearScriptErrors(self, recurse=False, error='*'): ...

	TDResources: 'COMP'

iop = _Expando()  # type: _T.Any
ipar = _Expando()  # type: _T.Any


class Run:
	active: bool
	group: str
	isCell: bool
	isDAT: bool
	isString: bool
	path: OP
	remainingFrames: int
	remainingMilliseconds: int
	source: _T.Union['DAT', 'Cell', str]

	def kill(self): ...

class Runs(_T.List[Run]): ...

me: 'OP'
absTime: 'AbsTime'
app: 'App'
ext: _T.Any
families: dict
licenses: 'Licenses'
mod: MOD
monitors: 'Monitors'
op: 'OP'
parent: '_Parent'
iop: 'OP'
ipar: 'OP'
project: 'Project'
root: 'baseCOMP'
runs: Runs
sysinfo: 'SysInfo'
ui: 'UI'


def op(path) -> '_AnyOpT': ...
def ops(*paths) -> _T.List['_AnyOpT']: ...
def isMainThread() -> bool: ...

# clears textport
def clear()-> None: ...
def passive(o: 'OP') -> 'OP': ...
def run(
		script, *args, endFrame=False, fromOP: 'OP' = None, asParameter=False, group=None, delayFrames=0,
		delayMilliSeconds=0, delayRef: 'OP' = None) -> Run: ...
def fetchStamp(key, default) -> _T.Union[_ValueT, str]: ...
def var(name) -> str: ...
def varExists(name: str) -> bool: ...
def varOwner(name: str) -> _T.Optional['_AnyOpT']: ...

def debug(*args): ...

# used for listCOMP callbacks
class XYUVTuple(_T.NamedTuple):
	x: float
	y: float
	u: float
	v: float

from _comps import *
from _chops import *
from _dats import *
from _sops import *
from _tops import *

_AnyOpT = _T.Union[OP, DAT, COMP, CHOP, SOP, TOP, MAT, AnyCompT, AnyDatT]

class VFSFile:
	name: str
	size: int
	date: _DT.datetime
	virtualPath: str
	originalFilePath: str
	owner: OP
	byteArray: bytearray

	def destroy(self): ...
	def export(self, folder: str) -> str: ...

class VFS:
	owner: OP

	def __getitem__(self, item: str) -> VFSFile: ...
	def addByteArray(self, byteArray: bytearray, name: str) -> VFSFile: ...
	def addFile(self, filePath: str, overrideName=None) -> VFSFile: ...
	def export(self, folder: str, pattern='*', overwrite=False) -> _T.List[str]: ...
	def find(self, pattern='*') -> _T.List[VFSFile]: ...

class Connector:
	index: int
	isInput: bool
	isOutput: bool
	inOP: '_AnyOpT'
	outOP: '_AnyOpT'
	owner: '_AnyOpT'
	connections: _T.List['Connector']

	def connect(self, target: _T.Union['_AnyOpT', 'Connector']): ...
	def disconnect(self): ...

class TextLine:
	text: str
	origin: 'tdu.Position'
	lineWidth: float

class MAT(OP):
	...


class App:
	architecture: str
	binFolder: str
	build: str
	compileDate: _T.Tuple[int, int, int]  # year, month, day
	configFolder: str
	desktopFolder: str
	enableOptimizedExprs: bool
	installFolder: str
	launchTime: float  # seconds since launch
	logExtensionCompiles: bool
	osName: str
	osVersion: str
	power: bool
	preferencesFolder: str
	product: str
	recentFiles: _T.List[str]
	samplesFolder: str
	userPaletteFolder: str
	version: str
	windowColorBits: int

	def addNonCommercialLimit(self, password: _T.Optional[str] = None) -> None: ...
	def removeNonCommercialLimit(self, password: _T.Optional[str] = None) -> bool: ...
	def addResolutionLimit(self, x: int, y: int, password: _T.Optional[str] = None) -> None: ...
	def removeResolutionLimit(self, password: _T.Optional[str] = None) -> bool: ...

class Dongle:
	serialNumber: int

	def applyUpdate(self, update: str) -> None: ...
	def createUpdateContext(self) -> str: ...

class DongleList(_T.List[Dongle]):
	def refreshDongles(self) -> None: ...
	def encrypt(self, firmCode, productCode, data: _T.Union[str, bytearray]) -> bytearray: ...
	def productCodeInstalled(self) -> bool: ...

class License:
	index: int
	isEnabled: bool
	isRemotelyDisabled: bool
	key: str
	remoteDisableDate: _T.Tuple[int, int, int]  # year, month, day
	status: int
	statusMessage: str
	systemCode: str
	type: str
	updateExpiryDate: _T.Tuple[int, int, int]  # year, month, day
	version: int

class Licenses(_T.List[License]):
	disablePro: bool
	dongles: DongleList
	machine: str
	systemCode: str
	type: str
	isPro: bool
	isNonCommercial: bool

	def install(self, key: str) -> bool: ...

class Bounds(_T.NamedTuple):
	min: _T.Any
	max: _T.Any
	center: _T.Any
	size: _T.Any

class ArtNetDevice(_T.NamedTuple):
	ip: bytes
	port: int
	version: int
	netswitch: int
	subswitch: int
	oem: int
	ubea: int
	status1: int
	estacode: int
	shortname: int
	longname: int
	report: int
	numports: int
	porttypes: bytes
	goodinputs: bytes
	goodoutputs: bytes
	swin: bytes
	swout: bytes
	swvideo: int
	swmacro: int
	swremote: int
	style: int
	mac: bytes
	bindip: bytes
	bindindex: int
	status2: int

class EtherDreamDevice(_T.NamedTuple):
	ip: _T.Any
	port: _T.Any
	mac_address: _T.Any
	hw_revision: _T.Any
	sw_revision: _T.Any
	buffer_capacity: _T.Any
	max_point_rate: _T.Any
	protocol: _T.Any
	light_engine_state: _T.Any
	playback_state: _T.Any
	source: _T.Any
	light_engine_flags: _T.Any
	playback_flags: _T.Any
	source_flags: _T.Any
	buffer_fullness: _T.Any
	point_rate: _T.Any
	point_count: _T.Any

class NDISource(_T.NamedTuple):
	sourceName: _T.Any
	url: _T.Any
	streaming: _T.Any
	width: _T.Any
	height: _T.Any
	fps: _T.Any
	audioSampleRate: _T.Any
	numAudioChannels: _T.Any

class AbsTime:
	frame: float
	seconds: float
	step: float
	stepSeconds: float
