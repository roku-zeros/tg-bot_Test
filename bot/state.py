YEAR_SELECTION_STATE = 0
COUNTRY_SELECTION_STATE = 1
DIRECTION_SELECTION_STATE = 2
MEDICINE_SELECTION_STATE = 3
PAYMENT_STATE = 4


class State:

    def __init__(self):
        self.state_now = YEAR_SELECTION_STATE

    def go_next(self):
        if self.state_now < 5:
            self.state_now += 1

    def go_back(self):
        if self.state_now > 0:
            self.state_now -= 1

    def __str__(self):
        return str(self.state_now)

