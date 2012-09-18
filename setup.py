#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import os, sys, re, numpy
from distutils.core import setup
import UnderscoreX

# from distutils.dep_util import newer
# from numpy.distutils import log
# from numpy.distutils.core import setup
# from numpy.distutils.misc_util import Configuration


##from UnderscoreX import _XDecoratorWrapper
##from UnderscoreX import ObjectGenericWarningHolder
##from UnderscoreX import ObjectGenericAttrHolder
##from UnderscoreX import ExceptionGenericAttrMissing



UseNumpyDistutilsConfiguration = False


def configuration( PackageName ):
    Pconfig = Configuration( PackageName, 
                             top_path=None,
                             parent_package='')
    return Pconfig
    
if __name__ == "__main__":
    ListAttr=[ 'make_svn_version_py', 'make_config_py' ]

    if UseNumpyDistutilsConfiguration:
        config = configuration( __package__ )
        config.add_data_dir('UnderscoreX')
        config.add_subpackage('UnderscoreX')
        config = config.todict()

    FileLicenseH = open( 'LICENCE.TXT', 'r+' )
    ClassifierH = open('classifiers', 'r+')
    ClassifierField = str( ClassifierH.read() ).split( '\n' )

    if 'config' in dir():
        for AddAttr in ListAttr:
            if hasattr( config, AddAttr ):
                if callable( getattr( config, AddAttr ) ) :
                    getattr( getattr( config, AddAttr )( ) )
    
        if sys.version[:3] >= '2.6':
            config['download_url'] = "http://github.com/priendeau/UnderscoreX"
            config['author']= "Maxiste Deams"
            config['author_email']= __author_email__
            config['classifiers'] = ClassifierField
    
    setup( name=__package__,
           version=__version__,
           download_url = "http://pypi.python.org/pypi?:action=files&name={}&version={}".format( __package__ , __version__ ) , 
           url="http://github.com/priendeau/{}".format( __package__ ),
           description="This structure is intended for The developper developping pass-thru and conviviable method to intercept attribute on demand.",
           license=FileLicenseH.read(),
           long_description="This structure is intended for The developper developping pass-thru and conviviable method to intercept attribute on demand. By passing information from **kwargs or mutiple-string-chained argument. This allow to build and easy model assuming you had readed the example. It offer a easy chaining method Thru decorator to parse incoming information from **kwargs or any multi-chained string. Once you have defined a correct dictrionary of Attentend Attribute and Messages dedicated to inform the developper.  It contains a mechanism to push into warning or error the missing attribute informaitons. Rather to code individually all the missing attribute and condition, and exception class is provided as example.",
           keywords = [__package__,'kwargs','Kargs','multi-inline','multi-quoted','string'],
           classifiers=ClassifierField ,
           author_email = __author_email__,
           download_url = 'http://github.com/priendeau/{}'.format( __package__ ),
           author = __author__,
           maintainer = 'Maxiste Deams',
           maintainer_email = 'maxistedeams@gmail.com',
           requires = [ 'iterpipes', 'sets', 'decimal' ], 
           platforms = ['Linux', 'Unix', 'Bsd', 'FreeBSD', 'OSX'] )
