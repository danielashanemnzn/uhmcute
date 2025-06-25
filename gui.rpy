################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(2560, 1440)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True


################################################################################Add commentMore actions
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

init python:
    # Class to manage GUI color settings
    class GUIColors:
        def __init__(self):
            # Define color attributes
            self.accent_color = '#002b20'
            self.idle_color = '#888888'
            self.idle_small_color = '#aaaaaa'
            self.hover_color = '#124d12'
            self.selected_color = '#124d12'
            self.insensitive_color = '#8888887f'
            self.muted_color = '#00513d'
            self.hover_muted_color = '#007a5b'
            self.text_color = '#540202'
            self.interface_text_color = '#b75f5f'

        # Method to apply colors to Ren'Py's gui namespace
        def apply_colors(self):
            gui.accent_color = self.accent_color
            gui.idle_color = self.idle_color
            gui.idle_small_color = self.idle_small_color
            gui.hover_color = self.hover_color
            gui.selected_color = self.selected_color
            gui.insensitive_color = self.insensitive_color
            gui.muted_color = self.muted_color
            gui.hover_muted_color = self.hover_muted_color
            gui.text_color = self.text_color
            gui.interface_text_color = self.interface_text_color

    # Instantiate and apply the color settings
    gui_colors = GUIColors()
    gui_colors.apply_colors()


init python:
    # Class to manage GUI font and size settings
    class GUIFontSettings:
        def __init__(self):
            # Define font attributes
            self.text_font = "PatrickHand-Regular.ttf"
            self.name_text_font = "Super Mario Bros..ttf"
            self.interface_text_font = "PatrickHand-Regular.ttf"

            # Define size attributes
            self.text_size = 40
            self.name_text_size = 60
            self.interface_text_size = 40
            self.label_text_size = 36
            self.notify_text_size = 24
            self.title_text_size = 90

        # Method to apply font and size settings to Ren'Py's gui namespace
        def apply_settings(self):
            gui.text_font = self.text_font
            gui.name_text_font = self.name_text_font
            gui.interface_text_font = self.interface_text_font
            gui.text_size = self.text_size
            gui.name_text_size = self.name_text_size
            gui.interface_text_size = self.interface_text_size
            gui.label_text_size = self.label_text_size
            gui.notify_text_size = self.notify_text_size
            gui.title_text_size = self.title_text_size

    # Instantiate and apply the font settings
    gui_font_settings = GUIFontSettings()
    gui_font_settings.apply_settings()


init python:
    # Class to manage GUI and config settings
    class GUIConfigSettings:
        def __init__(self):
            # Main and Game Menu Backgrounds
            self.main_menu_background = "gui/main_menu.png"
            self.game_menu_background = "gui/game_menu.png"

            # Dialogue Settings
            self.textbox_height = 288
            self.textbox_yalign = 1.0
            self.name_xpos = 360
            self.name_ypos = 0
            self.name_xalign = 0.0
            self.namebox_width = 480
            self.namebox_height = None
            self.namebox_borders = Borders(5, 5, 5, 5)
            self.namebox_tile = False
            self.dialogue_xpos = 402
            self.dialogue_ypos = 75
            self.dialogue_width = 1116
            self.dialogue_text_xalign = 0.0

            # Screen Resolution
            self.screen_width = 2560
            self.screen_height = 1440

            # Button Settings
            self.button_width = None
            self.button_height = None
            self.button_borders = Borders(6, 6, 6, 6)
            self.button_tile = False
            self.button_text_font = gui.interface_text_font
            self.button_text_size = gui.interface_text_size
            self.button_text_idle_color = gui.idle_color
            self.button_text_hover_color = gui.hover_color
            self.button_text_selected_color = gui.selected_color
            self.button_text_insensitive_color = gui.insensitive_color
            self.button_text_xalign = 0.0

        # Method to apply settings to Ren'Py's gui and config namespaces
        def apply_settings(self):
            # Main and Game Menu
            gui.main_menu_background = self.main_menu_background
            gui.game_menu_background = self.game_menu_background

            # Dialogue
            gui.textbox_height = self.textbox_height
            gui.textbox_yalign = self.textbox_yalign
            gui.name_xpos = self.name_xpos
            gui.name_ypos = self.name_ypos
            gui.name_xalign = self.name_xalign
            gui.namebox_width = self.namebox_width
            gui.namebox_height = self.namebox_height
            gui.namebox_borders = self.namebox_borders
            gui.namebox_tile = self.namebox_tile
            gui.dialogue_xpos = self.dialogue_xpos
            gui.dialogue_ypos = self.dialogue_ypos
            gui.dialogue_width = self.dialogue_width
            gui.dialogue_text_xalign = self.dialogue_text_xalign

            # Screen Resolution
            config.screen_width = self.screen_width
            config.screen_height = self.screen_height

            # Buttons
            gui.button_width = self.button_width
            gui.button_height = self.button_height
            gui.button_borders = self.button_borders
            gui.button_tile = self.button_tile
            gui.button_text_font = self.button_text_font
            gui.button_text_size = self.button_text_size
            gui.button_text_idle_color = self.button_text_idle_color
            gui.button_text_hover_color = self.button_text_hover_color
            gui.button_text_selected_color = self.button_text_selected_color
            gui.button_text_insensitive_color = self.button_text_insensitive_color
            gui.button_text_xalign = self.button_text_xalign

    # Instantiate and apply the settings
    gui_config_settings = GUIConfigSettings()
    gui_config_settings.apply_settings()

