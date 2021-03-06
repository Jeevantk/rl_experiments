#
# Tic-Tac-Toe experiment settings
#

# 
# Experiment settings
#

# Number of instances to run
instances = 30

# Number of episodes (i.e. games) to run for each instance
episodes = 1000

# Where to store results
results_dir = 'results'


#
# Agent settings
#
# Initial marble count
marble_count = 4

# Marble increment for each step
marble_inc = -1

# Marble win reward, i.e. number of marbles to place back into the matchboxes
# that resulted in a positive reward
marble_win_reward = 3

# Marble win reward increment. Will be applied starting from the first move.
marble_win_inc = 0

# Whether to remove marbles from matchboxes
marble_remove = True

# Set this to a filename to save the learned matchboxes
#save_to = 'learned.matchboxes'
save_to = None

# Set this to a filename to load learned matchboxes
#load_from = 'learned.matchboxes'
load_from = None

