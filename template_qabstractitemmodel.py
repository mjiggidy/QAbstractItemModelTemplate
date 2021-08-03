# This is a minimal template for Pyside/PyQt QAbstractItemModel with typehints
# based on documentation from https://doc.qt.io/qtforpython/PySide6/QtCore/QAbstractItemModel.html

import typing
from Pyside6 import QtCore

class TemplateAbstractItemModel(QtCore.QAbstractItemModel):

	def __init__(self):
		"""A model of all bookmarks"""
		super().__init__()
	
	def index(self, row:int, column:int, parent:typing.Optional[QtCore.QModelIndex]=QtCore.QModelIndex()) -> QtCore.QModelIndex:
		"""Returns the index of the item in the model specified by the given row, column and parent index."""
	
	def parent(self, child:QtCore.QModelIndex) -> QtCore.QModelIndex:
		"""Returns the parent of the model item with the given index. If the item has no parent, an invalid QModelIndex is returned."""

	def rowCount(self, parent:typing.Optional[QtCore.QModelIndex]=QtCore.QModelIndex()) -> int:
		"""Returns the number of rows under the given parent. When the parent is valid it means that is returning the number of children of parent."""
	
	def columnCount(self, parent:typing.Optional[QtCore.QModelIndex]=QtCore.QModelIndex()) -> int:
		"""Returns the number of columns for the children of the given parent."""

	def data(self, index:QtCore.QModelIndex, role:typing.Optional[int]=QtCore.Qt.DisplayRole) -> typing.Any:
		"""Returns the data stored under the given role for the item referred to by the index."""

	def headerData(self, section:int, orientation:QtCore.Qt.Orientation, role:typing.Optional[int]=QtCore.Qt.DisplayRole) -> typing.Any:
		"""Returns the data for the given role and section in the header with the specified orientation."""
