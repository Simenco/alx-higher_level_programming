#!/usr/bin/python3
"""Object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes and methods"""
    return (dir(obj))
