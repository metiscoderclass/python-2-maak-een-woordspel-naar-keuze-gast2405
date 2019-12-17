# Size of the window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Default friction used for sprites, unless otherwise specified
DEFAULT_FRICTION = 0.2

# Default mass used for sprites
DEFAULT_MASS = 1

# Gravity
GRAVITY = (0.0, -900.0)

# Player forces
PLAYER_MOVE_FORCE = 700
PLAYER_JUMP_IMPULSE = 600
PLAYER_PUNCH_IMPULSE = 600

# Grid-size
SPRITE_SIZE = 64

# How close we get to the edge before scrolling
VIEWPORT_MARGIN = 100

"""
import pymunk

from arcade.examples.pymunk_platformer.physics_utility import (
    PymunkSprite,
)
from constants import *


def create_floor(space, sprite_list):
    """  """
    for x in range(-1000, 2000, SPRITE_SIZE):
        y = SPRITE_SIZE / 2
        sprite = PymunkSprite("../images/grassMid.png", x, y, scale=0.5, body_type=pymunk.Body.STATIC)
        sprite_list.append(sprite)
        space.add(sprite.body, sprite.shape)


def create_platform(space, sprite_list, start_x, y, count):
    """  """
    for x in range(start_x, start_x + count * SPRITE_SIZE + 1, SPRITE_SIZE):
        sprite = PymunkSprite("../images/grassMid.png", x, y, scale=0.5, body_type=pymunk.Body.STATIC)
        sprite_list.append(sprite)
        space.add(sprite.body, sprite.shape)


def create_level_1(space, static_sprite_list, dynamic_sprite_list):
    """"""
    create_floor(space, static_sprite_list)
    create_platform(space, static_sprite_list, 200, SPRITE_SIZE * 3, 3)
    create_platform(space, static_sprite_list, 500, SPRITE_SIZE * 6, 3)
    create_platform(space, static_sprite_list, 200, SPRITE_SIZE * 9, 3)

    # Create the stacks of boxes
    for column in range(6):
        for row in range(column):
            x = 600 + column * SPRITE_SIZE
            y = (3 * SPRITE_SIZE / 2) + row * SPRITE_SIZE
            sprite = PymunkSprite("../images/boxCrate_double.png", x, y, scale=0.5, friction=0.4)
            dynamic_sprite_list.append(sprite)
            space.add(sprite.body, sprite.shape)
Some utility functions for physics.

physics_utility.py
import arcade
from arcade.examples.pymunk_platformer.constants import (
    DEFAULT_FRICTION,
    DEFAULT_MASS,
)

import pymunk
import math


class PymunkSprite(arcade.Sprite):
    
    def __init__(self,
                 filename,
                 center_x=0,
                 center_y=0,
                 scale=1,
                 mass=DEFAULT_MASS,
                 moment=None,
                 friction=DEFAULT_FRICTION,
                 body_type=pymunk.Body.DYNAMIC):

        super().__init__(filename, scale=scale, center_x=center_x, center_y=center_y)

        width = self.texture.width * scale
        height = self.texture.height * scale

        if moment is None:
            moment = pymunk.moment_for_box(mass, (width, height))

        self.body = pymunk.Body(mass, moment, body_type=body_type)
        self.body.position = pymunk.Vec2d(center_x, center_y)

        self.shape = pymunk.Poly.create_box(self.body, (width, height))
        self.shape.friction = friction


def check_grounding(player):
    
    grounding = {
        'normal': pymunk.Vec2d.zero(),
        'penetration': pymunk.Vec2d.zero(),
        'impulse': pymunk.Vec2d.zero(),
        'position': pymunk.Vec2d.zero(),
        'body': None
    }

    def f(arbiter):
        n = -arbiter.contact_point_set.normal
        if n.y > grounding['normal'].y:
            grounding['normal'] = n
            grounding['penetration'] = -arbiter.contact_point_set.points[0].distance
            grounding['body'] = arbiter.shapes[1].body
            grounding['impulse'] = arbiter.total_impulse
            grounding['position'] = arbiter.contact_point_set.points[0].point_b

    player.body.each_arbiter(f)

    return grounding


def resync_physics_sprites(sprite_list):
    
    for sprite in sprite_list:
        sprite.center_x = sprite.shape.body.position.x
        sprite.center_y = sprite.shape.body.position.y
        sprite.angle = math.degrees(sprite.shape.body.angle)
The main program.

main_window.py
"""




