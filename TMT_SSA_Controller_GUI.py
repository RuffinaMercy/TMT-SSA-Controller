# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1122,688 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.Selection_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,-1 ), wx.TAB_TRAVERSAL )
		self.Selection_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.button_ScanForComports = wx.Button( self.Selection_panel1, wx.ID_ANY, u"Scan For Comports", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.button_ScanForComports.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )
		self.button_ScanForComports.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer2.Add( self.button_ScanForComports, 0, wx.ALL, 7 )

		self.Select_staticText2 = wx.StaticText( self.Selection_panel1, wx.ID_ANY, u"Select COM Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Select_staticText2.Wrap( -1 )

		self.Select_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Gadugi" ) )

		bSizer2.Add( self.Select_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 7 )

		choice_COMChoices = [ u"COM1", u"COM2" ]
		self.choice_COM = wx.Choice( self.Selection_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,30 ), choice_COMChoices, 0 )
		self.choice_COM.SetSelection( 0 )
		self.choice_COM.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )
		self.choice_COM.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer2.Add( self.choice_COM, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 7 )

		self.toggleBtn_COMOpen = wx.ToggleButton( self.Selection_panel1, wx.ID_ANY, u"Open COM Port", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		self.toggleBtn_COMOpen.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )
		self.toggleBtn_COMOpen.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer2.Add( self.toggleBtn_COMOpen, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 7 )

		self.toggleBtn_Start_StopRecording = wx.ToggleButton( self.Selection_panel1, wx.ID_ANY, u"Start_StopRecording", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.toggleBtn_Start_StopRecording.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		bSizer2.Add( self.toggleBtn_Start_StopRecording, 0, wx.ALL, 5 )

		self.staticText_SelectFolder = wx.StaticText( self.Selection_panel1, wx.ID_ANY, u"Select Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_SelectFolder.Wrap( -1 )

		self.staticText_SelectFolder.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Gadugi" ) )

		bSizer2.Add( self.staticText_SelectFolder, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.dirPicker_SelectFolder = wx.DirPickerCtrl( self.Selection_panel1, wx.ID_ANY, u".\\Data", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.dirPicker_SelectFolder.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Gadugi" ) )

		bSizer2.Add( self.dirPicker_SelectFolder, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.Selection_panel1.SetSizer( bSizer2 )
		self.Selection_panel1.Layout()
		bSizer1.Add( self.Selection_panel1, 0, wx.ALL|wx.EXPAND, 10 )

		self.Main_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.Click_panel15 = wx.Panel( self.Main_panel14, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TAB_TRAVERSAL )
		self.Click_panel15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Channel = wx.StaticText( self.Click_panel15, wx.ID_ANY, u"  Channel", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.Channel.Wrap( -1 )

		self.Channel.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Gadugi" ) )

		fgSizer5.Add( self.Channel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 7 )

		Channel_choice3Choices = [ u"Ch_1", u"Ch_2", u"Ch_3", u"Ch_4", u"Ch_5", u"Ch_6", u"Ch_7" ]
		self.Channel_choice3 = wx.Choice( self.Click_panel15, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,30 ), Channel_choice3Choices, 0 )
		self.Channel_choice3.SetSelection( 1 )
		self.Channel_choice3.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.Channel_choice3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		fgSizer5.Add( self.Channel_choice3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 7 )

		self.staticText_Calibrate = wx.StaticText( self.Click_panel15, wx.ID_ANY, u"  Calibrate", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.staticText_Calibrate.Wrap( -1 )

		self.staticText_Calibrate.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Gadugi" ) )

		fgSizer5.Add( self.staticText_Calibrate, 0, wx.ALL, 7 )

		self.button_Calibrate = wx.Button( self.Click_panel15, wx.ID_ANY, u"Calibrate", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.button_Calibrate.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.button_Calibrate.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		fgSizer5.Add( self.button_Calibrate, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 7 )

		self.staticText_Clear = wx.StaticText( self.Click_panel15, wx.ID_ANY, u"  Clear_Graph", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.staticText_Clear.Wrap( -1 )

		self.staticText_Clear.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Gadugi" ) )

		fgSizer5.Add( self.staticText_Clear, 0, wx.ALL, 7 )

		self.button_Clear = wx.Button( self.Click_panel15, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.button_Clear.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.button_Clear.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		fgSizer5.Add( self.button_Clear, 0, wx.ALL|wx.ALIGN_BOTTOM, 7 )

		self.staticText_Start_Stop = wx.StaticText( self.Click_panel15, wx.ID_ANY, u"  Start_Stop", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.staticText_Start_Stop.Wrap( -1 )

		self.staticText_Start_Stop.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Gadugi" ) )

		fgSizer5.Add( self.staticText_Start_Stop, 0, wx.ALL, 5 )

		self.toggleBtn_Start_Stop = wx.ToggleButton( self.Click_panel15, wx.ID_ANY, u"Start_Stop", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.toggleBtn_Start_Stop.SetValue( True )
		self.toggleBtn_Start_Stop.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer5.Add( self.toggleBtn_Start_Stop, 0, wx.ALL, 5 )

		self.staticText_Reset = wx.StaticText( self.Click_panel15, wx.ID_ANY, u"   Reset", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.staticText_Reset.Wrap( -1 )

		self.staticText_Reset.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Gadugi" ) )

		fgSizer5.Add( self.staticText_Reset, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.button_Reset = wx.Button( self.Click_panel15, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.button_Reset.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer5.Add( self.button_Reset, 0, wx.ALL, 5 )


		self.Click_panel15.SetSizer( fgSizer5 )
		self.Click_panel15.Layout()
		bSizer4.Add( self.Click_panel15, 0, wx.EXPAND|wx.ALL, 5 )

		self.Main_notebook1 = wx.Notebook( self.Main_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_RIGHT )
		self.panel_Module1 = wx.Panel( self.Main_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,-1 ), wx.TAB_TRAVERSAL )
		self.panel_Module1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Narrow" ) )

		fgSizer1 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		fgSizer1.SetMinSize( wx.Size( 600,-1 ) )
		self.staticText_ChannelNumber1 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"       Ch_Num", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText_ChannelNumber1.Wrap( -1 )

		self.staticText_ChannelNumber1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )
		self.staticText_ChannelNumber1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.staticText_ChannelNumber1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer1.Add( self.staticText_ChannelNumber1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.staticText_StepNumber1 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"Position (μStep)", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText_StepNumber1.Wrap( -1 )

		self.staticText_StepNumber1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer1.Add( self.staticText_StepNumber1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.staticText_Position1 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"  Position (mm)", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText_Position1.Wrap( -1 )

		self.staticText_Position1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer1.Add( self.staticText_Position1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.staticText12 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"     μStrain", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText12.Wrap( -1 )

		self.staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer1.Add( self.staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

		self.staticText16 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"  Moment (Nm)", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText16.Wrap( -1 )

		self.staticText16.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer1.Add( self.staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 10 )

		self.staticText_11 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.staticText_11.Wrap( -1 )

		self.staticText_11.SetFont( wx.Font( 12, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer1.Add( self.staticText_11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl111 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl111, 0, wx.ALL, 8 )

		self.textCtrl112 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl112, 0, wx.ALL, 8 )

		self.textCtrl113 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl113, 0, wx.ALL, 8 )

		self.textCtrl114 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl114, 0, wx.ALL, 8 )

		self.staticText_12 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.staticText_12.Wrap( -1 )

		self.staticText_12.SetFont( wx.Font( 12, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer1.Add( self.staticText_12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl121 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl121, 0, wx.ALL, 8 )

		self.textCtrl122 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl122, 0, wx.ALL, 8 )

		self.textCtrl123 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl123, 0, wx.ALL, 8 )

		self.textCtrl124 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl124, 0, wx.ALL, 8 )

		self.staticText_13 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.staticText_13.Wrap( -1 )

		self.staticText_13.SetFont( wx.Font( 12, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer1.Add( self.staticText_13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl131 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl131, 0, wx.ALL, 8 )

		self.textCtrl132 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl132, 0, wx.ALL, 8 )

		self.textCtrl133 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl133, 0, wx.ALL, 8 )

		self.textCtrl134 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl134, 0, wx.ALL, 8 )

		self.staticText_14 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.staticText_14.Wrap( -1 )

		self.staticText_14.SetFont( wx.Font( 12, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer1.Add( self.staticText_14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl141 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl141, 0, wx.ALL, 8 )

		self.textCtrl142 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl142, 0, wx.ALL, 8 )

		self.textCtrl143 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl143, 0, wx.ALL, 8 )

		self.textCtrl144 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl144, 0, wx.ALL, 8 )

		self.staticText_15 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.staticText_15.Wrap( -1 )

		self.staticText_15.SetFont( wx.Font( 12, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer1.Add( self.staticText_15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl151 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl151, 0, wx.ALL, 8 )

		self.textCtrl152 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl152, 0, wx.ALL, 8 )

		self.textCtrl153 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl153, 0, wx.ALL, 8 )

		self.textCtrl154 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl154, 0, wx.ALL, 8 )

		self.staticText_16 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.staticText_16.Wrap( -1 )

		self.staticText_16.SetFont( wx.Font( 12, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer1.Add( self.staticText_16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl161 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl161, 0, wx.ALL, 8 )

		self.textCtrl162 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl162, 0, wx.ALL, 8 )

		self.textCtrl163 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl163, 0, wx.ALL, 8 )

		self.textCtrl164 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl164, 0, wx.ALL, 8 )

		self.staticText_17 = wx.StaticText( self.panel_Module1, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.staticText_17.Wrap( -1 )

		self.staticText_17.SetFont( wx.Font( 12, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer1.Add( self.staticText_17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl171 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl171, 0, wx.ALL, 8 )

		self.textCtrl172 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl172, 0, wx.ALL, 8 )

		self.textCtrl173 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl173, 0, wx.ALL, 8 )

		self.textCtrl174 = wx.TextCtrl( self.panel_Module1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer1.Add( self.textCtrl174, 0, wx.ALL, 8 )


		self.panel_Module1.SetSizer( fgSizer1 )
		self.panel_Module1.Layout()
		self.Main_notebook1.AddPage( self.panel_Module1, u"Module1", True )
		self.panel_Module2 = wx.Panel( self.Main_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,-1 ), wx.TAB_TRAVERSAL )
		self.panel_Module2.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		fgSizer11 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_ChannelNumber2 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"        Ch_Num", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText_ChannelNumber2.Wrap( -1 )

		self.staticText_ChannelNumber2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer11.Add( self.staticText_ChannelNumber2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.staticText_StepNumber2 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"Position (μStep)", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText_StepNumber2.Wrap( -1 )

		self.staticText_StepNumber2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer11.Add( self.staticText_StepNumber2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.staticText_Position2 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u" Position (mm)", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText_Position2.Wrap( -1 )

		self.staticText_Position2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer11.Add( self.staticText_Position2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.staticText291 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"      μStrain", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText291.Wrap( -1 )

		self.staticText291.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer11.Add( self.staticText291, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.staticText301 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u" Moment (Nm)", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText301.Wrap( -1 )

		self.staticText301.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer11.Add( self.staticText301, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.staticText_Ch21 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Ch21.Wrap( -1 )

		self.staticText_Ch21.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer11.Add( self.staticText_Ch21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 8 )

		self.textCtrl211 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl211, 0, wx.ALL, 8 )

		self.textCtrl212 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl212, 0, wx.ALL, 8 )

		self.textCtrl213 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl213, 0, wx.ALL, 8 )

		self.textCtrl214 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl214, 0, wx.ALL, 8 )

		self.m_staticText321 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText321.Wrap( -1 )

		self.m_staticText321.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer11.Add( self.m_staticText321, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl221 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl221, 0, wx.ALL, 8 )

		self.textCtrl222 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl222, 0, wx.ALL, 8 )

		self.textCtrl223 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl223, 0, wx.ALL, 8 )

		self.textCtrl224 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl224, 0, wx.ALL, 8 )

		self.staticText_23 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_23.Wrap( -1 )

		self.staticText_23.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer11.Add( self.staticText_23, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl231 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl231, 0, wx.ALL, 8 )

		self.textCtrl232 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl232, 0, wx.ALL, 8 )

		self.textCtrl233 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl233, 0, wx.ALL, 8 )

		self.textCtrl234 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl234, 0, wx.ALL, 8 )

		self.staticText_24 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_24.Wrap( -1 )

		self.staticText_24.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer11.Add( self.staticText_24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl241 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl241, 0, wx.ALL, 8 )

		self.textCtrl242 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl242, 0, wx.ALL, 8 )

		self.textCtrl243 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl243, 0, wx.ALL, 8 )

		self.textCtrl244 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl244, 0, wx.ALL, 8 )

		self.staticText_25 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_25.Wrap( -1 )

		self.staticText_25.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer11.Add( self.staticText_25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl251 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl251, 0, wx.ALL, 8 )

		self.textCtrl252 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl252, 0, wx.ALL, 8 )

		self.textCtrl253 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl253, 0, wx.ALL, 8 )

		self.textCtrl254 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl254, 0, wx.ALL, 8 )

		self.staticText_26 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_26.Wrap( -1 )

		self.staticText_26.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer11.Add( self.staticText_26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl261 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl261, 0, wx.ALL, 8 )

		self.textCtrl262 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl262, 0, wx.ALL, 8 )

		self.textCtrl263 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl263, 0, wx.ALL, 8 )

		self.textCtrl264 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl264, 0, wx.ALL, 8 )

		self.staticText_27 = wx.StaticText( self.panel_Module2, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_27.Wrap( -1 )

		self.staticText_27.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer11.Add( self.staticText_27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl271 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl271, 0, wx.ALL, 8 )

		self.textCtrl272 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl272, 0, wx.ALL, 8 )

		self.textCtrl273 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl273, 0, wx.ALL, 8 )

		self.textCtrl274 = wx.TextCtrl( self.panel_Module2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer11.Add( self.textCtrl274, 0, wx.ALL, 8 )


		self.panel_Module2.SetSizer( fgSizer11 )
		self.panel_Module2.Layout()
		self.Main_notebook1.AddPage( self.panel_Module2, u"Module2", False )
		self.panel_Module3 = wx.Panel( self.Main_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,-1 ), wx.TAB_TRAVERSAL )
		fgSizer12 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_ChannelNumber3 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"       Ch_Num", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText_ChannelNumber3.Wrap( -1 )

		self.staticText_ChannelNumber3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer12.Add( self.staticText_ChannelNumber3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.staticText_StepNumber3 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"Position (μStep)", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText_StepNumber3.Wrap( -1 )

		self.staticText_StepNumber3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer12.Add( self.staticText_StepNumber3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.staticText_Position3 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"   Position (mm)", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText_Position3.Wrap( -1 )

		self.staticText_Position3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer12.Add( self.staticText_Position3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.staticText29 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"      μStrain", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText29.Wrap( -1 )

		self.staticText29.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer12.Add( self.staticText29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.staticText30 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u" Moment (Nm)", wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		self.staticText30.Wrap( -1 )

		self.staticText30.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Gadugi" ) )

		fgSizer12.Add( self.staticText30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.staticText_31 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_31.Wrap( -1 )

		self.staticText_31.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer12.Add( self.staticText_31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 8 )

		self.textCtrl311 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl311, 0, wx.ALL, 8 )

		self.textCtrl312 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl312, 0, wx.ALL, 8 )

		self.textCtrl313 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl313, 0, wx.ALL, 8 )

		self.textCtrl314 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl314, 0, wx.ALL, 8 )

		self.staticText_32 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_32.Wrap( -1 )

		self.staticText_32.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer12.Add( self.staticText_32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl321 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl321, 0, wx.ALL, 8 )

		self.textCtrl322 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl322, 0, wx.ALL, 8 )

		self.textCtrl323 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl323, 0, wx.ALL, 8 )

		self.textCtrl324 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl324, 0, wx.ALL, 8 )

		self.staticText_33 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_33.Wrap( -1 )

		self.staticText_33.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer12.Add( self.staticText_33, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 8 )

		self.textCtrl331 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl331, 0, wx.ALL, 8 )

		self.textCtrl332 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl332, 0, wx.ALL, 8 )

		self.textCtrl333 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl333, 0, wx.ALL, 8 )

		self.textCtrl334 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl334, 0, wx.ALL, 8 )

		self.staticText_34 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_34.Wrap( -1 )

		self.staticText_34.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer12.Add( self.staticText_34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl341 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl341, 0, wx.ALL, 8 )

		self.textCtrl342 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl342, 0, wx.ALL, 8 )

		self.textCtrl343 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl343, 0, wx.ALL, 8 )

		self.textCtrl344 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl344, 0, wx.ALL, 8 )

		self.staticText_35 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_35.Wrap( -1 )

		self.staticText_35.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer12.Add( self.staticText_35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl351 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl351, 0, wx.ALL, 8 )

		self.textCtrl352 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl352, 0, wx.ALL, 8 )

		self.textCtrl353 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl353, 0, wx.ALL, 8 )

		self.textCtrl354 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl354, 0, wx.ALL, 8 )

		self.staticText_36 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_36.Wrap( -1 )

		self.staticText_36.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer12.Add( self.staticText_36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl361 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl361, 0, wx.ALL, 8 )

		self.textCtrl362 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl362, 0, wx.ALL, 8 )

		self.textCtrl363 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl363, 0, wx.ALL, 8 )

		self.textCtrl364 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl364, 0, wx.ALL, 8 )

		self.staticText_37 = wx.StaticText( self.panel_Module3, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_37.Wrap( -1 )

		self.staticText_37.SetFont( wx.Font( 11, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Felix Titling" ) )

		fgSizer12.Add( self.staticText_37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.textCtrl371 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl371, 0, wx.ALL, 8 )

		self.textCtrl372 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl372, 0, wx.ALL, 8 )

		self.textCtrl373 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl373, 0, wx.ALL, 8 )

		self.textCtrl374 = wx.TextCtrl( self.panel_Module3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,30 ), 0 )
		fgSizer12.Add( self.textCtrl374, 0, wx.ALL, 8 )


		self.panel_Module3.SetSizer( fgSizer12 )
		self.panel_Module3.Layout()
		self.Main_notebook1.AddPage( self.panel_Module3, u"Module3", False )

		bSizer4.Add( self.Main_notebook1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel11 = wx.Panel( self.Main_panel14, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.textCtrl_UART_Send = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.textCtrl_UART_Send, 0, wx.ALL|wx.EXPAND, 5 )

		self.button_UART_Send = wx.Button( self.m_panel11, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		self.button_UART_Send.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.button_UART_Send.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer5.Add( self.button_UART_Send, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.textCtrl_UART_Receive = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer5.Add( self.textCtrl_UART_Receive, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel11.SetSizer( bSizer5 )
		self.m_panel11.Layout()
		bSizer5.Fit( self.m_panel11 )
		bSizer4.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )


		self.Main_panel14.SetSizer( bSizer4 )
		self.Main_panel14.Layout()
		bSizer4.Fit( self.Main_panel14 )
		bSizer1.Add( self.Main_panel14, 1, wx.EXPAND |wx.ALL, 5 )

		self.panel_Graphs = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.panel_plot1 = wx.Panel( self.panel_Graphs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7.Add( self.panel_plot1, 1, wx.EXPAND |wx.ALL, 5 )

		self.staticText_Plot1Legend = wx.StaticText( self.panel_Graphs, wx.ID_ANY, u"X:00000, Y:00000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Plot1Legend.Wrap( -1 )

		self.staticText_Plot1Legend.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer7.Add( self.staticText_Plot1Legend, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.panel_plot2 = wx.Panel( self.panel_Graphs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8.Add( self.panel_plot2, 1, wx.EXPAND |wx.ALL, 5 )

		self.staticText_Plot2Legend = wx.StaticText( self.panel_Graphs, wx.ID_ANY, u"X:00000, Y:00000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Plot2Legend.Wrap( -1 )

		self.staticText_Plot2Legend.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer8.Add( self.staticText_Plot2Legend, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.panel_plot3 = wx.Panel( self.panel_Graphs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_plot3.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.panel_plot3, 1, wx.EXPAND |wx.ALL, 5 )

		self.staticText_Plot3Legend = wx.StaticText( self.panel_Graphs, wx.ID_ANY, u"X:00000, Y:00000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Plot3Legend.Wrap( -1 )

		self.staticText_Plot3Legend.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.staticText_Plot3Legend, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.panel_Graphs.SetSizer( bSizer3 )
		self.panel_Graphs.Layout()
		bSizer3.Fit( self.panel_Graphs )
		bSizer1.Add( self.panel_Graphs, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MainFrame_OnClose )
		self.button_ScanForComports.Bind( wx.EVT_BUTTON, self.button_ScanForComportsOnButtonClick )
		self.toggleBtn_COMOpen.Bind( wx.EVT_TOGGLEBUTTON, self.toggleBtn_COMOpenOnToggleButton )
		self.toggleBtn_Start_StopRecording.Bind( wx.EVT_TOGGLEBUTTON, self.toggleBtn_Start_StopRecordingOnToggleButton )
		self.dirPicker_SelectFolder.Bind( wx.EVT_DIRPICKER_CHANGED, self.dirPicker_SelectFolder_OnDirChanged )
		self.Channel_choice3.Bind( wx.EVT_CHOICE, self.Channel_choice3OnChoice )
		self.button_Clear.Bind( wx.EVT_BUTTON, self.button_ClearOnButtonClick )
		self.toggleBtn_Start_Stop.Bind( wx.EVT_TOGGLEBUTTON, self.toggleBtn_Start_StopOnToggleButton )
		self.button_Reset.Bind( wx.EVT_BUTTON, self.button_Reset_OnButtonClick )
		self.button_UART_Send.Bind( wx.EVT_BUTTON, self.button_UART_Send_OnClick )
		self.panel_plot1.Bind( wx.EVT_SIZE, self.panel_plot1_OnSize )
		self.panel_plot2.Bind( wx.EVT_SIZE, self.panel_plot1_OnSize )
		self.panel_plot3.Bind( wx.EVT_SIZE, self.panel_plot1_OnSize )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def MainFrame_OnClose( self, event ):
		event.Skip()

	def button_ScanForComportsOnButtonClick( self, event ):
		event.Skip()

	def toggleBtn_COMOpenOnToggleButton( self, event ):
		event.Skip()

	def toggleBtn_Start_StopRecordingOnToggleButton( self, event ):
		event.Skip()

	def dirPicker_SelectFolder_OnDirChanged( self, event ):
		event.Skip()

	def Channel_choice3OnChoice( self, event ):
		event.Skip()

	def button_ClearOnButtonClick( self, event ):
		event.Skip()

	def toggleBtn_Start_StopOnToggleButton( self, event ):
		event.Skip()

	def button_Reset_OnButtonClick( self, event ):
		event.Skip()

	def button_UART_Send_OnClick( self, event ):
		event.Skip()

	def panel_plot1_OnSize( self, event ):
		event.Skip()




