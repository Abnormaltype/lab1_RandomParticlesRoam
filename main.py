import random

M, N = 8, 8
X, Y = 4, 4
P1, P2, P3, P4 = 0.2, 0.2, 0.2, 0.2
NORTH, SOUTH, WEST, EAST, STOP = 0, 0, 0, 0, 0
PARTICLES = 10_000_00


class Particle:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.is_stopped = False

    def move(self):
        rand = random.random()

        if rand < P1:
            self.y_coord += 1
        elif rand < P1 + P2:
            self.y_coord -= 1
        elif rand < P1 + P2 + P3:
            self.x_coord += 1
        elif rand < P1 + P2 + P3 + P4:
            self.x_coord -= 1
        else:
            self.is_stopped = True


def main():
    global STOP, NORTH, WEST, EAST, SOUTH
    for i in range(PARTICLES):
        point = Particle(X, Y)

        while M > point.x_coord > 0 and N > point.y_coord > 0 and not point.is_stopped:
            point.move()

        if point.is_stopped:
            STOP += 1
        else:
            if point.y_coord == M:
                NORTH += 1
            elif point.y_coord == 0:
                SOUTH += 1
            elif point.x_coord == N:
                EAST += 1
            elif point.x_coord == 0:
                WEST += 1


if __name__ == "__main__":
    main()

    print("North: " + str(NORTH / PARTICLES))
    print("South: " + str(SOUTH / PARTICLES))
    print("East: " + str(EAST / PARTICLES))
    print("West: " + str(WEST / PARTICLES))
    print("Stopped: " + str(STOP / PARTICLES))
