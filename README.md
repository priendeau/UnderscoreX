UnderscoreX
===========

This is a set of Class and decorator to parse many type of argument.

This structure is intended for The developper developping pass-thru and conviviable method to 
intercept attribut on demande by passing information from **kwargs or mutiple-string-chained argument.

=========
    This allow to build and easy model assuming you had readed the example. It offer a easy chaining method
    Thru decorator to parse incoming information from **kwargs or any multi-chained string. Once you have 
    defined a correct dictrionary of Attentend Attribute and Messages dedicated to inform the developper. 
    It contains a mechanism to push into warning or error the missing attribute informaitons. Rather to
    code individually all the missing attribute and condition, and exception class is provided as example.


Installing
==========
  Under Development.
  
  You can download the latest versions released from <<No pypi for the moment, crude develpt and 
  in correct stuff will cause problem and rejection, but maxistedeams will release it >>
  or download the development version straight from the Github repository hosted by me at:
  git://github.com/priendeau/UnderscoreX.git

Documentation
=============
  Is currently lacking, about every method is documented in the source. But future prototype will
  become move and more verbosis and Final realse will include test-case and a lot of documentation.

::
		Example
		------------
		Generic Exception class model:

        Basics
        ------
        We need 2 Class to store attribute:
        
        class ObjectGenericWarningHolder( object ):
        
          def __init__( self ):
            print "Add Current Object Attribute %s" % self.__class__.__name__
        
        class ObjectGenericAttrHolder( object ):
        
          def __init__( self ):
            print "Add Current Object Attribute %s" % self.__class__.__name__
        
        
        We Need a Generic Exception class like this one.
        
        
        class ExceptionGenericAttrMissing( Exception ):
          
          msg                             ='__GENERIC_EXCEPTION_MESSAGES__'
          AttrCurrentExceptionHandled     = None
          HadDecoderTypeList              = False 
        
          def __Init__Attr( self , value ):
            self.AttrCurrentExceptionHandled = value
            DictListTemplateKey="%sList" % ( value )
            IsListTemplateKey="Had%sList" % ( value )
            if hasattr( self, IsListTemplateKey  ):
              if getattr( self, IsListTemplateKey ) == True:
                Exception.__init__( self, self.MsgDict[DictListTemplateKey] % ( self.AttrCurrentExceptionHandled ,
                                                                        getattr( self, DictListTemplateKey ) ) )
              else:
                Exception.__init__( self, self.MsgDict[self.AttrCurrentExceptionHandled]  % ( self.AttrCurrentExceptionHandled ) )
    
        
          @_XDecoratorWrapper.Kargs2Attr( ObjectWarningHolder )
          def __init__( self, **Kargs ):
            if hasattr( self, 'ListAttrFuncAccess' ):
              print "Available message for following Attr:[ %s ]" % ( self.ListAttrFuncAccess ) 
            self.RaisedExceptionByAttr = False
            for ExceptionByAttr in self.ListAttrFuncAccess:
              if hasattr( self, ExceptionByAttr ):
                self.RaisedExceptionByAttr = True
                getattr( self, "__Init__Attr")( ExceptionByAttr )

        ###
        ### Main class:
        ### 

        class GenericTest( object ):
        
          MsgDict = {
            'AppsName'        :'Internal Value AppsName not used, You should at least Specified an AppsName Value.',
            'ActionHelper'    :'Internal Value ActionHelper not used, You should at least Specified an ActionHelper Value.',
            'HelperSwitch'    :'Internal Value HelperSwitch not used, You should at least Specified an HelperSwitch Value.',
          }  

          OptionListDiscovery=list()
          TempOptionList=list()
          ErrorHandler = iterpipes.CalledProcessError

          ListAttrFuncAccess        = [ 'AppsName', 'ActionHelper', 'HelperSwitch' ]
          parser = OptionParser()

          def __start_cmdline_parser__( self ):
    
            self.parser.add_option("-A", "--AppsName",
                              dest="StrAppsName",
                              help="Add AppsName in your Class")
            self.parser.add_option("-J", "--ActionHelper",
                              dest="StrActionHelper",
                              help="Add ActionHelper in your Class")
            self.parser.add_option("-S", "--HelperSwitch",
                              dest="StrHelperSwitch",
                              help="Add HelperSwitch in your Class ")


          @_XDecoratorWrapper.Kargs2AttrPreException( ObjectIterAppsFilter )
          def __init__( self , **Kargs ):
            self.__start_cmdline_parser__()
            (self.options, self.args ) = self.parser.parse_args() 
            self.ErrorRaiser( )
        ### ...


          @_XDecoratorWrapper.ObjectClassRaiser( ObjectGenericAttrHolder , ExceptionGenericAttrMissing )
          def ErrorRaiser( self ):
            print "Inspecting Missing Attribute."



        ### Some Instantiation statement:

        if __name__.__eq__( '__main__' ):
          _XDecoratorWrapper.ErrorClassReceivedAttrListName = 'ListAttrFuncAccess'
          ExceptionGenericAttrMissing.ListAttrFuncAccess    = ItertAppsFilter.ListAttrFuncAccess
          ExceptionGenericAttrMissing.MsgDict               = ItertAppsFilter.MsgDict
          Ainstance=GenericTest( AppsName=None, ActionHelper=None, HelperSwitch=None )

        And We have Correct basic model of Attribute filtering thru the **kargs and will raise any Warning or exception
        upon definition of your class inside the Object Raiser inside _XDecoratorWrapper :
        --------
        @_XDecoratorWrapper.ObjectClassRaiser( __ANY_EXCEPTION_OR_WARNING_OBJECT__ , ExceptionGenericAttrMissing )
        def ErrorRaiser( self ):
         pass 
        --------

