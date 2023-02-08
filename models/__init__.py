#!/usr/bin/python3
"""this module instantiates an instance of the storage will be used"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
