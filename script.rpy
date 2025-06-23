################################################################################
##  CHARACTER DEFINITIONS
################################################################################
# Define a Character class to encapsulate character properties
init python:
    class GameCharacter:
        def __init__(self, name, color, namebox_style):
            self.name = name
            self.color = color
            self.namebox_style = namebox_style
            # Create Ren'Py Character object
            self.character = Character(name, color=color, namebox_style=namebox_style)

        # Method to access the Ren'Py Character object
        def get_character(self):
            return self.character

    
define text_color = "#FFFFFF"
   
# Instantiate character objects
define jus = GameCharacter("Justine", "#2ec14b", "namebox" ).get_character()
define g   = GameCharacter("Guard", "#966bf3", "namebox").get_character()
define k   = GameCharacter("Kim", "#c2ff1a", "namebox").get_character()
define c   = GameCharacter("Carl", "#0cff8d", "namebox").get_character()
define cj   = GameCharacter("Carl", "#113d29", "namebox").get_character()
define n   = GameCharacter("Nurse", "#E9967A", "namebox").get_character()
define ma  = GameCharacter("Mae", "#E23A32", "namebox").get_character()
define m   = GameCharacter("Mae", "#E23A32", "namebox").get_character()
define s   = GameCharacter("Sophie", "#A23A32", "namebox").get_character()
define l   = GameCharacter("Lyn", "#AB3A32", "namebox").get_character()
define e   = GameCharacter("Ella", "#3A3AB4", "namebox").get_character()
define v   = GameCharacter("Vidal", "#3A8084", "namebox").get_character()
define cs  = GameCharacter("Cashier", "#09091e", "namebox").get_character()
define j   = GameCharacter("Joriemer", "#519c90", "namebox").get_character()
define vd = GameCharacter("Vendor", "#519d80", "namebox").get_character()
# define gui.name_text_size = 100  # Commented out - now managed in gui.rpy

################################################################################
#  TRANSFORMS
################################################################################
init python:
    class Transform:
        def __init__(self, xalign, yalign, anchor, zoom):
            self.xalign = xalign
            self.yalign = yalign
            self.anchor = anchor
            self.zoom = zoom

        def to_renpy_transform(self):
            return f"""
transform {self.__class__.__name__.lower()}:
    xalign {self.xalign}
    yalign {self.yalign}
    anchor {self.anchor}
    zoom {self.zoom}
            """.strip()

    # Instantiate Transform objects
    justine_bottom_left = Transform(0.0, 1.0, (0.0, 1.0), 0.8)
    kim_bottom_right = Transform(0.75, 1.05, (0.0, 1.0), 0.8)
    justine_bottom_center = Transform(0.3, 0.9, (0.0, 1.0), 0.7)
    kim_bottom_center = Transform(0.5, 1.05, (0.05, 1.1), 0.8)
    kim_bottom_left = Transform(0.2, 1.05, (0.05, 1.1), 0.8)
    guard_bottom_right = Transform(0.75, 1.1, (0.0, 1.0), 0.8)
    mae_bottom_center = Transform(0.3, 0.9, (0.0, 1.0), 0.7)
    sophie_bottom_center = Transform(0.5, 0.9, (0.0, 1.0), 1.0)
    mae_bottom_left = Transform(0.0, 1.0, (0.0, 1.0), 0.7)
    justine_bottom_center = Transform(0.3, 0.9, (0.0, 1.0), 0.7)

    # Generate transform definitions as strings (for manual inclusion)
    transforms = [
        justine_bottom_left,
        kim_bottom_right,
        justine_bottom_center,
        kim_bottom_center,
        kim_bottom_left,
        guard_bottom_right,
        mae_bottom_center,
        sophie_bottom_center,
        mae_bottom_left,
        justine_bottom_center
    ]
    # Note: Removed eval() and store_dict assignment; transforms are now hardcoded below

# Ren'Py transform definitions (hardcoded based on Transform objects)

transform custom_size_transform:
    size (2580, 1520)

transform justine_bottom_left:
    xalign 0.0
    yalign 1.0
    anchor (0.0, 1.0)
    zoom 0.8

transform kim_bottom_right:
    xalign 0.75
    yalign 1.05
    anchor (0.0, 1.0)
    zoom 0.8

transform justine_bottom_center:
    xalign 0.3
    yalign 1.0
    anchor (0.0, 1.0)
    zoom 0.8

transform kim_bottom_center:
    xalign 0.5
    yalign 1.05
    anchor (0.05, 1.1)
    zoom 0.8

transform kim_bottom_left:
    xalign 0.2
    yalign 1.05
    anchor (0.05, 1.1)
    zoom 0.8

transform guard_bottom_right:
    xalign 0.75
    yalign 1.1
    anchor (0.0, 1.0)
    zoom 0.8

transform mae_bottom_center:
    xalign 0.3
    yalign 0.9
    anchor (0.0, 1.0)
    zoom 0.7

transform sophie_bottom_center:
    xalign 0.5
    yalign 0.9
    anchor (0.0, 1.0)
    zoom 1.0

transform mae_bottom_left:
    xalign 0.0
    yalign 1.0
    anchor (0.0, 1.0)
    zoom 0.7

transform fadein:
    alpha 0.0
    linear 1.0 alpha 1.0  # 1 second fade-in

################################################################################
#  IMAGE_DEFINITIONS+-
################################################################################

#_backgrounds__ (make sure these files exist in /game/images/)
image a                    = "images/a.jpg"
image bg_gate              = "images/bg_gate.jpg"
image bg_after_school_gate = "images/after_school_gate.jpg"
image bg_pub_lib_door      = "images/pub_lib_door.jpg"
image bg_guard_house       = "images/guard_house.jpg"
image bg_room              = "images/bg_room.jpg"
image splash_bg            = "images/splash_bg.png"
image bg_far_view_entrance      = "images/FarViewofEntranceArea.jpg"
image bg_new_building1     = "images/new_building1.jpg" 
image bg_new_building2     = "images/new_building2.jpg"
image bg_new_building3     = "images/new_building3.jpg"
image bg_new_building4     = "images/new_building4.jpg"  
image bg_new_building5     = "images/new_building5.jpg"
image bg_new_building6     = "images/new_building6.jpg"
image bg_nearing_new_building   = "images/NearingNewBuilding.jpg"
image bg_tambayan_to_entrance   = "images/TambayanAreaGoingtoEntrance.jpg"
image bg_circle_area_lower_view = "images/CircleAreaLowerView.jpg"
image bg_vendor            = "images/vendor.jpg"
image bg_vendor_view       = "images/vendor_view.jpg"
image Enter_choice2 = "images/Enter_choice2.jpg"
image bg_entering_hideout      = "images/Entering_hideout.jpg"
image bg_closed_hideout_gate   = "images/Closed_hideout_area_gate.jpg"
image bg_entering_the_school_lobby = "images/entering_the_school_lobby.jpg"
image bg_pup_lobby = "images/pup_lobby.jpg"
image bg_informationdesk = "images/informationdesk.jpg"
image bg_window1 = "images/window1.jpg"
image floor1_hallwayright = "images/floor1_hallwayright.jpg"
image bg_acad = "images/acad.jpg"
image bg_sas = "images/sas.jpg"
image bg_midstair = "images/mid_boys_stairs.jpg"
image bg_lgbt1 = "images/lgbt_cr.jpg"
image bg_lgbt2 = "images/lgbt_door.jpg"
image bg_lgbt3 = "images/lgbt_halfway.jpg"
image bg_stair1 = "images/first_stair1.jpg"  
image bg_stair2= "images/first_stair2.jpg"
image bg_stair3= "images/first_stair3.jpg"
image bg_stair4= "images/first_stair4.jpg"
image bg_stair5 = "images/first_stair5.jpg"
image bg_stair6 = "images/first_stair6.jpg"
image fire_exit1 = "images/fire_exit1.jpg"
image fire_exit2 = "images/fire_exit2.jpg"
image m1 = "images/m1.jpg"
image m2 = "images/m2.jpg"
image m3 = "images/m3.jpg"
image m4 = "images/m4.jpg"
image m5 = "images/m5.jpg"
image sf1 = "images/sf1.jpg"
image sf2 = "images/sf2.jpg"
image sf3 = "images/sf3.jpg"
image sf4 = "images/sf4.jpg"
image sf5 = "images/sf5.jpg"
image sf6 = "images/sf6.jpg"
image sf7 = "images/sf7.jpg"
image sf8 = "images/sf8.jpg"
image sf9 = "images/sf9.jpg"
image sf10 = "images/sf10.jpg"
image sf11 = "images/sf11.jpg"
image sf12 = "images/sf12.jpg"
image sf13 = "images/sf13.jpg"
image sf14 = "images/sf14.jpg"
image sf15 = "images/sf15.jpg"
image sf16 = "images/sf16.png"
image sf17 = "images/sf17.jpg"
image floor1_midhallwayleft = "images/floor1_midhallwayleft.jpg"
image floor1_hallwayleft = "images/floor1_hallwayleft.jpg"
image left_halfway_ground1 = "images/left_halfway_ground1.jpg"
image left_halfway_ground2 = "images/left_halfway_ground2.jpg"
image left_halfway_ground3 = "images/left_halfway_ground3.jpg"
image left_halfway_ground4 = "images/left_halfway_ground4.jpg"
image left_halfway_ground5 = "images/left_halfway_ground5.jpg"
image faculty_inside = "images/faculty_inside.jpg"
image pet_cat = "images/petcat.jpg"
image science_lab = "images/science_lab.jpg"
image rightside_staircase = "images/rightside_staircase.jpg"
image chair = "images/chair.jpg"
image chair1 = "images/chair1.jpg"
image lobbychairs = "images/lobbychairs.jpg"
image peak_window = "images/peak_window.jpg"
image office = "images/office.jpg"
image g1 = "images/g1.jpg"
image g2 = "images/g2.jpg"
image g3 = "images/g3.jpg"
image g4 = "images/g4.jpg"
image g5 = "images/g5.jpg"
image g6 = "images/g6.jpg"
image g7 = "images/g7.jpg"
image g8 = "images/g8.jpg"
image g9 = "images/g9.jpg"
image g10 = "images/g10.jpg"
image g11 = "images/g11.jpg"
image g12 = "images/g12.jpg"
image acad1 = "images/acad1.jpg"
image bg_director = "images/bg_director.jpg"
 
image faculty_normal = "images/faculty_normal.png"
image faculty_talking = "images/faculty_talking.png"

image hideout_fireexit = "images/hideout_fireexit.jpg"
image hideout_extension = "images/hideout_extension.jpg"

# __GARDEN__ and __EXIT__ (make sure these files exist in /game/imgaes/)
image bg_garden = "images/garden.jpg"
image bg_garden_cat = "images/view_cat.jpg"
image bg_garden1 = "images/garden1.jpg"
image bg_garden2 = "images/garden2.jpg"
image bg_garden3 = "images/garden3.jpg"
image bg_back_garden1 = "images/back_garden1.jpg"
image bg_exit1 = "images/exit1.jpg"
image bg_exit2 = "images/exit2.jpg"
image bg_exit3 = "images/exit3.jpg"
image bg_exit4 = "images/exit4.jpg"
image bg_exit5 = "images/exit5.jpg"
image bg_exit6 = "images/exit6.jpg"
image bg_exit7 = "images/exit7.jpg"
image bg_exit8 = "images/exit8.jpg"
image bg_exit9 = "images/exit9.jpg"
image bg_exit10 = "images/exit10.jpg"
image bg_fire_exit_inside1 = "images/fire_exit_inside1.jpg"
image bg_fire_exit_inside2 = "images/fire_exit_inside2.jpg"
image bg_fire_exit_inside3 = "images/fire_exit_inside3.jpg"
image bg_fire_exit_inside4 = "images/fire_exit_inside4.jpg"
image bg_fire_exit_inside5 = "images/fire_exit_inside5.jpg"
image library1 = "images/library1.jpg"
image library2 = "images/library2.jpg"
image discussion = "images/discussion.jpg"
image bg_nstp = "images/nstp.jpg)" 

# _Floor 2__ (make sure these files exist in /game/images/)
image bg_floor2_halfwayright = "images/floor2_halfwayright.jpg"

#___DOCUMENTS__ PROCESS___
image doc1 = "doc1.jpg"  # Replace with actual file names
image doc2 = "doc2.jpg"
image doc3 = "doc3.jpg"
image doc4 = "doc4.jpg"


image bg_admin_office = "images/admin_office.jpg"
image bg_authorized_exit = "images/authorized_personnelonlyareaexit.jpg"
image avr1 = "images/avr1.jpg"
image avr2 = "images/avr2.jpg"
image bg_avr_door = "images/avrdoor.jpg"
image bg_beside_avr = "images/besideavr.jpg"
image bg_beside_faculty_office = "images/besidefacultyoffice.jpg"
image bg_cashier_window = "images/cashierwindow.jpg"
image clinic1 = "images/clinic_inside.jpg"
image clinic2 = "images/clinic_outside.jpg"


# Up to the 3rd Floor
image stair1 = "images/stair1.jpg"
image stair2 = "images/stair2.jpg"
image stair3 = "images/stair3.jpg"
image stair4 = "images/stair4.jpg"
image stair5 = "images/stair5.jpg"

# Third floor left to the right
image hallway1 = "images/hallway1.jpg"
image hallway2 = "images/hallway2.jpg"
image hallway3 = "images/hallway3.jpg"
image hallway4 = "images/hallway4.jpg"
image hallway5 = "images/hallway5.jpg"
image hallway6 = "images/hallway6.jpg"
image hallway7 = "images/hallway7.jpg"
image hallway8 = "images/hallway8.jpg"
image hallway9 = "images/hallway9.jpg"

# Room 305 Scene
image room307_1 = "images/room307_1.jpg"
image room307_1 = "images/room307_1.jpg"
image room307_1 = "images/room307_1.jpg"
image room307_1 = "images/room307_1.jpg" 

