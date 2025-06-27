# servicer.py

class Service:
    """
    Communicates .

    Attributes:
        model (object): The hand detection model.
        gesture (enum): The active gesture being done
    """
    def __init__(self, model): # ctor
        self.model = model
        self.socket = None

    def bind_socket():
        pass