

def boot_test(code):
    lines_executed = []
    accumulator = 0
    line = 0

    # Loop through the code until a line is executed for a second time, or the end of the code is reached
    while line not in lines_executed and line < len(code):
        lines_executed.append(line)

        instruction = code[line]
        action = instruction[:3]
        value = int(instruction[4:].replace('+', ''))

        if action == 'jmp':
            line += value
        else:
            line += 1

            if action == 'acc':
                accumulator += value

    # At this point, the boot test either attempted to execute an instruction for a second time, or
    # it reached the line below the last instruction (654). If it's the latter, then it was a success
    if line == len(code):
        return {'success': True, 'accumulator': accumulator}
    else:
        return {'success': False, 'accumulator': accumulator}



if __name__ == '__main__':
    
    boot_code = open('input.txt', 'r').read().splitlines()

    ### Part 1 ###

    result = boot_test(boot_code)

    print('solution 1: ' + str(result['accumulator']))


    ### Part 2 ###

    # For each instance of 'jmp' or 'nop' in the boot code, run a test after changing to the 'other' action
    for line, instruction in enumerate(boot_code):
        action = instruction[:3]
        
        if action == 'jmp' or action == 'nop':
            # Create a copy of the boot code, so we can make changes without affecting the original
            # boot_code_copy = boot_code
            boot_code_copy = boot_code.copy() # Fixed!

            if action == 'jmp':
                boot_code_copy[line] = boot_code_copy[line].replace('jmp', 'nop')
            else:
                boot_code_copy[line] = boot_code_copy[line].replace('nop', 'jmp')

            result = boot_test(boot_code_copy)

            # If the test reached the end of the code, then 'success' will be True and we can quit the test loop
            if result['success']:
                print('solution 2: ' + str(result['accumulator']))
                break
