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

class YouTubeIcon(Scene):
	def construct(self):
		# Rounded Rectangle
		rect = RoundedRectangle(corner_radius=0.3, height=1.5, width=1.5,
			   color=RED_E, fill_opacity=1.0)

		triangle = Triangle(color=WHITE, fill_opacity=1.0).scale(0.4)\
						 	 .rotate(-PI/2)\
						 	 .next_to(rect, DOWN, buff=-1.1)\
						 	 .shift(RIGHT*0.1)

		self.play(
			Create(rect),
			FadeIn(triangle),
			run_time=1.2
		)
		self.wait()

		group = VGroup(rect, triangle)

		self.play(
			group.animate.shift(UP+LEFT*4),
			run_time=1.2
		)

		tex_1 = MathTex(r"\textbf{Code}").scale(1.5)\
					.set_color_by_gradient(BLUE)\
					.next_to(group, buff=0.4)

		tex_2 = Text("-").scale(1.5)\
					 .set_color(RED)\
					 .next_to(tex_1, buff=0.1)\
					 .shift(DOWN*0.2)

		tex_3 = MathTex(r"\textbf{Tech}").scale(1.5)\
					 .set_color(ORANGE)\
					 .next_to(tex_2, buff=0.1)\
					 .shift(UP*0.2)

		self.play(
			Write(tex_1),
			Write(tex_2),
			Write(tex_3),
			run_time=1.2
		)
		self.wait(2)

class YouTubeBanner(Scene):
	def construct(self):

		text = Text("Manim Cast #3", font='Times New Roman').scale(2.5)\
							.set_color_by_gradient(YELLOW, GREEN_D, PINK)\
							.to_edge(UP, buff=0.8)

		self.play(
			Write(text)
		)

		rect = RoundedRectangle(corner_radius=0.3, height=1.5, width=1.5,
			   color=RED_E, fill_opacity=1.0)

		triangle = Triangle(color=WHITE, fill_opacity=1.0).scale(0.4)\
						 	 .rotate(-PI/2)\
						 	 .next_to(rect, DOWN, buff=-1.1)\
						 	 .shift(RIGHT*0.1)

		self.play(
			Create(rect),
			FadeIn(triangle),
			run_time=1.2
		)

		my_group = VGroup(rect, triangle)
		self.play(
			my_group.animate.scale(1.5),
		)
		self.play(
			my_group.animate.shift(DOWN*0.5)
		)
		self.wait()

class Target(Scene):
	def construct(self):

		ring_1 = Annulus(inner_radius=0.30,
						 outer_radius=0.60,
						 color=YELLOW_C,
						 fill_opacity=1.0
					)

		ring_2 = Annulus(inner_radius=0.60,
						 outer_radius=0.90,
						 color=YELLOW_C,
						 fill_opacity=1.0
					)

		ring_3 = Annulus(inner_radius=0.90,
						 outer_radius=1.20,
						 color=RED_E,
						 fill_opacity=1.0
					)

		ring_4 = Annulus(inner_radius=1.20,
						 outer_radius=1.50,
						 color=RED_E,
						 fill_opacity=1.0
					)

		ring_5 = Annulus(inner_radius=1.50,
						 outer_radius=1.80,
						 color=WHITE,
						 fill_opacity=1.0
					)

		ring_6 = Annulus(inner_radius=1.80,
						 outer_radius=2.10,
						 color=WHITE,
						 fill_opacity=1.0
					)

		ring_7 = Annulus(inner_radius=2.10,
						 outer_radius=2.40,
						 color=BLUE_D,
						 fill_opacity=1.0
					)

		ring_8 = Annulus(inner_radius=2.40,
						 outer_radius=2.70,
						 color=BLUE_D,
						 fill_opacity=1.0
					)

		self.play(
			DrawBorderThenFill(ring_1),
			DrawBorderThenFill(ring_2),
			DrawBorderThenFill(ring_3),
			DrawBorderThenFill(ring_4),
			DrawBorderThenFill(ring_5),
			DrawBorderThenFill(ring_6),
			DrawBorderThenFill(ring_7),
			DrawBorderThenFill(ring_8),
			run_time=1.5,
			rate_func=linear
		)
		self.wait(2)
