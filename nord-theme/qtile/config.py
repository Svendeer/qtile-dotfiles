# Svendeer's Qtile config

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os, subprocess

mod = "mod4"

def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

autostart( )

keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Floating window
    Key([mod], "t", lazy.window.toggle_floating()),

    # Normalize
    Key([mod], "n", lazy.layout.normalize()),

    # Toggle bwtween layouts
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.toggle_split()),

    # Toggle between different layouts as defined below
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),

    Key([mod], "q", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    # Volume
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -1%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +1%")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 1")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 1")),

    # Programm keys
    Key([mod],          "Return", lazy.spawn("st"), desc="Launch ST terminal"),
    Key([mod],          "s", lazy.spawn("subl"), lazy.spawn("notify-send 'Abriendo: Sublime-text.'")),
    Key([mod],          "p", lazy.spawn('rofi -combi-modi window,drun,ssh -font "Iosevka 7" -show combi -show-icons')),

    Key([mod, "shift"], "b", lazy.spawn("netsurf"), lazy.spawn("notify-send 'Abriendo: netsurf.'")),
    Key([mod, "shift"], "p", lazy.spawn("pcmanfm"), lazy.spawn("notify-send 'Abriendo: PcmanFM.'")),
    Key([mod, "shift"], "f", lazy.spawn("flameshot gui")),
    Key([mod, "shift"], "t", lazy.spawn("telegram-desktop"), lazy.spawn("notify-send 'Abriendo: Telegram.'")),
    Key([mod, "shift"], "c", lazy.spawn("sh /home/svendeer/.config/qtile/Screenshot.sh")),
    Key([mod, "shift"], "l", lazy.spawn("leafpad"), lazy.spawn("notify-send 'Abriendo: leafpad...'")),
    Key([mod, "shift"], "a", lazy.spawn("atril"), lazy.spawn("notify-send 'Abriendo: Atril.'")),
    Key([mod, "shift"], "w", lazy.spawn("whatsdesk"), lazy.spawn("notify-send 'Abriendo: Whatsdesk.'")),
    Key([mod, "shift"], "m", lazy.spawn("megasync"), lazy.spawn("notify-send 'Abriendo: MEGA sync'")),
    Key([mod, "shift"], "Return", lazy.spawn("uxterm"), desc="Launch xterm"),

    Key([mod, "control"], "t", lazy.spawn("tor-browser"), lazy.spawn("notify-send 'Abriendo: Tor.'")),
    Key([mod, "control"], "p", lazy.spawn("picom"), lazy.spawn("notify-send 'Iniciando compositor.'")),
    Key([mod, "control"], "k", lazy.spawn("killall picom"), lazy.spawn("notify-send 'Cerrando compositor.'")),
    Key([mod, "control"], "m", lazy.spawn("microsoft-edge-dev"), lazy.spawn("notify-send 'Abriendo: Microsoft Edge.'")),
    Key([mod, "control"], "c", lazy.spawn("code"), lazy.spawn("notify-send 'Abriendo: VS Code.'")),
    Key([mod, "control"], "w", lazy.spawn("nitrogen"), lazy.spawn("notify-send 'Abriendo: nitrogen.'")),
    Key([mod, "control"], "s", lazy.spawn("scrot -s -e 'mv $f /home/svendeer/Pictures/Screenshots/'")),
]

# ㈠ ㈡ ㈢ ㈣ ㈤ ㈥ ㈦ ㈧ ㈨
#  ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨
# ⓵ ⓶ ⓷ ⓸ ⓹ ⓺ ⓻ ⓼ ⓽
# ⓿ ❶ ❷ ❸ ❹ ❺ ❻ ❼ ❽ ❾ 

#groups = [
#        Group(i) for i in "1234567"
#]

groups = [Group(i) for i in [
    "  ", "  ", "  ", " ﬏ ", "  ", "  ", "  ",
    #"⓿", "❶", "❷", "❸", "❹", "❺", "❻", "❼",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    layout.Floating(
       border_focus="#800000",
       border_width=1,
    ),
    layout.Bsp(
        margin=5,
        padding=5,
        border_width=1,
        border_focus='#800000',
    ),
    layout.MonadTall(
        margin=5,
        padding=5,
        border_width=1,
        border_focus='#800000',
    ),
    layout.Matrix(
        margin=5,
        padding=5,
        border_focus='#800000',
        border_width=1,
    ),
]

