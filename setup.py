#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setup.py for installing UnderscoreX

Usage:
   python setup.py install

Copyright 2011-2023 Maxiste Deams all rights reserved,
Maxiste Deams <maxistedeams@gmail.com>
Permission to use, modify, and distribute this software is given under the
terms of the New BSD license :
    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided when fullfiling requirement in
    License.txt, take time to read. 

"""
import os, sys, re, sets, base64
if sys.version_info < (3,):
    from sets import Set
    ### It's built-in set in python 3.x
else:
    import io
    from io import StringIO
    

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension, setup

Base64License           = "CkNvcHlyaWdodCAoYykgMjAwNC0yMDEyLCBNYXhpc3RlIERlYW1zLCBhbGlzIFBhdHJpY2sgUmllbmRlYXUuCkFsbCByaWdodHMgcmVzZXJ2ZWQuCgpSZWRpc3RyaWJ1dGlvbiBhbmQgdXNlIGluIHNvdXJjZSBhbmQgYmluYXJ5IGZvcm1zLCB3aXRoIG9yIHdpdGhvdXQKbW9kaWZpY2F0aW9uLCBhcmUgcGVybWl0dGVkIHByb3ZpZGVkIHRoYXQgdGhlIGZvbGxvd2luZyBjb25kaXRpb25zIGFyZSBtZXQ6CiAgICAqIFJlZGlzdHJpYnV0aW9ucyBvZiBzb3VyY2UgY29kZSBtdXN0IHJldGFpbiB0aGUgYWJvdmUgY29weXJpZ2h0CiAgICAgIG5vdGljZSwgdGhpcyBsaXN0IG9mIGNvbmRpdGlvbnMgYW5kIHRoZSBmb2xsb3dpbmcgZGlzY2xhaW1lci4KICAgICogUmVkaXN0cmlidXRpb25zIGluIGJpbmFyeSBmb3JtIG11c3QgcmVwcm9kdWNlIHRoZSBhYm92ZSBjb3B5cmlnaHQKICAgICAgbm90aWNlLCB0aGlzIGxpc3Qgb2YgY29uZGl0aW9ucyBhbmQgdGhlIGZvbGxvd2luZyBkaXNjbGFpbWVyIGluIHRoZQogICAgICBkb2N1bWVudGF0aW9uIGFuZC9vciBvdGhlciBtYXRlcmlhbHMgcHJvdmlkZWQgd2l0aCB0aGUgZGlzdHJpYnV0aW9uLgogICAgKiBOZWl0aGVyIHRoZSBuYW1lIG9mIHRoZSA8b3JnYW5pemF0aW9uPiBub3IgdGhlCiAgICAgIG5hbWVzIG9mIGl0cyBjb250cmlidXRvcnMgbWF5IGJlIHVzZWQgdG8gZW5kb3JzZSBvciBwcm9tb3RlIHByb2R1Y3RzCiAgICAgIGRlcml2ZWQgZnJvbSB0aGlzIHNvZnR3YXJlIHdpdGhvdXQgc3BlY2lmaWMgcHJpb3Igd3JpdHRlbiBwZXJtaXNzaW9uLgoKVEhJUyBTT0ZUV0FSRSBJUyBQUk9WSURFRCBCWSBUSEUgQ09QWVJJR0hUIEhPTERFUlMgQU5EIENPTlRSSUJVVE9SUyAiQVMgSVMiIEFORApBTlkgRVhQUkVTUyBPUiBJTVBMSUVEIFdBUlJBTlRJRVMsIElOQ0xVRElORywgQlVUIE5PVCBMSU1JVEVEIFRPLCBUSEUgSU1QTElFRApXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSBBTkQgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQVJFCkRJU0NMQUlNRUQuIElOIE5PIEVWRU5UIFNIQUxMIDxDT1BZUklHSFQgSE9MREVSPiBCRSBMSUFCTEUgRk9SIEFOWQpESVJFQ1QsIElORElSRUNULCBJTkNJREVOVEFMLCBTUEVDSUFMLCBFWEVNUExBUlksIE9SIENPTlNFUVVFTlRJQUwgREFNQUdFUwooSU5DTFVESU5HLCBCVVQgTk9UIExJTUlURUQgVE8sIFBST0NVUkVNRU5UIE9GIFNVQlNUSVRVVEUgR09PRFMgT1IgU0VSVklDRVM7CkxPU1MgT0YgVVNFLCBEQVRBLCBPUiBQUk9GSVRTOyBPUiBCVVNJTkVTUyBJTlRFUlJVUFRJT04pIEhPV0VWRVIgQ0FVU0VEIEFORApPTiBBTlkgVEhFT1JZIE9GIExJQUJJTElUWSwgV0hFVEhFUiBJTiBDT05UUkFDVCwgU1RSSUNUIExJQUJJTElUWSwgT1IgVE9SVAooSU5DTFVESU5HIE5FR0xJR0VOQ0UgT1IgT1RIRVJXSVNFKSBBUklTSU5HIElOIEFOWSBXQVkgT1VUIE9GIFRIRSBVU0UgT0YgVEhJUwpTT0ZUV0FSRSwgRVZFTiBJRiBBRFZJU0VEIE9GIFRIRSBQT1NTSUJJTElUWSBPRiBTVUNIIERBTUFHRS4K"
if sys.version_info.major < 3 :
    LicenseDecoded          = base64.b64decode( cStringIO.StringIO( Base64License ).read() )
else:
    LicenseDecoded          = base64.b64decode( StringIO( Base64License ).read() )
    
ActualModuleInformation = dir( )

PackageHandler          = open( 'PKG-INFO', 'r+' )
PackagesRequires        = open( 'requires_modules', 'r+')
FileLicenseH            = open( 'LICENCE.TXT', 'w+' )

FileLicenseH.write( str(LicenseDecoded ) )
FileLicenseH.close() 

TagSplit=re.compile( r'(?i):' )
TagReg=re.compile( r'(?i)^[a-z0-9\-]*:' )

ExceptionTag            =[ 'metadata_version', 'license' ]

RequiredTag             =[  'url',      'keywords',     'classifiers',  'requires',
                            'platforms','description',  'download_url', 'license',
                            'author_email', 'author',   'home_page',    'summary',
                            'version',      'name',     'long_description',
                            'maintainer',   'maintainer_email' ]
TypeAttrFormat={
    'str':{
        'format':'str',
        'name':"Unique{}" 
        },
    'list':{
        'format':'list',
        'name':'List{}',
        'member':[ 'keywords','classifiers','requires','platforms']
        }
    }

ResolvedPkgInfoTag=[]


def Kargs2Attr( ):
    
    """
    This Decorator Will:
     Read **kwargs key and add it to current Object-class ClassTinyDecl under current
     name readed from **kwargs key name. 
            
    """
    def decorator( func ):
        def inner( **kwargs ):
          for ItemName in kwargs.keys():
            setattr( __builtins__, ItemName , kwargs[ItemName] )
          func( **kwargs )
        return inner
    return decorator

def GetTagFormatted( reTag , StrItem ):
    TagInfo=reTag.split( StrItem, 1  )
    TagTransform=TagInfo[0].replace( '-', '_' ).lower()
    NewTag=[ TagTransform , TagInfo[1] ]
    return NewTag

def CleanTagContent( Strtag ):
    return Strtag.replace( '\n', '' )
    #return TagContent=TagInfo[1]

def GetRequiresList( FileHandler , CharExclusionList=[ '\n', ' ', '\t' ], replacementChar='' ):
    Alist=list()
    for Item in FileHandler.readlines():
        for ChrReplace in CharExclusionList:
            Item=Item.replace( ChrReplace , replacementChar )
        Alist.append( Item )
    return Alist

DictRef=dict()
for Item in PackageHandler.readlines( ):
    if TagReg.search( Item):
        TagTransform, TagContent = GetTagFormatted( TagSplit, Item )
        TagContent=CleanTagContent( TagContent )
        if TagTransform not in ResolvedPkgInfoTag:
            ResolvedPkgInfoTag.append( TagTransform )
        if TagTransform not in ExceptionTag:
            if TagTransform in TypeAttrFormat['list']['member']:
                nameListVar=TypeAttrFormat['list']['name'].format( TagTransform )
                if not hasattr( __builtins__, nameListVar ):
                    print( "No List present for Item %s" % ( nameListVar ) ) 
                    setattr( __builtins__, nameListVar, getattr( __builtins__, TypeAttrFormat['list']['format'] )() )
                else:
                    print( "Append %s to Var %s" % ( TagContent, nameListVar ) ) 
                    getattr( getattr( __builtins__, nameListVar ), 'append' )( TagContent )
            else:
                nameUniqueVar=TypeAttrFormat['str']['name'].format( TagTransform )
                print("Var %s will hold: [ %s ] " % ( nameUniqueVar, TagContent)) 
                setattr( __builtins__, TypeAttrFormat['str']['name'].format( TagTransform ), TagContent )

print( "Resolved Tag: %s" % ( ResolvedPkgInfoTag ) ) 
PackageHandler.close()

if sys.version_info < (3,):
    AttrSetListParsed       =   Set( ResolvedPkgInfoTag  )
    AttrSetFromRequired     =   Set( RequiredTag )
    AttrSetFromList         =   Set( TypeAttrFormat['list']['member'] )
else:
    AttrSetListParsed       =   set( ResolvedPkgInfoTag  )
    AttrSetFromRequired     =   set( RequiredTag )
    AttrSetFromList         =   set( TypeAttrFormat['list']['member'] )
    
MissingAttrSet          =   getattr( AttrSetFromRequired, 'difference')( AttrSetListParsed )
MissingAttrFromList     =   getattr( AttrSetFromList    , 'difference')( AttrSetListParsed )


### Using sets.Set to extract easily missing tag from required field and will
### verify ones inside member or required and will create it .
print( "Detected Missing Attribute: %s\n\tFrom List attribute field %s" % ( MissingAttrSet, MissingAttrFromList ) ) 
if len( MissingAttrSet ) > 0 :
    for ItemAttrMissing in MissingAttrSet:
        if ItemAttrMissing in MissingAttrFromList:
            setattr( __builtins__, TypeAttrFormat['list']['name'].format( ItemAttrMissing ), getattr( __builtins__, TypeAttrFormat['list']['format'])() )
        else:
            setattr( __builtins__, TypeAttrFormat['str']['name'].format( ItemAttrMissing ), 'None' )
    
        
        
UseNumpyDistutilsConfiguration = False

def ListFileInstallByExclusion( listReglarExprExclusion ):
    import re
    listRe = list()
    returnList=list() 
    for itemReCp in listReglarExprExclusion:
        listRe.append( re.compile(itemReCp) )
    awalk=os.walk( './' )
    for root, dirs, files in awalk :
        for item in files :
            fetcName = "%s/%s" % ( root,item)
            statusMatch=False
            for reMatchItem in listRe:
                if reMatchItem.match( fetcName ):
                  statusMatch=True
                  print("\tFound match in string[%s]" % reMatchItem.match( fetcName ) )
            if statusMatch is False:
                returnList.append( fetcName )
              #print( fetcName )
    return returnList


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

    
    if 'config' in dir():
        for AddAttr in ListAttr:
            if hasattr( config, AddAttr ):
                if callable( getattr( config, AddAttr ) ) :
                    getattr( getattr( config, AddAttr )( ) )
    
        if sys.version[:3] >= '2.6':
            config['download_url']      = "http://github.com/priendeau/UnderscoreX"
            config['author']            = "Maxiste Deams"
            config['author_email']      = __author_email__
            config['classifiers']       = ClassifierField

    ListRequires                =   GetRequiresList( PackagesRequires )
    PackagesRequires.close()

    import UnderscoreX
    
    setup(  name                =   Uniquename,
            version             =   Uniqueversion,
            url                 =   Uniqueurl,
            description         =   Uniquedescription,
            license             =   LicenseDecoded,
            long_description    =   Uniquelong_description,
            keywords            =   Listkeywords,
            classifiers         =   Listclassifiers ,
            author_email        =   Uniqueauthor_email,
            download_url        =   Uniquedownload_url,
            author              =   Uniqueauthor,
            maintainer          =   Uniquemaintainer,
            maintainer_email    =   Uniquemaintainer_email,
            requires            =   Listrequires, 
            platforms           =   Listplatforms,
            py_modules          =   ["UnderscoreX"],
            package_data={ "": [ "index.html",
                                 "README.md",
                                 "setup.py",
                                 "MANIFEST",
                                 "index.zip",
                                 "LICENCE.TXT",
                                 "requires.txt",
                                 "requires_modules",
                                 "UnderscoreX.py",
                                 "UnderscoreX/BluetoothK6/Connection.py",
                                 "UnderscoreX/BluetoothK6/__init__.py"]},
            include_package_data=   True,
            install_requires    =   ListRequires )


   