# Room 307 Scene
image room307_1 = "images/room307_1.jpg"
image room307_2 = "images/room307_2.jpg"
image room307_3 = "images/room307_3.jpg"

# Girl's CR
image girls1 = "images/girls1.jpg"
image girls2 = "images/girls2.jpg"
image girls3 = "images/girls3.jpg"
image girls4 = "images/girls4.jpg"

# Rooms
image room1 = "images/room1.jpg"
image room2 = "images/room2.jpg"

# Fourth Floor
image 1 = "images/1.jpg"
image 2 = "images/2.jpg"
image 3 = "images/3.jpg"

# 4th Hallway
image f1 = "images/f1.jpg"
image f2 = "images/f2.jpg"
image f3 = "images/f3.jpg"
image f4 = "images/f4.jpg"
image f5 = "images/f5.jpg"
image f6 = "images/f6.jpg"
image f7 = "images/f7.jpg"
image f8 = "images/f8.jpg"
image f9 = "images/f9.jpg"
image f10 = "images/f10.jpg"
image f11 = "images/f11.jpg"

# Fourth Room
image comlab = "images/comlab.jpg"
image comhardware = "images/comhardware.jpg"
image housekeeping_room = "images/housekeeping_room.jpg"
image travel_and_tours_room1 = "images/travel_and_tours_room1.jpg"
image travel_and_tours_room2 = "images/travel_and_tours_room2.jpg"
image student_org1 = "images/student_org1.jpg"
image hm_storage_room1 = "images/hm_storage_room1.jpg"
image kitchen_lab2 = "images/kitchen_lab2.jpg"
image proj = "images/proj.jpg"
image food_and_bev_room2 = "images/food_and_bev_room2.jpg"
image csc_room1 = "images/csc_room1.jpg"
image csc_room2 = "images/csc_room2.jpg"
image lab_management = "images/lab_management.jpg"
image standard_room = "images/standard_room.jpg"
image deluxe = "images/deluxe.jpg"

# Roof Deck
image rf1 = "images/rf1.jpg"
image rf2 = "images/rf2.jpg"
image rf3 = "images/rf3.jpg"
image rf4 = "images/rf4.jpg"
image rf5 = "images/rf5.jpg"
image rf6 = "images/rf6.jpg"

default visited_sas = False

init python:
    class CharacterImages:
        """Base class for character image management."""
        def __init__(self, name, image_path, default_width, default_height):
            self.name = name
            self.image_path = image_path
            self.default_width = default_width
            self.default_height = default_height
            self.images = {}

        def add_image(self, state, file_name, width=None, height=None):
            """Add an image for a specific state with optional custom dimensions."""
            width = width or self.default_width
            height = height or self.default_height
            self.images[state] = im.Scale(f"{self.image_path}/{file_name}", width, height)

        def get_image(self, state):
            """Retrieve the image for a given state."""
            return self.images.get(state, self.images.get("normal", None))

    # Nurse
    class Nurse(CharacterImages):
        def __init__(self):
            super().__init__("Nurse", "images", 925, 1200)
            self.add_image("normal", "nurse_normal.png")

    # Cashier
    class Cashier(CharacterImages):
        def __init__(self):
            super().__init__("Cashier", "images", 925, 1200)
            self.add_image("talking", "cashier_talking.png", 1200, 1350)
            self.add_image("normal", "cashier_normal.png")

    # Carl
    class Carl(CharacterImages):
        def __init__(self):
            super().__init__("Carl", "images", 1200, 1300)
            self.add_image("normal", "Carl_normal.png", 1200, 1350)
            self.add_image("talking", "Carl_talking.png")
            self.add_image("suggesting", "Carl_suggesting.png")
            self.add_image("thinking", "Carl_thinking.png")

    # Justine
    class Justine(CharacterImages):
        def __init__(self):
            super().__init__("Justine", "images", 925, 1200)
            states = [
                "normal", "talking", "happy", "alarmed", "disappointed",
                "crying", "holding_id", "holding_phone", "waving", "sighing",
                "smiling", "realised", "sad", "laughing", "scared"
            ]
            for state in states:
                self.add_image(state, f"Justine_{state}.png")

    # Kim
    class Kim(CharacterImages):
        def __init__(self):
            super().__init__("Kim", "images", 925, 1200)
            states = ["normal", "holdingID", "smiling", "talking", "calling"]
            for state in states:
                self.add_image(state, f"kim_{state}.png")

    # Guard
    class Guard(CharacterImages):
        def __init__(self):
            super().__init__("Guard", "images", 925, 1200)
            self.add_image("normal", "guard_normal.png")
            self.add_image("happy", "guard_happy_talking.png")
            self.add_image("annoyed", "guard_talking_annoyed.png")
            self.add_image("angry", "guard_talking_angry.png")

    # Lyn
    class Lyn(CharacterImages):
        def __init__(self):
            super().__init__("Lyn", "images", 925, 1200)
            states = [
                "talking", "angry", "anya_smirk", "disgusted", "normal",
                "pouting_talking", "pouting", "smug", "worried"
            ]
            for state in states:
                self.add_image(state, f"Lyn_{state}.png")

    # Ella
    class Ella(CharacterImages):
        def __init__(self):
            super().__init__("Ella", "images", 925, 1200)
            states = ["grinning", "normal", "smiling", "talking", "whispering"]
            for state in states:
                self.add_image(state, f"Ella_{state}.png")

    # Vidal
    class Vidal(CharacterImages):
        def __init__(self):
            super().__init__("Vidal", "images", 925, 1200)
            states = ["angry_talking", "angry", "normal", "smiling", "talking"]
            for state in states:
                self.add_image(state, f"Vidal_{state}.png")

    # Sophie
    class Sophie(CharacterImages):
        def __init__(self):
            super().__init__("Sophie", "images", 925, 1200)
            states = ["normal", "smiling", "talking"]
            for state in states:
                self.add_image(state, f"Sophie_{state}.png")

    # Jorie
    class Jorie(CharacterImages):
        def __init__(self):
            super().__init__("Jorie", "images", 925, 1200)
            states = ["normal", "smiling", "talking"]
            for state in states:
                self.add_image(state, f"Jorie_{state}.png")

    # Mae
    class Mae(CharacterImages):
        def __init__(self):
            super().__init__("Mae", "images", 925, 1200)
            states = ["holding_paper", "normal", "smiling", "talking"]
            for state in states:
                self.add_image(state, f"Mae_{state}.png")

    # Faculty
    class Faculty(CharacterImages):
        def __init__(self):
            super().__init__("Faculty", "images", 925, 1200)
            states = ["normal", "talking"]
            for state in states:
                self.add_image(state, f"Faculty_{state}.png")

    class Vendor(CharacterImages):
        def __init__(self):
            super().__init__("Vendor", "images", 925, 1200)
            states = ["normal", "talking"]
            for state in states:
                self.add_image(state, f"Vendor_{state}.png")
            

# Instantiate character objects
define nurse = Nurse()
define cashier = Cashier()
define carl = Carl()
define justine = Justine()
define kim = Kim()
define guard = Guard()
define lyn = Lyn()
define ella = Ella()
define vidal = Vidal()
define sophie = Sophie()
define jorie = Jorie()
define mae = Mae()
define faculty = Faculty()
define vendor = Vendor()


label before_main_menu:
    $ apply_ui_theme()
    return

$ persistent.ui_theme = "dark"

default persistent.ui_theme = "default"  # This saves the user's selected theme

init python:

    def apply_ui_theme():
        # Use persistent color or default to white
        text_color = persistent.text_color if hasattr(persistent, "text_color") else "#5fa121"

        # Change the say dialogue text color
        style.say_dialogue.color = text_color

        # Optionally, change window background text color or other UI elements here too
        # For example, change textbox window text color or font color if needed

        # To refresh styles immediately, call:
        renpy.restart_interaction()
# Example usage in Ren'Py

label splashscreen:
    play music "audio/main_theme.mp3" fadein 1.0
    $ splash_done = False
    scene black
    show screen splash_screen
    with fade  # Fade-in

    while not splash_done:
        $ renpy.pause(0.5)

    hide screen splash_screen
    with fade  # Fade-out

    return
label staret:
    # Show Justine in normal state
    show expression justine.get_image("normal") as justine
    "Justine" "Hello, I'm in my normal state!"

    # Show Justine in talking state
    show expression justine.get_image("talking") as justine
    "Justine" "Now I'm talking!"

    # Show Carl in thinking state
    show expression carl.get_image("thinking") as carl
    "Carl" "Hmm, I'm thinking..."

label start:
    scene bg_room at custom_size_transform with fade
    play music "audio/bgmusictut.mp3" volume 0.1 loop    

    voice "audio/carl/line1.MP3"
    show expression carl.get_image("normal") at center with dissolve
    cj "Hey there."

    voice "audio/carl/line2.MP3"
    show expression carl.get_image("talking") at center with dissolve
    cj "Are you new to visual novels?"

    menu:
        "I'm new at this, sorry.":
            jump tutorial
        "I already know, thank you.":
            jump skip_tutorial

label tutorial:   
    voice "audio/carl/line3.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    cj "No worries! I'm here to guide you around."

    voice "audio/carl/line4.MP3"
    show expression carl.get_image("talking") at center with dissolve
    cj "This box below me? That's the text box."

    voice "audio/carl/line5.MP3"
    show expression carl.get_image("thinking") at center with dissolve
    cj "All the story, dialogue, and narration happens here."

    voice "audio/carl/line6.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    cj "Want a cleaner view of the background? Just press the H key on your keyboard to hide the UI."

    voice "audio/carl/line7.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    cj "You can also roll back to dialogue with ease using your scroll wheel in you mouse!"

    voice "audio/carl/line8.MP3"
    show expression carl.get_image("talking") at center with dissolve
    cj "You can press H again to bring everything back."

    voice "audio/carl/line9.MP3"
    show expression carl.get_image("thinking") at center with dissolve
    cj "Now if you press the Esc key, you'll open the game menu."

    voice "audio/carl/line10.MP3"
    show expression carl.get_image("normal") at center with dissolve
    cj "Let me explain the buttons there real quick!"

    voice "audio/carl/line11.MP3"
    show expression carl.get_image("talking") at center with dissolve
    cj "History – lets you view past dialogue in case you missed something."

    voice "audio/carl/line12.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    cj "Save and Load – save your progress or return to a previous point."

    voice "audio/carl/line13.MP3"
    show expression carl.get_image("thinking") at center with dissolve
    cj "Preferences – change text speed, music volume, and other settings."

    voice "audio/carl/line14.MP3"
    show expression carl.get_image("talking") at center with dissolve
    cj "About – gives info about the game."

    voice "audio/carl/line15.MP3"
    show expression carl.get_image("normal") at center with dissolve
    cj "Help – shows all the controls."

    voice "audio/carl/line16.MP3"
    show expression carl.get_image("thinking") at center with dissolve
    cj "And Quit – well... exits the game. Careful with that one."

    voice "audio/carl/line17.MP3"
    show expression carl.get_image("suggesting") at center with dissolve
    cj "And don't forget the Return button – it brings you right back to the game."

    voice "audio/carl/line18.MP3"
    show expression carl.get_image("talking") at center with dissolve
    cj "Got it? Sweet. Let's get started!"
    stop music 

    jump main_game

label skip_tutorial:
    voice "audio/carl/line19.MP3"
    show expression carl.get_image("normal") at center with dissolve
    cj "Ah, a veteran I see. I'll leave you to it then."

    jump main_game

label main_game:
    voice "audio/carl/line20.MP3"
    show expression carl.get_image("talking") at center with dissolve
    c "This is where the real story begins..."
    stop music fadeout 1.0

    play music "audio/bgmusicstart.mp3" loop
    scene bg_gate at custom_size_transform with fade
    # Lower BGM volume before voice
    $ renpy.music.set_volume(0.1, channel="music")  # 30% volume

    voice "audio/guard/line1.MP3"
    show expression justine.get_image("normal") at justine_bottom_left with dissolve
    jus "Grabe, hindi ako makapaniwala malapit narin akong makapagtapos sa paaralang ito."
    hide expression justine.get_image("normal") at justine_bottom_left with dissolve

    voice "audio/guard/line2.MP3"
    # The guard appears
    show expression guard.get_image("normal") at kim_bottom_right
    show expression guard.get_image("annoyed") at kim_bottom_right
    g "Good morning, iho. Asan yung I.D mo?"
    hide expression guard.get_image("normal") at kim_bottom_right with dissolve
    hide expression guard.get_image("annoyed") at kim_bottom_right with dissolve

    voice "audio/guard/line3.MP3"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Sorry po kuya, naiwan ko po yung I.D ko."
    hide expression justine.get_image("talking") at justine_bottom_left

    show expression guard.get_image("annoyed") at kim_bottom_right with dissolve
    voice "audio/guard/line4.mp3"
    g "Ayy, pasensya na iho pero bawal kang pumasok pag wala kang I.D."
    hide expression guard.get_image("annoyed") at kim_bottom_right with dissolve
    # CHOICE MENU -------------------------------------------------------------
    menu:
        "Bumalik na lang ako sa bahay":
            jump go_home
        "Tawagan si Kim para kuhanin ang I.D":
            jump call_kim

