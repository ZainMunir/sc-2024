polynomial = [1, 0, 1, 0, 0, 1, 0, 0, 0, 1]
initial_states = [1, 1, 1, 0, 0, 0, 0, 1, 0, 1]
bits = 20

polynomial = input(
    "Enter the polynomial (sequence of 1s and 0s, no spaces) (c) (c_n,...,c_1): "
)
initial_states = input(
    "Enter the initial states (sequence of 1s and 0s, no spaces) (s) (s_n-1,...,s_0): "
)
polynomial = [int(i) for i in polynomial]
initial_states = [int(i) for i in initial_states]

if len(polynomial) != len(initial_states):
    print("Polynomial and initial states must have the same length.")
    exit()
if not all(i in [0, 1] for i in polynomial) or not all(
    i in [0, 1] for i in initial_states
):
    print("Polynomial and initial states must only contain 1s and 0s.")
    exit()


def lfsr_step(polynomial, state):
    output_bit = state[-1]
    new_bit = 0
    for i in range(len(polynomial)):
        if polynomial[i] == 1:
            new_bit ^= state[i]
    state = [new_bit] + state[:-1]
    return state, output_bit


def find_period(polynomial, initial_states):
    state = initial_states
    period = 1
    while True:
        state, _ = lfsr_step(polynomial, state)
        if state == initial_states:
            return period
        period += 1


for i in range(bits):
    initial_states, bit = lfsr_step(polynomial, initial_states)
    print(bit, end="")

print("\nPeriod:", find_period(polynomial, initial_states))
