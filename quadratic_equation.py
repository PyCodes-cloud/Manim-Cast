from manim import*

class quadratic_formula(Scene):
    def construct(self):
        text = Text("Quadratic Formula ").scale(0.8)\
                        .to_edge(UP)\
                        .set_color(BLUE)
        self.play(
            Write(text),
            run_time=0.8
        )
        self.wait()

        formu = MathTex("ax^{2} + bx + c = 0").scale(1.0)\
                            .set_color_by_gradient(YELLOW,ORANGE)\
                            .to_edge(LEFT,buff=1.5)\
                            .next_to(text,DOWN,buff=0.4)

        frame = SurroundingRectangle(formu, buff=0.1,fill_opacity=0)
        frame.set_color_by_gradient(BLUE,RED,GREEN_D)
        self.play(
            Write(formu)
        )
        self.play(
            ShowCreation(frame)
        )
        self.wait(2)

        self.play(
            Uncreate(frame),
            run_time=1.5
        )

        text_1 = Text("Dividing this equation by a we get:").scale(0.70)\
                                .set_color(ORANGE)\
                                .next_to(formu,DOWN,buff=0.3)

        self.play(
            Write(text_1),
            run_time=1.5
        )
        self.wait()

        formu_1 = MathTex("\\frac{a x^{2}+ bx + c}{a}=0").scale(1.0)\
                                .set_color_by_gradient(PINK,GOLD_D)\
                                .next_to(text_1,DOWN,buff=0.3)
        self.play(
            ReplacementTransform(formu.copy(), formu_1),
            run_time=1.5
        )
        self.wait(2)

        formu_2 = MathTex("x^{2}+","\\frac{b}{a}x+","\\frac{c}{a}","=0").scale(1.0)\
                                .set_color_by_gradient(BLUE,YELLOW)\
                                .next_to(formu_1,DOWN,buff=0.3)
        self.play(
            Write(formu_2[0])
        )
        self.play(
            Write(formu_2[1])
        )
        self.play(
            Write(formu_2[2])
        )
        self.play(
            Write(formu_2[3])
        )
        self.wait(3)

        text_2 = Text("Using completing the square method we get -:").scale(0.70)\
                                .set_color(YELLOW)\
                                .next_to(formu_2,DOWN,buff=0.3)

        self.play(
            Write(text_2),
            run_time=1.5
        )
        self.wait(2)

        formu_3 = MathTex("x^{2}+\\frac{b}{a}x+",
                          "\\left( \\frac{b}{2a} \\right)^{2}",
                          "-\\left( \\frac{b}{2a} \\right)^{2}",
                          "= -\\frac{c}{a}"
                          ).scale(1.0)

        formu_3[0].set_color(BLUE)
        formu_3[1].set_color(ORANGE)
        formu_3[2].set_color(GREEN_D)
        formu_3[3].set_color(PINK)

        formu_3[0].next_to(text_2,DOWN,buff=0.3)
        formu_3[1].next_to(formu_3[0],buff=0.1)
        formu_3[2].next_to(formu_3[1],buff=0.1)
        formu_3[3].next_to(formu_3[2],buff=0.1)

        group_1 = VGroup(formu_3[0], formu_3[1], formu_3[2], formu_3[3])
        group_1.shift(LEFT*2)

        self.play(
            ReplacementTransform(formu_2[0].copy(), formu_3[0]),
            ReplacementTransform(formu_2[0].copy(), formu_3[0]),
            run_time=1.5
        )
        self.play(
            Write(formu_3[1]),
            run_time=1.5
        )
        self.play(
            Write(formu_3[2]),
            run_time=1.5
        )
        self.play(
            ReplacementTransform(formu_2[2].copy(), formu_3[3]),
            run_time=1.5
        )
        self.wait(3)

        self.remove(text, text_1,text_2, formu, formu_1, formu_2[0],
        formu_2[1], formu_2[2], formu_2[3])

        self.wait()

        self.play(
            group_1.animate.shift(UP*6),
            run_time=1.5
        )
        self.wait(2)

        formu_4 = MathTex("\\left ( x + \\frac{b}{2a} \\right )^{2}",
                          "= \\frac{b^{2}}{4a^{2}} - \\frac{c}{a}"
                          ).scale(1.0)\
                           .set_color_by_gradient(ORANGE, GOLD_D, RED)

        formu_4[0].next_to(formu_3[0],DOWN,buff=0.3)
        formu_4[1].next_to(formu_4[0],buff=0.1)

        self.play(
            ReplacementTransform(formu_3[0].copy(), formu_4[0]),
            ReplacementTransform(formu_3[1].copy(), formu_4[0]),
            run_time=1.5
        )
        self.play(
            ReplacementTransform(formu_3[2].copy(), formu_4[1]),
            ReplacementTransform(formu_3[3].copy(), formu_4[1]),
            run_time=1.5
        )
        self.wait(3)

        formu_5 = MathTex("\\left ( x + \\frac{b}{2a} \\right )^{2}",
                          "= \\frac{b^{2} - 4ac}{4a^{2}}"
                          ).scale(1.0)\
                           .set_color_by_gradient(BLUE,PINK)

        formu_5[0].next_to(formu_4[0],DOWN,buff=0.3)
        formu_5[1].next_to(formu_5[0], buff=0.1)

        self.play(
            ReplacementTransform(formu_4[0].copy(), formu_5[0]),
            run_time=1.5
        )
        self.wait()
        self.play(
            ReplacementTransform(formu_4[1].copy(), formu_5[1]),
            run_time=1.5
        )
        self.wait(3)

        formu_6 = MathTex("\\left ( x + \\frac{b}{2a} \\right )",
                          "= \\pm \\frac{\\sqrt{b^{2}-4ac}}{2a}"
                         ).scale(1.0)\
                          .set_color_by_gradient(ORANGE,GREEN_D)

        formu_6[0].next_to(formu_5[0],DOWN,buff=0.3)
        formu_6[1].next_to(formu_6[0], buff=0.1)

        self.play(
            ReplacementTransform(formu_5[0].copy(), formu_6[0]),
            run_time=1.5
        )
        self.wait()
        self.play(
            ReplacementTransform(formu_5[1].copy(), formu_6[1]),
            run_time=1.5
        )
        self.wait(3)

        formu_7 = MathTex("x=-\\frac{b}{2a}",
                          "\\pm \\frac{\\sqrt{b^{2}-4ac}}{2a}"
                         ).scale(1.0)\
                          .set_color_by_gradient(RED,YELLOW)

        formu_7[0].next_to(formu_6[0],DOWN,buff=0.3)
        formu_7[1].next_to(formu_7[0], buff=0.1)

        self.play(
            ReplacementTransform(formu_6[0].copy(), formu_7[0]),
            run_time=1.5
        )
        self.wait()
        self.play(
            ReplacementTransform(formu_6[1].copy(), formu_7[1]),
            run_time=1.5
        )
        self.wait(3)

        formu_8 = MathTex("x = \\frac{-b \\pm \\sqrt{b^{2}-4ac}}{2a}").scale(1.0)\
                        .set_color(BLUE)\
                        .set_color_by_gradient(RED,GOLD_D)

        box_1 = SurroundingRectangle(formu_8,buff=0.1)

        background = AnimatedBoundary(box_1, colors=[BLUE,RED,ORANGE], cycle_rate=3)

        self.remove(formu_4[0], formu_4[1], formu_5[0], formu_5[1], formu_6[0], formu_6[1],
        formu_3[0], formu_3[1], formu_3[2], formu_3[3])

        self.play(
            ReplacementTransform(formu_7, formu_8),
            run_time=1.5
        )
        self.play(
            ShowCreation(box_1),
            ShowCreation(background),
            run_time=2
        )
        self.wait(5)

class thumbnail(Scene):
    def construct(self):
        text = Text("Quadratic Formula", font = 'Times New Roman')\
                                    .scale(2.0)\
                                    .set_color_by_gradient(YELLOW,PINK)\
                                    .to_edge(UP)
        self.play(
            Write(text)
        )


        text_1 = Text("Why for quadratic equation ", font = 'Times New Roman')\
                                    .scale(1.8)\
                                    .set_color(GREEN_D)\
                                    .next_to(text,DOWN,buff=0.6)\
                                    .to_edge(LEFT,buff=0.5)
        self.play(
            Write(text_1)
        )

        eqn = MathTex("ax^{2} + bx + c = 0").scale(2.0)\
                                    .set_color(ORANGE)\
                                    .next_to(text_1,DOWN,buff=0.4)

        self.play(
            Write(eqn)
        )

        formu = MathTex("x = \\frac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a} \\, \\, ?").scale(2.0)\
                                    .set_color_by_gradient(BLUE,ORANGE,RED)\
                                    .next_to(eqn,DOWN,buff=0.8)
        self.play(
            Write(formu)
        )
