# What did you see on line 1?
# Line 1 creates random integer between 5 and 20 inclusive.
# What was the smallest number you could have seen, what was the largest?
# The smallest 5, the largest 20

# What did you see on line 2?
# Line 2 generates random number between 3 and 10 (exclusive 10) with step 2
# What was the smallest number you could have seen, what was the largest?
# The smallest: 3, the largest: 9
# Could line 2 have produced a 4?
# No because the step is 2, so the values are (3,5,7,9)

# What did you see on line 3?
# Line 3 generates random floating numbers between 2.5 inclusive and 5.5 exclusive
# What was the smallest number you could have seen, what was the largest?
# Smallest number: 2.5, largest: 5.49999

import random
print(random.randint(1, 100))
