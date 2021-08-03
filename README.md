# QAbstractItemModelTemplate

## About
Minimal template for Pyside/PyQt QAbstractItemModel with typehints and notes.
Based on documentation from https://doc.qt.io/qtforpython/PySide6/QtCore/QAbstractItemModel.html

## Additional Notes
- The QAbstractItemModel should be thought of as an *adapter* class, although I typically do use it to fully encapsulate the data.
- An invalid model index (created by `QtCore.QModelIndex()`) object is used to refer to an invisible "root" node.
- Indexes to child objects should be created with the class' `self.createIndex()` (inherited implementation) method.
- I have typically found it useful to return a pointer to the full object in the `nullptr` argument of `self.createIndex()`, then use the `self.data()` method in conjunction with the `QModelIndex` `.row()` and `.column()` methods to determine the actual data to return.  Not always, but that usually works well.
