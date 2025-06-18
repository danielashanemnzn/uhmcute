################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"
        # dialog box settings here

        if who:
            if who == "???":
                window:
                    id "namebox"                
                    style "namebox"
                    text who id "who"
            else:
                window:
                    id "namebox"
                    style "namebox"    
                    text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0




## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.3, yalign=1.0)


style namebox:
    xalign 0.05  # Set to 0.0 (left), 0.5 (center), or 1.0 (right)
    yalign 0.0 
    xoffset 1000  # Adjust as needed for horizontal shift
    yoffset -153 # A
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=0.0)
    padding (50, 30)

style sec_namebox is namebox:
    xalign 0.05  # Set to 0.0 (left), 0.5 (center), or 1.0 (right)
    yalign 0.0 
    xoffset 1300  # Adjust as needed for horizontal shift
    yoffset -153 # Adjust as needed for vertical shift
    padding (6, 2)
    color "#000000"


style say_label:
    properties gui.text_properties("name", accent=True)
    
    xalign 0.3
    yalign 0.5


style say_dialogue:
    color "#00f662"   # Black text
    properties gui.text_properties("dialogue")

    xalign 0.12
    yalign 0.710
    xpos 643
    ypos 123

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 725
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
init python:
    # Class to manage GUI color settings
    class GUIColors:
        def __init__(self):
            self.accent_color = '#00cc99'
            self.idle_color = '#888888'
            self.idle_small_color = '#aaaaaa'
            self.hover_color = '#66e0c1'
            self.selected_color = '#ffffff'
            self.insensitive_color = '#8888887f'
            self.muted_color = '#00513d'
            self.hover_muted_color = '#007a5b'
            self.text_color = '#ffffff'
            self.interface_text_color = '#ffffff'
            self.quick_button_color = '#000000'  # Idle color for quick menu buttons

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

        # Method to update quick menu button idle color
        def set_quick_button_color(self, color):
            self.quick_button_color = color
            self.apply_colors()
            # Update style directly to set idle color
            style.quick_button_text.color = color
            # Keep hover_color different (e.g., use gui.hover_color)
            style.quick_button_text.hover_color = gui.hover_color  # Retains #66e0c1 or your custom hover color

    # Instantiate and apply the color settings
    gui_colors = GUIColors()
    gui_colors.apply_colors()
    gui_colors.set_quick_button_color('#000000')  # Set quick menu buttons to black for idle state


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
    color "#000000"  # Set idle text color to black
    hover_color gui.hover_color  # Use the original hover color (#66e0c1) or a custom contrast color like "#333333"
    selected_color gui.selected_color  # Optional: Keep selected color as white or adjust as needed


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen main_navigation():
    fixed:
        style_prefix "navigation"
        spacing gui.navigation_spacing

        imagebutton auto "gui/mm_start_%s.png" focus_mask True action Start() hovered [Play("sound", "audio/click.wav")]
        imagebutton auto "gui/mm_save_%s.png" focus_mask True action ShowMenu("load")
        imagebutton auto "gui/mm_pref_%s.png" focus_mask True action ShowMenu("preferences")
        imagebutton auto "gui/mm_about_%s.png" focus_mask True action ShowMenu("about")
        imagebutton auto "gui/mm_help_%s.png" focus_mask True action ShowMenu("help")
        imagebutton auto "gui/mm_exit_%s.png" focus_mask True action Quit(confirm=True)

    if gui.show_name:
        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"
        

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")




## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu
    add gui.main_menu_background

    use main_navigation
    ## This empty frame darkens the main menu.
    #frame:
    #    style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        textbutton _("History") action ShowMenu("history")
        textbutton _("Save") action ShowMenu("save")
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("UI Customization") action ShowMenu("ui_customization")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")
        textbutton _("Help") action ShowMenu("help")
        textbutton _("Quit") action Quit(confirm=True)

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 560
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -40
    xmaximum 1600
    yalign 1.0
    yoffset -40

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 60
    top_padding 240

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 560
    yfill True

style game_menu_content_frame:
    left_margin 80
    right_margin 40
    top_margin 20

style game_menu_viewport:
    xsize 1840

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 20

style game_menu_label:
    xpos 100
    ysize 240

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -60


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 100
    ypadding 6

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    frame:
        style_prefix "pref"

        has vbox

        label _("Preferences")
        textbutton _("Return") action Return()

        # You can insert the UI theme section anywhere inside this vbox:
        label _("UI Theme")

        textbutton "Default" action [SetVariable("persistent.ui_theme", "default"), Function(apply_ui_theme)]
        textbutton "Dark Mode" action [SetVariable("persistent.ui_theme", "dark"), Function(apply_ui_theme)]

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 4

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 450

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 700

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 20

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 900


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 30

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 16

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 500
    right_padding 40

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 60

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 200

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 12

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 900

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 680

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 800

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 1200

