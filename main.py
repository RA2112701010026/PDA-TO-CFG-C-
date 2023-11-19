import csv

def generate_permutations(states, temp, permutes, k):
    if k == 0:
        permutes.append(temp.copy())
    else:
        for i in range(len(states)):
            temp[k - 1] = states[i]
            generate_permutations(states, temp, permutes, k - 1)

def print_permutes(from_state, input, top_stack, to_state, push_stack, states):
    temp = [None] * len(push_stack)
    permutes = []

    generate_permutations(states, temp, permutes, len(push_stack))

    for i in range(len(permutes)):
        print(f"[{from_state}{top_stack}{permutes[i][0]}] -> {input} [{to_state}{push_stack[0]}", end="")
        for j in range(1, len(permutes[i])):
            print(f"{permutes[i][j]}] [{permutes[i][j]}{push_stack[j]}", end="")
        print(f"{permutes[i][0]}]")
# 'C:/Users/asus/Desktop/fla/pda_input (1).txt'
def PDA_to_CFG(from_state, input, top_stack, to_state, push_stack, states):
    n = len(from_state)
    print("Start State = S -> ", end="")
    print(f"[{states[0]}Z{states[0]}]", end="")
    for i in range(1, len(states)):
        print(f" | [{states[0]}Z{states[i]}]", end="")
    print()

    for i in range(n):
        print(f"\nδ({from_state[i]},{input[i]},{top_stack[i]}) = ({to_state[i]},{push_stack[i]})")
        if push_stack[i] == "ε":
            print(f"[{from_state[i]}{top_stack[i]}{to_state[i]}] -> {input[i]}")
        else:
            print_permutes(from_state[i], input[i], top_stack[i], to_state[i], push_stack[i], states)

def main():
    from_state = []
    to_state = []
    top_stack = []
    input = []
    push_stack = []
    states = []

    with open('C:/Users/asus/Desktop/fla/pda_input (1).txt', 'r') as file:
        reader = file.readlines()
        states = reader[0].split()
        for row in reader[1:]:
            parts = row.strip().split(' ')
            if '->' in parts:
                transition_index = parts.index('->')
                if transition_index == 3 and len(parts) == 5:
                    from_state.append(parts[0])
                    input.append(parts[1])
                    top_stack.append(parts[2])
                    to_state.append(parts[4])
                    push_stack.append(parts[3])
                else:
                    print(f"Error: Incorrect transition format - {row.strip()}")
            else:
                print(f"Error: Expected '->' in {row.strip()}")

    print("PDA given as input:")
    print("States =", ' '.join(states))

    print("PDA Transitions:")
    for i in range(len(from_state)):
        print(f"δ({from_state[i]},{input[i]},{top_stack[i]}) = ({to_state[i]},{push_stack[i]})")

    print("Corresponding CFG:")
    PDA_to_CFG(from_state, input, top_stack, to_state, push_stack, states)

if __name__ == "__main__":
    main()


