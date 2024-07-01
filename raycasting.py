from settings import *

class Raycasting():
    def __init__(self, game):
        self.game = game

    def raycast(self):
        px, py = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.000001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # finding horizontal walls
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 0.000001, -1)
            depth_hor = (y_hor - py) / sin_a
            x_hor = px + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # finding vertical walls
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 0.000001, -1)
            depth_vert = (x_vert - px) / cos_a
            y_vert = py + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            # Walls
            wall_height = SCREEM_DIST / (depth + 0.000001)
            pg.draw.rect(self.game.screen, 'Teal', (ray * SCALE, (HEIGHT/2) - wall_height // 2, SCALE, wall_height))

            ray_angle += DElTA_ANGLE


    def update(self):
        self.raycast()