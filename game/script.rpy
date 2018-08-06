# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Cindy = Character("Cindy")
define Veronica = Character("Veronica")
define AIO = Character("AI-0")
define Mother = Character("Mom")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    "Being realistic, this is the last time I’ll be home."

    "Hell, it’s probably going to be a while before I even contact my parents again."

    "Sure everyone talks about going home for the holidays, and talks about how they should call their parents, but its always just talk."

    "Jobs keep you busy, exams keep you locked in the dorm rooms during your breaks, and well, life gets in the way."

    #scene house
    #TODO: Add screenshake
    Mother "MY BAAAAYYYBBBEEEE"

    #scene blank
    # These display lines of dialogue.

    "My mother has a severe case of empty nest syndrome right now, but I still love her"

    "Dad’s worked pretty heavily at the dental office for as long as I can remember, so I worry that my Mom’s going to be feeling a bit more lonely at home."

    "Maybe I should convince Dad to get her a dog."


    # This ends the game.

    return