widget_defaults = dict(
    font='ProFont for Powerline',
    fontsize=11,
    padding=3,
)

extension_defaults = widget_defaults.copy(),

colors =  [#["#434c5e", "#434c5e"], # color 0
        ["#2E3440"],
        ["#434C5E"],
        ["#4C566A"],
        ["#5E81AC"],
        ["#81A1C1"],
        ["#8FBCBB"],
        ["#B48EAD"],
        ["#A3BE8C"],
        ["#EBCB8B"],
        ["#D08770"],
        ["#BF616A"]
]

screens =[
    Screen(
        top = bar.Bar(
                [
                    #Current widget Background 
                    #Next widget Background

                    widget.CurrentLayoutIcon(
                        background = colors[0],
                        foreground = '#ffffff',
                        fontsize = 15
                    ),
                    widget.TextBox(
                        background = colors[2], 
                        foreground = colors[1],
                        text = '', 
                        fontsize=73, 
                        padding=-14
                    ),
                    widget.WindowName(
                        background = colors[2],
                        foreground = '#ffffff',
                        fontsize = 13
                    ),
                    widget.TextBox(
                        background = colors[4], 
                        foreground = colors[2],
                        text = '', 
                        fontsize=73, 
                        padding=-14
                    ),
                    widget.GroupBox(
                        background = colors[4],
                        foreground = '#ffffff',
                        block_highlight_text_color = '#FFF300',
                        center_aligned = True,
                        margin = 3,
                        disable_drag = True,
                        #this_current_screen_border = '#654321',
                        inactive = '#717171',
                        urgent_alert_method = 'text',
                        urgent_text = '#FF0000',
                        borderwidth = 0,
                        fontsize = 20
                    ),
                    widget.TextBox(
                        background = colors[5], 
                        foreground = colors[4],
                        text = '', 
                        fontsize=73, 
                        padding=-14
                    ),
                    widget.Clock(
                        format='  %a/%d/%B ', 
                        background = colors[5],
                        foreground = '#000000',
                        fontsize = 13
                    ),

                    widget.TextBox(
                        background = colors[6], 
                        foreground = colors[5],
                        text = '', 
                        fontsize=73, 
                        padding=-14
                    ),
                    widget.Clock(
                        format='  %I:%M:%S ', 
                        background = colors[6],
                        foreground = '#000000',
                        fontsize = 14
                    ),

                    widget.TextBox(
                        background = colors[7], 
                        foreground = colors[6],
                        text = '', 
                        fontsize=73, 
                        padding=-14
                    ),
                    widget.TextBox(
                        text=" ",
                        background = colors[7],
                        foreground = "#000000",
                        fontsize = 22
                    ),
                    widget.Volume(
                        background = colors[7],
                        foreground = '#000000',
                        update_interval = 0.1,
                        volume_app = 'pamixer',
                        fontsize = 12
                    ),
                    widget.TextBox(
                        background = colors[8], 
                        foreground = colors[7],
                        text = '', 
                        fontsize=73, 
                        padding=-14
                    ),
                    widget.TextBox(
                        text = "  ",
                        background = colors[8],
                        foreground='#000000',
                        padding = 0,
                        fontsize = 15
                    ),
                    widget.Backlight(
                        background = colors[8],
                        foreground='#000000',
                        backlight_name = "intel_backlight",
                        brightness_file = "brightness",
                        max_brightness_file = "max_brightness",
                        fontsize = 13
                    ),
                    widget.TextBox(
                        background = colors[9], 
                        foreground = colors[8],
                        text = '', 
                        fontsize=73, 
                        padding=-14
                    ),
                    widget.TextBox(
                        text = "   ",
                        background = colors[9],
                        foreground='#000000',
                        padding = 0,
                        fontsize = 20
                    ),
                    widget.Memory(
                        background = colors[9],
                        foreground='#000000',
                        fontsize = 12
                    ),
                    widget.TextBox(
                        background = colors[10], 
                        foreground = colors[9],
                        text = '', 
                        fontsize=73, 
                        padding=-14
                    ),
                    widget.Systray(
                        background = colors[10],
                        foreground = '#ffffff'
                    ),
                    widget.TextBox(
                        background = colors[10], 
                        foreground = colors[10],
                        text = '', 
                        fontsize=73, 
                        padding=-14
                    ),
                ],
            20,
            margin=[3,3,3,3],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "qtile"
