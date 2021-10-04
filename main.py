from manim import *
import functools

# Text = functools.partial(Text, font="Comic Sans")

'''
The first scene:

In this scene we animate the simplification of an equation
'''
class S1(Scene):
    def construct(self):
        # Create and display the starting equation on the top left of the screen
        q1 = MathTex('{(2x+6)\over{2}} - x', ' = 3').scale(2).to_edge(UL).shift(RIGHT*0.5)
        # Display the text using the write animation and run for 4 seconds
        self.play(Write(q1, run_time=4))
        self.wait(1)
        
        # Create and display the second simplification equation just below the first
        q2 = MathTex('0.5(2x+6) - x = 3').set_color(YELLOW_C).scale(1.5).next_to(q1, DOWN, buff=1)
        # Use the TransformFromCopy function to animate a transition from the first equation to the second
        self.play(TransformFromCopy(q1, q2))

        # Third equation
        q3 = MathTex('x + 3 - x = 3').set_color(RED_C).scale(1.5).next_to(q2, DOWN, buff=1)
        self.play(TransformFromCopy(q2, q3))

        # Fourth equation
        q4 = MathTex('3 = 3').set_color(BLUE_C).scale(1.5).move_to(q3)
        # Instead of the TransformFromCopy function, we simply transform the third equation into the fourth
        self.play(Transform(q3, q4))

        # Highlight the solution
        r1 = SurroundingRectangle(q4, color=YELLOW)
        self.play(Create(r1))
        self.wait(0.5)
        self.play(FadeOut(r1))
        self.wait()

        self.play(*map(FadeOut, self.mobjects))
        self.wait()

class S2(MovingCameraScene):
    def construct(self):
        # Save the initial camera state for later
        self.camera.frame.save_state()

        # Create the axes
        axes = Axes(
            x_range=[-100, 103, 20],
            y_range=[-100, 103, 20],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.array([-100, 100, -50, 50]),
                "numbers_with_elongated_ticks": np.arange(-100, 100, 20),
            },
            y_axis_config={
                "numbers_to_include": np.array([-100, 100, -50, 50]),
                "numbers_with_elongated_ticks": np.arange(-100, 100, 20),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        # Graph using the simplified function
        graph = axes.get_graph(lambda x: 3, color=BLUE)

        moving_dot = Dot(axes.i2gp(graph.t_min, graph), color=ORANGE)
        # Create a dot at the left side and right side of the graph
        dot_1 = Dot(axes.i2gp(graph.t_min, graph))
        dot_2 = Dot(axes.i2gp(graph.t_max, graph))

        graph_label = axes.get_graph_label(
            graph, MathTex('{(2x+6)\over{2}} - x', ' = 3'), x_val=-10, direction=UP / 2
        ).shift(LEFT*2).scale(0.5)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        x_coord = ValueTracker(0)

        def update_text(mob):
            x = axes.point_to_coords(moving_dot.get_center())[0]
            mob.become(
                Text(str(round(x, 2)) + ', 3')
            ).move_to(moving_dot.get_center()).shift(UP*0.75).scale(0.5)
            #mob.become(Text(str()).move_to(moving_dot.get_center()).shift(UP*0.5).scale(0.5))

        self.play(FadeIn(axes, run_time=2), Wait(run_time=0.1), Write(axes_labels, run_time=1))
        self.play(Create(graph, run_time=5))
        self.play(Write(graph_label))
        self.wait(2)

        t1 = Text('5')

        # Intiialize the camera animation
        self.play(FadeIn(dot_1, dot_2, moving_dot))
        self.add(dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))
        self.camera.frame.add_updater(update_curve)
        self.add(t1)
        # Add the update text updater
        t1.add_updater(update_text)
        # Animate the function
        self.play(MoveAlongPath(moving_dot, graph, rate_func=smooth, run_time=4), MoveAlongPath(t1, graph, rate_func=smooth, run_time=4))
        self.camera.frame.remove_updater(update_curve)
        self.wait(0.2)
        self.play(Restore(self.camera.frame))
        self.wait()
        t1.remove_updater(update_text)

        # Fade out all objects
        self.play(*map(FadeOut, self.mobjects))
        self.wait()

class S3(Scene):
    def construct(self):
        # Create the initial equation like Scene 1
        q1 = MathTex('{(2', 'x', '+6)\over{2}} - ', 'x', '= 3').scale(2).to_edge(UL).shift(RIGHT*0.5)
        self.play(Write(q1, run_time=4))
        self.wait(1)

        # Create the 42 number
        n1 = MathTex('42').scale(2).to_edge(UR)
        self.play(Write(n1))

        # Animate setting x and 42 to red
        n2 = n1.copy().set_color(RED_C)
        q2 = q1.copy()
        q2.set_color_by_tex('x', RED_C)
        self.play(TransformFromCopy(n1, n2), Wait(1), Transform(q1, q2))

        q3 = MathTex('{(2', '(', '42', ')', '+6)\over{2}} - ', '(', '42', ')', '= 3').scale(1.5).next_to(q2, DOWN)
        q3.set_color_by_tex('42', RED_C)
        self.play(TransformFromCopy(q2, q3))

        q4 = MathTex('{90}\over{2}} - ', '42', '= 3').scale(1.5).next_to(q3, DOWN, buff=1)
        q4.set_color_by_tex('42', RED_C)
        self.play(TransformFromCopy(q3, q4))

        q5 = MathTex('45 - ', '42', '= 3').scale(1.5).move_to(q4)
        q5.set_color_by_tex('42', RED_C)
        self.play(Transform(q4, q5))

        q6 = MathTex('3', '= 3', color=BLUE_C).scale(1.5).move_to(q5)
        self.play(Transform(q4, q6))

        r1 = SurroundingRectangle(q6, color=YELLOW)
        self.play(Create(r1))
        self.wait(0.5)
        self.play(FadeOut(r1))
        self.wait()

        self.play(*map(FadeOut, self.mobjects))
        self.wait()

# class S3(Scene):
#     def construct(self):
#         axes = Axes(
#             x_range=[-10, 10.3, 1],
#             y_range=[-1.5, 1.5, 1],
#             x_length=10,
#             axis_config={"color": GREEN},
#             x_axis_config={
#                 "numbers_to_include": np.arange(-10, 10.01, 2),
#                 "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
#             },
#             tips=False,
#         )
#         axes_labels = axes.get_axis_labels()
#         sin_graph = axes.get_graph(lambda x: np.sin(x), color=BLUE)
#         cos_graph = axes.get_graph(lambda x: np.cos(x), color=RED)

#         sin_label = axes.get_graph_label(
#             sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
#         )
#         cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

#         vert_line = axes.get_vertical_line(
#             axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
#         )
#         line_label = axes.get_graph_label(
#             cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
#         )

#         self.play(FadeIn(axes, run_time=2), Wait(run_time=0.1), Write(axes_labels, run_time=1))
#         self.wait()
#         self.play(Create(cos_graph, run_time=5), Wait(run_time=0.5), Create(sin_graph, run_time=5))
#         self.wait()
#         self.play(Write(sin_label), Write(cos_label))
#         self.play(Create(vert_line), Wait(run_time=0.4), Write(line_label))
#         self.wait(5)
