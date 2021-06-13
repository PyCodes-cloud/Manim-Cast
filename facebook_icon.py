from manim import *

class FacebookIcon(Scene):
	def construct(self):
		
		# Creating circle
		my_circle = Circle(radius=1.6, color=DARK_BLUE, fill_opacity=1.0)
		
		# Text 'f'
		icon = Text("f", font='Calibri').scale(6.0)\
							.set_color(WHITE)\
							.move_to(my_circle)\
							.shift(DOWN*0.25)

		self.play(
			GrowFromCenter(my_circle),
			Write(icon),
			run_time = 1.2
		)
		self.wait()

		my_group = VGroup(my_circle, icon)

		self.play(
			my_group.animate.shift(UP+LEFT*2),
			run_time=1.2
		)
		self.wait()
