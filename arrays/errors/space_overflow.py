class SpaceOverFlowException(Exception):

    def __init__(self, max_space: int):
        super().__init__(f"You've surpassed the space of the array. Limit is {max_space}")