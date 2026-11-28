"""Render with Manim Community: manim -qm uttarayan_kite.py UttarayanKite."""
from math import atan2, cos, sin

import numpy as np
from manim import (
    DashedLine, Dot, FadeIn, Line, Polygon,
    ReplacementTransform, RIGHT, Scene, Text, UP, ValueTracker, VGroup,
    always_redraw, smooth,
)


PAPER = "#FAF6EC"
INK = "#172D36"
MUTED = "#40616A"
ORANGE = "#A53E20"
TEAL = "#006A70"
GOLD = "#F7BD55"


def label(words, x, y, size, color=INK, max_width=None):
    text = Text(words, font="Nirmala UI", font_size=size, color=color)
    if max_width and text.width > max_width:
        text.scale_to_fit_width(max_width)
    return text.move_to([x + text.width / 2, y, 0])


class UttarayanKite(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        hand = np.array([-6.0, -1.92, 0.0])
        scale = 0.33
        angle = ValueTracker(atan2(12, 5))

        def tip():
            theta = angle.get_value()
            return hand + 13 * scale * np.array([cos(theta), sin(theta), 0])

        def rig():
            point = tip()
            foot = np.array([point[0], hand[1], 0.0])
            corner = VGroup(
                Line(foot - 0.12 * RIGHT, foot - 0.12 * RIGHT + 0.12 * UP),
                Line(foot - 0.12 * RIGHT + 0.12 * UP, foot + 0.12 * UP),
            ).set_color(MUTED).set_stroke(width=2)
            kite = Polygon([0,0.27,0], [0.19,0,0], [0,-0.27,0], [-0.19,0,0],
                           fill_color=GOLD, fill_opacity=1, stroke_color=INK, stroke_width=2).shift(point)
            return VGroup(
                Line(hand, foot, color=TEAL, stroke_width=5),
                DashedLine(foot, point, dash_length=0.12, color=TEAL, stroke_width=4),
                Line(hand, point, color=ORANGE, stroke_width=5),
                corner, kite, Dot(point, radius=0.038, color=INK), Dot(hand, radius=0.07, color=INK),
            )

        def card(question, gujarati, count, equation, result, gu_result):
            return VGroup(
                label(question, 0.55, 1.60, 28, INK, 5.85),
                label(gujarati, 0.55, 1.04, 24, MUTED, 5.95),
                label(count, 0.55, 0.12, 22, ORANGE),
                label(equation, 0.55, -0.52, 33, INK, 5.8),
                label(result, 0.55, -1.26, 27, TEAL, 5.8),
                label(gu_result, 0.55, -1.85, 23, TEAL, 5.94),
            )

        self.add(label("ઉત્તરાયણ  /  Ahmedabad • Kite geometry", -6.35, 3.27, 29, INK, 12.4),
                 label("Does a 13 m string fix the height?", -6.35, 2.67, 28, MUTED),
                 label("Hand level  /  હાથનું સ્તર", -6.0, -2.40, 21, MUTED),
                 Line([-6.35,-2.91,0], [6.35,-2.91,0], color="#BDCCC9", stroke_width=2),
                 label("ModuMath   •   Straight, taut string; height is measured above the hand.",
                       -6.35, -3.30, 19, MUTED, 12.3))
        # All three lengths use the same scale, including throughout the rotation.
        self.add(always_redraw(rig))
        first = card("Horizontal distance: 5 m", "આડું અંતર: 5 મીટર", "STRING  13 m",
                     "h² = 13² − 5² = 144", "Height above hand: 12 m", "હાથથી ઉપરની ઊંચાઈ: 12 મીટર")
        self.play(FadeIn(first), run_time=0.8)
        self.wait(3.4)
        second = card("Move the kite farther out.", "આડું અંતર વધારો.", "SAME STRING  13 m",
                      "What changes?", "Predict the new height.", "નવી ઊંચાઈ વિચારો.")
        self.play(ReplacementTransform(first, second), run_time=0.6)
        self.play(angle.animate.set_value(atan2(5, 12)), run_time=2.5, rate_func=smooth)
        self.wait(1.8)
        third = card("Horizontal distance: 12 m", "આડું અંતર: 12 મીટર", "SAME STRING  13 m",
                     "h² = 13² − 12² = 25", "Height above hand: 5 m", "હાથથી ઉપરની ઊંચાઈ: 5 મીટર")
        self.play(ReplacementTransform(second, third), run_time=0.6)
        self.wait(4)
