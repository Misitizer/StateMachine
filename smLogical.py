from enum import Enum
import random


class State(Enum):
    b1, b2, b3, b4 = 1, 2, 3, 4


class Input(Enum):
    z1, z2, z3, z4 = 1, 2, 3, 4


def no_state():
    return random.randint(1, 4)


class StateMachine:

    def __init__(self):
        self.firstState = State.b1
        self.activeState = State.b1

    def active(self, active_input):
        if Input(active_input) == Input.z1:
            if self.activeState == State.b1:
                self.activeState = State.b2
                return self.activeState.name, 1

            elif self.activeState == State.b2:
                self.activeState = State.b3
                return self.activeState.name, 0

            elif self.activeState == State.b3:
                self.activeState = State(no_state())
                return self.activeState.name, random.randint(0, 3)

            elif self.activeState == State.b4:
                self.activeState = State.b1
                return self.activeState.name, 0

        elif Input(active_input) == Input.z2:
            if self.activeState == State.b1:
                self.activeState = State.b1
                return self.activeState.name, 0

            elif self.activeState == State.b2:
                self.activeState = State.b3
                return self.activeState.name, random.randint(0, 3)

            elif self.activeState == State.b3:
                self.activeState = State.b3
                return self.activeState.name, 1

            elif self.activeState == State.b4:
                self.activeState = State.b1
                return self.activeState.name, 0

        elif Input(active_input) == Input.z3:
            if self.activeState == State.b1:
                self.activeState = State.b4
                return self.activeState.name, 2

            elif self.activeState == State.b2:
                self.activeState = State.b3
                return self.activeState.name, 1

            elif self.activeState == State.b3:
                self.activeState = State.b1
                return self.activeState.name, 0

            elif self.activeState == State.b4:
                self.activeState = State.b3
                return self.activeState.name, 3

        elif Input(active_input) == Input.z4:
            if self.activeState == State.b1:
                self.activeState = State.b2
                return self.activeState.name, 0

            elif self.activeState == State.b2:
                self.activeState = State.b3
                return self.activeState.name, 3

            elif self.activeState == State.b3:
                self.activeState = State.b4
                return self.activeState.name, random.randint(0, 3)

            elif self.activeState == State.b4:
                self.activeState = State(no_state())
                return self.activeState.name, random.randint(0, 3)


s = StateMachine()