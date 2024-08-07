class Projectiles:
    def __init__(self,x,y,width,height, damage,xspeed,yspeed,sprite, effects):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.damage= damage
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.sprite = sprite

        self.effects = effects

    def move(self, xspeed, yspeed):
        self.x+=xspeed
        self.y+=yspeed