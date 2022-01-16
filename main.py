from engine import Engine
from context import Context


if __name__ == "__main__":
    file = "plot.json"
    Engine.register_context(Context(file))
    Engine.init()
    Engine.play()
