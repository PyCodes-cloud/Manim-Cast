from manim import *

class Car(Scene):
    def construct(self):

        my_rect = Rectangle(width=3, height=1.0, color=BLUE)\
                            .to_edge(LEFT, buff=1)\
                            .shift(DOWN*0.9)

        s1 = Square().shift(DOWN*0.9)\
                     .scale(0.2)\
                     .to_edge(LEFT, buff=3.3)

        s2 = Square().shift(DOWN*0.9)\
                     .scale(0.2)\
                     .to_edge(LEFT, buff=2.3)

        s3 = Square().shift(DOWN*0.9)\
                     .scale(0.2)\
                     .to_edge(LEFT, buff=1.3)

        tier_1 = Circle(radius=0.1, color=ORANGE, fill_opacity=1.0)\
                        .next_to(my_rect, DOWN, buff=0.02)\
                        .shift(LEFT*1)

        tier_2 = Circle(radius=0.1, color=ORANGE, fill_opacity=1)\
                        .next_to(my_rect, DOWN, buff=0.02)\
                        .shift(RIGHT*1)

        cut = Cutout(my_rect, s1, s2, s3, fill_opacity=1, color=DARK_BLUE, stroke_color=RED)

        car = VGroup(cut, tier_1, tier_2)

        self.play(
            Write(cut),
            DrawBorderThenFill(tier_1),
            DrawBorderThenFill(tier_2),
            run_time=1.2
        )
        self.wait(2)

        path1 = Line([-5,-1,0], [-0.2,-1,0], color=WHITE)
        path2 = Line([1.3,-0.4,0], [2.7,1.1,0], color=WHITE)

        path3 = Line([-6,-1.7,0], [1,-1.7,0],color=WHITE)
        path4 = Line([1,-1.7,0], [4,1.3,0], color=WHITE)

        self.play(
            FadeIn(path3),
            FadeIn(path4)
        )

        self.wait()

        self.play(
            MoveAlongPath(car, path1),
            run_time=1.5
        )
        self.wait(2)

        car.shift(RIGHT*1)
        car.rotate(45*DEGREES)

        self.wait(2)

        self.play(
            MoveAlongPath(car, path2),
            run_time=1.5
        )
        self.wait(2)
