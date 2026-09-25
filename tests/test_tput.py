# vim:ts=4:sw=4:cc=80:et:si:sta:ai:nu:nowrap:cul:sm:is:hls:pt=<F3>:
# pylint: disable=missing-module-docstring, missing-function-docstring
# pylint: disable=trailing-newlines


from tcolorize import tput


def test_tput():
    assert tput.can_tput() in [True, False]


def test_can_tput():
    if tput.can_tput():
	    assert len(tput.fg_red()) > 0
	    assert len(tput.fg_cyan()) > 0
	    assert len(tput.fg_yellow()) > 0
	    assert len(tput.fg_orange()) > 0
	    assert len(tput.fg_light_blue()) > 0
	    assert len(tput.fg_light_green()) > 0
	    assert len(tput.fg_light_green_2()) > 0
	    assert len(tput.fg_light_red()) > 0
	    assert len(tput.bg_black()) > 0
	    assert len(tput.bg_light_black()) > 0
	    assert len(tput.bg_dark_black()) > 0
	    assert len(tput.style_bold()) > 0
	    assert len(tput.style_dim()) > 0
	    assert len(tput.style_underline()) > 0
	    assert len(tput.reset_all()) > 0


def test_can_not_tput():
    if not tput.can_tput():
	    assert len(tput.fg_red()) == 0
	    assert len(tput.fg_cyan()) == 0
	    assert len(tput.fg_yellow()) == 0
	    assert len(tput.fg_orange()) == 0
	    assert len(tput.fg_light_blue()) == 0
	    assert len(tput.fg_light_green()) == 0
	    assert len(tput.fg_light_green_2()) == 0
	    assert len(tput.fg_light_red()) == 0
	    assert len(tput.bg_black()) == 0
	    assert len(tput.bg_light_black()) == 0
	    assert len(tput.bg_dark_black()) == 0
	    assert len(tput.style_bold()) == 0
	    assert len(tput.style_dim()) == 0
	    assert len(tput.style_underline()) == 0
	    assert len(tput.reset_all()) == 0
        

