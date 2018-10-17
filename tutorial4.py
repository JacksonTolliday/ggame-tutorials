from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,65,125), 4, 'vertical')                                     # PROBLEMA CON ESA LINEA?

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)

class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()                                                      #so yeah i don't get what I'm doing enough to know how to fix the problem
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)           #ok then
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))            #] aaaaaa?!                                    ] aaaaaa?!
        SpaceShip((150,150))            #] aaaaaa?!   what's happening? y u no ship?   ] aaaaaa?!
        SpaceShip((200,50))             #] aaaaaa?!                                    ] aaaaaa?!


myapp = SpaceGame()


myapp.run()
