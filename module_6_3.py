# ошибка эволюции
class Animal:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'изначально отсуствует'
        _DEGREE_DANGER = 0
        _cords=[0,0,0]

class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Bird (Animal,Horse ):

    def __init__(self):
        self.y_distance = 0
        self.sound = 'Click-Click-Click'

    def fly(self, dy):
        self.y_distance += dy
        #qweruioa/ beak = True

class Predator (Animal):
    Animal__init__(self)
    Horse.__init__(self)



def move(self, dx, dy):
    super().run(dx)



def get_pos(self):
    return self.x_distance, self.y_distance


def voice(self):
    print(self.sound)

class Duckbill (Animal,Horse):
    def __init__(self, Beak=None):
        Horse.__init__( self )
        Bird.__init__( self )
        Beak.__init__(self )

    def move(self, dx, dy):
        super().run( dx )
        super().fly( dy )

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print( self.sound )


p1 = Duckbill ()

print( p1.get_pos() )
p1.move( 10, 15 )
print( p1.get_pos() )
p1.move( -5, 20 )
print( p1.get_pos() )

p1.voice()