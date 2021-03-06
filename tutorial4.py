from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "a", self.rotl)
        SpaceGame.listenKeyEvent("keydown", "d", self.rotr)
        self.fxcenter = self.fycenter = 0.5
        self.thrust = 0
        self.thrustframe = 1
        

    def step(self):
        '''self.x += self.vx'''
        self.y += -self.thrust
        self.rotation += self.vr
        # manage thrust animation
        if self.thrust == 1:
            print('step')
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def rotl(self, event):
        self.rotation += 1
        
    def rotr(self, event):
        self.rotation = 0

    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0


class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((200,200))
        SpaceShip((250,250))
        SpaceShip((300,150))
        self.thrust = 0
        self.thrustframe = 1


    def step(self):
        print('vroom')
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame()
myapp.run()