################################################################################
# CHOICE 1 – GO HOME –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
################################################################################
label go_home:
    voice "audio/guard/choice1/line1.MP3"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Ayy ganon po ba… sige po kuya, uwi na lang po ako."
    show expression guard.get_image("normal") at kim_bottom_right
    voice "audio/guard/choice1/line2.MP3"
    g "Sa susunod, siguraduhing may I.D ka ha."
    hide expression guard.get_image("normal") at kim_bottom_right with dissolve
    show expression justine.get_image("talking") at justine_bottom_left
    $ renpy.pause(0.3)
    window hide
    show expression justine.get_image("normal") at justine_bottom_left
    hide expression justine.get_image("normal") with None
    $ renpy.pause(0.2)
    window show
    voice "audio/guard/choice1/line3.MP3"
    jus "(Grabe nakalimutan ko nga pala ang higpit pala ng guard pero ok lang atleast safe ang estudyante dito sa higpit ng guard, kaysa
    \n naman sa ibang school may guard nga pero wala namang pakialam pano nalang kung may insidente, at least dito samin safe naman."
    voice "audio/guard/choice1/line4.MP3"
    jus "(hayss, nu bayan pagbabalik pa ko malalate din naman ako, hindi pa nagpapapasok yung prof namin kapag late, sige na nga 
    \n bukas nalang ako papasok.)"
    "THE END"
    return


################################################################################
# CHOICE 2 – CALL KIM ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
################################################################################
label call_kim:
    voice "audio/guard/choice2/line1.mp3"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Ayy ganon po ba, wait lang kuya. Papakuha ko lang I.D ko."
    hide expression justine.get_image("talking") with dissolve

    show expression justine.get_image("holding_phone") at justine_bottom_left
    "Tumawag si Justine sa kanyang kaibigan…"

    voice "audio/guard/choice2/line2.mp3"
    jus "Hi Kim, nasaan ka ngayon?"
    hide expression justine.get_image("holding_phone") at justine_bottom_left

    scene a at custom_size_transform with fade
    show expression kim.get_image("calling") at right with dissolve
    voice "audio/guard/choice2/line3.mp3"
    k "Nasa bahay te. Malamang"
    hide expression kim.get_image("calling") at right with dissolve

    scene bg_gate at custom_size_transform with fade
    show expression justine.get_image("holding_phone") at justine_bottom_left
    voice "audio/guard/choice2/line4.mp3"
    jus "Gusto ko kasing mag-ikot sa school kaso naiwan ko I.D ko, pwde ka bang dumaan sa bahay? Kunin mo yung ID ko."
    hide expression justine.get_image("holding_phone") at justine_bottom_left

    scene a at custom_size_transform with fade
    show expression kim.get_image("calling") at right with dissolve
    voice "audio/guard/choice2/line5.mp3"
    k "Ah okay, sakto may gagawin din naman ako sa school e"
    hide expression kim.get_image("calling") at right with dissolve

    "Ilang minuto ang lumipas…"
    
    scene bg_gate at custom_size_transform with fade

    show expression kim.get_image("holdingID") at kim_bottom_right with dissolve
    voice "audio/guard/choice2/line6.mp3"
    k "Jas! Eto na I.D mo!"
    hide expression kim.get_image("holdingID") with dissolve

    voice "audio/guard/choice2/line7.mp3"
    show expression justine.get_image("holding_id") at justine_bottom_left
    show expression kim.get_image("normal") at kim_bottom_left with dissolve
    jus "Sige! Salamat!"
    

    voice "audio/guard/choice2/line8.mp3"

    show expression guard.get_image("happy") at kim_bottom_right with dissolve
    voice "audio/guard/choice2/line8.mp3"
    g "Hmm… sige, pwede na kayong pumasok."
    hide expression guard.get_image("happy") with dissolve
    hide expression justine.get_image("holding_phone") with dissolve
    hide expression justine.get_image("talking") with dissolve
    hide expression kim.get_image("normal") at kim_bottom_left with dissolve
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("holding_id") with dissolve

    voice "audio/guard/choice2/line9.mp3"
    show expression kim.get_image("smiling") at kim_bottom_center
    show expression justine.get_image("smiling") at justine_bottom_center
    jus "Sige, salamat po"
    hide expression kim.get_image("smiling") with dissolve
    hide expression justine.get_image("smiling") with dissolve
    scene bg_guard_house at custom_size_transform with fade


label hub_room:
    scene bg_after_school_gate at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    call screen nav_door_gate
    return

default visited_library = False
label door_label:
    if visited_library:
        voice "audio/public_library/line6.mp3"
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Sarado na ang public library. Kanina pa tayo dumaan doon."
        jump hub_room
    else:
        $ visited_library = True
        voice "audio/public_library/line1.mp3"
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Ohhh, yung Public Library... ang dami naming memory dito.…"
        scene bg_pub_lib_door at custom_size_transform with fade
        voice "audio/public_library/line2.mp3"    
        show expression justine.get_image("smiling") at justine_bottom_left
        jus "Dito kami lagi natambay ng mga kaibigan ko sa tuwing may vacant kami."

        voice "audio/public_library/line3.mp3"
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Minsan sabay-sabay kaming gumagawa ng homework dito, pero mas madalas puro kwentuhan lang talaga, May isang beses\npa nga, napagalitan kami ng librarian kasi masyado kaming maingay"

        voice "audio/public_library/line4.mp3"
        show expression justine.get_image("laughing") at justine_bottom_left
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Kung tama ang pagka-alala ko... open to every weekdays, 8 AM to 5 PM. Kaya minsan napapaovertime yung mga staff dito \nkasi di namin namamalayan — 5 na pala. Sorry po."
        hide expression justine.get_image("Sighing") with dissolve

        voice "audio/public_library/line5.mp3"
        show expression justine.get_image("smiling") at justine_bottom_left
        jus "Hay... nami-miss ko ‘yung mga ganung araw. Para bang ang gaan ng lahat."
        hide expression justine.get_image("smiling") with dissolve
        jump hub_room

default visited_explore_new_building = False
label explore_new_building:
    if not visited_explore_new_building:
        $ visited_explore_new_building = True
        scene bg_nearing_new_building at custom_size_transform with fade
        voice "audio/new_building/line1.mp3"
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Grabe... matatapos na 'yung school year, pero 'tong building na 'to, hindi pa rin tapos."

        voice "audio/new_building/line2.mp3"
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Parang hindi rin ako makaka-graduate kung hihintayin ko 'yang matapos. I wonder, magkakaroon kaya ng bagong program \ndito?"

        voice "audio/new_building/line3.mp3"
        show expression justine.get_image("normal") at justine_bottom_left
        jus "Hay... sana naman, pagbalik ko next sem, may progreso na."
    else:
        scene bg_nearing_new_building at custom_size_transform with fade
        pause 0.1
        scene bg_new_building1 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building2 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building3 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building4 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building5 at custom_size_transform with fade
        pause 0.1
        scene bg_new_building6 at custom_size_transform with fade
        pause 0.1
        show expression justine.get_image("talking") at justine_bottom_left with dissolve
        voice "audio/new_building/line4.mp3"
        jus "Gina-gawa parin hanggang ngayon."
        hide expression justine.get_image("talking") with dissolve
        scene bg_new_building6 at custom_size_transform with fade
        pause
    jump callscreen

label callscreen:
    scene bg_far_view_entrance at custom_size_transform with fade
    call screen custom_choice_menu
    return

label resting_ground:
    scene bg_tambayan_to_entrance at custom_size_transform with fade

    voice "audio/resting/line1.mp3"
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Ang tahimik dito ngayon ha."
    hide expression justine.get_image("happy") with dissolve
    jump choicethree

label choicethree:
    scene bg_tambayan_to_entrance at custom_size_transform with fade
    call screen rest_choice_menu
    return

default visited_stone_circle = False
label stone_circle:
    if not visited_stone_circle:
        $ visited_stone_circle = True
        scene bg_tambayan_to_entrance at custom_size_transform with fade
        scene bg_circle_area_lower_view at custom_size_transform with fade
        voice "audio/table_scene/line1.mp3"
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Ahh, eto lagi after ng klase. Grabe kami makatakbo kasi inuunahan namin 'yung mga estudyante—baka mawalan kami ng pwesto, \n kasi dito kami nakain tuwing lunch time."
        show expression justine.get_image("laughing") at justine_bottom_left
        hide expression justine.get_image("happy") at justine_bottom_left
        hide expression justine.get_image("laughing") at justine_bottom_left
    else:
        scene bg_tambayan_to_entrance at custom_size_transform with fade
    
        voice "audio/table_scene/line2.mp3"
        show expression justine.get_image("happy") at justine_bottom_left
        jus "Ka-miss makipag-chismisan dito haha"
        hide expression justine.get_image("happy") with dissolve
    jump choicethree

label vendor:
    scene bg_vendor_view at custom_size_transform with fade

    voice "audio/vendor/line9.mp3"
    show expression vendor.get_image("talking") at kim_bottom_right with dissolve
    vd "Oyyyy, pogi bili kana"
    hide expression vendor.get_image("talking") at kim_bottom_right with dissolve
    menu:
        "Bumili":
            jump bumili
        "Huwag bumili":
            jump huwag_bumili

label bumili:
    scene bg_vendor at custom_size_transform with fade

    voice "audio/vendor/line1.mp3"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Kuya, magkano yung softdrinks?"
    hide expression justine.get_image("talking") with dissolve

    voice "audio/vendor/line2.mp3"
    show expression vendor.get_image("talking") at kim_bottom_right with dissolve
    "Anong softdrinks pogi"
    hide expression vendor.get_image("talking") at kim_bottom_right with dissolve

    voice "audio/vendor/line3.mp3"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Coke po"
    hide expression justine.get_image("talking") with dissolve

    voice "audio/vendor/line4.mp3"
    show expression vendor.get_image("talking") at kim_bottom_right with dissolve
    "Sige, ito oh"
    hide expression vendor.get_image("talking") at kim_bottom_right with dissolve
    
    voice "audio/vendor/line5.mp3"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Salamat po"
    hide expression justine.get_image("talking") with dissolve
    jump choicethree

label huwag_bumili:
    scene bg_vendor_view at custom_size_transform with fade

    voice "audio/vendor/line6.mp3"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "Salamat na lang po"
    hide expression justine.get_image("talking") with dissolve

    voice "audio/vendor/line7.mp3"
    show expression vendor.get_image("talking") at kim_bottom_right with dissolve
    "Sure ka pogi? Baka gutom ka na?"
    hide expression vendor.get_image("talking") at kim_bottom_right with dissolve

    voice "audio/vendor/line8.mp3"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "haha... next time na lang po"
    hide expression justine.get_image("talking") with dissolve
    jump choicethree

label hideout:
    scene bg_vendor_view at custom_size_transform with fade

    show expression justine.get_image("laughing") at justine_bottom_left
    voice "audio/hideout/line9.mp3"
    jus "Solid netong tambayan na to! Sa dulo kaso sarado"
    menu:
        "Greet the Guard":
            jump greet_guard
        "Just walk away":
            jump walk_away
    pause

label greet_guard:
    scene bg_entering_hideout at custom_size_transform with fade

    voice "audio/hideout/line1.mp3"
    show expression justine.get_image("happy") at justine_bottom_left
    jus "Oh eto yung hideout according sa boys"

    voice "audio/hideout/line2.mp3"
    jus "Pero siguro ang pinaka-memorable kong time sa lugar na , is siguro yung nag open forum kami..."

    voice "audio/hideout/line3.mp3"
    show expression justine.get_image("Sighing") at justine_bottom_left
    jus "Hays, hindi ko parin makalimutan yung memory na yun, grabe ang awkward ng atmosphere"
    hide expression justine.get_image("Sighing") with dissolve
    jump choicethree

label walk_away:
    scene bg_entering_hideout at custom_size_transform with fade

    voice "audio/hideout/line4.mp3"
    show expression guard.get_image("annoyed") at kim_bottom_right with dissolve
    g "oyy, oyy ano ginagawa mo dito?"
    hide expression guard.get_image("annoyed") with dissolve

    voice "audio/hideout/line5.mp3"
    show expression justine.get_image("talking") at justine_bottom_left
    jus "ahh, nag-iikot ikot lang po"
    hide expression justine.get_image("talking") with dissolve

    voice "audio/hideout/line6.mp3"
    show expression guard.get_image("angry") at kim_bottom_right
    g "di mo ba alam na bawal pumasok dito ng walang paalam?!"
    hide expression guard.get_image("angry") with dissolve

    voice "audio/hideout/line7.mp3"
    show expression justine.get_image("scared") at justine_bottom_left
    jus "sorry po kuya guard aalis na po ako…"
    hide expression justine.get_image("scared") with dissolve

    voice "audio/hideout/line8.mp3"
    show expression guard.get_image("annoyed") at kim_bottom_right with dissolve
    g "wag na mauulit to kung hindi i-re-report kita sa SAS"
    hide expression guard.get_image("annoyed") with dissolve
    jump choicethree


################################################################################
#  ENTER BUILDING – Lobby hub
################################################################################
label enter_buildingcampus:
    scene bg_entering_the_school_lobby at custom_size_transform with fade

    show expression justine.get_image("normal") at justine_bottom_left
    voice "audio/main_building/line1.mp3"
    jus "Pasok tayo sa main building. Saan kaya pupunta ngayon?"
    scene bg_informationdesk at custom_size_transform with fade
    pause
    scene bg_pup_lobby at custom_size_transform with fade
    jump inside_building

label inside_building:
    scene bg_window1 at custom_size_transform with fade
    call screen inside_choice_menu
    call screen information_desk
    return

label cashier:
    scene bg_cashier_window at custom_size_transform with fade

    voice "audio/cashier/line1.mp3"
    show expression justine.get_image("smiling") at justine_bottom_left
    jus "{size=50}Cashier… mabuti na wala ako kailangan na bayarin. Tinamad pa kasi sa ibang subjects ayan tuloy \nbumayad pa siya ng tuition para sa tatlong semesters…"

    voice "audio/cashier/line2.mp3"
    show expression cashier.get_image("talking") at kim_bottom_right
    cs "{size=50}Hello, may babayaran pa ba kayo ngayon?"
    hide expression cashier.get_image("talking") with dissolve

    voice "audio/cashier/line3.mp3"    
    show expression justine.get_image("smiling") at justine_bottom_left
    jus "{size=50}Ay wala naman, pasensya na sa paga-abala."
    hide expression justine.get_image("smiling") at justine_bottom_left

    voice "audio/cashier/line4.mp3"
    show expression cashier.get_image("talking") at kim_bottom_right
    cs "{size=50}Okay lang po. Kung may transaction kayo na gagawin"
    voice "audio/cashier/line5.mp3"
    cs "{size=50}pwede po kayo magbayad online sa PUP SIS or dalhin mo nalang ID mo dito para ma-verify \nang transaction niyo po."
    hide expression cashier.get_image("talking") with dissolve
    jump left_ground_1

