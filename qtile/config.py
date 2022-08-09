# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from faulthandler import disable
import os
import subprocess
from libqtile import hook

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
red = 'wlan0'
color_barra = "#15101c"
fuente_predeterminada = "Ubuntu Mono Nerd Font"
tamano_barra = 24
tamano_fuente = 14
color_activo = "#f1fa8c"
tamano_iconos = 20
color_fg = "#ffffff"
color_bg = "#15101c"
color_inactivo = "#6272a4"
color_oscuro = "#44475a"
color_claro = "#bd93f9"
color_urgent = "#ff5555"
color_texto1 = "#bd93f9"
color_grupo1 = "#c13d3d" #rojo pastel
color_grupo2 = "#733dc1"
color_grupo3 = "#3d40c1"
color_grupo4 = "#e7611c"
mod = "mod4"
terminal = guess_terminal()

def fc_separador():
    return widget.Sep(
        padding = 6,
        foreground = color_bg,
        linewidth = 0,
    )

def fc_rectan(vColor,tipo):
    if tipo == 0:
        icono = "" #nf-ple-left_half_circle_thick
    else:
        icono = "" #nf-ple-right_half_circle_thick
    return widget.TextBox(
        text = icono,
        fontsize = 26 + 5,
        foreground = vColor,
        background = color_bg,
        padding = -3,
    )
    
def fc_icono(icono, color_grupo):
    return widget.TextBox(
        text = icono,
        foreground = color_fg,
        background = color_grupo,
        fontsize = 26
    )





keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    #menu
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Menu"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "s", lazy.spawn("scrot"), desc="Menu"),
]

#Nombre de iconos nerd fonts
# nf-linux-gentoo
# nf-dev-firefox
# nf-oct-terminal
# nf-dev-code
# nf-mdi-folder_open
# nf-mdi-forum_outline
# nf-fa-gamepad
# nf-fa-podcast
# nf-fa-desktop
groups = [Group(i) for i in [
    "  ","  ","  ","  ","  ","  ","  ","  ","  ",
    #"uno","dos","tres","cuatro"
    ]]

for i, group in enumerate(groups):
    numeroEscritorio =str(i+1) 
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font= fuente_predeterminada,
    fontsize= tamano_fuente,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=color_activo,
                    border_width = 1,
                    disable_drag = True,
                    fontsize = tamano_iconos,
                    foreground = color_fg,
                    highlight_method = 'block', #tambien se pudede con line
                    inactive = color_inactivo,
                    margin_x = 0,
                    margin_y = 5,
                    other_current_screen_border = color_oscuro,
                    other_screen_border = color_oscuro,
                    padding_x = 0,
                    padding_y = 10,
                    this_current_screen_border = color_claro,
                    this_screen_border = color_claro,
                    urgent_alert_method = 'block',
                    urgent_border = color_urgent,
                ),
                fc_separador(),
                widget.Prompt(
                    foreground = color_texto1,
                    background = color_bg,
                ),
                widget.WindowName(
                    foreground = color_texto1,
                    background = color_bg,
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # grupo 0
                
                widget.Systray(),
                
                # fin del grupo 0
                fc_separador(),
                # grupo 1
                fc_rectan(color_grupo1,0),
                fc_icono(" ", color_grupo1), #nf-fa-thermometer
                widget.ThermalSensor(
                    foreground = color_fg,
                    background = color_grupo1,
                    threshold = 70,
                    tag_sensor = "temp1",
                    fmt = 'Temp1:{}',
                ),
                fc_rectan(color_grupo1, 1),
                #fin del grupo 1
                fc_separador(),
                fc_rectan(color_grupo3,0),
                fc_icono("  ", color_grupo3),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",
                   foreground = color_fg,
                   background = color_grupo3,
                ),
                fc_icono(" 龍 ", color_grupo3),
                widget.Net(
                   foreground = color_fg,
                   background = color_grupo3,
                   format = ' {down} {up}  ',
                   interface = red,
                   use_bits = 'true'
                ),
                fc_rectan(color_grupo3,1),
                fc_separador(),
                fc_rectan(color_grupo4,0),
                widget.CurrentLayoutIcon(
                   background = color_grupo4,
                   scale = 0.7,
                ),
                widget.CurrentLayout(
                   background = color_grupo4,
                ),
                fc_rectan(color_grupo4,1),
                fc_separador(),
            ],
            tamano_barra,
            background=color_barra,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
