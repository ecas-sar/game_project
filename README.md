# game_project\
The purpose of this project is to understand and implement pursuit curves in order to understand how enemies can chase
the player as the player attempts to avoid them. Today, the menu screen was implemented although none of the buttons work yet.

Now the buttons work, although the logic needs updating, the maths works fine here but the button also is considered clicked if the mouse is simply close to it and not necessarily over it.

It is possible to play as a white square that moves when you use the arrow keys, and it moves smoothly in 8 directions.

Now, instead of the square, there is a sprite made using piskel, and there are different sprites used for which direction you move in (the character points their sword in different directions).

The health bar is displayed in the top left and the background is now an image made using piskel rather than just a black backround. 

The bat is displayed with the x and y coordinates probability being uniformly distributed (i.e. the bat is equally likely to spawn anywhere on the screen), and the flap animation works correctly.

The character cannot exit the boundaries, and the bat will chase the character around the map. The player can now attack, with the sprite changing for an attack in each direction.

The buttons work with correct logic now, the collision detection, health, and death mechanics all work, and the losing screen has been made and the text and buttons all work properly. Also, it is possible to attack the bat, and the player doesn't lose hp if they attack the bat.

The score now works and displays properly. When you get a score of 10, the winning screen shows.