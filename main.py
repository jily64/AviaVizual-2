import pyglet
from pyglet.window import Window, FPSDisplay

window = Window(width=800, height=600, caption="Пример Pyglet")
fps_display = FPSDisplay(window)

label = pyglet.text.Label(
    'Привет, Pyglet!',
    font_name='Arial',
    font_size=36,
    y=window.height // 2,
    anchor_x='center',
    anchor_y='center',
    color=(255, 255, 255, 255)
)

@window.event
def on_draw():
    window.clear()
    fps_display.draw()

# Запускаем приложение
pyglet.app.run()