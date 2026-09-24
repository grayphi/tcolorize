# vim:ts=4:sw=4:cc=80:et:si:sta:ai:nu:nowrap:cul:sm:is:hls:pt=<F3>:
# pylint: disable=missing-module-docstring, missing-function-docstring
# pylint: disable=trailing-newlines

import os

import tput


_NO_COLOR = False
_NC_ENVARS = [
    "NO_COLOR",
    "TCOLORIZE_NO_COLOR"
]
_NC_ENV_VALS = ["0", "no_color", "true"]

for ev in _NC_ENVARS:
    if os.environ.get(ev, "").lower() in _NC_ENV_VALS:
        _NO_COLOR = True
        break


def _cont(t, es):
    return t.replace(tput.reset_all(), tput.reset_all() + es)


def _color(t, es):
    return es + _cont(t, es) + tput.reset_all()


def as_red(text):
    return text if _NO_COLOR else _color(text, tput.fg_red())


def as_cyan(text):
    return text if _NO_COLOR else _color(text, tput.fg_cyan())
    

def as_yellow(text):
    return text if _NO_COLOR else _color(text, tput.fg_yellow())
    

def as_orange(text):
    return text if _NO_COLOR else _color(text, tput.fg_orange())
    

def as_light_blue(text):
    return text if _NO_COLOR else _color(text, tput.fg_light_blue())
    

def as_light_green(text):
    return text if _NO_COLOR else _color(text, tput.fg_light_green())
    

def as_light_green_2(text):
    return text if _NO_COLOR else _color(text, tput.fg_light_green_2())
    

def as_light_red(text):
    return text if _NO_COLOR else _color(text, tput.fg_light_red())
    

def on_black(text):
    return text if _NO_COLOR else _color(text, tput.bg_black())
    

def on_light_black(text):
    return text if _NO_COLOR else _color(text, tput.bg_light_black())
    

def on_dark_black(text):
    return text if _NO_COLOR else _color(text, tput.bg_dark_black())
    

def as_bold(text):
    return text if _NO_COLOR else _color(text, tput.style_bold())
    

def as_dim(text):
    return text if _NO_COLOR else _color(text, tput.style_dim())
    

def as_underline(text):
    return text if _NO_COLOR else _color(text, tput.style_underline())
    