import timeit
import os
import arcade
import pymunk

from arcade.examples.pymunk_platformer.create_level import create_level_1
from arcade.examples.pymunk_platformer.physics_utility import (
    PymunkSprite,
    check_grounding,
    resync_physics_sprites,
)

from constants import *

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        # -- Pymunk
        self.space = pymunk.Space()
        self.space.gravity = GRAVITY

        # Physics joint used for grabbing items
        self.grab_joint = None

        # Lists of sprites
        self.dynamic_sprite_list = arcade.SpriteList()
        self.static_sprite_list = arcade.SpriteList()

        # Used for dragging shapes around with the mouse
        self.shape_being_dragged = None
        self.last_mouse_position = 0, 0

        # Draw and processing timings
        self.draw_time = 0
        self.processing_time = 0

        # Current force applied to the player for movement by keyboard
        self.force = (0, 0)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        create_level_1(self.space, self.static_sprite_list, self.dynamic_sprite_list)

        # Create player
        x = 50
        y = (SPRITE_SIZE + SPRITE_SIZE / 2)
        self.player = PymunkSprite("../images/character.png", x, y, scale=0.5, moment=pymunk.inf, mass=1)
        self.dynamic_sprite_list.append(self.player)
        self.space.add(self.player.body, self.player.shape)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        # Draw all the sprites
        self.static_sprite_list.draw()
        self.dynamic_sprite_list.draw()

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20 + self.view_left, SCREEN_HEIGHT - 20 + self.view_bottom, arcade.color.WHITE, 12)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20 + self.view_left, SCREEN_HEIGHT - 40 + self.view_bottom, arcade.color.WHITE, 12)

        # Display instructions
        output = "Use the mouse to move boxes, space to punch, hold G to grab an item to the right."
        arcade.draw_text(output, 20 + self.view_left, SCREEN_HEIGHT - 60 + self.view_bottom, arcade.color.WHITE, 12)

        self.draw_time = timeit.default_timer() - draw_start_time

    def on_mouse_press(self, x, y, button, modifiers):
        """ Handle mouse down events """

        if button == arcade.MOUSE_BUTTON_LEFT:

            # Store where the mouse is clicked. Adjust accordingly if we've
            # scrolled the viewport.
            self.last_mouse_position = (x + self.view_left, y + self.view_bottom)

            # See if we clicked on any physics object
            shape_list = self.space.point_query(self.last_mouse_position, 1, pymunk.ShapeFilter())

            # If we did, remember what we clicked on
            if len(shape_list) > 0:
                self.shape_being_dragged = shape_list[0]

    def on_mouse_release(self, x, y, button, modifiers):
        """ Handle mouse up events """

        if button == arcade.MOUSE_BUTTON_LEFT:

            # Release the item we are holding (if any)
            self.shape_being_dragged = None

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle mouse motion events """

        if self.shape_being_dragged is not None:

            # If we are holding an object, move it with the mouse
            self.last_mouse_position = (x + self.view_left, y + self.view_bottom)
            self.shape_being_dragged.shape.body.position = self.last_mouse_position
            self.shape_being_dragged.shape.body.velocity = dx * 20, dy * 20

    def scroll_viewport(self):
        """ Manage scrolling of the viewport. """

        # Flipped to true if we need to scroll
        changed = False

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.player.left < left_bndry:
            self.view_left -= left_bndry - self.player.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player.right > right_bndry:
            self.view_left += self.player.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player.top > top_bndry:
            self.view_bottom += self.player.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

    def update(self, delta_time):
        """ Update the sprites """

        # Keep track of how long this function takes.
        start_time = timeit.default_timer()

        # If we have force to apply to the player (from hitting the arrow
        # keys), apply it.
        self.player.body.apply_force_at_local_point(self.force, (0, 0))

        # check_collision(self.player)

        # See if the player is standing on an item.
        # If she is, apply opposite force to the item below her.
        # So if she moves left, the box below her will have
        # a force to move to the right.
        grounding = check_grounding(self.player)
        if self.force[0] and grounding and grounding['body']:
            grounding['body'].apply_force_at_world_point((-self.force[0], 0), grounding['position'])

        # Check for sprites that fall off the screen.
        # If so, get rid of them.
        for sprite in self.dynamic_sprite_list:
            if sprite.shape.body.position.y < 0:
                # Remove sprites from physics space
                self.space.remove(sprite.shape, sprite.shape.body)
                # Remove sprites from physics list
                sprite.kill()

        # Update physics
        # Use a constant time step, don't use delta_time
        # See "Game loop / moving time forward"
        # http://www.pymunk.org/en/latest/overview.html#game-loop-moving-time-forward
        self.space.step(1 / 60.0)

        # If we are dragging an object, make sure it stays with the mouse. Otherwise
        # gravity will drag it down.
        if self.shape_being_dragged is not None:
            self.shape_being_dragged.shape.body.position = self.last_mouse_position
            self.shape_being_dragged.shape.body.velocity = 0, 0

        # Resync the sprites to the physics objects that shadow them
        resync_physics_sprites(self.dynamic_sprite_list)

        # Scroll the viewport if needed
        self.scroll_viewport()

        # Save the time it took to do this.
        self.processing_time = timeit.default_timer() - start_time

    def punch(self):
        # --- Punch left
        # See if we have a physics object to our right
        self.check_point = (self.player.right + 10, self.player.center_y)
        shape_list = self.space.point_query(self.check_point, 1, pymunk.ShapeFilter())

        # Apply force to any object to our right
        for shape in shape_list:
            shape.shape.body.apply_impulse_at_world_point((PLAYER_PUNCH_IMPULSE, PLAYER_PUNCH_IMPULSE),
                                                          self.check_point)

        # --- Punch right
        # See if we have a physics object to our left
        self.check_point = (self.player.left - 10, self.player.center_y)
        shape_list = self.space.point_query(self.check_point, 1, pymunk.ShapeFilter())

        # Apply force to any object to our right
        for shape in shape_list:
            shape.shape.body.apply_impulse_at_world_point((-PLAYER_PUNCH_IMPULSE, PLAYER_PUNCH_IMPULSE),
                                                          self.check_point)

    def grab(self):
        """ Grab something """
        # See if we have a physics object to our right
        self.check_point = (self.player.right + 10, self.player.center_y)
        shape_list = self.space.point_query(self.check_point, 1, pymunk.ShapeFilter())

        # Create a joint for an item to our right
        for shape in shape_list:
            self.grab_joint = pymunk.PinJoint(self.player.shape.body, shape.shape.body)
            self.space.add(self.grab_joint)

    def let_go(self):
        """ Let go of whatever we are holding """
        if self.grab_joint:
            self.space.remove(self.grab_joint)
            self.grab_joint = None

    def on_key_press(self, symbol: int, modifiers: int):
        """ Handle keyboard presses. """
        if symbol == arcade.key.RIGHT:
            # Add force to the player, and set the player friction to zero
            self.force = (PLAYER_MOVE_FORCE, 0)
            self.player.shape.friction = 0
        elif symbol == arcade.key.LEFT:
            # Add force to the player, and set the player friction to zero
            self.force = (-PLAYER_MOVE_FORCE, 0)
            self.player.shape.friction = 0
        elif symbol == arcade.key.UP:
            # find out if player is standing on ground
            grounding = check_grounding(self.player)
            if grounding['body'] != None and abs(grounding['normal'].x / grounding['normal'].y) < self.player.shape.friction:
                # She is! Go ahead and jump
                self.player.body.apply_impulse_at_local_point((0, PLAYER_JUMP_IMPULSE))
        elif symbol == arcade.key.SPACE:
            self.punch()
        elif symbol == arcade.key.G:
            self.grab()


    def on_key_release(self, symbol: int, modifiers: int):
        """ Handle keyboard releases. """
        if symbol == arcade.key.RIGHT:
            # Remove force from the player, and set the player friction to a high number so she stops
            self.force = (0, 0)
            self.player.shape.friction = 15
        elif symbol == arcade.key.LEFT:
            # Remove force from the player, and set the player friction to a high number so she stops
            self.force = (0, 0)
            self.player.shape.friction = 15
        elif symbol == arcade.key.G:
            self.let_go()


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)

    arcade.run()


if __name__ == "__main__":
    main()