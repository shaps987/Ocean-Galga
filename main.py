ENEMY_INTERVAL_MS = 750

scene.set_background_color(8)

shark = sprites.create(assets.image("""shark"""), SpriteKind.player)
shark.set_stay_in_screen(True)

info.set_life(3)

controller.move_sprite(shark, vx=200, vy=200)
def on_event_pressed():
    burger = sprites.create_projectile_from_sprite(assets.image("""burger"""), 
    shark, 
    vx=200, 
    vy=0)
    burger.set_scale(4/9, ScaleAnchor.MIDDLE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

def on_update_interval():
    fish = sprites.create(assets.image("""fish"""), SpriteKind.enemy)
    fish.set_velocity(-50, 0)
    fish.left = scene.screen_width()
    fish.y = randint(0, scene.screen_height())
    fish.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(ENEMY_INTERVAL_MS, on_update_interval)

def lose_life(sprite, enemySprite):
    enemySprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, lose_life)

def projectile_collision_overlap(projectileSprite, enemySprite):
    enemySprite.destroy()
    projectileSprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, projectile_collision_overlap)

ENEMY_INTERVAL_MS = ENEMY_INTERVAL_MS/(info.score() // 5)