label right_hall:
    scene floor1_hallwayright at custom_size_transform with fade
    show expression justine.get_image("Sighing") at justine_bottom_left
    voice "audio/mid/line1.mp3"
    jus "grabe walang katao tao himala?"
    hide expression justine.get_image("Sighing") with dissolve

label floor1_right_hall:
    scene floor1_hallwayright at custom_size_transform with fade
    call screen right_hall_menu
    return

label clinic_room:
    scene clinic2 at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/clinic/line1.mp3"
    jus "Clinic… ayan, tahimik pero dito sikat ang lahat ng drama sa buhay."
    show expression justine.get_image("normal") at justine_bottom_left
    voice "audio/clinic/line2.mp3"
    jus "Dito ako tumatambay minsan dahil sa sakit ng ulo, pati na din dahil sa minsan na pasakit ng loob."
    show expression justine.get_image("Sighing") at justine_bottom_left
    voice "audio/clinic/line3.mp3"
    jus "Minsang umupo ako d'yan hindi dahil sa masamang pakiramdam kundi dahil gusto ko lang ng pahinga. \nAt ang Nurse? Parang naging nanay ko pa."
    show expression justine.get_image("smiling") at justine_bottom_left
    voice "audio/clinic/line4.mp3"
    jus "Palagi niya akong tinatanong, 'Okay ka lang ba talaga? Nakakamiss toh talaga."
    # Start of flashback sequence
    scene clinic1 at custom_size_transform with fade
    show expression nurse.get_image("normal") at right
    show expression justine.get_image("normal") at justine_bottom_left
    voice "audio/clinic/line5.mp3"
    n "Ay dios mio, tambay ka nanaman dito uli? Ano nanaman pakiramdam mo hijo."
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/clinic/line6.mp3"
    jus "Wala po ma'am, unting sakit lang ng ulo po."
    voice "audio/clinic/line7.mp3" 
    n "Wag mo kalimutan na alagaan ang sarili mo hijo."
    # End of flashback
    scene clinic2 at custom_size_transform with fade
    show expression justine.get_image("happy") at justine_bottom_left
    voice "audio/clinic/line8.mp3" 
    jus "Ang bait talaga ni ma'am. Sana makadalaw ako ulit dito."
    hide expression justine.get_image("happy") with dissolve
    jump floor1_right_hall

label sas:
    if not visited_sas:
        $ visited_sas = True
        scene bg_sas at custom_size_transform with fade
        show expression justine.get_image("normal") at justine_bottom_left with dissolve
        show expression justine.get_image("talking") at justine_bottom_left with dissolve
        voice "audio/sas/line1.mp3"
        jus "Yung SAS Office. Hays.. Naalala ko tuloy tuwing enrollment. Paunahan talaga"
        show expression justine.get_image("sighing") at justine_bottom_left with dissolve
        hide expression justine.get_image("normal")
        hide expression justine.get_image("talking")
        hide expression justine.get_image("sighing")
    else:
        scene bg_sas at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left 
        voice "audio/sas/line2.mp3"
        jus "Buti nalang tapos na ako sa mga ganyan ganyan"
        hide expression justine.get_image("happy") with dissolve
    jump floor1_right_hall
return

label right_hall_forward2:
    scene bg_acad at custom_size_transform with fade
    call screen right_hall_menu1
    return

label show_documents:
    scene bg_acad at custom_size_transform

    show doc1 with fade
    show expression justine.get_image("happy") at justine_bottom_left  
    voice "audio/show_documents/line1.mp3"
    "This is the QR Code where you can scan thru phone"
    pause 1.0  # Added duration for pause

    show doc2 with fade
    voice "audio/show_documents/line2.mp3"
    "Here is the second request letter template"
    pause 1.0

    show doc3 with fade
    voice "audio/show_documents/line3.mp3"
    "This is the third document for the campus reservation"
    pause 1.0

    show doc4 with fade
    voice "audio/show_documents/line4.mp3"
    "Lastly, this is the SINTA where you can do appointment"
    pause 1.0
    jump right_hall_forward2

label director:
    scene bg_director at custom_size_transform with fade
    
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/director/line1.mp3"
    jus "Oh, ito yung director office"
    hide expression justine.get_image("talking") with dissolve

    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    voice "audio/director/line2.mp3"
    jus "Hehe, naaalala ko laging busy si Direk. Para mas lalong mapa-unlad ang Campus na ito."
    show expression justine.get_image("happy") at justine_bottom_left
    hide expression justine.get_image("laughing") with dissolve

    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    voice "audio/director/line3.mp3"
    jus "Huwag na natin istorbohin si Director.."
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("laughing") with dissolve
    jump right_hall_forward2

label admin:
    scene adminoffice at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/admin/line1.mp3"
    jus "Na-alala ko nung gumawa kami ng system para sa finals namin sa comprog pumunta kami dito para humingi ng permiso \nna mag-ikot sa campus at mag-picture"

    show expression justine.get_image("Sighing") at justine_bottom_left
    voice "audio/admin/line2.mp3"
    jus "naka-ilang balik kami dahil may proper procedure pala bago pumunta dito."

    # Start of flashback sequence
    scene lobbychairs at custom_size_transform with fade
    show expression mae.get_image("talking") at left
    show expression sophie.get_image("normal") at right
    voice "audio/admin/line3.mp3"
    m "Kaming dalawa nalang ni Sophie yung papasok sa loob para ipasa yung letter"
    # 1st Attempt
    scene bg_admin_office at custom_size_transform with fade
    show expression mae.get_image("smiling") at left with dissolve
    show expression sophie.get_image("smiling") at right with dissolve
    "(Left the office after a few minutes)"
    hide expression mae.get_image("smiling") with dissolve
    hide expression sophie.get_image("smiling") with dissolve
    scene lobbychairs at custom_size_transform with fade

    show expression sophie.get_image("talking") at right
    voice "audio/admin/line4.mp3"
    s "Guys ulitin daw mali raw yung format ng letter"
    hide expression sophie.get_image("talking") with dissolve

    show expression mae.get_image("talking") at left
    voice "audio/admin/line5.mp3"
    m "Ganito raw yung proper format"
    show expression mae.get_image("holding_paper") at left
    # 2nd Attempt
    scene bg_admin_office at custom_size_transform with fade
    show expression sophie.get_image("talking") at right
    show expression mae.get_image("normal") at left
    "Few minutes"
    scene lobbychairs at custom_size_transform with fade

    show expression mae.get_image("talking") at left
    voice "audio/admin/line6.mp3"
    m "need naman daw ng appointment sa sinta"
    # 3rd Attempt
    scene bg_admin_office at custom_size_transform with fade

    show expression sophie.get_image("talking") at right
    voice "audio/admin/line7.mp3"
    s "Manifesting ma-approve na to"
    show expression mae.get_image("normal") at left
    "After long long minutes"

    scene lobbychairs at custom_size_transform with fade

    show expression mae.get_image("talking") at right
    voice "audio/admin/line8.mp3"
    ma "Finally! na-approve na rin"
    hide expression mae.get_image("talking") with dissolve
    # End of Flashback

    show expression justine.get_image("laughing") at justine_bottom_left
    voice "audio/admin/line9.mp3"
    jus "Haha... naaawa ako sa kanila"
    hide expression justine.get_image("laughing") with dissolve
    menu:
        "knock and enter the admin office":
            jump adm_office1
        "Just enter the door":
            jump adm_office2
    jump right_hall_forward2

label adm_office1:
    scene bg_admin_office at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/admin/line10.mp3"
    jus "Hello po ma'am vidal"

    show expression vidal.get_image("talking") at right
    voice "audio/admin/line11.mp3"
    v "And you are..?"

    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/admin/line12.mp3"
    jus "Justine po ma'am from BSIT 4-1"

    show expression vidal.get_image("talking") at right
    voice "audio/admin/line13.mp3"
    v "Oh why hello Justine, what can I do for you?"

    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/admin/line14.mp3"
    jus " nag-iikot Ikot lang po para sa huling sandali ko as a student of this sintang paaralan"
    
    show expression vidal.get_image("talking") at right
    voice "audio/admin/line15.mp3"
    v "Kung ganon ay, enjoyin mo na habang nandito ka"

    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/admin/line16.mp3"
    jus "Maraming salamat po"
    hide expression justine.get_image("talking") with dissolve
    hide expression vidal.get_image("talking") with dissolve
    jump right_hall_forward2

label adm_office2:
    scene bg_admin_office at custom_size_transform with fade
    show expression vidal.get_image("angry_talking") at right
    voice "audio/admin/line17.mp3"
    v "Sino ka at bakit ka pumapasok lang ng basta basta?"

    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/admin/line18.mp3"
    jus "uhmmm... Justine po ma'am from BSIT 4-1 po"

    show expression vidal.get_image("angry_talking") at right
    voice "audio/admin/line19.mp3"
    v "Justine!!! Ilang taon ka nang nag-aaral dito pero hindi mo man lang alam ang tamang proseso bago pumasok?"
    
    show expression justine.get_image("scared") at justine_bottom_left
    voice "audio/admin/line20.mp3"
    jus "Sorry po Ma'am Vidal, hindi na po mau-ulit"

    show expression vidal.get_image("angry_talking") at right
    voice "audio/admin/line21.mp3"
    v "Kakatok ka lang ng 3 beses and give your greetings, ganoon ba kahirap yon?"

    show expression vidal.get_image("angry_talking") at right with dissolve
    voice "audio/admin/line22.mp3"
    v "Labas!, marami pa kaming ginagawa at dadagdag ka pa!!!"
    scene adminoffice at custom_size_transform with fade
    "Justine was forced out"
    hide expression vidal.get_image("angry_talking") with dissolve
    jump right_hall_forward2

label mid:
    scene bg_midstair at custom_size_transform
    
    

label right_hall_forward3:
    scene bg_midstair at custom_size_transform with fade
    call screen right_hall_menu2

label lgbt_cr:
    scene bg_lgbt3 at custom_size_transform with fade
    scene bg_lgbt2 at custom_size_transform with fade
    scene bg_lgbt1 at custom_size_transform with fade

    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/lgbt/line1.mp3"
    jus "Nung nag PUPCET kami dati, nagulat ako na may LGBTQ na cr, Kasi sa lahat ng school na napag-entrance exam ko. Ngayon \nlang ako nakakita ng cr na para talaga sa member ng LGTBQ"

    show expression justine.get_image("talking") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    voice "audio/lgbt/line2.mp3"
    jus "Iba talaga ang PUP"
    hide expression justine.get_image("talking") with dissolve
    hide expression justine.get_image("laughing") with dissolve
    jump lgbt_cr_menu

label lgbt_cr_menu:
    scene bg_lgbt1 at custom_size_transform with fade
    call screen lgbt_cr

label back_garden:
    scene g1 at custom_size_transform with fade
    scene g2 at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/garden/line1.mp3"
    jus "Hmmmm, naaalala ko sa banda rito namin nilagay yung mga project na halaman noong first year kami"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve

    show expression guard.get_image("normal") at kim_bottom_right
    show expression guard.get_image("talking_annoyed") at kim_bottom_right
    voice "audio/garden/line2.mp3"
    g "Oyyy oyy, bawal pumunta rito ng walang paalam"
    hide expression guard.get_image("normal") with dissolve
    hide expression guard.get_image("talking_annoyed") with dissolve

    
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/garden/line3.mp3"
    jus "Ahhh sige po kuya, alis na lang ako"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve
    jump right_hall_forward3
    return

