let ENEMY_INTERVAL_MS = 750
scene.setBackgroundColor(8)
let shark = sprites.create(assets.image`shark`, SpriteKind.Player)
shark.setStayInScreen(true)
info.setLife(3)
controller.moveSprite(shark, 200, 200)
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed() {
    let burger = sprites.createProjectileFromSprite(assets.image`burger`, shark, 200, 0)
    burger.setScale(4 / 9, ScaleAnchor.Middle)
})
game.onUpdateInterval(ENEMY_INTERVAL_MS, function on_update_interval() {
    let fish = sprites.create(assets.image`fish`, SpriteKind.Enemy)
    fish.setVelocity(-50, 0)
    fish.left = scene.screenWidth()
    fish.y = randint(0, scene.screenHeight())
    fish.setFlag(SpriteFlag.AutoDestroy, true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function lose_life(sprite: Sprite, enemySprite: Sprite) {
    enemySprite.destroy()
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function projectile_collision_overlap(projectileSprite: Sprite, enemySprite: Sprite) {
    enemySprite.destroy()
    projectileSprite.destroy(effects.fire, 100)
    info.changeScoreBy(1)
})
ENEMY_INTERVAL_MS = ENEMY_INTERVAL_MS / Math.idiv(info.score(), 5)
