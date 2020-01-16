import datetime
class Building:
    def __init__(self, address, stories):
        self.designer = "James Chapman"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        today = datetime.datetime.today()
        self.date_constructed =  today.strftime("%m/%d/%Y")
    
    def purchase(self, owner):
        self.owner = owner

    def new_article(self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.")


three_hundred_fourth = Building("300 4th street", 20)
three_hundred_fourth.purchase("Terry Crews")
three_hundred_fourth.construct()
three_hundred_fourth.new_article()