class Scores:

    def __init__(self, director):
        self.scores = []

    def on_update(self,state=""):
        "Called from the director and defined on the subclass."
        raise NotImplemented("on_update abstract method must be defined in subclass.")

    def on_event(self, event):
        "Called when a specific event is detected in the loop."
        raise NotImplemented("on_event abstract method must be defined in subclass.")

    def on_draw(self, screen, director):
        "Called when you want to draw the screen."
        raise NotImplemented("on_draw abstract method must be defined in subclass.")