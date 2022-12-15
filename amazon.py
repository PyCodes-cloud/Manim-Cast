from manim import *

class Amazon(Scene):
    def construct(self):
        letter = Text(
            text = "amazon",
            font = "Roman",
            font_size = 60,
            # Setting bold!
            t2w = {"amazon": BOLD}
        )

        # Creating curved arrow!
        arrow = CurvedArrow(
            start_point=np.array([-1.2, -0.35, 0]),
            end_point=np.array([0.5, -0.35, 0]),
            angle = 1.25,
            tip_length= 0.2,
            color="#ffb703"
        )
        self.play(
            Write(letter),
            Create(arrow),
            run_time=2.0
        )
        self.wait(2)