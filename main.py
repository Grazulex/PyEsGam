from scripts.game import Game

if __name__ == "__main__":
    Game(
        screen_width=1080,
        screen_height=720,
        fps=60,
        title="My Game",
        display_width=540,
        display_height=360
    ).run()