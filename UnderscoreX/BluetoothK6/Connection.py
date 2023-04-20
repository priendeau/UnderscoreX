#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- file : Connection.py -*-

import bluetooth
import socket
from time import sleep

class BluetoothMediaWarning( Warning ):
  StrMsgFormat="[WARNING] :%s"
  def __init__(self, msg):
    Warning.__init__( self, self.StrMsgFormat % msg )
    pass 

class BluetoothAddrWarning( Warning ):
  StrMsgFormat="[WARNING] :%s"
  def __init__(self, msg):
    Warning.__init__( self, self.StrMsgFormat % msg )
    pass 

class PortHandlerWarning( Warning ):
  StrMsgFormat="[WARNING] :%s"
  def __init__(self, msg):
    Warning.__init__( self, self.StrMsgFormat % msg )
    pass 

class AlreadyChoosenSequenceWarning( Warning ):
  StrMsgFormat="[WARNING] :%s"
  def __init__(self, msg):
    Warning.__init__( self, self.StrMsgFormat % msg )
    pass

class SequenceRequireAppendWarning( Warning ):
  StrMsgFormat="[WARNING] :%s"
  def __init__(self, msg, value ):
    Warning.__init__( self, self.StrMsgFormat % msg )
    value.append(0)
    pass

class BlueToothScanner( object ):

  SleepTime=1
  SetMinRangeFirst=True
  listRange=[ 0, 0]

  def __init__( self, value ):
    self.addr=value
    self.BTSocket=None
    self.isRefused=False
    self.isResetByPeer=False
    self.LastIndex=None
    self.SleepTimeProperty=1

  def GetSleep( self ):
    return self.SleepTime

  def SetSleep( self, value ):
    self.SleepTime=value

  def GetRange( self, value ):
    return self.listRange

  ###
  ### SetRange and it's sub-functions
  ### SetRange as the goal to associate the begin of whitch port have to  start and when to 
  ### stop. 
  ###
  ### -SubFunction TestStateRange
  ###
  ### In this case were we have the proof the the value have a type of type list 
  ### and do own 2 free space inside list or it raise SequenceRequireAppendWarning
  ### to correct the problems. It perform accross else-try statement of Warning to  
  ### raise SequenceRequireAppendWarning . This case lead to delete or use del actor
  ### over property to tell to reset the condition. The correct case will simply
  ### add it where also finally-state of the try-warning section fall here.  
  ###
  ### -SubFunction ByRangingAndStore
  ###
  ### Since we do allow insertion of 1 integer as unique element or accepting 2 int 
  ### in a list, this mechanism invert the SetMinRangeFirst that is used to monitor
  ### which state[0] or state[1] of the RangeProperty . 
  ###
  ###
  ### Comment-001 : finally section explain and reste of SetRange Mechanism 
  ###
  ### When it fall accross the except Warning(...) -> raised SequenceRequireAppendWarning
  ### to the internal stuff of SequenceRequireAppendWarning and should change the value
  ### into list of 2 value. It fall here a finally. Like Except everything it finally pass.
  ### It also require to set SetMinRangeFirst back to True ; allowing an overwriting of the
  ### state[0] of RangeProperty in adding only one number at the time :
  ### state description :
  ### - adding 1 in RangeProperty
  ###   - add 1 at state[0]
  ### - adding 11 in RangeProperty
  ###   - add 11 at state[1]
  ### - do the scan 
  ###   - the scan emit a warning of faillure at port number 4.
  ### - adding 4 in RangeProperty
  ###   - add 4 at state[0] 
  ### - adding 6 in RangeProperty
  ###   - add 6 at state[1]
  ### - do the scan
  ###   - the scan emit a warning of faillure at port number 5.
  ###   ...
  ### Comment-002 : 
  ### When it pass the value is an list with two value.
  ### This place will also made the addition.
  ### This property use the Delete property, by calling del + Property it will
  ### execute in this case self.ResetRange( )
  
  def SetRange( self, value ):
    def TestStateRange( self, value ):
      if type( value ) == type( list() ):
        ### Be sure to know it's full-state try clause where all [ Try:, except ...: else : and finally are
        ### all member of the Try-Statement.
        try:
          if len( value ) < 2 :
            raise Warning( "Internal problems, listRange should be 2 elements list." )
        except Warning:
          raise SequenceRequireAppendWarning( "Require to add more value ; The object should be a list of 2 value.", value ) 
        else:
          ### see Comment-002
          del self.RangeProperty
        finally:
          self.SetMinRangeFirst=True
          ### See Comment-001 in SetRange
        ###
        ### .. after-block of else and finally will fall here ... 
        self.RangeProperty = value 
        #AlreadyChoosenSequenceWarning
    def ByRangingAndStore( self, value ):
      if self.SetMinRangeFirst is True :
        self.listRange[ 0 ]=value
        self.SetMinRangeFirst=False
      else:
        self.listRange[ 1 ]=value
        self.SetMinRangeFirst=True
    ### Main Body function is here with 2 sub-functions
    if type( value ) == type( int() ):
      ByRangingStore( value )
    if type( value ) == type( list() ):
      if len( value ) <= 1 :
        ByRangingAndStore( value )
      if len( value ) == 2 :
        TestStateRange( value )

  def ResetRange( self ):
    self.SetMinRangeFirst=True
    self.listRange=[ 0 , 0 ]

  ###
  ### RangeProperty action.
  ### Having a slight different action than filling one value and
  ### returning it ; RangeProperty work on fashion you can fill 
  ### one range-element at the time like : 
  ###
  ### self.RangeProperty = 1 
  ###
  ### Will : 
  ### - set to [ 1 , 0 ] => self.listRange
  ###
  ### Using it again with :
  ### self.RangeProperty = 5
  ### - set to [ 1 , 5 ] => self.listRange
  ###
  ###
  ### 
  ###
  RangeProperty = property( GetRange, SetRange, ResetRange, None )
  
  SleepTimeProperty = property( GetSleep, SetSleep, None, None )

  @property  
  def DefaultSleep( self ):
    "Default Sleep, do simply user property and use the self.DefaultSleep and sleep for."
    sleep( self.SleepTimeProperty ) 


  def FindBluetooth( self ):
    print("Scanning for bluetooth devices:")
    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
    number_of_devices = len(devices)
    print("%i devices found" % number_of_devices )
    for addr, name, device_class in devices:
      print("\nDevice:\nDevice Name: %s\nDevice MAC Address: %s\nDevice Class: %s\n\n" % ( name, addr, device_class ) )

  ### StartScanner depend of RangeProperty to work . 
  ### Assumming you are using between extended bluetooth where you have almost as 65535 port
  ### or an Arduino Bluetooth facility; that let you open specific port, like Number-one at least.
  ### The RangeProperty
  def StartScanner( self, IntStartrange, IntEndrange):
    print("Start Scan port in range: %i, %i\n"% ( IntStartrange, IntEndrange ) )
    for intCount in range( IntStartrange, IntEndrange, 1):
      self.DefaultSleep
      self.BTSocket = socket.socket( socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM )
      try:
        print("Trying port %i" % intCount )
        self.isRefused, self.isResetByPeer = False, False
        if hasattr( self.BTSocket , 'connect' ):
          self.BTSocket.connect( ( self.addr , intCount) )
          self.DefaultSleep
        #socket.connect( ( self.addr , intCount) )
        
        if hasattr( self.BTSocket , 'close' ):
          self.BTSocket.close()
          self.DefaultSleep
      except ConnectionRefusedError:
        if hasattr( self.BTSocket , 'close' ):
          self.BTSocket.close()
          self.DefaultSleep
        del( self.BTSocket )
        self.BTSocket=None
        self.isRefused=True
        self.LastIndex=intCount
        pass
      except ConnectionResetError:
        if hasattr( self.BTSocket , 'close' ):
          self.BTSocket.close()
          self.DefaultSleep
        del( self.BTSocket )
        self.BTSocket=None
        self.isResetByPeer=True
        self.LastIndex=intCount
        pass
      finally:
        if hasattr( self.BTSocket , 'close' ):
          self.BTSocket.close()
          self.DefaultSleep

      print("Port scan port %i, end, error may have repored:\n\tIsRefused: %s\n\tisResetByPeer: %s\n" % ( intCount , self.isRefused, self.isResetByPeer ) )
       


