# bot/guido.py

class Guido:
    def __init__(self):
        self.tutorials = {
            "python": "Visit python.org to start learning Python.",
            "flask": "Check out the Flask Mega-Tutorial on Miguel Grinberg's blog."
        }

    def provide_guidance(self, topic):
        return self.tutorials.get(topic, "I can't find a tutorial on that subject.")

    def list_topics(self):
        # Provide a list of available tutorial topics
        return "I can provide guidance on the following topics: " + ", ".join(self.tutorials.keys())