init python:
    # Class to manage GUI button settings
    class GUIButtonSettings:
        def __init__(self):
            # Define border attributes
            self.radio_button_borders = Borders(27, 6, 6, 6)
            self.check_button_borders = Borders(27, 6, 6, 6)
            self.page_button_borders = Borders(15, 6, 15, 6)

            # Define text alignment attribute
            self.confirm_button_text_xalign = 0.5

        # Method to apply settings to Ren'Py's gui namespace
        def apply_settings(self):
            gui.radio_button_borders = self.radio_button_borders
            gui.check_button_borders = self.check_button_borders
            gui.page_button_borders = self.page_button_borders
            gui.confirm_button_text_xalign = self.confirm_button_text_xalign

    # Instantiate and apply the button settings
    gui_button_settings = GUIButtonSettings()
    gui_button_settings.apply_settings()

init python:
    # Class to manage quick_button GUI settings
    class GUIQuickButtonSettings:
        def __init__(self):
            # Define border attributes
            self.quick_button_borders = Borders(15, 6, 15, 0)

            # Define text size attribute
            self.quick_button_text_size = 31

            # Define text color attributes
            self.quick_button_text_idle_color = '#000000'  # References existing gui.idle_small_color (#aaaaaa)
            self.quick_button_text_selected_color = '#000000'

        # Method to apply settings to Ren'Py's gui namespace
        def apply_settings(self):
            gui.quick_button_borders = self.quick_button_borders
            gui.quick_button_text_size = self.quick_button_text_size
            gui.quick_button_text_idle_color = self.quick_button_text_idle_color
            gui.quick_button_text_selected_color = self.quick_button_text_selected_color

    # Instantiate and apply the quick_button settings
    gui_quick_button_settings = GUIQuickButtonSettings()
    gui_quick_button_settings.apply_settings()


## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


init python:
    # Class to manage choice and slot button GUI settings
    class GUIButtonSettings:
        def __init__(self):
            # Choice Button Settings
            self.choice_button_width = 900
            self.choice_button_height = 130
            self.choice_button_tile = False
            self.choice_button_borders = Borders(150, 8, 150, 8)
            self.choice_button_text_font = gui.text_font
            self.choice_button_text_size = gui.text_size
            self.choice_button_text_xalign = 0.5
            self.choice_button_text_yalign = 0.5
            self.choice_button_text_idle_color = '#888888'
            self.choice_button_text_hover_color = '#ac2c79'
            self.choice_button_text_insensitive_color = '#8888887f'

            # Slot Button Settings
            self.slot_button_width = 414
            self.slot_button_height = 309
            self.slot_button_borders = Borders(15, 15, 15, 15)
            self.slot_button_text_size = 22
            self.slot_button_text_xalign = 0.5
            self.slot_button_text_idle_color = gui.idle_small_color
            self.slot_button_text_selected_idle_color = gui.selected_color
            self.slot_button_text_selected_hover_color = gui.hover_color

        # Method to apply settings to Ren'Py's gui namespace
        def apply_settings(self):
            # Choice Button Settings
            gui.choice_button_width = self.choice_button_width
            gui.choice_button_height = self.choice_button_height
            gui.choice_button_tile = self.choice_button_tile
            gui.choice_button_borders = self.choice_button_borders
            gui.choice_button_text_font = self.choice_button_text_font
            gui.choice_button_text_size = self.choice_button_text_size
            gui.choice_button_text_xalign = self.choice_button_text_xalign
            gui.choice_button_text_yalign = self.choice_button_text_yalign
            gui.choice_button_text_idle_color = self.choice_button_text_idle_color
            gui.choice_button_text_hover_color = self.choice_button_text_hover_color
            gui.choice_button_text_insensitive_color = self.choice_button_text_insensitive_color

            # Slot Button Settings
            gui.slot_button_width = self.slot_button_width
            gui.slot_button_height = self.slot_button_height
            gui.slot_button_borders = self.slot_button_borders
            gui.slot_button_text_size = self.slot_button_text_size
            gui.slot_button_text_xalign = self.slot_button_text_xalign
            gui.slot_button_text_idle_color = self.slot_button_text_idle_color
            gui.slot_button_text_selected_idle_color = self.slot_button_text_selected_idle_color
            gui.slot_button_text_selected_hover_color = self.slot_button_text_selected_hover_color

    # Instantiate and apply the button settings
    gui_button_settings = GUIButtonSettings()
    gui_button_settings.apply_settings()

