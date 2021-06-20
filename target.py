from manim import *

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