screen splash_screen():
    tag menu

    add "splash_bg"  # Replace with your background image filename

    text "Press to Continue" xpos 0.5 ypos 0.9 xanchor 0.5 yanchor 0.5 size 40 color "#FFFFFF" outlines [(2, "#000000")]

    key "mouseup_1" action Return()  # Mouse click
    key "K_RETURN" action Return()   # Enter key
    key "K_SPACE" action Return()    # Spacebar






screen ui_customization():
    tag menu

    frame:
        style_prefix "pref"
        has vbox

        label "UI Customization"

        text "Text Color:"
        hbox:
            spacing 10
            textbutton "White" action [SetVariable("persistent.text_color", "#FFFFFF"), Function(apply_ui_theme)]
            textbutton "Black" action [SetVariable("persistent.text_color", "#000000"), Function(apply_ui_theme)]
            textbutton "Red" action [SetVariable("persistent.text_color", "#5b3838"), Function(apply_ui_theme)]

        textbutton "Return" action Return()


        
##############################################################################
#  CUSTOM NAVIGATION CHOICE SCREEN
##############################################################################
screen nav_door_gate():
    # ── Door choice ─────────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)     # your textbox BG
        padding (20, 45)                                 # inner padding
        xpos 450         #  ← adjust these two numbers
        ypos 750         #  ← until the box sits right over the door
        textbutton "Public Library" action Jump("door_label")

    # ── Gate choice ─────────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 45)
        xpos 1380        #  ← move this one near the gate sprite
        ypos 940
        textbutton "Campus Grounds" action Jump("callscreen")

    # ── Fire Exit ─────────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 45)
        xpos 2000      #  ← move this one near the gate sprite
        ypos 940
        textbutton "Fire Exit" action Jump("fire_exit_inside_menu")

screen custom_choice_menu():

    # background frame for the choice box (optional)
    frame:
        background Frame("gui/nav_box.png", 15, 15)      # your textbox BG
        padding (20, 65)                                 # inner padding
        xpos 1150         #  ← adjust these two numbers
        ypos 1200         #  ← until the box sits right over the door
        textbutton "Explore the new building" action Jump("explore_new_building")

    # ── Gate choice ─────────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 70        #  ← move this one near the gate sprite
        ypos 750
        textbutton "Check resting area" action Jump("resting_ground")

    # ── ENTRANCE ─────────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1550        #  ← move this one near the gate sprite
        ypos 750
        textbutton "Enter Building" action Jump("enter_buildingcampus")

    frame:
        background Frame("gui/nav_box.png", 15, 15)      # your textbox BG
        padding (20, 65)                                 # inner padding
        xpos 2200     #  ← adjust these two numbers
        ypos 1200         #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("outside_exit_menu")

screen rest_choice_menu():

    # ── Hideout button ─────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 150      # ← tweak these numbers until
        ypos 1200      # ← the frame sits over the hide-out spot
        textbutton "Go to the Hideout" action Jump("hideout")

    # ── Stone-circle button ────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1810        # ← where the stone circle tables are
        ypos 1200
        textbutton "Check Stone-Circle Table" action Jump("stone_circle")

    # ── Vendor button ────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 100      # ← where the stone circle tables are
        ypos 1000
        textbutton "Check Vendor" action Jump("vendor")



    # ── Stone-circle button ────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1110        # ← where the stone circle tables are
        ypos 1200
        textbutton "Walk Back" action Jump("callscreen")

################################################################################
#  SCREEN – pick a room inside the building
################################################################################
screen information_desk():
    # to view the information desk image
    frame:
        background Frame("gui/nav_png", 15, 15)
        padding(20, 65)
        xpos 1000
        ypos 550
        textbutton "Check Information Desk" action Jump("information_desk") 
    
    # to view the information desk image
    frame:
        background Frame("gui/nav_png", 15, 15)
        padding(20, 65)
        xpos 1000
        ypos 550
        textbutton "Walk Back" action Jump("callscreen") 

screen inside_choice_menu():

    # ── Stone-circle button ────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 2250        # ← where the stone circle tables are
        ypos 600
        textbutton "Turn Right" action Jump("right_hall")

    # ── Stone-circle button ────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 250        # ← where the stone circle tables are
        ypos 600
        textbutton "Turn Left" action Jump("left_ground1")

    # ── Stone-circle button ────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1250        # ← where the stone circle tables are
        ypos 1250
        textbutton "walk back" action Jump("callscreen")