label back_garden_1:
    scene g1 at custom_size_transform with fade
    scene g2 at custom_size_transform with fade
    scene g3 at custom_size_transform with fade
    scene g4 at custom_size_transform with fade
    scene g5 at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    voice "audio/garden/line4.mp3"
    jus "Hmmmm, naaalala ko banda rito namin nilagay yung mga project na halaman noong first year kami"
    hide expression justine.get_image("normal") with dissolve

    show expression guard.get_image("annoyed") at right
    voice "audio/garden/line5.mp3"
    g "Ang kulit mo ah! Diba sinabi ko na bawal dito?!"
    hide expression guard.get_image("annoyed") with dissolve

    show expression justine.get_image("normal") at justine_bottom_left
    voice "audio/garden/line6.mp3"
    jus "Sorry po kuya, hindi na po mauulit"
    hide expression justine.get_image("normal") with dissolve
    show expression guard.get_image("annoyed") at right
    voice "audio/garden/line7.mp3"
    g "Talagang hindi na mau-ulit to"
    voice "audio/garden/line8.mp3"
    g "Dahil dadalhin na kita sa Admin Office"
    hide expression guard.get_image("annoyed") with dissolve

    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/garden/line9.mp3"
    jus "Sorry po kuya, patawarin niyo na po ako, gusto ko lang naman pong mag-ikot"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve

    show expression guard.get_image("annoyed") at right
    voice "audio/garden/line10.mp3"
    g "Magpaliwanag ka nalang sa Admin Office"
    hide expression guard.get_image("annoyed") with dissolve

    scene bg_admin_office at custom_size_transform with fade
    show expression guard.get_image("annoyed") at right
    voice "audio/garden/admin/line1.mp3"
    g "Good morning po Ma'am, irereklamo ko lang po ito. Paulit-ulit na kasi at hindi sumusunod"
    voice "audio/garden/admin/line2.mp3"
    g "Pumupunta sa mga lugar na hindi dapat puntahan ng walang permiso"
    hide expression guard.get_image("annoyed") with dissolve
    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("talking") at right
    voice "audio/garden/admin/line3.mp3"
    v "Ano pangalan, year at section mo iho?"
    hide expression vidal.get_image("normal") with dissolve
    hide expression vidal.get_image("talking") with dissolve

    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/garden/admin/line4.mp3"
    jus "Justine po from BSIT 4-1"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve
    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("talking") at right
    voice "audio/garden/admin/line5.mp3"
    v "Okay Justine, is that true?"
    hide expression vidal.get_image("normal") with dissolve
    hide expression vidal.get_image("talking") with dissolve
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/garden/admin/line6.mp3"
    jus "Pasensya po Ma'am. Gusto ko lang naman po mag-ikot"
    
    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("talking") at right
    voice "audio/garden/admin/line7.mp3"
    v "Dahil diyan magkakaroon ka ng punishment dahil sa hindi pagsunod at paglabag"
    voice "audio/garden/admin/line8.mp3"
    v "Kinakailangan mo na gawin ang mga dapat na i-utos o i-aassign sayong gawain"
    voice "audio/garden/admin/line9.mp3"
    v "Kailangan mo itong matapos at magawa kung hindi malalate ang pag-graduate mo"
    hide expression vidal.get_image("normal") with dissolve
    hide expression vidal.get_image("talking") with dissolve

    show expression justine.get_image("talking") at justine_bottom_left
    show expression justine.get_image("Sighing") at justine_bottom_left
    show expression justine.get_image("scared") at justine_bottom_left
    voice "audio/garden/admin/line10.mp3"
    jus "Pero po Ma'am...."
    hide expression justine.get_image("talking") 
    hide expression justine.get_image("Sighing")
    hide expression justine.get_image("scared") with dissolve

    show expression vidal.get_image("normal") at right
    show expression vidal.get_image("angry") at right
    show expression vidal.get_image("angry_talking") at right
    voice "audio/garden/admin/line11.mp3"
    v "No more buts, you may go now"
    hide expression vidal.get_image("normal") 
    hide expression vidal.get_image("angry") 
    hide expression vidal.get_image("angry_talking") with dissolve

    "THE END"

    jump right_hall_forward2


label garden_1:
    scene bg_garden at custom_size_transform with fade
    
label garden_view_menu:
    scene bg_garden at custom_size_transform with fade
    call screen garden_view

label garden_view_menu1:
    scene bg_garden1 at custom_size_transform with fade
    call screen cat

label garden_view2:
    scene bg_garden2 at custom_size_transform with fade
    pause 1.0
    scene bg_garden3 at custom_size_transform with fade
    pause 1.0
         
    jump back_garden_view

label back_garden_view:
    scene bg_garden3 at custom_size_transform 
    menu:
        "Back Garden and Greet the Guard":
            jump back_garden
        "Back Garden and Didn't Greet the GUard":
            jump back_garden_1

label g:
    scene g12 at custom_size_transform with dissolve
    call screen entrance_hideout

label right_exit:
    scene bg_exit1 at custom_size_transform with fade
    scene bg_exit2 at custom_size_transform with fade
    scene bg_exit3 at custom_size_transform with fade
    scene bg_exit4 at custom_size_transform with fade
    scene bg_exit5 at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/right_exit/line1.mp3"
    jus "Ohhh.. ito yung short cut palabas sa gate pero usually kasi naka-sara to."
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve

    menu:
        "Pet the Cat":  # _____Choice 1_______
            jump pet_cat
        "Do not Pet the Cat":
            jump donotpet

label pet_cat:
    scene pet_cat at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    voice "audio/right_exit/line2.mp3"
    jus "Wow! Ang cute naman ng pusa"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("laughing") with dissolve

    jump right_exit_menu

label donotpet:
    scene bg_exit5 at custom_size_transform with fade
    jump right_exit_menu

label maingate:
    scene bg_after_school_gate at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    voice "audio/roofdeck/line10.mp3"
    jus "ang daming ko naging memorya dito may maganda pero may mga part na gusto ko din kalimutan pero masasabi ko \ntalaga na ma mi-miss ko talaga to sa susunod ulit sintang paaralan"
    "THE END"
    jump outside_exit_menu

label right_exit_menu:
    scene bg_exit6 at custom_size_transform with fade
    pause 1.0
    scene bg_exit7 at custom_size_transform with fade
    call screen right_exit_menu1

label outside_exit:
    scene bg_exit8 at custom_size_transform with fade
    pause 1.0
    scene bg_exit9 at custom_size_transform with fade
    pause 1.0
    scene bg_exit10 at custom_size_transform with fade
    pause 1.0
    jump outside_exit_menu

label fire_exit_inside1:
    scene bg_fire_exit_inside1 at custom_size_transform with fade
    scene bg_fire_exit_inside2 at custom_size_transform with fade
    scene bg_fire_exit_inside3 at custom_size_transform with fade
    scene bg_fire_exit_inside4 at custom_size_transform with fade
    scene bg_fire_exit_inside5 at custom_size_transform with fade

label fire_exit_inside_menu:
    scene bg_fire_exit_inside5 at custom_size_transform with fade
    call screen fire_exit_inside_menu1

label outside_exit_menu:
    scene bg_after_school_gate at custom_size_transform with fade
    call screen nav_door_gate

label upstairs:
    scene bg_stair1 at custom_size_transform with fade
    pause 1.0
    scene bg_stair2 at custom_size_transform with fade
    pause 1.0
    scene bg_stair3 at custom_size_transform with fade

    jump second_floor_stair

label second_floor_stair:
    scene bg_stair4 at custom_size_transform with fade
    scene bg_stair5 at custom_size_transform with fade
    jump second_floor_menu


label male_bathroom1:
    scene m1 at custom_size_transform with fade
    scene m2 at custom_size_transform with fade
    scene m3 at custom_size_transform with fade
    scene m4 at custom_size_transform with fade
    scene m5 at custom_size_transform with fade
    call screen male_bathroom
    return

label fire_exit:
    if not visited_fire_exit:
        $ visited_fire_exit = True
        scene fire_exit2 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/fire_exit/line1.mp3"
        jus "Na-aalala ko rito lagi pumupunta si Mae. Tuwing nag-aantay kami sa last subject"
        hide expression justine.get_image("talking") with dissolve
        hide expression justine.get_image("happy") with dissolve
        # Start of Flashback Scene____
        scene fire_exit1 at custom_size_transform with fade
        show expression mae.get_image("smiling") at kim_bottom_right
        show expression mae.get_image("talking") at kim_bottom_right
        voice "audio/fire_exit/line2.mp3"
        m "grabe ang sarap ng hangin"
        voice "audio/fire_exit/line3.mp3"
        m "nakaka relax pwede ka mag emote dito oh"
        hide expression mae.get_image("smiling") with dissolve
        hide expression mae.get_image("talking") with dissolve
        # End of Flashback
    else:
        # IRL
        show expression justine.get_image("smiling") at justine_bottom_left
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/fire_exit/line4.mp3"
        jus "hmmm.. Nakakrelax nga"
        # Justine Monologue
        voice "audio/fire_exit/line5.mp3"
        jus "Pero alis na tayo rito kasi hindi dapat tinatambayan 'to"
        hide expression justine.get_image("smiling") with dissolve
        hide expression justine.get_image("happy") with dissolve
        # End of Justine Monologue
    jump second_floor_menu

default visited_fire_exit = False
label second_floor_menu:
    scene bg_floor2_halfwayright at custom_size_transform with fade
    call screen right_hall_menu3

label floor2_1:
    scene sf1 at custom_size_transform with fade
    scene sf2 at custom_size_transform with fade
    scene sf3 at custom_size_transform with fade
    scene sf4 at custom_size_transform with fade
    scene sf5 at custom_size_transform with fade
    scene sf6 at custom_size_transform with fade
    call screen room
    return

label floor2_2:
    scene sf6 at custom_size_transform with fade
    call screen room
    return

label room_204:
    if not visited_room_204:
        $ visited_room_204 = True
        scene chair at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/room_204/line1.mp3"
        jus "madami kong memory dito pero ang pinaka paborito ko siguro yung nag pra-practice kami para sa chorale"
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/room_204/line2.mp3"
        jus "Na-aalala ko tuloy si Carl nung huling practice namin"
        show expression justine.get_image("laughing") at justine_bottom_left
        hide expression justine.get_image("happy") with dissolve
        hide expression justine.get_image("talking") with dissolve
        # Start of the Flashback
        scene chair1 at custom_size_transform with fade
        show expression carl.get_image("suggesting") at right
        voice "audio/room_204/line3.mp3"
        c "kabayo ay di natin problema~  pulot at damo lang ay tama na~"
        show expression carl.get_image("talking") at right
        hide expression carl.get_image("suggesting") with dissolve
        hide expression carl.get_image("talking") with dissolve
        # End of Flashback
    else:
        # IRL
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/room_204/line4.mp3"
        jus "Kahit 2 days lang practice namin na-clutch pa rin namin"
        show expression justine.get_image("laughing") at justine_bottom_left
        hide expression justine.get_image("happy") with dissolve
        hide expression justine.get_image("laughing") with dissolve
    jump floor2_2

default visited_room_204 = False
label floor2_3:
    scene sf7 at custom_size_transform with fade
    call screen pup
    return

default visited_pup_library = False
label pup_library:
    if not visited_pup_library:
        $ visited_pup_library = True
        scene library1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left with dissolve
        voice "audio/pup/line1.mp3"
        jus "Dito sa library na 'to. Naaalala ko lagi kaming nag-tatambay dito, pag may vacant time o kaya kapag nags-study kami rito"

        show expression justine.get_image("happy") at justine_bottom_left
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/pup/line2.mp3"
        jus "na alala ko tuloy yung sinabi ni Sophie"
        hide expression justine.get_image("talking") with dissolve
        hide expression justine.get_image("happy") with dissolve
        # Start of the Flashbacks
        scene library1 at custom_size_transform with fade
        show expression sophie.get_image("smiling") at kim_bottom_right
        voice "audio/pup/line3.mp3"
        jus "At ang sobrang lamig sa room nato dahil may aircon kaya ang maganda tambayan. Lalo na kung sa room namin pag ka-klase \nang init-init kaya after ng class namin dito agad kami pupunta sa library."
        show expression sophie.get_image("talking") at kim_bottom_right
        hide expression sophie.get_image("smiling") with dissolve
        hide expression sophie.get_image("talking") with dissolve
        # End of flashback

        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/pup/line4.mp3"
        jus "well, totoo naman malamig dito"

        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/pup/line5.mp3"
        jus "at pwede ka din humiram ng libro para pang palipas oras din"
        hide expression justine.get_image("happy") with dissolve
        hide expression justine.get_image("talking") with dissolve
        jump floor2_3
    else:
        scene library2 at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/pup/line6.mp3"
        jus "Tambayan at Studyhan namin dito"
        show expression justine.get_image("talking") at justine_bottom_left
        hide expression justine.get_image("talking") with dissolve
        hide expression justine.get_image("happy") with dissolve
        jump floor2_3
    return
    # Note: 'jump floor2_3' was moved before 'return' in the original to avoid unreachable code; kept as 'return' here per your input

label floor_1:
    scene sf7 at custom_size_transform with fade
    scene sf8 at custom_size_transform with fade
    scene sf9 at custom_size_transform with fade
    scene sf10 at custom_size_transform with fade
    scene sf11 at custom_size_transform with fade
    scene sf12 at custom_size_transform with fade
    scene sf13 at custom_size_transform with fade
    call screen discussion
    return

label discussion_room:
    scene discussion at custom_size_transform with fade

    show expression justine.get_image("normal") at justine_bottom_left
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/discussion/line1.mp3"
    jus "Pagkakatanda ko, pwede gamitin tong room na to. Basta magpapaalam lang sa librarian sa library"
    hide expression justine.get_image("normal") with dissolve
    hide expression justine.get_image("talking") with dissolve
    jump floor_2

label floor_2:
    scene sf13 at custom_size_transform with fade
    call screen discussion
    return

label floor__1:
    scene sf14 at custom_size_transform with fade
    scene sf15 at custom_size_transform with fade
    scene sf16 at custom_size_transform with fade
    scene sf17 at custom_size_transform with fade
    call screen second_last_floor
    return

label floor__2:
    scene sf17 at custom_size_transform with fade
    call screen second_last_floor
    return

label second_floor:
    scene bg_second_floor at custom_size_transform
    call screen second_floor_menu

label halfwayground:
    scene left_halfway_ground1 at custom_size_transform with fade
    call screen left_halfway_menu

label nstp:
    scene nstp at custom_size_transform with fade
    call screen nstp_room
    return

default visited_faculty_lounge = False
label faculty_lounge:
    if not visited_faculty_lounge:
        $ visited_faculty_lounge = True
        scene faculty_inside at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left with dissolve
        show expression justine.get_image("normal") at justine_bottom_left
        voice "audio/faculty/line1.mp3"
        jus "Ang tagal ko ring hindi nakatapak dito sa faculty… pero parang walang nag bago."
        hide expression justine.get_image("talking")
        hide expression justine.get_image("normal")
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/faculty/line2.mp3"
        jus "Dito ako laging nakatambay. Dito ako palagi nakikiusap sa professor namin nung Discrete Structures para makapa consult sa project. \nMinsan, nakikipag kwentuhan o nakiki chismis lang pagkatapos ng klase."
        show expression justine.get_image("laughing") at justine_bottom_left
        hide expression justine.get_image("happy") 
        hide expression justine.get_image("laughing")

        # Start of flashback
        "(Flashback Sequence)"
        show expression faculty.get_image("normal") at kim_bottom_right
        show expression faculty.get_image("talking") at kim_bottom_right
        voice "audio/faculty/line3.mp3"
        "Yan naman, nakalimutan mo pa kasi ipasa yung assignment mo. Swerte ka na pagbibigyan kita dito ah, wag mo naman kalimutan sa \nsusunod ha?"
        hide expression faculty.get_image("normal") 
        hide expression faculty.get_image("talking") 
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/faculty/line4.mp3"
        jus "Opo ma'am, pasensya na."
        hide expression justine.get_image("talking") at justine_bottom_left
        # End of Flashback
        jump left_ground_2
    else:
        show expression justine.get_image("scared") at justine_bottom_left
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/faculty/line5.mp3"
        jus "Ramdam ko pa din 'yung kaba tuwing kumakatok ako sa pinto."
        show expression justine.get_image("scared")
        hide expression justine.get_image("talking") 
        jump left_ground_2

