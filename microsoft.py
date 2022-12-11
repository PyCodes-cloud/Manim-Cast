from manim import *

yellow = "#E19823"
orange = "#D35C31"
blue = "#2C98CB"
green = "#649D5B"

class MicrosoftLogo(Scene):
    def construct(self):
        # First Square!
        square_one = Square(
            side_length=1.0,
            fill_color=orange,
            stroke_color=orange,
            fill_opacity=1
        ).shift(UP+LEFT*2.0)

        # Second Square!
        square_two = Square(
            side_length=1.0,
            fill_color=green,
            stroke_color=green,
            fill_opacity=1
        ).next_to(square_one, RIGHT, buff= 0.2)

        # Third Square!
        square_three = Square(
            side_length=1.0,
            fill_color=blue,
            stroke_color=blue,
            fill_opacity=1
        ).next_to(square_one, DOWN, buff=0.2)

        # Fourth Square!
        square_four = Square(
            side_length=1.0,
            fill_color="#E19823",
            stroke_color="#E19823",
            fill_opacity=1
        ).next_to(square_two, DOWN, buff=0.2)

        self.play(
            DrawBorderThenFill(square_one),
            DrawBorderThenFill(square_two),
            DrawBorderThenFill(square_three),
            DrawBorderThenFill(square_four)
        )
        self.wait()

        text = Text(
            text = "Microsoft",
            font_size = 60,
            t2w = {"Microsoft": BOLD},
            font = "Arial"
        ).next_to(square_two, RIGHT, buff=0.75)\
         .shift(DOWN*0.6)

        self.play(
            AddTextLetterByLetter(text)
        )
        self.wait(2)