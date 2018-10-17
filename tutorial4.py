from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,65,125), 4, 'vertical')                                     # PROBLEMA CON ESA LINEA?

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        # manage thrust animation
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0


class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):                                                 #like what even is __init__???
        super().__init__()                                                      #so yeah i don't get what I'm doing enough to know how to fix the problem
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)           #ok then        I DID NOTHING WHY DOES IT WORK NOW?!
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))            #] aaaaaa?!                                    ] aaaaaa?!
        SpaceShip((150,150))            #] aaaaaa?!   what's happening? y u no ship?   ] aaaaaa?!
        SpaceShip((200,50))             #] aaaaaa?!                                    ] aaaaaa?!
        self.thrust = 0
        self.thrustframe = 1


    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame()


myapp.run()
