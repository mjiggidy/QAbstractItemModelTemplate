# QAbstractItemModelTemplate

## About
Minimal template for Pyside/PyQt QAbstractItemModel with typehints and notes.
Based on documentation from https://doc.qt.io/qtforpython/PySide6/QtCore/QAbstractItemModel.html

## Additional Notes
- The QAbstractItemModel should be thought of as an *adapter* class, although I typically do use it to fully encapsulate the data.

- An invalid model index (created by `QtCore.QModelIndex()`) object is used to refer to an invisible "root" node.
