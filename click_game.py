WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((255, 200, 100))

character = Actor('character')
character.pos = 100, 55

WIDTH = 500
HEIGHT = character.height + 500

def draw():
    character.draw()

character.topright = 0, 10
def update():
    character.left += 2
    if character.left >WIDTH:
        character.right = 0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        print("Why!")

    else:
        print("Missed Me!")

def on_mouse_down(pos):
    if character.collidepoint(pos):
        set_character_clicked()

def set_character_clicked():
    character.image = 'character_clicked'
    clock.schedule_unique(set_character_normal, 1.0)

def set_character_normal():
    character.image = 'character'
