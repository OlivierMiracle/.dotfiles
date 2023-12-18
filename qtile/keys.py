import popups
from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [
    Key([mod], "r", lazy.spawn("rofi -show drun -font 'JetBrains Mono Nerd Font 12' "),
        desc="App launcher"),
    
    Key([mod], "Tab", lazy.spawn("rofi -show window -f 'JetBrains Mono Nerd Font 12'"), 
        desc="Tab between opened windows"),
    
    #Run Terminal
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "c", lazy.window.kill(), 
        desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), 
        desc="Toggle fullscreen on the focused window", ),
    Key([mod], "t", lazy.window.toggle_floating(), 
        desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), 
        desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), 
        desc="Shutdown Qtile"),

    #Keybindings for volume control
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 4- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 4+ unmute")),

    #microphone
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Dmic0 toggle")),
            
    #Keybindings for brightness control
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5000-")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5000+")),

    #####
    #       Keys for popups
    #####

    Key([], "Home", lazy.function(popups.show_wall_screen))
]