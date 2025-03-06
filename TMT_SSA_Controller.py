import wx
import zipfile
import TMT_SSA_Controller_GUI
import numpy as np
from wx_VispyPlotCanvas import wx_VispyPlotCanvas
from SerialObject import SerialObject
import serial
import glob
import csv
from datetime import datetime
import os

K1 = 0.0303
K2 = 0.0404
K3 = 0.0404
K4 = 0.0404
K5 = 0.0404
K6 = 0.0404
K7 = 0.0404

DIGITAL_2_USTRAIN_FACTOR = 0.000338
ARM_LENGTH_L = 0.12
ARM_LENGTH_S = 0.19

STEP_CONVERSION_FACTOR = 0.0001984


class TMT_SSA_Controller(TMT_SSA_Controller_GUI.MainFrame):
    def __init__(self, parent):
        TMT_SSA_Controller_GUI.MainFrame.__init__(self, parent)
        
        self.mapping = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 6, 14: 7, 15: 1,
                        16: 2, 17: 3, 18: 4, 19: 5, 20: 6, 21: 7}
        
        self.recording_enabled = False
        self.file_path = None
        self.chosen_dir = None
        
        self.stress = []
        self.strain = []
        self.position = []
        self.moment = []

        self.channel_text_ctrl_mapping = {
            1: [getattr(self, "textCtrl111"), getattr(self, "textCtrl113"), getattr(self, "textCtrl112"),
                getattr(self, "textCtrl114")],
            2: [getattr(self, "textCtrl121"), getattr(self, "textCtrl123"), getattr(self, "textCtrl122"),
                getattr(self, "textCtrl124")],
            3: [getattr(self, "textCtrl131"), getattr(self, "textCtrl133"), getattr(self, "textCtrl132"),
                getattr(self, "textCtrl134")],
            4: [getattr(self, "textCtrl141"), getattr(self, "textCtrl143"), getattr(self, "textCtrl142"),
                getattr(self, "textCtrl144")],
            5: [getattr(self, "textCtrl151"), getattr(self, "textCtrl153"), getattr(self, "textCtrl152"),
                getattr(self, "textCtrl154")],
            6: [getattr(self, "textCtrl161"), getattr(self, "textCtrl163"), getattr(self, "textCtrl162"),
                getattr(self, "textCtrl164")],
            7: [getattr(self, "textCtrl171"), getattr(self, "textCtrl173"), getattr(self, "textCtrl172"),
                getattr(self, "textCtrl174")],
            # Add more mappings as needed
            8: [getattr(self, "textCtrl211"), getattr(self, "textCtrl213"), getattr(self, "textCtrl212"),
                getattr(self, "textCtrl214")],
            9: [getattr(self, "textCtrl221"), getattr(self, "textCtrl223"), getattr(self, "textCtrl222"),
                getattr(self, "textCtrl224")],
            10: [getattr(self, "textCtrl231"), getattr(self, "textCtrl233"), getattr(self, "textCtrl232"),
                 getattr(self, "textCtrl234")],
            11: [getattr(self, "textCtrl241"), getattr(self, "textCtrl243"), getattr(self, "textCtrl242"),
                 getattr(self, "textCtrl244")],
            12: [getattr(self, "textCtrl251"), getattr(self, "textCtrl253"), getattr(self, "textCtrl252"),
                 getattr(self, "textCtrl254")],
            13: [getattr(self, "textCtrl261"), getattr(self, "textCtrl263"), getattr(self, "textCtrl262"),
                 getattr(self, "textCtrl264")],
            14: [getattr(self, "textCtrl271"), getattr(self, "textCtrl273"), getattr(self, "textCtrl272"),
                 getattr(self, "textCtrl274")],
            
            15: [getattr(self, "textCtrl311"), getattr(self, "textCtrl313"), getattr(self, "textCtrl312"),
                 getattr(self, "textCtrl314")],
            16: [getattr(self, "textCtrl321"), getattr(self, "textCtrl323"), getattr(self, "textCtrl322"),
                 getattr(self, "textCtrl324")],
            17: [getattr(self, "textCtrl331"), getattr(self, "textCtrl333"), getattr(self, "textCtrl332"),
                 getattr(self, "textCtrl334")],
            18: [getattr(self, "textCtrl341"), getattr(self, "textCtrl343"), getattr(self, "textCtrl342"),
                 getattr(self, "textCtrl344")],
            19: [getattr(self, "textCtrl351"), getattr(self, "textCtrl353"), getattr(self, "textCtrl352"),
                 getattr(self, "textCtrl354")],
            20: [getattr(self, "textCtrl361"), getattr(self, "textCtrl363"), getattr(self, "textCtrl362"),
                 getattr(self, "textCtrl364")],
            21: [getattr(self, "textCtrl371"), getattr(self, "textCtrl373"), getattr(self, "textCtrl372"),
                 getattr(self, "textCtrl374")]
            # Add more mappings as needed
        }
        self.button_Reset.Bind(wx.EVT_BUTTON, self.button_Reset_OnButtonClick)
        self.toggleBtn_Start_Stop.Bind( wx.EVT_TOGGLEBUTTON, self.toggleBtn_Start_StopOnToggleButton )

        self.panel_plot1.canvas = wx_VispyPlotCanvas(app='wx', parent=self.panel_plot1, size=self.panel_plot1.GetSize(),
                                                     axes_color='teal', x_axis_label='t', y_axis_label='  Position (mm)',
                                                     resizable=True)
        x_data = 100 * np.linspace(0, 2 * np.pi, 100)
        y_data = np.sin(x_data)
        self.panel_plot1.canvas.plot_xy(x_data, y_data, color='white')

        self.text_controls = None

        self.panel_plot2.canvas = wx_VispyPlotCanvas(app='wx', parent=self.panel_plot2, size=self.panel_plot2.GetSize(),
                                                     axes_color='pink', x_axis_label='t', y_axis_label='μStrain',
                                                     resizable=True)
        x_data = 100 * np.linspace(0, 2 * np.pi, 100)
        y_data = np.sin(x_data)
        self.panel_plot2.canvas.plot_xy(x_data, y_data, color='white')

        self.panel_plot3.canvas = wx_VispyPlotCanvas(app='wx', parent=self.panel_plot3, size=self.panel_plot3.GetSize(),
                                                     axes_color='yellow', x_axis_label='μStrain',
                                                     y_axis_label='Position (mm)',
                                                     resizable=True)
        x_data = 100 * np.linspace(0, 2 * np.pi, 100)
        y_data = np.sin(x_data)
        self.panel_plot3.canvas.plot_xy(x_data, y_data, color='white')

        # Interactions with the figure
        self.panel_plot1.canvas.events.mouse_move.connect(self.plot1_ImageOnMove)
        self.panel_plot2.canvas.events.mouse_move.connect(self.plot2_ImageOnMove)
        self.panel_plot3.canvas.events.mouse_move.connect(self.plot3_ImageOnMove)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer_tick, self.timer)
        self.row_index = 0


        # Reset row index and arrays when changing channels
        self.row_index = 0

        # Initialize a counter to keep track of the number of values plotted
        self.plot_counter = 0

        # Scan for COM ports when initializing
        self.choice_COM.Clear()
        self.availablePorts = SerialObject.scan_for_serial_ports()
        print(self.availablePorts)
        if not self.availablePorts:
            wx.MessageBox('No COM ports found. Please check the connections and serial port driver.', 'Verify COM port',
                          wx.OK | wx.ICON_EXCLAMATION)
            self.toggleBtn_COMOpen.Disable()
        else:
            for port in self.availablePorts:
                self.choice_COM.Append(port)
            self.choice_COM.SetSelection(0)
            self.toggleBtn_COMOpen.Enable()

        self.button_UART_Send.Disable()

        self.serial_port = None

        self.panel_plot1.Bind(wx.EVT_SIZE, self.update_plot_sizes)

    def update_plot_sizes(self, event):
        # Get the size of panel_plot1
        size = self.panel_plot1.GetSize()

        # Set the sizes of panel_plot2 and panel_plot3 to match panel_plot1
        self.panel_plot2.SetSize(size)
        self.panel_plot3.SetSize(size)

        # Update the canvas sizes
        self.panel_plot2.canvas.size = size
        self.panel_plot3.canvas.size = size

        # Update the plots
        self.update_plot()

    def button_ClearOnButtonClick(self, event):
        # Clear the stress and strain arrays
        self.stress = []
        self.strain = []

        # Clear the plots by removing the lines
        self.panel_plot1.canvas.clear_plot()# Clear plot 1
        self.panel_plot2.canvas.clear_plot()  # Clear plot 2
        self.panel_plot3.canvas.clear_plot() # Clear plot 3

        # Restart updating the plots from the beginning
        self.update_plot()

    def button_ScanForComportsOnButtonClick(self, event, os_type="Windows"):
        self.choice_COM.Clear()
        self.portChoice = {}
        if os_type == "Windows":
            key = 0
            for i in range(256):
                try:
                    s = serial.Serial("COM" + str(i))
                except serial.SerialException:
                    pass
                else:
                    self.portChoice.update({key: s.portstr})
                    self.choice_COM.Append(s.portstr)
                    key = key + 1
                    s.close()
        elif os_type == "Linux":
            key = 0
            s = glob.glob('/dev/ttyUSB*')
            print(s)
            for i in range(s.__len__() - 1, -1, -1):
                self.portChoice.update({key: s[i]})
                self.choice_COM.Append(s[i])
                key = key + 1

            s = glob.glob('/dev/ttyS[0-2]')
            for i in range(s.__len__() - 1, -1, -1):
                self.portChoice.update({key: s[i]})
                self.choice_COM.Append(s[i])
                key = key + 1

        if self.portChoice == {}:
            wx.MessageBox('No COM ports found. Please check the connections and serial port driver.',
                          'Verify COM port',
                          wx.OK | wx.ICON_EXCLAMATION)
            self.toggleBtn_COMOpen.Disable()
        else:
            self.choice_COM.SetSelection(0)
            self.toggleBtn_COMOpen.Enable()
    
    def switch_to_module(self, first_value):
        module_index = 0
        if 0 <= first_value <= 7:
            module_index = 0
        elif 8 <= first_value <= 14:
            module_index = 1
        elif 15 <= first_value <= 21:
            module_index = 2
        
        # Switch to the appropriate module
        self.Main_notebook1.SetSelection(module_index)
    
    def UART_ReceiveMessage(self, message):
        # Initializing value4 and value5
        """Updates the Receive textbox and processes received values"""
        if isinstance(message, bytes):
            message = message.decode('utf-8')  # Decode bytes to string
        self.textCtrl_UART_Receive.AppendText(message)
        
        # Append newline if the message doesn't end with a newline
        if not message.endswith('\n'):
            self.textCtrl_UART_Receive.AppendText('\n')
        
        lines = message.strip().split('\n')
        
        for line in lines:
            received_values = line.strip().split(',')
            values_grouped = [received_values[i:i + 3] for i in range(0, len(received_values), 3)]
            for group in values_grouped:
                if len(group) == 3:
                    self.textCtrl_UART_Receive.AppendText(','.join(group) + '\n')
                    
                    first_value = int(group[0])
                    value2 = float(group[1])
                    value3 = float(group[2])
                    
                    self.switch_to_module(first_value)
                    
                    if 1 <= first_value <= 21:
                        first_value_mapped = self.mapping[first_value]
                        self.Channel_choice3.SetSelection(first_value_mapped - 1)
                        
                        for j, text_ctrl in enumerate(self.channel_text_ctrl_mapping[first_value]):
                            if j == 0:
                                text_ctrl.SetValue(str(value2))
                                text_ctrl.SetForegroundColour(wx.Colour(255, 0, 0))
                                font = text_ctrl.GetFont()
                                font.SetPointSize(9)  # Set font size
                                text_ctrl.SetFont(font)
                                # Set initial color to red
                            elif j == 1:
                                text_ctrl.SetValue(str(value3))
                                text_ctrl.SetForegroundColour(wx.Colour(255, 0, 0))
                                font = text_ctrl.GetFont()
                                font.SetPointSize(9)  # Set font size
                                text_ctrl.SetFont(font)
                                self.stress.append(value2)
                                self.strain.append(value3)
                                
                            
                            elif j == 2:
                                # Initialize value4 with a default value
                                value4 = 0.0
                                # Calculate value4 based on conditions
                                if first_value == 1:  # Check if the channel number is 1
                                    value4 = value3 * STEP_CONVERSION_FACTOR * K1 * ARM_LENGTH_S
                                else:
                                    value4 = value2 * DIGITAL_2_USTRAIN_FACTOR * K2 * ARM_LENGTH_S
                                text_ctrl.SetValue("{:.3f}".format(value4))
                                text_ctrl.SetValue(f"{value4:.3f}")
                                text_ctrl.SetForegroundColour(wx.Colour(255, 0, 0))
                                font = text_ctrl.GetFont()
                                font.SetPointSize(9)  # Set font size
                                text_ctrl.SetFont(font)
                                # Set initial color to red
                            elif j == 3:
                                value5 = 0.0
                                # Calculate value5 based on conditions
                                if first_value == 1:  # Check if the channel number is 1
                                    value5 = value3 * STEP_CONVERSION_FACTOR * K1 * ARM_LENGTH_L
                                else:
                                    value5 = value2 * DIGITAL_2_USTRAIN_FACTOR * K2 * ARM_LENGTH_S
                                text_ctrl.SetValue("{:.3f}".format(value5))
                                text_ctrl.SetValue(f"{value5:.3f}")
                                text_ctrl.SetForegroundColour(wx.Colour(255, 0, 0))
                                font = text_ctrl.GetFont()
                                font.SetPointSize(9)  # Set font size
                                text_ctrl.SetFont(font)
                                # Set initial color to red
                                
                                # Append values to respective lists
                                self.position.append(value4)
                                self.moment.append(value5)
                                
                                # Change text control color based on channel matching
    
    def button_UART_Send_OnClick(self, event):
        input_values = self.textCtrl_UART_Send.GetValue().strip()
        values_array = input_values.split(',')
        
        if len(values_array) < 3:
            wx.MessageBox('Please enter at least three values separated by commas.', 'Invalid Input',
                          wx.OK | wx.ICON_EXCLAMATION)
            return
        
        receive_message = f"{input_values}\n"
        self.UART_ReceiveMessage(receive_message)
        
        try:
            first_value = int(values_array[0].strip())
            value2 = float(values_array[1].strip())
            value3 = float(values_array[2].strip())
        except (ValueError, IndexError):
            return
        
        self.switch_to_module(first_value)
        
        if 1 <= first_value <= 7:
            self.Channel_choice3.SetSelection(first_value - 1)
            
            value4 = 0.0  # Define value4 here
            value5 = 0.0  # Define value5 here
            
            for j, text_ctrl in enumerate(self.channel_text_ctrl_mapping[first_value]):
                if j == 0:
                    text_ctrl.SetValue(str(value2))
                    text_ctrl.SetForegroundColour(wx.Colour(255, 0, 0))
                    font = text_ctrl.GetFont()
                    font.SetPointSize(9)  # Set font size
                    text_ctrl.SetFont(font)
                elif j == 1:
                    text_ctrl.SetValue(str(value3))
                    text_ctrl.SetForegroundColour(wx.Colour(255, 0, 0))
                    font = text_ctrl.GetFont()
                    font.SetPointSize(9)  # Set font size
                    text_ctrl.SetFont(font)
                elif j == 2:
                    # Initializing value4 and value5
                    
                    text_ctrl.SetValue("{:.3f}".format(value4))
                    text_ctrl.SetValue(f"{value4:.3f}")
                    text_ctrl.SetForegroundColour(wx.Colour(255, 0, 0))
                    font = text_ctrl.GetFont()
                    font.SetPointSize(9)  # Set font size
                    text_ctrl.SetFont(font)
                elif j == 3:
                    # Initializing value4 and value5
                    
                    text_ctrl.SetValue("{:.3f}".format(value5))
                    text_ctrl.SetValue(f"{value5:.3f}")
                    text_ctrl.SetForegroundColour(wx.Colour(255, 0, 0))
                    font = text_ctrl.GetFont()
                    font.SetPointSize(9)  # Set font size
                    text_ctrl.SetFont(font)
        
        x_data = np.linspace(0, 2 * np.pi, 100)
        self.panel_plot1.canvas.plot_xy(x_data, np.full_like(x_data, value2), color='red')
        self.panel_plot1.canvas.update()
        
        self.panel_plot2.canvas.plot_xy(x_data, np.full_like(x_data, value3), color='blue')
        self.panel_plot2.canvas.update()
        
        self.stress.append(value2)
        self.strain.append(value3)
        
        y_data = np.array(self.stress)
        x_data = np.array(self.strain)
        self.panel_plot3.canvas.plot_xy(x_data, y_data, color='white')
        self.panel_plot3.canvas.update()
    
    
    
    def dirPicker_SelectFolder_OnDirChanged(self, event):
        # Get the chosen directory from the directory picker
        self.chosen_dir = self.dirPicker_SelectFolder.GetPath()
        
        # If no directory is chosen, create the CSV file in a folder named "data"
        if not self.chosen_dir:
            self.chosen_dir = "Data"
        
        # Create the directory if it doesn't exist
        if not os.path.exists(self.chosen_dir):
            os.makedirs(self.chosen_dir)
        
        # Save the file when starting recording for the first time
        if self.recording_enabled and not self.file_path:
            self.save_file()
    
    def toggleBtn_Start_StopRecordingOnToggleButton(self, event):
        # Toggle recording state
        self.recording_enabled = not self.recording_enabled
        
        # Change button label based on recording state
        if self.recording_enabled:
            self.toggleBtn_Start_StopRecording.SetLabel("Stop Recording")
            # Activate dirPicker1OnDirChanged if recording is started for the first time
            if not self.file_path:
                self.dirPicker_SelectFolder.Enable(True)
                self.dirPicker_SelectFolder_OnDirChanged(None)
        else:
            self.toggleBtn_Start_StopRecording.SetLabel("Start Recording")
            # Disable dirPicker1OnDirChanged when recording is stopped
            self.dirPicker_SelectFolder.Enable(False)
        
        # If recording is stopped, save the file
        if not self.recording_enabled and self.file_path:
            self.save_file()
    
    def save_file(self):
        # Get the current system time
        current_time = datetime.now()
        
        # Format the time as per your requirement
        file_name = current_time.strftime("%Y-%m-%d_%H-%M-%S.csv")
        
        # Construct the full path to the CSV file
        self.file_path = os.path.join(self.chosen_dir, file_name)
        
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Assuming the data is newline separated and you want each line as a separate row in the CSV
            lines = self.textCtrl_UART_Receive.GetValue().split('\n')
            for line in lines:
                writer.writerow([line])
    
    def toggleBtn_COMOpenOnToggleButton(self, event):
        if not self.toggleBtn_COMOpen.GetValue():
            self.toggleBtn_COMOpen.SetLabel("Open COM Port")
            if self.serial_port and self.serial_port.is_open:
                self.serial_port.close()
                self.serial_port = None
                self.button_UART_Send.Disable()
                self.toggleBtn_Start_Stop.SetValue(False)
                self.toggleBtn_Start_Stop.SetLabel("Start")
            return
        
        self.toggleBtn_COMOpen.SetLabel("Close COM Port")
        port = self.choice_COM.GetStringSelection()
        try:
            self.serial_port = serial.Serial(port, baudrate=115200, timeout=1)
            self.serial_port.reset_input_buffer()
            self.serial_port.reset_output_buffer()
            self.button_UART_Send.Enable()
            self.toggleBtn_Start_Stop.SetValue(True)
            self.toggleBtn_Start_Stop.SetLabel("Stop")
            self.timer.Start(500)  # Start the timer for UART communication
        except serial.SerialException as e:
            wx.MessageBox(f'Failed to open serial port: {e}', 'Error', wx.OK | wx.ICON_ERROR)
            self.toggleBtn_COMOpen.SetValue(False)
            self.toggleBtn_COMOpen.SetLabel("Open COM Port")
            return
    
    def on_timer_tick(self, event):
        if self.serial_port and self.serial_port.is_open:
            try:
                message = self.serial_port.readline().decode('utf-8').strip()
                if message:
                    self.UART_ReceiveMessage(message)
                    self.update_plot()
            except Exception as e:
                print("Error reading from serial port:", e)

    def update_values(self, line=None):
        if line is not None:
            try:
                value1 = float(line[1])
            except ValueError:
                value1 = 0.0

            try:
                value3 = float(line[2])
            except (ValueError, IndexError):
                value3 = 0.0

            self.stress[:-1] = self.stress[1:]
            self.stress[-1] = value1
            self.strain[:-1] = self.strain[1:]
            self.strain[-1] = value3

            #self.timer.Start(1000)

    def update_plot(self, x_data=None, y_data=None):
        if x_data is None or y_data is None:
            if not self.stress or not self.strain or not self.position:
                # If any of the arrays are empty, don't update the plots
                return
            
            # Update the first plot (stress vs. time)
            x_data_stress = np.linspace(0, len(self.stress), len(self.stress))
            self.panel_plot1.canvas.plot_xy(x_data_stress, np.array(self.stress), color='white')
            self.panel_plot1.canvas.update()
            
            # Update the second plot (strain vs. time)
            x_data_strain = np.linspace(0, len(self.strain), len(self.strain))
            self.panel_plot2.canvas.plot_xy(x_data_strain, np.array(self.strain), color='white')
            self.panel_plot2.canvas.update()
            
            # Update the third plot (stress vs. strain)
            self.panel_plot3.canvas.plot_xy(np.array(self.strain), np.array(self.stress), color='white')
            self.panel_plot3.canvas.update()
            
            # Update the first plot (position vs. time)
            x_data_position = np.linspace(0, len(self.position), len(self.position))
            self.panel_plot1.canvas.plot_xy(x_data_position, np.array(self.position), color='red')  # Assuming red color
            self.panel_plot1.canvas.update()
        
        else:
            x_data_stress_initial = np.linspace(0, len(x_data), len(x_data))
            self.panel_plot1.canvas.plot_xy(x_data_stress_initial, np.array(y_data), color='white')
            self.panel_plot1.canvas.update()
            
            # Update the second plot (strain vs. time) with initial data
            x_data_strain_initial = np.linspace(0, len(x_data), len(x_data))
            self.panel_plot2.canvas.plot_xy(x_data_strain_initial, np.array(y_data), color='white')
            self.panel_plot2.canvas.update()
            
            # Update the third plot (stress vs. strain) with initial data
            self.panel_plot3.canvas.plot_xy(np.array(y_data), np.array(y_data),
                                            color='white')  # Example data, modify as needed
            self.panel_plot3.canvas.update()
    
    def plot_data(self, data, color='teal'):
        assert data.ndim in [1, 2], "Plotting FAILED. Plot Data should be of the format (n,) or (n,2)"
        if data.ndim == 1:
            self.y_data = data
            self.x_data = np.linspace(0, len(self.y_data), len(self.y_data))
            data = np.column_stack((self.x_data, self.y_data))

        if self.line is None:
            self.line = scene.Line(data, color=color, parent=self.plotArea)
            self.line_transform = self.line.transforms.get_transform(map_to="canvas")
        else:
            self.line.set_data(data)

        # auto-scale to see the whole line.
        xmin, xmax = np.min(data[:, 0]), np.max(data[:, 0])
        ymin, ymax = np.min(data[:, 1]), np.max(data[:, 1])
        self.x_lim = (xmin, xmax)
        self.y_lim = (ymin, ymax)
        self.auto_set_viewBox_range()

    # Update all plots with initial data
    # Implement your logic to update plots with initial data here

    def panel_plot1_OnSize(self, event):
        self.panel_plot1.canvas.size = self.panel_plot1.GetSize()

    def panel_plot2_OnSize(self, event):
        self.panel_plot2.canvas.size = self.panel_plot2.GetSize()

    def panel_plot3_OnSize(self, event):
        self.panel_plot3.canvas.size = self.panel_plot3.GetSize()

    def MainFrame_OnClose(self, event):
        if self.serial_port is not None and self.serial_port.is_open:
            self.serial_port.close()  # Close the serial port if it's open
        self.Destroy()

    def toggleBtn_Start_StopOnToggleButton(self, event):
        if self.toggleBtn_Start_Stop.GetValue():
            self.toggleBtn_Start_Stop.SetLabel("Stop")
            if not self.update_plot():
                # Open COM port if not already open
                if not self.serial_port or not self.serial_port.is_open:
                    port = self.choice_COM.GetStringSelection()
                    try:
                        self.serial_port = serial.Serial(port, baudrate=115200, timeout=1)
                        self.serial_port.reset_input_buffer()
                        self.serial_port.reset_output_buffer()
                        self.button_UART_Send.Enable()
                    except serial.SerialException as e:
                        wx.MessageBox(f'Failed to open serial port: {e}', 'Error', wx.OK | wx.ICON_ERROR)
                        self.toggleBtn_Start_Stop.SetValue(False)
                        self.toggleBtn_Start_Stop.SetLabel("Start")
                        return
                # Start UART communication and plotting
                self.timer.Start(500)  # Start the timer for UART communication
        else:
            self.toggleBtn_Start_Stop.SetLabel("Start")
            if self.timer.IsRunning():
                self.timer.Stop()  # Stop the timer for UART communication
            # Close COM port if open
            if self.serial_port and self.serial_port.is_open:
                self.serial_port.close()
                self.serial_port = None
                self.button_UART_Send.Disable()

    def button_Reset_OnButtonClick(self, event):
        # Clear the stress and strain arrays
        self.stress = []
        self.strain = []

        # Close the serial port if it's open
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.serial_port = None
            self.button_UART_Send.Disable()
            self.toggleBtn_Start_Stop.SetValue(False)
            self.toggleBtn_Start_Stop.SetLabel("Start")

        # Reinitialize the serial port if it's available
        if self.availablePorts:
            selected_port = self.choice_COM.GetStringSelection()
            try:
                self.serial_port = serial.Serial(selected_port, baudrate=115200, timeout=1)
                self.serial_port.reset_input_buffer()
                self.serial_port.reset_output_buffer()
                self.button_UART_Send.Enable()
            except serial.SerialException as e:
                wx.MessageBox(f'Failed to open serial port: {e}', 'Error', wx.OK | wx.ICON_ERROR)
                self.toggleBtn_COMOpen.SetValue(False)
                self.toggleBtn_COMOpen.SetLabel("Open COM Port")
                return
        else:
            wx.MessageBox('No COM ports found. Please check the connections and serial port driver.',
                          'Verify COM port', wx.OK | wx.ICON_EXCLAMATION)
            self.toggleBtn_COMOpen.Disable()
            return

        # Read values from UART and plot the graphs accordingly
        try:
            while self.serial_port.in_waiting:
                message = self.serial_port.readline().decode('utf-8').strip()
                if message:
                    self.UART_ReceiveMessage(message)
                    self.update_plot()
        except Exception as e:
            print("Error reading from serial port:", e)

    def plot1_ImageOnMove(self, event):
        # if event.button == 1:
        self.staticText_Plot1Legend.SetLabelText(
            f"t: {self.panel_plot1.canvas.line_transform.imap(event.pos)[0]:6.3f}, Position: {self.panel_plot1.canvas.line_transform.imap(event.pos)[1]:6.3f}")

    def plot2_ImageOnMove(self, event):
        # if event.button == 1:

        self.staticText_Plot2Legend.SetLabelText(
            f"t: {self.panel_plot2.canvas.line_transform.imap(event.pos)[0]:6.3f},Stress: {self.panel_plot2.canvas.line_transform.imap(event.pos)[1]:6.3f}")

    def plot3_ImageOnMove(self, event):
        # if event.button == 1:
        self.staticText_Plot3Legend.SetLabelText(
            f"Stress: {self.panel_plot3.canvas.line_transform.imap(event.pos)[0]:6.3f}, Position: {self.panel_plot3.canvas.line_transform.imap(event.pos)[1]:6.3f}")
        
    

if __name__ == '__main__':
    app = wx.App(False)
    serial_object = None
    frame = TMT_SSA_Controller(None)
    frame.Show(True)
    app.MainLoop()