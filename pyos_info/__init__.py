import sys
from pathlib import Path
from xml.etree import ElementTree

from .utils import camel_to_pyname


def get_os_info():
    if sys.platform == "linux":
        return _linux_info()
    elif sys.platform == "darwin":
        return _mac_info()
    else:
        raise RuntimeError("program does not work on Windows. Sorry.")


def _mac_info():
    tree = ElementTree.parse("/System/Library/CoreServices/SystemVersion.plist")
    d = tree.find("dict")
    info = {}
    k = ""
    v = ""
    for elem in d:
        if elem.tag == "key":
            k = elem.text
        elif elem.tag == "string":
            v = elem.text
        if k and v:
            info[k] = v
            k = v = ""
    return info


def _linux_info():
    os_release = Path("/etc/os-release")
    if not os_release.exists():
        raise RuntimeError(f"os release file not found: {str(os_release)}")
    info = {}
    with os_release.open("r") as fid:
        for line in fid.readlines():
            k, v = line.split("=", maxsplit=1)
            info[k.lower()] = v.strip()
    return info