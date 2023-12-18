#  ________  _________  ___  ___       _______      
# |\   __  \|\___   ___\\  \|\  \     |\  ___ \     
# \ \  \|\  \|___ \  \_\ \  \ \  \    \ \   __/|    
#  \ \  \\\  \   \ \  \ \ \  \ \  \    \ \  \_|/__  
#   \ \  \\\  \   \ \  \ \ \  \ \  \____\ \  \_|\ \ 
#    \ \_____  \   \ \__\ \ \__\ \_______\ \_______\
#     \|___| \__\   \|__|  \|__|\|_______|\|_______|
#           \|__|                                   

import os
import subprocess
from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration

from keys import keys, mod
from colors import colors

##################################################
#
#                      HOOKS
#
##################################################

@hook.subscribe.startup_once
def startup_once():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.startup_complete
def startup_completee():
    qtile.cmd_simulate_keypress([], 'Home')

##################################################
#
#                      GROUPS
#
##################################################

group_names = "123456789"

groups = [Group(name=name, label="") for name in group_names]

for i, (name) in enumerate(group_names, 1):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key( [mod], str(i), lazy.group[name].toscreen(),
                desc="Switch to group {}".format(name), ),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key( [mod, "shift"], str(i), lazy.window.togroup(name, switch_group=False),
                desc="Move focused window to group {}".format(name) ),
        ]
    )

##################################################
#
#                    LAYOUTS
#
##################################################

layouts = [
    layout.Columns(
        border_focus_stack=colors[2],
        border_focus=colors[2],
        border_normal=colors[0],
        border_on_single=True,
        border_width=2,
        margin=6,
        ),
    # layout.Max(),
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

##################################################
#
#                    WIDGETS
#
##################################################

widget_defaults = dict(
    font="JetBrains Mono Nerd Font Mono",
    background=colors[7][0],
    fontsize=12,
)
extension_defaults = widget_defaults.copy()

decoration_group = {
    "decorations": [
        RectDecoration(
            colour=colors[7][0], 
            radius=0,
            filled=True, 
            group=True,
        )
    ],
    "padding": 8,
}

decoration_group_start = {
    "decorations": [
        RectDecoration(
            use_widget_background=True,
            radius=0,
            filled=True, 
            group=True,
            extrawidth=0,
            padding_x=5,
        ),
        PowerLineDecoration(
            path="back_slash",
            color=colors[0][0],
        ),
    ],
    "padding": 8,
}

decoration_group_end = {
    "decorations": [
        RectDecoration(
            use_widget_background=True,
            radius=0,
            filled=True, 
            group=True,
            padding_x=5,
        ),
        PowerLineDecoration(
            path="forward_slash",
            color=colors[7][0],
        ),
    ],
    "padding": 8,
}

##################################################
#
#                     SCREENS
#
##################################################

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    block_highlight_text_color='FF0044',
                    borderwidth=0,
                    fontsize=20,
                    **decoration_group_end
                    ),
                widget.Spacer(
                    length=527,
                    background=colors[0][0],
                    **decoration_group_start
                    ),
                widget.Clock(
                    format=" %a %m.%d ",
                    fontsize=14,
                    **decoration_group
                    ),
                widget.TextBox(
                    text="󰣇",
                    fontsize=30,
                    foreground=colors[2][0],
                    background=colors[0][0],
                    **decoration_group
                    ),
                widget.Clock(
                    format=" %I:%M  ",
                    fontsize=14,
                    **decoration_group_end
                    ),
                widget.Spacer(
                    length=bar.STRETCH,
                    background=colors[0][0],
                    **decoration_group_start
                    ),
                widget.Battery(
                    format="{char}",
                    charge_char="󱐋",
                    discharge_char="󰁹",
                    fontsize=15,
                    update_interval=5,
                    battery=0,
                    **decoration_group
                    ),
                widget.Battery(
                    format="{percent:2.0%}",
                    update_interval=30,
                    battery=0,
                    **decoration_group
                    ),
                widget.TextBox(
                    text="",
                    fontsize=30,
                    **decoration_group
                    ),
                widget.Volume(
                    **decoration_group
                    ),
                widget.TextBox(
                    text="",
                    fontsize=30,
                    **decoration_group
                    ),
                widget.Backlight(
                    format="{percent:2.0%}",
                    backlight_name='intel_backlight',
                    **decoration_group
                    ),
                widget.QuickExit(
                    default_text="󰅙",
                    fontsize=30,
                    countdown_format="󰜺",
                    **decoration_group
                    ),
            ],
            30,
            background=colors[0][0],
            margin=[6, 0, 6, 0],
        ),

        wallpaper='~/Downloads/opeth.jpg',
        wallpaper_mode='fill',

        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
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

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "QTile"