screen right_hall_menu():

    # ── Enter Clinic ───────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 200   # Adjust x/y until each button sits over the door, window, etc.
        ypos 850
        textbutton "Clinic" action Jump("clinic_room")

    # ── Inspect LIN Door ───────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1200
        ypos 1300
        textbutton "Walk back" action Jump("inside_building")

    # ── Move Forward ───────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1200
        ypos 700
        textbutton "Walk Further" action Jump("right_hall_forward2")
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1850
        ypos 700
        textbutton "SAS Office" action Jump("sas")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1500
        ypos 700
        textbutton "ACAD Office" action Jump("acads1")

screen acads():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("floor1_right_hall")

screen right_hall_menu1():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 100        #  ← adjust these two numbers
        ypos 750         #  ← until the box sits right over the door
        textbutton "Admin Office" action Jump("admin")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 500       #  ← adjust these two numbers
        ypos 800    #  ← until the box sits right over the door
        textbutton "Process" action Jump("show_documents")

    # ── Academic Paper Process the choice ─────────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 2100     #  ← move this one near the gate sprite
        ypos 750
        textbutton "Director's Office" action Jump("director")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1200        #  ← move this one near the gate sprite
        ypos 750
        textbutton "Walk Further" action Jump("mid")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1250  #  ← move this one near the gate sprite
        ypos 1300
        textbutton "Walk Back" action Jump("floor1_right_hall")


screen right_hall_menu2():
    frame:
        background Frame("gui/nav_box.png", 15, 15)        
        padding (20, 65)                                 # inner padding
        xpos 100        #  ← adjust these two numbers
        ypos 750         #  ← until the box sits right over the door
        textbutton "LGBT CR" action Jump("lgbt_cr")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1325    #  ← move this one near the gate sprite
        ypos 700
        textbutton "Garden" action Jump("garden_1")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1800     #  ← move this one near the gate sprite
        ypos 750
        textbutton "Go upstair" action Jump("upstairs")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1300   #  ← move this one near the gate sprite
        ypos 1200
        textbutton "Walk Back" action Jump("right_hall_forward2")

screen lgbt_cr():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("right_hall_forward3")

screen garden_view():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 900   #  ← adjust these two numbers
        ypos 900#  ← until the box sits right over the door
        textbutton "Garden" action Jump("garden_view_menu1")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1800      #  ← adjust these two numbers
        ypos 900        #  ← until the box sits right over the door
        textbutton "Exit" action Jump("right_exit")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1250     #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("right_hall_forward3")

screen cat():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 800    #  ← adjust these two numbers
        ypos 900#  ← until the box sits right over the door
        textbutton "Walk further" action Jump("back_garden_view")
        
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1250     #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("garden_view_menu")

screen back_garden():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 800    #  ← adjust these two numbers
        ypos 900#  ← until the box sits right over the door
        textbutton "Walk further" action Jump("garden_back1")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1250     #  ← adj  ust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("garden_view_menu1")

screen entrance_hideout():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1000    #  ← adjust these two numbers
        ypos 700 #  ← until the box sits right over the door
        textbutton "Go inside" action Jump("left_ground_3")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1300    #  ← adjust these two numbers
        ypos 1000#  ← until the box sits right over the door
        textbutton "Go outside the Hideout" action Jump("choicethree")
    
    

screen menu1():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 800    #  ← adjust these two numbers
        ypos 900#  ← until the box sits right over the door
        textbutton "Walk further" action Jump("walk")


screen right_exit_menu1():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1000  #  ← adjust these two numbers
        ypos 880      #  ← until the box sits right over the door
        textbutton "Go outside" action Jump("outside_exit")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1250     #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("garden_view_menu")

screen fire_exit_inside_menu1():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding(20, 65)
        xpos 650
        ypos 750
        textbutton "Go inside" action Jump("right_hall_forward3")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding(20, 65)
        xpos 1380
        ypos 750
        textbutton "Garden" action Jump("garden_view2")


screen right_hall_menu3():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 750         #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("floor2_1")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1900    #  ← adjust these two numbers
        ypos 750         #  ← until the box sits right over the door
        textbutton "Male Bathroom" action Jump("male_bathroom1")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 50    #  ← adjust these two numbers
        ypos 700         #  ← until the box sits right over the door
        textbutton "Go upstair" action Jump("turn_left")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 50       #  ← adjust these two numbers
        ypos 1250         #  ← until the box sits right over the door
        textbutton "Go downstair" action Jump("right_hall_forward3")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100    #  ← adjust these two numbers
        ypos 1250         #  ← until the box sits right over the door
        textbutton "Fire Exit" action Jump("fire_exit") 
   

