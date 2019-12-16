
def solve():
    fo = open("input.txt","r")

    line=fo.readline()
    input_store = [int(i) for i in line.split(",")]

    for noun in range(100):
        for verb in range(100):
            input = input_store[:]
            pos = 0
            input[1] = noun
            input[2] = verb

            while input[pos] != 99:
                if input[pos] == 1:
                    input[input[pos+3]] = input[input[pos+1]] + input[input[pos+2]]
    
                if input[pos] == 2:
                    input[input[pos+3]] = input[input[pos+1]] * input[input[pos+2]]

                pos += 4
    
            if input[0] == 19690720:
                return 100 * noun + verb

result = solve()
print("Solution: "+str(result))