default visited_girls_cr = False

label left_ground1:
    scene left_halfway_ground1 at custom_size_transform with fade
    scene left_halfway_ground2 at custom_size_transform with fade
    call screen left_ground_menu1

label left_ground_1:
    scene left_halfway_ground2 at custom_size_transform with fade
    call screen left_ground_menu1
    return

label left_ground2:
    scene left_halfway_ground3 at custom_size_transform with fade
    scene left_halfway_ground4 at custom_size_transform with fade
    scene left_halfway_ground5 at custom_size_transform with fade
    call screen left_ground_menu2
    return

label left_ground_2:
    scene left_halfway_ground5 at custom_size_transform with fade
    call screen left_ground_menu2
    return

label avr_room:
    scene avr1 at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/avr/line1.mp3"
    jus "Ah, yung AVR... Naalala ko si Sophie tuloy. Na high blood pa siya noon dahil pinalinis pa siya nung nakalat namin yung AVR..."

    # Start of flashback
    scene avr1 at custom_size_transform with fade
    show expression sophie.get_image("talking") at kim_bottom_right
    show expression justine.get_image("shocked") at justine_bottom_left
    voice "audio/avr/line2.mp3"
    s "Ano ba yan, itatapon nalang eto! Mas lalo na ikaw Justin ah! Lagot ka sa akin mamaya!"
    hide expression sophie.get_image("talking") with dissolve
    hide expression justine.get_image("shocked") with dissolve
    # End of flashback
    scene avr2 at custom_size_transform with fade
    show expression justine.get_image("shivering") at justine_bottom_left
    voice "audio/avr/line3.mp3"
    jus "Inabangan niya pa ako sa gate nung uwian...Nakakaiba talaga yung galit netong babae na 'to…"
    hide expression justine.get_image("shivering") with dissolve
    jump left_ground_3

label left_ground3:
    scene left_halfway_ground6 at custom_size_transform with fade
    scene left_halfway_ground7 at custom_size_transform with fade
    call screen left_ground_menu3
    return

label left_ground_3:
    scene left_halfway_ground7 at custom_size_transform with fade
    call screen left_ground_menu3
    return

label third1:
    scene stair1 at custom_size_transform with fade
    scene stair2 at custom_size_transform with fade
    scene stair3 at custom_size_transform with fade
    scene stair4 at custom_size_transform with fade
    scene stair5 at custom_size_transform with fade
    call screen third_floor1
    return

label third1_1:
    scene stair5 at custom_size_transform with fade
    call screen third_floor1
    return

label thirdfloor_hall:
    scene hallway1 at custom_size_transform with fade

default visited_room_302 = False
label room_302:
    if not visited_room_302:
        $ visited_room_302 = True # Marked as visited
        scene room1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/room_302/line2.mp3"
        jus "Room 302…naalala ko tuloy yung nangyari dati hahaha"
        show expression justine.get_image("laughing") at justine_bottom_left
        hide expression justine.get_image("talking") with dissolve
        hide expression justine.get_image("laughing") with dissolve

        # Start of the Flashback
        scene room1 at custom_size_transform with fade
        show expression kim.get_image("calling") at kim_bottom_right with dissolve
        voice "audio/room_302/line3.mp3"
        k "Nasaan kayo guys? (nag-call sa gc)"
        hide expression kim.get_image("calling") with dissolve
        show expression justine.get_image("holding_phone") at justine_bottom_left
        voice "audio/room_302/line4.mp3"
        jus "Nasa room 303 po"
        hide expression justine.get_image("holding_phone") with dissolve
        "(After a few minutes, Kim entered the room a bit irritated)"

        show expression carl.get_image("talking") at justine_bottom_left
    
        c "Ay… room 303 kase nakalagay sa table eh"
        hide expression carl.get_image("talking") with dissolve

        show expression kim.get_image("talking") at kim_bottom_right
        voice "audio/room_302/line6.mp3"
        k "Pagsilip ko sa room 303 te ibang estudyante nakita ko tas nakatitigan ko pa. Nakakahiya.."
        show expression kim.get_image("normal") at kim_bottom_right
        hide expression kim.get_image("talking") with dissolve
        hide expression kim.get_image("normal") with dissolve
        jump turn_right_4
    else:
        scene room2 at custom_size_transform with fade
        show expression justine.get_image("laughing") at justine_bottom_left
        voice "audio/room_302/line1.mp3"
        jus "Yung table talaga may kasalanan"
        hide expression justine.get_image("laughing") with dissolve
        jump turn_right_4

label room_305:
    scene room307_2 at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/room_305/line1.mp3"
    jus "Room 305… ilang klase rin natin dito ginanap."
    hide expression justine.get_image("talking") with dissolve
    show expression mae.get_image("talking") at right
    voice "audio/room_305/line2.mp3"
    ma "Oo, dito ako unang na tawag sa graded recitation"
    hide expression mae.get_image("talking") with dissolve
    show expression mae.get_image("smiling") at right
    voice "audio/room_305/line3.mp3"
    ma "wala pa akong review noon. Haha."
    hide expression mae.get_image("smiling") with dissolve
    show expression justine.get_image("alarmed") at justine_bottom_left
    voice "audio/room_305/line4.mp3"
    jus "Oh Mae andito ka pala"
    hide expression justine.get_image("alarmed") with dissolve
    show expression mae.get_image("smiling") at right
    voice "audio/room_305/line5.mp3"
    ma "Oo HAHAHA"
    hide expression mae.get_image("smiling") with dissolve
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/room_305/line6.mp3"
    jus "Naalala ko rin 'yung lecture na walang kuryente. Ang init, pero tuloy pa rin, 'yun ang tunay na dedication"
    show expression justine.get_image("happy") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    hide expression justine.get_image("talking ") with dissolve
    hide expression justine.get_image("happy") with dissolve
    hide expression justine.get_image("laughing") with dissolve

    scene hallway3 at custom_size_transform with fade
    menu:
        "Peek through the Window":
            jump peek_window
        "Walk away":
            jump walk_away1
    jump turn_right_2

label peek_window:
    scene peak_window at custom_size_transform with fade
    "Justine looks through the glass window in the door"
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/room_305/line7.mp3"
    jus "Parang hindi na siya kasing gulo gaya nung dati"
    hide expression justine.get_image("talking") with dissolve
    show expression mae.get_image("talking") at right 
    voice "audio/room_305/line8.mp3"
    ma "Oo. Pero kahit pa-paano, may sentimental value pa rin."
    hide expression mae.get_image("talking") with dissolve
    jump turn_right_2

label walk_away1:
    scene hallway3 at custom_size_transform with fade
    "Justine smiles faintly and continues walking down the hallway."
    show expression justine.get_image("waving") at justine_bottom_left
    voice "audio/room_305/line9.mp3"
    jus "Salamat, Room 305. Kahit minsan stressful, naging parte ka ng journey."
    show expression justine.get_image("talking") at justine_bottom_left
    hide expression justine.get_image("waving") 
    hide expression justine.get_image("talking") with dissolve

    show expression mae.get_image("talking") at right
    voice "audio/room_305/line10.mp3"
    ma "Sige na nga"
    hide expression mae.get_image("talking")  
    show expression mae.get_image("smiling") at right 
    voice "audio/room_305/line11.mp3"
    ma "Baka maiyak pa tayo niyan"
    hide expression mae.get_image("smiling") with dissolve
    jump turn_right_2

label room_307:
    "(Justine entered the Room 307)"
    scene room307_1 at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/room_307/line1.mp3"
    jus " ayy naalala ko tong room na 'to. Ito yung isa sa mga room na 'di ko makalimutan."
    show expression justine.get_image("happy") at justine_bottom_left
    hide expression justine.get_image("happy") 
    hide expression justine.get_image("talking") with dissolve

    scene room307_3 at custom_size_transform with fade
    show expression justine.get_image("laughing") at justine_bottom_left
    voice "audio/room_307/line2.mp3"
    jus "dito kami nagpatay ng oras para sa PE namin hahaha. Tapos wala palang klase. Prinactice pa naman namin mga excercises namin."
    show expression justine.get_image("Sighing") at justine_bottom_left
    show expression justine.get_image("disappointed") at justine_bottom_left
    hide expression justine.get_image("Sighing") with dissolve
    hide expression justine.get_image("laughing") with dissolve
    hide expression justine.get_image("disappointed") with dissolve
    jump turn_right_1

label turn_right_2:
    scene hallway3 at custom_size_transform with fade
    call screen third_floor3
    return

label boys_cr:
    scene m1 at custom_size_transform with fade
    pause
    "(Justine entered the Boys' CR)"
    scene m2 at custom_size_transform with fade
    pause
    scene m3 at custom_size_transform with fade
    pause
    scene m4 at custom_size_transform with fade
    pause
    scene m5 at custom_size_transform with fade

    show expression justine.get_image("scared") at justine_bottom_left
    voice "audio/boys/line1.mp3"
    show expression justine.get_image("smiling") at justine_bottom_left
    jus "Yung salamin, andito pa rin. At mga urinal wala paring pagbabago. Classic."
    show expression justine.get_image("talking") at justine_bottom_left
    show expression justine.get_image("laughing") at justine_bottom_left
    voice "audio/boys/line2.mp3"
    jus "Dito ako minsang nagtago noon. Para makapag isip isip."
    hide expression justine.get_image("scared") with dissolve
    hide expression justine.get_image("smiling") with dissolve
    hide expression justine.get_image("talking") with dissolve
    hide expression justine.get_image("laughing") with dissolve

    call screen boy_bathroom

return
label turn_right:
    scene hallway1 at custom_size_transform with fade
    scene hallway2 at custom_size_transform with fade

label turn_right_1:
    scene hallway2 at custom_size_transform with fade
    call screen third_floor2
    return

label girls_cr:
    if not visited_girls_cr:
        $ visited_girls_cr = True
        scene girls1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/girls/line1.mp3"
        jus "hmm? Eto yung CR for girls, ano kaya itsura neto sa loob?"
        hide expression justine.get_image("talking") with dissolve
        show expression justine.get_image("laughing") at justine_bottom_left
        voice "audio/girls/line2.mp3"
        jus "naalala ko tuloy yung sinabi ni Lyn"
        hide expression justine.get_image("laughing") with dissolve
        # Start of the Flashback
        scene girls2 at custom_size_transform with fade
        show expression lyn.get_image("talking") at right
        voice "audio/girls/line3.mp3"
        l "ano itsura ng sa boys justine? Kasi samin may salamin na may tubig pa yung sa inyo?"
        show expression lyn.get_image("smug") at right
        hide expression lyn.get_image("talking") with dissolve
        hide expression lyn.get_image("smug") with dissolve
        # End of Flashback
    else:
        # IRL
        scene girls1 at custom_size_transform with fade
        show expression justine.get_image("realised") at justine_bottom_left
        voice "audio/girls/line4.mp3"
        jus "na-curious tuloy ako ano itsura ng loob"
        hide expression justine.get_image("realised") with dissolve
        "Ella suddenly appear"
        show expression ella.get_image("talking") at right
        voice "audio/girls/line5.mp3"
        e "huyy, ano ginagawa mo dyan?"
        show expression ella.get_image("smiling") at right
        voice "audio/girls/line6.mp3"
        e "Bat ka nakatitig sa cr?"
        hide expression ella.get_image("talking") with dissolve
        hide expression ella.get_image("smiling") with dissolve
        show expression justine.get_image("alarmed") at justine_bottom_left
        voice "audio/girls/line7.mp3"
        jus "Hu-huh? Kung ano man ang iniisip mo mali yun"
   
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/girls/line8.mp3"
        jus "na alala ko lang yung sinabi ni Lyn tungkol sa CR ng girls"
        hide expression justine.get_image("alarmed") with dissolve
        hide expression justine.get_image("Sighing") with dissolve
        hide expression justine.get_image("talking") with dissolve
        show expression ella.get_image("grinning") at right
        voice "audio/girls/line9.mp3"
        e "ayy!Speaking of cr ng girls"
        hide expression ella.get_image("grinning") with dissolve
    
        show expression ella.get_image("whispering") at right
        voice "audio/girls/line10.mp3"
        e "alam mo ba…kasi one time, mag isa lang akong pumunta  tas may nafeel ako na kakaiba kaya sumilip ako"
        hide expression ella.get_image("whispering") with dissolve
    
        show expression ella.get_image("grinning") at right
        voice "audio/girls/line11.mp3"
        e "sa door ng cr tapos wala naman tas pag tingin ko ulit…"
        hide expression ella.get_image("grinning") with dissolve
        show expression justine.get_image("scared") at justine_bottom_left
        voice "audio/girls/line12.mp3"
        jus "ta-tapos…?"
        hide expression justine.get_image("scared") with dissolve
        show expression ella.get_image("whispering") at right
        voice "audio/girls/line13.mp3"
        e "…si Lyn lang pala kala mo nakakatakot noh kala ko rin e hahahah"
        show expression ella.get_image("grinning") at right
        show expression ella.get_image("smiling") at right
        hide expression ella.get_image("smiling") with dissolve
        hide expression ella.get_image("grinning") at right
        hide expression ella.get_image("whispering") at right
        show expression justine.get_image("Sighing") at justine_bottom_left
        voice "audio/girls/line14.mp3"
        jus "hayss ano ba yan akala ko kung ano na hahaha…"
        hide expression justine.get_image("Sighing") 
        show expression justine.get_image("laughing") at justine_bottom_left
        hide expression justine.get_image("laughing") 

        show expression ella.get_image("talking") at right with dissolve
        voice "audio/girls/line15.mp3"
        e "well anyway alis na ako may pupuntahan pa ako"
        hide expression ella.get_image("talking") with dissolve
        show expression justine.get_image("waving") at justine_bottom_left
        voice "audio/girls/line16.mp3"
        jus "ok bye"
        hide expression justine.get_image("waving") with dissolve
    jump third1_1

