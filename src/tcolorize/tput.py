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


@cache
def fg_red():
    return get_tput("setaf", "196") or ""
 

@cache
def fg_cyan():
    return get_tput("setaf", "44") or ""
 

@cache
def fg_yellow():
    return get_tput("setaf", "190") or ""
 

@cache
def fg_orange():
    return get_tput("setaf", "202") or ""
 

@cache
def fg_light_blue():
    return get_tput("setaf", "42") or ""
 

@cache
def fg_light_green():
    return get_tput("setaf", "2") or ""
 

@cache
def fg_light_green_2():
    return get_tput("setaf", "10") or ""
 

@cache
def fg_light_red():
    return get_tput("setaf", "9") or ""
 

@cache
def bg_black():
    return get_tput("setab", "16") or ""
 

@cache
def bg_light_black():
    return get_tput("setab", "236") or ""
 

@cache
def bg_dark_black():
    return get_tput("setab", "233") or ""
 

@cache
def style_bold():
    return get_tput("bold") or ""
 

@cache
def style_dim():
    return get_tput("dim") or ""
 

@cache
def style_underline():
    return get_tput("smul") or ""


@cache
def reset_all():
    return get_tput("sgr0") or ""