class ObjectHelper( object ):
  
  OH={
    }

  def __init__( self ):
    "Start with no history "
    self.OH['cache']=None


  def SearchDir( self, cstrreg, modulename ):
    "Return the result of passed regular expression on a dir( module )"
    Areg=re.compile( cstrreg )
    for item in dir( modulename ) :
      if Areg.search( item ):
        print( item )    


class WainluxEngraver( object ):
  "Object Created for initializing Wainlux K6 Laser engraver and compatible device working with bluetooth."

  ConnectBt={
    'BluetoothAddr':None,
    'peername':None,
    'addressBt':None,
    'portBtConn':None,
    'sock':None,
    'IsConnect':False ,
    'Send':None,
    'WaitState':1,
    'MediaType':None}

  def GetMediaType( self ):
    return self.ConnectBt['MediaType']

  def SetMediaType( self , value):
    "SetMediaType  Accept an int type because belong to type(bluetooth.RFCOMM)"
    "and type(L2CAP) report both int it easy to add them. "
    if type( value ) == type( int() ):
      self.ConnectBt['MediaType']=value 
      print("Using media type:%i\nCreating the socket for Addr:%s, port:%s" % ( value,self.BluetoothAddr,self.PortHandler) )
      self.ConnectBt['sock']=bluetooth.BluetoothSocket( self.BluetoothMedia )

  def DelMediaType( self ):
    self.ConnectBt['MediaType']=None

  def GetWaitState( self ):
    return self.ConnectBt['WaitState']

  def SetWaitState( self, intValue ):
    self.ConnectBt['WaitState'] = intValue

  def ResetWaitState( self ):
    self.ConnectBt['WaitState']=1

  @property 
  def Wait( self ):
    sleep( self.ConnectBt['WaitState'] )
  
  def GetAddr( self ):
    return self.ConnectBt['addressBt']

  def SetAddr( self, strAddr ):
    print("Following bluetooth-address is registered: %s" % strAddr )
    self.ConnectBt['addressBt'] = strAddr

  def DelAddr( self ):
    self.ConnectBt['addressBt']=None

  def GetPort( self ):
    return self.ConnectBt['portBtConn']

  def SetPort( self, intValue ):
    print("Connection will be done on bluetooth-port number: %i" % intValue )
    self.ConnectBt['portBtConn'] = intValue

  def DelPort( self ):
    print("Removing connection bluetooth-port number : %i" % self.portBtConn )
    self.ConnectBt['portBtConn']=None

  def SetFlagConnect( self ):
    self.ConnectBt['IsConnect']=True

  def GetFlagConnect( self ):
    return self.ConnectBt['IsConnect']

  def DelFlagConnect( self ):
    self.ConnectBt['IsConnect']=False

  def GetConnect( self ):
    return self.ConnectBt['peername']

  ### Appeal to weirdest way to use a Property Setter and Getter
  ### altogether : 
  ### - We do acknowledge of a property to Retreive information should be
  ### available on the line to express it Getter action and the
  ### first members on the line is the Setter and this action should
  ### reloop what I do have collect of an __init__( self, "DC:0D:30:FC:4E:D9" )
  @property
  def Connect( self ):
    if self.BluetoothAddr is None:
      raise BluetoothAddrWarning( "Address is require to pair a Bluetooth" )
    if self.PortHandler is None:
      raise PortHandlerWarning( "Bluetooth do also require to use a port connection." )
    if self.BluetoothMedia is None:
      raise BluetoothMediaWarning( "Bluetooth media description not set, usually: bluetooth.RFCOMM or bluetooth.L2CAP " )
    print("Attempt to make a connection")
    self.ConnectHandler = self.ConnectHandler
  
  def SetConnect (self, value ):
    if type( value ) == type(str()):
      if value != None :
        self.BluetoothAddr = value
    if type( value ) == type( tuple() ):
      valAddrBt, valPort = value
      self.BluetoothAddr = valAddrBt
      self.PortHandler = valPort
    self.ConnectBt['sock'].connect( (self.BluetoothAddr, self.PortHandler) )
    self.ConnectBt['peername']=self.ConnectBt['sock'].getpeername()

  def DelConnect( self ):
    self.ConnectBt['sock'].close()
    del self.ConnectFlag

  BluetoothMedia=property( GetMediaType, SetMediaType, DelMediaType, None)

  WaitStateTransfert=property( GetWaitState, SetWaitState, ResetWaitState, None )
  
  ConnectHandler=property( GetConnect ,SetConnect , DelConnect, None )

  ConnectFlag=property(GetFlagConnect, SetFlagConnect,DelFlagConnect, None)

  PortHandler=property(GetPort, SetPort, DelPort, None )

  BluetoothAddr=property(GetAddr, SetAddr, DelAddr , None )

  def __init__( self , strAddr ) :
    if type( strAddr ) == type(str()):
      if strAddr != None :
        ### First adding Bluetooth addr, port 
        self.BluetoothAddr = strAddr
    if type( strAddr ) == type( tuple() ):
      if len( strAddr) < 3 :
        valAddrBt, valPort = strAddr
        self.BluetoothAddr = valAddrBt
        self.PortHandler = valPort
      elif len( strAddr ) == 3 :
        valAddrBt, valPort, valMedia = strAddr
        self.BluetoothAddr = valAddrBt
        self.PortHandler = valPort
        self.BluetoothMedia = valMedia
    #self.ConnectHandler = strAddr
    #self.ConnectBt['BluetoothAddr'] = strAddr
    #self.ConnectBt['sock']=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    # or even with L2CAP -> self.ConnectBt['sock']=bluetooth.BluetoothSocket(bluetooth.L2CAP)
    #self.WaitStateTransfert = 2 


    #sleep(10)
    #sock.send("M0\n")
    

### Wainlux K6 laser engraver with bluetooth
### connection. 
### Wainlux Engraver addr: DC:0D:30:FC:4E:D9
### name : Engraver-0C4ED9
###
if __name__.__eq__( '__main__' ):
  oScan=BlueToothScanner( "DC:0D:30:FC:4E:D9" )
  oScan.StartScanner(1, 4 ) 
  Aobj=WainluxEngraver( ("DC:0D:30:FC:4E:D9",4) )
  Aobj.BluetoothMedia=bluetooth.RFCOMM
  
