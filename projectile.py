class Projectiles:
    def __init__(self,options):
        self.x = options["x"]
        self.y = options["y"]
        self.width = options["width"]
        self.height = options["height"]
        self.damage= options["damage"]
        self.xspeed = options["xspeed"]
        self.yspeed = options["yspeed"]
        self.sprite = options["sprite"]

        self.effects = options["effects"]

    def move(self, xspeed, yspeed):
        self.x+=xspeed
        self.y+=yspeed