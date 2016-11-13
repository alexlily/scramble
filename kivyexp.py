import kivy
kivy.require('1.9.1') 

from scramble import * 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Line, Rectangle

class MyBackground(Widget):
    def __init__(self, source, **kwargs):
        super(MyBackground, self).__init__(**kwargs)
        with self.canvas:
            self.bg = Rectangle(source=source, pos=self.pos, size=self.size)

class MyWidget(GridLayout):
	def __init__(self, **kwargs):
	 	super(MyWidget, self).__init__(**kwargs)
	 	self.puzzle = Puzzle(4,4)
	 	self.cols=4
	 	self.spacing=[0,0]
	 	self.puzzleWidgets = []
	 	self.draw()
	def on_touch_down(self, touch):
		for widget in self.puzzleWidgets:
			if widget.collide_point(*touch.pos):
				self.puzzle.swap_pieces(int(widget.index))
				self.clear_widgets()
				self.draw()
	def draw(self):
		self.puzzleWidgets = []
		for i in range(len(self.puzzle.puzzle)):
	 		if self.puzzle.blank == i:
	 			cell = Image(source="blank.jpg", allow_stretch=True)
	 		else:
	 			cell = Image(source= "puppy/" + self.puzzle.puzzle[i] + ".jpg", allow_stretch=True) 
	 		self.puzzleWidgets.append(cell)
	 		cell.index = i
	 		self.add_widget(cell)

class MyApp(App):
	def build(self):
		parent = MyWidget()
		return parent

if __name__ == '__main__':
    MyApp().run()