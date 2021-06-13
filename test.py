from manim import *

class instagram_logo(Scene):
	def construct(self):

		rect_1 = RoundedRectangle(corner_radius=0.3, height=1.5, width=1.5,
                            color=PINK)

		obj = Circle(radius=0.4, color=PINK).next_to(rect_1, DOWN, buff=-1.15)
		dot = Dot(color=PINK).scale(0.6)\
							 .next_to(obj, buff=0.15)\
							 .shift(UP*0.4)

		self.play(
			Create(rect_1),
			Create(obj),
			FadeIn(dot),
			run_time=1.2
		)
		self.wait()

		group= VGroup(rect_1, obj, dot)

		self.play(
			group.animate.shift(UP+LEFT*4),
			run_time=1.2
		)

		my_id1 = Text("_ ", font="Times New Roman").scale(1.5)\
					.next_to(group, buff=0.3)\
					.set_color(BLUE)

		my_id2 = MathTex(r"\textrm{\bf{code.py}}").scale(1.5)\
						.set_color_by_gradient(BLUE, ORANGE)\
						.next_to(my_id1, buff=0.1)\
						.shift(UP*0.1)

		my_id3 = Text("_", font="Times New Roman").scale(1.5)\
						.set_color(ORANGE)\
						.next_to(my_id2, buff=0.05)\
						.shift(DOWN*0.2)

		self.play(
			Write(my_id1),
			Write(my_id2),
			Write(my_id3),
			run_time=1.2
		)
		self.wait(2)

class FacebookIcon(Scene):
	def construct(self):

		my_circle = Circle(radius=1.6, color=DARK_BLUE, fill_opacity=1.0)
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