label turn_right1:
    scene hallway4 at custom_size_transform with fade
    scene hallway5 at custom_size_transform with fade
    call screen third_floor6
    return

label turn_right_3:
    scene hallway5 at custom_size_transform with fade
    call screen third_floor6
    return

label turn_right_4:
    scene hallway6 at custom_size_transform with fade
    call screen third_floor4
    return

label turn_right5:
    scene hallway7 at custom_size_transform with fade
    scene hallway8 at custom_size_transform with fade
    scene hallway9 at custom_size_transform with fade
    call screen third_floor5
    return

label turn_right_5:
    scene hallway9 at custom_size_transform with fade
    call screen third_floor5

label science_lab:
    scene science_lab at custom_size_transform with fade
    show expression justine.get_image("alarmed") at justine_bottom_left
    jus "" 
    call screen science_lab1
    return


label turn_left:
    scene rightside_staircase at custom_size_transform with fade
    call screen turn_left_1
    return

label fourth_floor:
    scene 1 at custom_size_transform with fade
    scene 2 at custom_size_transform with fade
    scene 3 at custom_size_transform with fade
    call screen fourth_floor1
    return

label fourth_floor_1:
    scene 3 at custom_size_transform with fade
    call screen fourth_floor1
    return

label m_bathroom:
    scene m1 at custom_size_transform with fade
    scene m2 at custom_size_transform with fade
    scene m3 at custom_size_transform with fade
    scene m4 at custom_size_transform with fade
    scene m5 at custom_size_transform with fade
    call screen ma_bathroom
    return

label fourth_floors1:
    scene f1 at custom_size_transform with fade
    call screen fourth
    return

default visited_comlab = False
default visited_project_proposal = False
default visited_lab_management = False
default visited_food_beverage = False
default visited_org = False
default visited_housekeeping_room = False
default visited_csc = False

label comlab:
    if not visited_comlab:
        $ visited_comlab = True
        scene comlab at custom_size_transform with fade
        show expression justine.get_image("alarmed") at justine_bottom_left
        voice "audio/comlab/line1.mp3"
        jus "Ay! naalala ko bigla nung first time pa lang namin pumasok dito nung freshman pa lang kami nakita ko si carl binuksan yung pc \nat nagdrawing ng pasimple."
        show expression justine.get_image("laughing") at justine_bottom_left
        hide expression justine.get_image("alarmed") 
        hide expression justine.get_image("laughing")

        # Flashback
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/comlab/line2.mp3"
        jus "Uy carl ano ginagawa mo?"
        hide expression justine.get_image("talking")

        show expression carl.get_image("talking") at right
        c "shhh wag kang maingay, mamaya makita tayo ni sir"
        hide expression carl.get_image("talking") with dissolve
    else:
        show expression justine.get_image("laughing") at justine_bottom_left
        voice "audio/comlab/line4.mp3"
        jus "grabe ang tapang talaga nya hahaha…"
        hide expression justine.get_image("laughing") with dissolve

    jump fourth_floors1

label computer_hardware:
    scene comhardware at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/comp_hardware/line1.mp3"
    jus "Dito kami pumupunta kapag may hands on activity ang maintenance at repair ng mga equipment dito lalo na pag computer."
    hide expression justine.get_image("talking") with dissolve

    show expression justine.get_image("happy") at justine_bottom_left
    voice "audio/comp_hardware/line2.mp3"
    jus "Naalala ko tuloy dati si Ella. Halos sya lang ang naka ayos ng mga computer na pinapaayos sa amin noon"
    hide expression justine.get_image("happy") with dissolve

    jump fourth_floors1

label project_proposal:
    if not visited_project_proposal:
        $ visited_project_proposal = True
        scene proj at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/project_proposal/line1.mp3"
        jus "Dito kami pumunta nung nag project defense kami"
        hide expression justine.get_image("talking") with dissolve

        show expression justine.get_image("scared") at justine_bottom_left
        voice "audio/project_proposal/line2.mp3"
        jus "Naalala ko grabe yung kaba ko nung proposal defense pero mas malala parin yung kaba ni Mae non hanggang ngayon \nhindi ko parin nalilimutan."
        hide expression justine.get_image("scared") with dissolve

        # Flashback
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/project_proposal/line3.mp3"
        jus "Mae try mo kumalma, nanginginig kana"
        hide expression justine.get_image("talking") with dissolve

        show expression mae.get_image("talking") at kim_bottom_right
        voice "audio/project_proposal/line4.mp3"
        ma "Tinatry ko ok?"
        voice "audio/project_proposal/line5.mp3"
        ma "Pero what if ma-reject yung proposal?"
        voice "audio/project_proposal/line6.mp3"
        ma "What if ma blanko ako? What if-"
        hide expression mae.get_image("talking") with dissolve
    else:
        show expression justine.get_image("laughing") at justine_bottom_left
        voice "audio/project_proposal/line7.mp3"
        jus "Grabe ang pag overthink nya halos nanginginig buong katawan nya noon HAHAHAHA"
        hide expression justine.get_image("laughing") with dissolve

    jump fourth_floors2

label lab_management:
        scene lab_management at custom_size_transform with fade
        show expression justine.get_image("realised") at justine_bottom_left
        voice "audio/lab_management/line1.mp3"
        jus "Hmm, ano kayang itsura neto sa loob? Hanggang ngayon kase di ko parin nakikita dahil lagi 'tong walang tao at nakalock."
        hide expression justine.get_image("realised")

        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/lab_management/line2.mp3"
        jus "'Di ko rin nasasaktuhan na bukas 'to, dahil bihira lang ako nakaka-akyat sa floor na 'to, haysss.'"
        hide expression justine.get_image("talking") with dissolve

        jump fourth_floors2
label food_beverage:
    scene food_and_bev_room2 at custom_size_transform with fade
    if not visited_food_beverage:
        $ visited_food_beverage = True
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/food_beverage/line1.mp3"
        jus "Pag napapadaan ako rito feel ko laging may birthday dahil sa ganda ng pagkakaayos"
        voice "audio/food_beverage/line2.mp3"
        jus "naalala ko yung sinabi ni Jorie tungkol sa room na to"
        hide expression justine.get_image("talking") with dissolve
        # Flashback
        show expression jorie.get_image("talking") at right
        voice "audio/food_beverage/line3.mp3"
        j "Kaya pala ganyan ang ayos nyan kase dyan nag t-training ang mga HM Students"
        hide expression jorie.get_image("talking") with dissolve

        show expression jorie.get_image("smiling") at right
        voice "audio/food_beverage/line4.mp3"
        j "kung ano nga ba ang dapat nilang gawin pag sila ay natatrabaho na."
        hide expression jorie.get_image("smiling") with dissolve
    else:
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/food_beverage/line5.mp3"
        jus "feel ko ang intense ng training nila dyan"
        hide expression justine.get_image("talking") with dissolve

    jump fourth_floors3

default visited_kitchen_lab = False
label kitchen_lab:
    if not visited_kitchen_lab:
        $ visited_kitchen_lab = True
        scene kitchen_lab2 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/kitchen/line1.mp3"
        jus "Kung may storage room sila, syempre may kitchen din."
        hide expression justine.get_image("talking")

        show expression lyn.get_image("talking") at right
        voice "audio/kitchen/line2.mp3"
        l "Dito naman nagluluto ang mga HM Students kaya pag napapadaan ako rito nagugutom agad ako dahil sa bango ng mga niluluo nila"
        hide expression lyn.get_image("talking") with dissolve

        show expression justine.get_image("alarmed") at justine_bottom_left
        voice "audio/kitchen/line3.mp3"
        jus "TALAGA NAMAN LYN? BIBIGYAN MO BA AKO NG SAKIT SA PUSO?"
        hide expression justine.get_image("alarmed") with dissolve

        show expression lyn.get_image("talking") at right
        voice "audio/kitchen/line4.mp3"
        l "HAHAHA… SORRRY NA ANYWAY BABALIK NA SANA AKO KASO NA KITA KITA MYBAD MYBAD"
        voice "audio/kitchen/line5.mp3"
        l "Minsan gusto ko nalang tumayo dyan nang matagal dahil di nakakasawang amuyin ang mga niluluo nila"
        hide expression lyn.get_image("talking") with dissolve

        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/kitchen/line6.mp3"
        jus "sa totoo lang"
        hide expression justine.get_image("talking") with dissolve

        show expression lyn.get_image("talking") at right
        voice "audio/kitchen/line7.mp3"
        l "anyway bibigay ko papala tong drive kay kim, Bye~"
        hide expression lyn.get_image("talking") with dissolve
    else:
        scene kitchen_lab2 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/kitchen/line8.mp3"
        jus "Lagi akong nagugutom sa tuwing napapadaan ako dito lalo na pag naglututo ang mga HM"
        hide expression justine.get_image("talking")


    jump fourth_floors3

label HM_storage:
    scene hm_storage_room1 at custom_size_transform with fade
    show expression justine.get_image("happy") at justine_bottom_left
    voice "audio/HM/line1.mp3"
    jus "Ang ganda talaga rito. Andito yung mga plato,baso, at uniform na ginagamit ng mga HM Students"
    voice "audio/HM/line2.mp3"
    jus "Pag nakikita ko nga silang may dalang lutong pagkain ay naiinggit ako kase akala ko dati puro lang sila linis yung parang \nmga House keeping yun pala may halong pagkain din"
    hide expression justine.get_image("happy") with dissolve

    jump fourth_floors4

label student_org:
    if not visited_org:
        $ visited_org = True
        scene student_org1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/student_org/line1.mp3"
        jus "Hmm, org room eto yung room na ginagamit nila pag kaylangan ng mga org. Andito din mga gamit ng iba't ibang org"
        hide expression justine.get_image("talking") at justine_bottom_left
        
        show expression justine.get_image("laughing") at justine_bottom_left
        voice "audio/student_org/line2.mp3"
        jus "Naalala ko sabi ni Ela nung first year kami"
        hide expression justine.get_image("laughing") with dissolve
    else:
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/student_org/line3.mp3"
        jus "grabe, ang strict talaga ng school na ito"
        hide expression justine.get_image("talking") with dissolve

    jump fourth_floors4

label housekeeping_room:
    if not visited_housekeeping_room:
        $ visited_housekeeping_room = True
        scene housekeeping_room at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/housekeeping/line1.mp3"
        jus "Housekeeping Room."
        voice "audio/housekeeping/line2.mp3"
        jus "Parang ilang beses ko nang nadadaanan 'to pero never ko pa rin siya napapasok"
        voice "audio/housekeeping/line3.mp3"
        jus "Naalala ko yung sabi ni Mae dati…"
        hide expression justine.get_image("talking") with dissolve

        # Flashback
        show expression justine.get_image("smiling") at justine_bottom_left
        voice "audio/housekeeping/line4.mp3"
        jus "Para saan kaya 'to?"
        hide expression justine.get_image("smiling") with dissolve

        show expression mae.get_image("talking") at right
        voice "audio/housekeeping/line5.mp3"
        m "Ah, 'yan?"
        voice "audio/housekeeping/line6.mp3"
        m "Diyan raw nagpa-practice yung HM students ng mga housekeeping tasks"
        voice "audio/housekeeping/line7.mp3"
        m "like bed making, towel folding, at room cleaning."
        voice "audio/housekeeping/line8.mp3"
        m "Parang mini-hotel room training area."
        voice "audio/housekeeping/line9.mp3"
        m "May mga gamit d'yan like mop, linen, tsaka mga hotel-grade supplies."
        voice "audio/housekeeping/line10.mp3"
        m "Parang combo siya ng storage at simulation room."
        voice "audio/housekeeping/line11.mp3"        
        m "Hindi halata, pero malaking tulong 'to sa training nila"
        voice "audio/housekeeping/line12.mp3"
        m "Diyan nila natututunan 'yung mga standard na pang-hotel service."
        voice "audio/housekeeping/line13.mp3"
        m "Kaya malinis din sa paligid—sanay sila"
        hide expression mae.get_image("talking") with dissolve

        scene f6 at custom_size_transform with fade
        menu:
            "Try to Open the Door":
                jump door_open
            "Continue walking":
                jump continue_walking
    else:
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/housekeeping/line14.mp3"
        jus "Oo nga, makes sense yung sinabi ni Mae..."
        hide expression justine.get_image("talking") with dissolve
    jump fourth_floors5



label continue_walking:
    scene housekeeping_room at custom_size_transform with fade
    "(Justine glanced at the door one last time, then walked on.)"
    show expression justine.get_image("happy") at justine_bottom_left
    voice "audio/housekeeping/line15.mp3"
    jus "Wala rin naman akong kailangan dito. Pero nice na malaman na hindi lang siya simpleng storage room—training room pala \ntalaga"
    hide expression justine.get_image("happy") with dissolve

    jump fourth_floors5

