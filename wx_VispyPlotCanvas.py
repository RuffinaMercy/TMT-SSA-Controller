import numpy as np
from vispy import scene

class wx_VispyPlotCanvas(scene.SceneCanvas):
	def __init__(self, *args, **kwargs):
		size = kwargs.pop("size", (300, 300))  # Default value is (300, 300)
		axes_color = kwargs.pop("axes_color", "teal")
		x_axis_label = kwargs.pop("x_axis_label", '')
		y_axis_label = kwargs.pop("y_axis_label", '')
		plot_title = kwargs.pop("plot_title", '')
		x_lim = kwargs.pop("x_lim", (0.0, 10.0))
		y_lim = kwargs.pop("y_lim", (0.0, 10.0))
		
		scene.SceneCanvas.__init__(self, *args, **kwargs)
		
		self.unfreeze()
		# Add all properties after unfreezing
		self.size = size
		self.axes_color = axes_color
		self.line = None
		self.lineVisuals = []
		# Add a grid to place the widgets aligned to the grid
		self.grid = self.central_widget.add_grid(margin=10, spacing=0)
		
		# Add title to the plot
		title = scene.Label(plot_title, color=self.axes_color)
		title.height_max = 40
		self.grid.add_widget(title, row=0, col=0, col_span=2)
		
		self.xaxis = scene.AxisWidget(orientation='bottom', axis_label=x_axis_label, axis_font_size=10,
		                              axis_label_margin=25, tick_label_margin=15, axis_color=self.axes_color,
		                              tick_color=self.axes_color, text_color=self.axes_color)
		# self.xaxis.stretch = (10, 10) # width, height
		# Set only height and not width of x-axis to allow for expansion during resizing event of the parent
		self.xaxis.height_max = 50
		# self.xaxis.width_max = self.size[0] * 0.9
		self.grid.add_widget(self.xaxis, row=2, col=1)
		
		self.yaxis = scene.AxisWidget(orientation='left', axis_label=y_axis_label, axis_font_size=10,
		                              axis_label_margin=25, tick_label_margin=5, axis_color=self.axes_color,
		                              tick_color=self.axes_color, text_color=self.axes_color)
		# self.yaxis.stretch = (10, 10) # width, height
		# Set only width and not height of y-axis to allow for expansion during resizing event of the parent
		self.yaxis.width_max = 50
		# self.yaxis.height_max = self.size[1] * 0.9
		self.grid.add_widget(self.yaxis, row=1, col=0)
		
		# Add a view inside the grid. NOTE: Add the view only after adding the axes
		self.view = self.grid.add_view(row=1, col=1, border_color=self.axes_color, camera='panzoom')
		self.plotArea = self.view.scene
		
		self._x_lim = x_lim
		self._y_lim = y_lim
		# Link to the axes so that the axes can move along with the view when panned
		self.xaxis.link_view(self.view)
		self.yaxis.link_view(self.view)
		
		self.auto_set_viewBox_range()
		
		right_padding = self.grid.add_widget(row=1, col=2, row_span=1)
		right_padding.width_max = 50
		
		self.x_data = None
		self.y_data = None
		self.line_transform = None
		
		self.freeze()
		
		self.show()
	
	@property
	def x_lim(self):
		return self._x_lim
	
	@x_lim.setter
	def x_lim(self, x_lim):
		self._x_lim = x_lim
		self.auto_set_viewBox_range()
	
	@property
	def y_lim(self):
		return self._y_lim
	
	@y_lim.setter
	def y_lim(self, y_lim):
		self._y_lim = y_lim
		self.auto_set_viewBox_range()
	
	def plot_xy(self, xdata, ydata, color='teal'):
		self.x_data = xdata
		self.y_data = ydata
		data = np.column_stack((xdata, ydata))
		self.plot_data(data, color=color)
	
	def plot_data(self, data, color='teal'):
		assert data.ndim in [1, 2], "Plotting FAILED. Plot Data should be of the format (n,) or (n,2)"
		if data.ndim == 1:
			self.y_data = data
			self.x_data = np.linspace(0, len(self.y_data), len(self.y_data))
			data = np.column_stack((self.x_data, self.y_data))
		
		if self.line is not None:
			self.line.parent = None
		self.line = scene.Line(data, color=color, parent=self.plotArea)
		self.line_transform = self.line.transforms.get_transform(map_to="canvas")
		
		# auto-scale to see the whole line.
		xmin, xmax = np.min(data[:, 0]), np.max(data[:, 0])
		ymin, ymax = np.min(data[:, 1]), np.max(data[:, 1])
		self.x_lim = (xmin, xmax)
		self.y_lim = (ymin, ymax)
		self.auto_set_viewBox_range()
	
	def auto_set_viewBox_range(self):
		# auto-scale to see the whole line.
		self.view.camera.set_range(x=self._x_lim, y=self._y_lim)
		
	def clear_plot(self):
		if self.line is not None:
			self.line.parent= None
	
	# def on_mouse_press(self, event):
	# 	print(np.round(self.line_transform.imap(event.pos)[:2],3))
	#
	# def on_mouse_move(self, event):
	# 	print(f"[{self.line_transform.imap(event.pos)[0]:6.3f}, {self.line_transform.imap(event.pos)[1]:6.3f}]")#: {self.y_data[int(self.line_transform.imap(event.pos)[0])]}")

