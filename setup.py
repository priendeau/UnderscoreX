# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
setup.py for installing UnderscoreX

Usage:
   python setup.py install

Copyright 2011-2012 Maxiste Deams all rights reserved,
Maxiste Deams <maxistedeams@gmail.com>
Permission to use, modify, and distribute this software is given under the
terms of the New BSD license :
    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided when fullfiling requirement in
    License.txt, take time to read. 

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
$Revision: 0.0.1r001a-yusut-bozlon $
$Date: Mon Sep 10 22:01:31 EDT 2012 $
Maxiste Deams
"""

import os
import sys
from distutils.dep_util import newer
from numpy.distutils import log
from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

##import UnderscoreX
##from UnderscoreX import _XDecoratorWrapper
##from UnderscoreX import ObjectGenericWarningHolder
##from UnderscoreX import ObjectGenericAttrHolder
##from UnderscoreX import ExceptionGenericAttrMissing

__version__ = '0.0.1r001a-yusut-bozlon'

def configuration(parent_package='',top_path=None):
    config = Configuration('UnderscoreX', parent_package, top_path)
    return config
    
if __name__ == "__main__":
    config = configuration(top_path='')
    config = config.todict()
    
    if sys.version[:3]>='2.3':
        config['download_url'] = "http://github.com/priendeau/UnderscoreX"
        config['name'] = "UnderscoreX"
        config['classifiers'] = [
            'Classifier: Development Status :: 4 - Alpha'
            'Classifier: Intended Audience :: Developers'
            'Classifier: License :: OSI Approved :: BSD License'
            'Classifier: Natural Language :: English'
            'Classifier: Operating System :: OS Independent'
            'Classifier: Programming Language :: Python'
            'Classifier: Topic :: Program engineering :: Development'
            'Classifier: Environment :: Console'
            'Classifier: Intended Audience :: Developers'
            'Classifier: Operating System :: OS Independent'
            ]


    setup(
        version=__version__,
        description="This structure is intended for The developper developping pass-thru and conviviable method to intercept attribute on demand.",
        license="BSD NEW LICENCE",
        url="http://github.com/priendeau/UnderscoreX",
        long_description="This structure is intended for The developper developping pass-thru and conviviable method to intercept attribute on demand. By passing information from **kwargs or mutiple-string-chained argument. This allow to build and easy model assuming you had readed the example. It offer a easy chaining method Thru decorator to parse incoming information from **kwargs or any multi-chained string. Once you have defined a correct dictrionary of Attentend Attribute and Messages dedicated to inform the developper.  It contains a mechanism to push into warning or error the missing attribute informaitons. Rather to code individually all the missing attribute and condition, and exception class is provided as example.",
        packages=["UnderscoreX"],
        keywords = ['UnderscoreX','kwargs','Kargs','multi-inline','multi-quoted','string'],
        **config
    )
