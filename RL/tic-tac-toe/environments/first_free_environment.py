"""
Environment which always plays the first free spot available on the board.
"""

from rlglue.environment import EnvironmentLoader
from wrapper_environment import WrapperEnvironment

class FirstFreeEnvironment(WrapperEnvironment):
    
    name = 'first_free'
    
    def env_play(self):
        """
        Pick the first free spot, and play there.
        """
        for i in range(len(self.state)):
            if self.state[i] == 0:
                self.state[i] = self.color
                return

if __name__ == "__main__":
    EnvironmentLoader.loadEnvironment(FirstFreeEnvironment())
