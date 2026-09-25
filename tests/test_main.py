# vim:ts=4:sw=4:cc=80:et:si:sta:ai:nu:nowrap:cul:sm:is:hls:pt=<F3>:
# pylint: disable=missing-module-docstring, missing-function-docstring
# pylint: disable=trailing-newlines


from tcolorize import main
from tcolorize import tput


def test_can_color():
    if tput.can_tput():
        msg1 = "this is sample test string."
        msg2 = "random string"
        msg3 = "another random string"
        funcs = [
            main.as_red,
            main.as_cyan,
            main.as_yellow,
            main.as_orange,
            main.as_light_blue,
            main.as_light_green,
            main.as_light_green_2,
            main.as_light_red,
            main.on_black,
            main.on_light_black,
            main.on_dark_black,
            main.as_bold,
            main.as_dim,
            main.as_underline,
        ]

        for fn in funcs:
            assert fn(msg1) != msg1
            assert len(fn(msg1)) > len(msg1)


        for f in funcs:
            for g in funcs:
                assert f(msg1 + g(msg2) + f(msg3)) != msg1 + msg2 + msg3
                assert len(f(msg1 + g(msg2) + f(msg3))) > len(
                    msg1 + msg2 + msg3)



def test_cant_color():
    if not tput.can_tput():
        msg1 = "this is sample test string."
        msg2 = "random string"
        msg3 = "another random string"
        funcs = [
            main.as_red,
            main.as_cyan,
            main.as_yellow,
            main.as_orange,
            main.as_light_blue,
            main.as_light_green,
            main.as_light_green_2,
            main.as_light_red,
            main.on_black,
            main.on_light_black,
            main.on_dark_black,
            main.as_bold,
            main.as_dim,
            main.as_underline,
        ]

        for fn in funcs:
            assert len(fn("")) == 0

        for fn in funcs:
            assert fn(msg1) == msg1
            assert len(fn(msg1)) == len(msg1)


        for f in funcs:
            for g in funcs:
                assert f(msg1 + g(msg2) + f(msg3)) == msg1 + msg2 + msg3
                assert len(f(msg1 + g(msg2) + f(msg3))) == len(
                    msg1 + msg2 + msg3)


