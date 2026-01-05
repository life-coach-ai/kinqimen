# -*- coding: utf-8 -*-
"""
kinqimen - Python Qimen Dunjia (奇門遁甲) library
堅奇門排盤

Simple python package of Qimendunjia in Chinese hour-based system,
minute-based system and golden letter jade mirror style Qimendunjia for prediction.

Author: kentang2017
Maintained by: honza (fork with fixes)
"""

from .kinqimen import Qimen

# Alias for common naming convention
QiMen = Qimen

__version__ = "0.2.0"
__all__ = ["Qimen", "QiMen"]
