from manim import *

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