screen room():
    # ── 2nd Floor Room───────────────────────────────────────────────────
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1900  #  ← adjust these two numbers
        ypos 800       #  ← until the box sits right over the door
        textbutton "Room 204" action Jump("room_204")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1150    #  ← adjust these two numbers
        ypos 800        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("floor2_3")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1175    #  ← adjust these two numbers
        ypos 1250        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("second_floor_menu")
        
screen pup():
    # ── PUP Library ───────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 300   #  ← adjust these two numbers
        ypos 800       #  ← until the box sits right over the door
        textbutton "Library" action Jump("pup_library")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1215    #  ← adjust these two numbers
        ypos 800        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("floor_1")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1250    #  ← adjust these two numbers
        ypos 1250        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("floor2_2")

screen discussion():
    # ── PUP Library ───────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 200   #  ← adjust these two numbers
        ypos 800       #  ← until the box sits right over the door
        textbutton "Discussion" action Jump("discussion_room")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1200    #  ← adjust these two numbers
        ypos 800        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("floor__1")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1225    #  ← adjust these two numbers
        ypos 1250        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("floor2_3")
    
screen second_last_floor():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1000   #  ← adjust these two numbers
        ypos 1000        #  ← until the box sits right over the door
        textbutton "Go downstair" action Jump("left_ground_3")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1800   #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Go upstair" action Jump("third1")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1250    #  ← adjust these two numbers
        ypos 1250        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("floor_2")

screen left_ground_menu1():

    # ── Inspect LIN Door ───────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1200
        ypos 1200
        textbutton "Walk back" action Jump("inside_building")

    # ── Cashier─────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 2300  # ← tweak these numbers until
        ypos 720     # ← the frame sits over the hide-out spot
        textbutton "Cashier" action Jump("cashier")

# ── Cashier─────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 250     # ← tweak these numbers until
        ypos 720     # ← the frame sits over the hide-out spot
        textbutton "NSTP Room" action Jump("nstp")

    # ── Move Forward ───────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1121
        ypos 750
        textbutton "Walk Further" action Jump("left_ground2")

screen nstp_room():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("left_ground_1")



screen left_ground_menu2():

    # ── Inspect LIN Door ───────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1200
        ypos 1200
        textbutton "Walk back" action Jump("left_ground_1")

    # ── Cashier─────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1930     # ← tweak these numbers until
        ypos 720     # ← the frame sits over the hide-out spot
        textbutton "Faculty Lounge" action Jump("faculty_lounge")

# ── Move Forward ───────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1121
        ypos 750
        textbutton "Walk Further" action Jump("left_ground3")

screen left_ground_menu3():

    # ── Inspect LIN Door ───────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1100
        ypos 1300
        textbutton "Walk back" action Jump("left_ground_2")

    # ── AVR Inside ───────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 400
        ypos 500
        textbutton "AVR" action Jump("avr_room")

    
    # ── AVR Inside ───────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 900
        ypos 700
        textbutton "Walk Further" action Jump("floor__2")
    
    # ── HIDE OUT ───────────────────────────────────────────────────────
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 55)
        xpos 1225
        ypos 800
        textbutton "Hide Out" action Jump("g")
    

screen third_floor1():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1370   #  ← adjust these two numbers
        ypos 800        #  ← until the box sits right over the door
        textbutton "Girl's CR" action Jump("girls_cr")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1600   #  ← adjust these two numbers
        ypos 950        #  ← until the box sits right over the door
        textbutton "Turn right" action Jump("turn_right")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1250    #  ← adjust these two numbers
        ypos 1250        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("floor_2")

screen third_floor2():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1700   #  ← adjust these two numbers
        ypos 820        #  ← until the box sits right over the door
        textbutton "Room 307" action Jump("room_307")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1115  #  ← adjust these two numbers
        ypos 775        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("turn_right_2")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1150   #  ← adjust these two numbers
        ypos 1250        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("third1_1")

screen third_floor3():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1700   #  ← adjust these two numbers
        ypos 820        #  ← until the box sits right over the door
        textbutton "Room 305" action Jump("room_305")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1115  #  ← adjust these two numbers
        ypos 775        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("turn_right1")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1150   #  ← adjust these two numbers
        ypos 1250        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("turn_right_1")

screen third_floor4():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1700   #  ← adjust these two numbers
        ypos 820        #  ← until the box sits right over the door
        textbutton "Room 302" action Jump("room_302")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1115  #  ← adjust these two numbers
        ypos 775        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("turn_right5")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1150   #  ← adjust these two numbers
        ypos 1250        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("turn_right_3")