init python:
    # Class to manage GUI and config settings for thumbnails, slots, and positioning
    class GUIConfigLayoutSettings:
        def __init__(self):
            # Thumbnail Sizes
            self.thumbnail_width = 384
            self.thumbnail_height = 216

            # File Slot Grid
            self.file_slot_cols = 3
            self.file_slot_rows = 2

            # Positioning and Spacing
            self.navigation_xpos = 60
            self.skip_ypos = 15
            self.notify_ypos = 68
            self.choice_spacing = 33
            self.navigation_spacing = 6
            self.pref_spacing = 15
            self.pref_button_spacing = 0
            self.page_spacing = 0
            self.slot_spacing = 15
            self.main_menu_text_xalign = 1.0

        # Method to apply settings to Ren'Py's gui and config namespaces
        def apply_settings(self):
            # Thumbnail Sizes (config namespace)
            config.thumbnail_width = self.thumbnail_width
            config.thumbnail_height = self.thumbnail_height

            # File Slot Grid (gui namespace)
            gui.file_slot_cols = self.file_slot_cols
            gui.file_slot_rows = self.file_slot_rows

            # Positioning and Spacing (gui namespace)
            gui.navigation_xpos = self.navigation_xpos
            gui.skip_ypos = self.skip_ypos
            gui.notify_ypos = self.notify_ypos
            gui.choice_spacing = self.choice_spacing
            gui.navigation_spacing = self.navigation_spacing
            gui.pref_spacing = self.pref_spacing
            gui.pref_button_spacing = self.pref_button_spacing
            gui.page_spacing = self.page_spacing
            gui.slot_spacing = self.slot_spacing
            gui.main_menu_text_xalign = self.main_menu_text_xalign

    # Instantiate and apply the layout settings
    gui_config_layout_settings = GUIConfigLayoutSettings()
    gui_config_layout_settings.apply_settings()


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(6, 6, 6, 6)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

init python:
    # Class to manage GUI settings for bars, scrollbars, and sliders
    class GUIBarSettings:
        def __init__(self):
            # Size settings
            self.bar_size = 38
            self.scrollbar_size = 18
            self.slider_size = 38

            # Tiling settings
            self.bar_tile = False
            self.scrollbar_tile = False
            self.slider_tile = False

            # Horizontal borders
            self.bar_borders = Borders(6, 6, 6, 6)
            self.scrollbar_borders = Borders(6, 6, 6, 6)
            self.slider_borders = Borders(6, 6, 6, 6)

            # Vertical borders
            self.vbar_borders = Borders(6, 6, 6, 6)
            self.vscrollbar_borders = Borders(6, 6, 6, 6)
            self.vslider_borders = Borders(6, 6, 6, 6)

        # Method to apply settings to Ren'Py's gui namespace
        def apply_settings(self):
            gui.bar_size = self.bar_size
            gui.scrollbar_size = self.scrollbar_size
            gui.slider_size = self.slider_size
            gui.bar_tile = self.bar_tile
            gui.scrollbar_tile = self.scrollbar_tile
            gui.slider_tile = self.slider_tile
            gui.bar_borders = self.bar_borders
            gui.scrollbar_borders = self.scrollbar_borders
            gui.slider_borders = self.slider_borders
            gui.vbar_borders = self.vbar_borders
            gui.vscrollbar_borders = self.vscrollbar_borders
            gui.vslider_borders = self.vslider_borders

    # Instantiate and apply the bar settings
    gui_bar_settings = GUIBarSettings()
    gui_bar_settings.apply_settings()

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

define gui.namebox_style = "namebox"
define gui.name_text_style = "name_text"


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 173

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 15

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 22
        gui.name_text_size = 45
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Adjust the location of the textbox.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
