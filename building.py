class Building:
    def __init__(self):
        self.designer = "James Chapman"
        self.date_constructed = ""
        self.owner = ""
        self.address = ""
        self.stories = ""

    def construct(self, owner, address, stories):
        self.date_constructed = datetime.now()
        self.owner = owner
        self.address = address
        self.stories = stories