screen third_floor5():

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1700       #  ← adjust these two numbers
        ypos 750         #  ← until the box sits right over the door
        textbutton "Turn left" action Jump("turn_left")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 200    #  ← adjust these two numbers
        ypos 750         #  ← until the box sits right over the door
        textbutton "Boy's CR" action Jump("boys_cr")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1200       #  ← adjust these two numbers
        ypos 1300         #  ← until the box sits right over the door
        textbutton "Walk back" action Jump("turn_right_4")    

screen third_floor6():

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 700    #  ← adjust these two numbers
        ypos 750         #  ← until the box sits right over the door
        textbutton "Science Lab" action Jump("science_lab")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 1200       #  ← adjust these two numbers
        ypos 1300         #  ← until the box sits right over the door
        textbutton "Walk back" action Jump("turn_right_2")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1130  #  ← adjust these two numbers
        ypos 775        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("turn_right_4")

screen science_lab1():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("turn_right_3")

screen turn_left_1():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)
        xpos 700   #  ← adjust these two numbers
        ypos 775         #  ← until the box sits right over the door
        textbutton "Go upstair" action Jump("fourth_floor_1")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1500 #  ← adjust these two numbers
        ypos 1200        #  ← until the box sits right over the door
        textbutton "Go downstair" action Jump("second_floor_menu")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("turn_right_5")

screen fourth_floor1():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 700    #  ← adjust these two numbers
        ypos 900        #  ← until the box sits right over the door
        textbutton "Turn left" action Jump("fourth_floors1")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1000    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Boy's CR" action Jump("m_bathroom")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 2100    #  ← adjust these two numbers
        ypos 1300         #  ← until the box sits right over the door
        textbutton "roof deck" action Jump("stair_roofdeck")    
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 900   #  ← adjust these two numbers
        ypos 1300       #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("right_hall_forward3") 

screen boy_bathroom():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("turn_right_5")

screen ma_bathroom():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("fourth_floor_1")

screen male_bathroom():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("second_floor_menu")

screen fourth():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 50    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Computer Laboratory" action Jump("comlab")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 2200    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Computer Hardware" action Jump("computer_hardware")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1115  #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("fourth_floors2")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1150      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("fourth_floor_1")

screen fourth1():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 100    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Project Proposal Room" action Jump("project_proposal")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 2050    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Laboratory Management" action Jump("lab_management")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1115  #  ← adjust these two numbers
        ypos 600        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("fourth_floors3")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1150      #  ← adjust these two numbers
        ypos 1250        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("fourth_floors1")

screen fourth2():
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 80    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Travel & Tours" action Jump("travel_tours")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 2100    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Kitchen Laboratory" action Jump("kitchen_lab")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1050  #  ← adjust these two numbers
        ypos 700       #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("fourth_floors4_1")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1095      #  ← adjust these two numbers
        ypos 1200        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("fourth_floors2")

screen fourth3():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 800    #  ← adjust these two numbers
        ypos 800        #  ← until the box sits right over the door
        textbutton "Student Org" action Jump("student_org")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1500    #  ← adjust these two numbers
        ypos 800        #  ← until the box sits right over the door
        textbutton "Housekeeping Room" action Jump("housekeeping_room")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 100    #  ← adjust these two numbers
        ypos 800        #  ← until the box sits right over the door
        textbutton "Food and Beverage" action Jump("food_beverage")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 2200    #  ← adjust these two numbers
        ypos 800        #  ← until the box sits right over the door
        textbutton "HM Storage" action Jump("HM_storage")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1180  #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("fourth_floors5")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1200      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("fourth_floors3")

screen fourth4():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 850    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "CSC Room" action Jump("csc")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1300    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Deluxe Room" action Jump("deluxe_room")
    
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1070  #  ← adjust these two numbers
        ypos 775        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("fourth_floors6")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("fourth_floors4_1")

screen fourth5():
    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 700    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Front Office of Travel & Tours" action Jump("frontofficetravel_tours")
    

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1115  #  ← adjust these two numbers
        ypos 600        #  ← until the box sits right over the door
        textbutton "Walk Further" action Jump("floor1_2")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1100      #  ← adjust these two numbers
        ypos 1280        #  ← until the box sits right over the door
        textbutton "Walk Back" action Jump("fourth_floors5")

    frame:
        background Frame("gui/nav_box.png", 15, 15)
        padding (20, 65)                                 # inner padding
        xpos 1400    #  ← adjust these two numbers
        ypos 700        #  ← until the box sits right over the door
        textbutton "Standard Room" action Jump("standard_room")





