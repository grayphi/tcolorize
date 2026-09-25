# vim:ts=4:sw=4:cc=80:et:si:sta:ai:nu:nowrap:cul:sm:is:hls:pt=<F3>:
# pylint: disable=missing-module-docstring, missing-function-docstring
# pylint: disable=trailing-newlines

import os
import shutil
import subprocess
from functools import cache


@cache
def can_tput():
    return (
        os.isatty(1)
        and shutil.which("tput") is not None
    )


@cache
def get_tput(*args):
    if not can_tput():
        return None 

    result = subprocess.run(
        ["tput", *args],
        capture_output=True,
        text=True,
    )

    if result and result.returncode == 0:
        return result.stdout


class Fg:
    LIGHT_GREEN = 2
    LIGHT_RED = 9
    LIGHT_GREEN_2 = 10
    LIGHT_BLUE = 42
    CYAN = 44
    YELLOW = 190
    ORANGE = 202
    RED = 196


class Bg:
    BLACK = 16
    DARK_BLACK = 233
    LIGHT_BLACK = 236


class Style:
    BOLD = "bold"
    DIM = "dim"
    UNDERLINE = "smul"


class Other:
    RESET_ALL = "sgr0"


fg = Fg()
bg = Bg()
style = Style()
other = Other()


@cache
def fg_red():
    return get_tput("setaf", fg.RED) or ""
 

@cache
def fg_cyan():
    return get_tput("setaf", fg.CYAN) or ""
 

@cache
def fg_yellow():
    return get_tput("setaf", fg.YELLOW) or ""
 

@cache
def fg_orange():
    return get_tput("setaf", fg.ORANGE) or ""
 

@cache
def fg_light_blue():
    return get_tput("setaf", fg.LIGHT_BLUE) or ""
 

@cache
def fg_light_green():
    return get_tput("setaf", fg.LIGHT_GREEN) or ""
 

@cache
def fg_light_green_2():
    return get_tput("setaf", fg.LIGHT_GREEN_2) or ""
 

@cache
def fg_light_red():
    return get_tput("setaf", fg.LIGHT_RED) or ""
 

@cache
def bg_black():
    return get_tput("setab", bg.BLACK) or ""
 

@cache
def bg_light_black():
    return get_tput("setab", bg.LIGHT_BLACK) or ""
 

@cache
def bg_dark_black():
    return get_tput("setab", bg.DARK_BLACK) or ""
 

@cache
def style_bold():
    return get_tput(style.BOLD) or ""
 

@cache
def style_dim():
    return get_tput(style.DIM) or ""
 

@cache
def style_underline():
    return get_tput(style.UNDERLINE) or ""


@cache
def reset_all():
    return get_tput(other.RESET_ALL) or ""