label door_open:
    scene housekeeping_room at custom_size_transform with fade
    show expression justine.get_image("smiling") at justine_bottom_left
    voice "audio/housekeeping/line16.mp3"
    jus "Locked. Yeah... expected"
    voice "audio/housekeeping/line17.mp3"
    jus "Siguro bawal talaga pumasok kung wala kang activity dito. Sensitive din kasi gamit—di biro ang linen at cleaning tools ng HM."
    hide expression justine.get_image("smiling") with dissolve
    jump fourth_floors5

label fourth_floors2:
    scene f2 at custom_size_transform with fade
    call screen fourth1
    return

label fourth_floors3:
    scene f3 at custom_size_transform with fade
    call screen fourth2
    return


label fourth_floors4_1:
    scene f5 at custom_size_transform with fade
    call screen fourth3
    return

label fourth_floors5:
    scene f6 at custom_size_transform with fade
    call screen fourth4
    return

label fourth_floors6:
    scene f7 at custom_size_transform with fade
    call screen fourth5
    return

label csc:
    if not visited_csc:
        $ visited_csc = True
        scene csc_room2 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/csc/line1.mp3"
        jus "CSC Room."
        voice "audio/csc/line2.mp3"
        jus "Laging naka-lock 'to tuwing dumadaan ako. Pero parang may aura siya na… 'di ka basta-basta puwedeng pumasok"
        hide expression justine.get_image("talking") with dissolve
        # Flashback
        scene csc_room1 at custom_size_transform with dissolve
        voice "audio/csc/line3.mp3"
        show expression justine.get_image("Sighing") at justine_bottom_left
        jus "Sophie, anong meron dito? Para kasing... 'secret base."
        hide expression justine.get_image("Sighing") with dissolve

        show expression sophie.get_image("talking") at right
        voice "audio/csc/line4.mp3"
        s "Haha! In a way, oo."
        voice "audio/csc/line5.mp3"
        s "'Yan yung office ng Central Student Council."
        voice "audio/csc/line6.mp3"
        s "Diyan ginagawa lahat ng mga plans, meetings, at minsan drama rin—lalo na pag elections."
        voice "audio/csc/line7.mp3"
        s "May mga whiteboard, mga files, event permits,"
        voice "audio/csc/line8.mp3"
        s "tapos minsan may snacks pa kasi hindi sila natatapos agad."
        voice "audio/csc/line9.mp3"
        s "Diyan naka-base yung mga officers para ayusin ang mga events, policies, at minsan..."
        voice "audio/csc/line10.mp3"
        s "mga chismis ng orgs"
        hide expression sophie.get_image("talking") with dissolve

        voice "audio/csc/line11.mp3"
        show expression justine.get_image("talking") at justine_bottom_left
        jus "Kaya pala parang ang tahimik pero busy sa loob"
        hide expression justine.get_image("talking") with dissolve

        
        show expression sophie.get_image("smiling") at right
        voice "audio/csc/line12.mp3"
        s "Exactly. Kung may problemang student-related"
        voice "audio/csc/line13.mp3"
        s "malamang dito napag-uusapan 'yon bago makarating sa admin."
        hide expression sophie.get_image("smiling") with dissolve
        # End Flashback
        scene csc_room2 at custom_size_transform with fade
    else:
        scene csc_room1 at custom_size_transform with fade
        voice "audio/csc/line14.mp3"
        show expression justine.get_image("talking") at justine_bottom_left
        jus "So, dito ginagawa ang lahat ng desisyon ng CSC"
        hide expression justine.get_image("talking") with dissolve
    jump fourth_floors5



default visited_deluxe_room = False
default visited_travel_tours = False
default visited_standard_room = False

label deluxe_room:
    if not visited_deluxe_room:
        $ visited_deluxe_room = True
        scene deluxe at custom_size_transform with fade
        show expression justine.get_image("realised") at justine_bottom_left
        voice "audio/deluxe/line1.mp3"
        jus "De Luxe Room…"
        voice "audio/deluxe/line2.mp3"
        jus "Grabe, kahit yung pangalan palang, parang bawal mag-ingay, no?"
        hide expression justine.get_image("realised") with dissolve
        # Flashback
        scene deluxe at custom_size_transform with dissolve
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/deluxe/line3.mp3"
        jus "Uy, parang hotel room yung vibe. Ano 'to?"
        hide expression justine.get_image("happy") with dissolve
        show expression kim.get_image("talking") at right
        voice "audio/deluxe/line4.mp3"
        k "Ay, 'yan yung De Luxe Room!"
        voice "audio/deluxe/line5.mp3"
        k "Pang-simulation 'yan ng hotel setup para sa HM students."
        voice "audio/deluxe/line6.mp3"
        k "Diyan sila natututo kung paano mag-set up ng real hotel room"
        voice "audio/deluxe/line7.mp3"
        k "from bed sheets to lighting, pati na rin 'yung guest interaction."
        voice "audio/deluxe/line8.mp3"
        k "Kompleto 'yann—may bed CR, vanity area, towels, pillows, like sa real hotels"
        voice "audio/deluxe/line9.mp3"
        hide expression kim.get_image("talking") with dissolve
        show expression justine.get_image("realised") at justine_bottom_left
        jus "Whoa. Kala ko parang show room lang. Training area pala talaga."
        hide expression justine.get_image("realised") with dissolve
        show expression kim.get_image("happy") at right
        voice "audio/deluxe/line10.mp3"
        k "Yup! Parang practice stage nila para maging legit hotel staff someday"
        voice "audio/deluxe/line11.mp3"
        k "Kaya sobrang linis at bawal basta-basta pumasok"
        hide expression kim.get_image("happy") with dissolve
        # End Flashback
        scene deluxe at custom_size_transform with fade
    else:
        scene deluxe at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/deluxe/line12.mp3"
        jus "High-end training space pala talaga. May pagka-exclusive… pero inspiring rin."
        hide expression justine.get_image("happy") with dissolve
    jump fourth_floors6

label floor1_2:
    scene sf17 at custom_size_transform with fade
    show expression justine.get_image("normal") at justine_bottom_left
    voice "audio/roof/line1.mp3"
    jus "This leads to the other side of the roofdeck entrance"
    voice "audio/roof/line2.mp3"
    jus "its closed"
    hide expression justine.get_image("normal") with dissolve
    call screen second_last_floor
    jump fourth_floors6  # Kept jump before return as per your input
    return

label travel_tours:
    if not visited_travel_tours:
        $ visited_travel_tours = True
        scene travel_and_tours_room1 at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/travel_tours/line1.mp3"
        jus "Travel and Tour Room"
        hide expression justine.get_image("happy") with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/travel_tours/line2.mp3"
        jus "Every time I pass by this room parang naiisip ko agad yung mga airport, plane, at beach. Vibe pa lang, parang may adventure"
        hide expression justine.get_image("talking") with dissolve
        # Flashback
        scene travel_and_tours_room2 at custom_size_transform with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/travel_tours/line3.mp3"
        jus "Anong meron dito, Jorie? Bakit may mga mini flags saka posters ng mga bansa?"        
        hide expression justine.get_image("talking") with dissolve
        show expression jorie.get_image("talking") at right
        voice "audio/travel_tours/line4.mp3"
        j "Ah, 'yan yung Travel and Tour Room nila."
        voice "audio/travel_tours/line5.mp3"
        j "Dito sila nagpa-practice yung Tourism students kung paano maging travel agents"
        voice "audio/travel_tours/line6.mp3"
        j "May mga props pa nga like luggage, destination brochures, at uniforms."
        voice "audio/travel_tours/line7.mp3"
        j "Super hands-on nila dito!"
        hide expression jorie.get_image("talking") with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/travel_tours/line8.mp3"
        jus "Ayos ah. Parang biyahe without leaving the room."
        hide expression justine.get_image("talking") with dissolve
        # End Flashback
        scene travel_and_tours_room1 at custom_size_transform with fade
    else:
        scene travel_and_tours_room1 at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/travel_tours/line9.mp3"
        jus "Kaya pala sobrang themed sa loob. May mapa pa ng buong mundo sa pader"
        hide expression justine.get_image("talking") with dissolve
    jump fourth_floors4


label frontofficetravel_tours:
    scene office at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/front_office/line1.mp3"
    jus "Hmm, ano kaya ito?.  Ahh baka dito ginaganap yung training nila, kunwari pag napunta sila sa front desk na nag-aayos ng \nmga hotel's check-in."
    voice "audio/front_office/line2.mp3"
    jus "O kaya naman dito ina-asikaso yung mga flight ng ibang studyante kapag ilalaban sila sa ibang bansa. Nung 1st year kase  \nako may inilaban ang school namin sa ibang bansa, dito siguro inaasikaso ang mga iyon."
    hide expression justine.get_image("talking") at justine_bottom_left with dissolve
    jump fourth_floors6
label acads1:
    scene acad1 at custom_size_transform with fade
    call screen acads
    return

label standard_room:
    if not visited_standard_room:
        $ visited_standard_room = True
        scene standard_room at custom_size_transform with fade
        show expression justine.get_image("happy") at justine_bottom_left
        voice "audio/standard_room/line1.mp3"
        jus "Mas simple compared sa Deluxe pero may charm parin. Parang 'yung classic na kwarto sa probinsya na may aircon"
        hide expression justine.get_image("happy") with dissolve
        # Flashback
        scene standard_room at custom_size_transform with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/standard_room/line2.mp3"
        jus "Akala ko bodega lang 'to dati. Standard Room pala ang tawag?"
        hide expression justine.get_image("talking") with dissolve
        show expression mae.get_image("smiling") at right
        voice "audio/standard_room/line3.mp3"
        m "Haha! Hindi 'yan bodega, uy. Training room 'yan ng HM students."
        voice "audio/standard_room/line4.mp3"
        m "Mas basic siya kaysa sa De Luxe, pero dito muna sila nagpa-practice bago dun"
        voice "audio/standard_room/line5.mp3"
        m "Diyan nila unang natutunan 'yung bed making, towel folding, guest essentials setup."
        voice "audio/standard_room/line6.mp3"
        m "Halos lahat ng firsts nila bilang hotelier, dito nagsisimula"
        hide expression mae.get_image("smiling") with dissolve
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/standard_room/line7.mp3"
        jus "So parang 'foundations room'?"
        hide expression justine.get_image("talking") with dissolve
        show expression mae.get_image("talking") at right
        voice "audio/standard_room/line8.mp3"
        m "Exactly. 'Pag nagkamali ka dito, okay lang"
        voice "audio/standard_room/line9.mp3"
        m "Dito ka muna matututo bago ka iharap sa mas sosyal na kwarto."
        hide expression mae.get_image("talking") with dissolve
        # End Flashback
        scene standard_room at custom_size_transform with fade
    else:
        scene standard_room at custom_size_transform with fade
        show expression justine.get_image("talking") at justine_bottom_left
        voice "audio/standard_room/line10.mp3"
        jus "Makes sense. Dito pala pinapanday ang hospitality skills. Every detail counts"
        hide expression justine.get_image("talking") with dissolve
    jump fourth_floors6

label stair_roofdeck:
    scene rf1 at custom_size_transform with fade
    scene rf2 at custom_size_transform with fade
    scene rf3 at custom_size_transform with fade
    scene rf4 at custom_size_transform with fade
    scene rf5 at custom_size_transform with fade
    show expression justine.get_image("sighing") at justine_bottom_left
    voice "audio/roofdeck/line1.mp3"
    jus "Di pa ko nakakaalis pero namimiss ko na agad dito."
    hide expression justine.get_image("sighing") with dissolve
    show expression justine.get_image("sighing") at justine_bottom_left
    voice "audio/roofdeck/line2.mp3"
    jus "Dito kami laging nag p-p.e at seminar ng tipong di pa nagsisimula ang event o class pero pagod ka na agad sa taas ng a-akysatin mo."
    hide expression justine.get_image("sighing") with dissolve
    show expression justine.get_image("happy") at justine_bottom_left
    voice "audio/roofdeck/line3.mp3"
    jus "Pero worth it naman dahil ma-e-enjoy mo ang view na makikita mo sa galling sa itaas. akikita mo rito yung mga naglalakihang \neroplano at mga magagandang gusali."
    show expression justine.get_image("talking") at justine_bottom_left
    hide expression justine.get_image("happy") with dissolve
    hide expression justine.get_image("talking") with dissolve
    menu:
        "Go back":
            jump fourth_floors1
        "Don't go back":
            jump main_gate_last
        "Main Gate":
            jump maingate

label main_gate_last:
    scene rf6 at custom_size_transform with fade
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/roofdeck/line4.mp3"
    jus "Grabe... tapos ko na lahat."
    voice "audio/roofdeck/line5.mp3"
    jus "Parang ang dami palang lugar dito na dinaanan ko lang dati, pero ngayon… iba na."
    hide expression justine.get_image("talking")  
    show expression justine.get_image("crying") at justine_bottom_left 
    voice "audio/roofdeck/line6.mp3"
    jus "Lahat ng tawanan, pagod, kaba, iyak, at ingay… naiwan na dito sa mga pader, sa sahig, sa hangin"
    voice "audio/roofdeck/line7.mp3"
    jus "Hindi lang pala ito basta campus. Ito yung naging background ng halos lahat ng memories ko nitong mga nakaraang taon"
    hide expression justine.get_image("crying")  
    show expression justine.get_image("sighing") at justine_bottom_left
    voice "audio/roofdeck/line8.mp3"
    jus "ang hirap pala magpaalam… pero ang sarap din sa puso kapag alam mong hindi mo sayang 'yung bawat araw na nandito ka"
    hide expression justine.get_image("sighing")
    show expression justine.get_image("talking") at justine_bottom_left
    voice "audio/roofdeck/line9.mp3"
    jus "Salamat, PUP Parañaque. Sa alaala, sa mga taong nakilala ko, at sa kung sino ako ngayon."
    show expression justine.get_image("waving") at justine_bottom_left
    hide expression justine.get_image("waving") with dissolve
    hide expression justine.get_image("talking")  
    scene black with fade
    "THE END"
    return

