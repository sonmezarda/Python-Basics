#TIC TAC TOE
inputs = ["-","-","-",
         "-","-","-",
         "-","-","-"]
isXturn = True
isFinished = False
isDraw = False
    
def show_board():
    print(inputs[0],"|",inputs[1],"|",inputs[2])
    print(inputs[3],"|",inputs[4],"|",inputs[5])
    print(inputs[6],"|",inputs[7],"|",inputs[8])

def check_board_status():
    if inputs[0] != "-" and (inputs[0] == inputs[1] == inputs[2] or inputs[0] == inputs[3] == inputs[6] or inputs[0] == inputs[4] == inputs[8]):
        return True
    elif inputs[3] != "-" and inputs[3] == inputs[4] == inputs[5]:
        return True
    elif inputs[6] != "-" and (inputs[6] == inputs[7] == inputs[8] or inputs[6] == inputs[4] == inputs[2]):
        return True
    elif inputs[1] != "-" and inputs[1] == inputs[4] == inputs[7]:
        return True
    elif inputs[2] != "-" and inputs[2] == inputs[5] == inputs[8]:
        return True
    else:
        return False

show_board()

while not isFinished:
    if isXturn:
        playNumber = int(input("X's Turn!\nPlease input a nuber 1-9: "))
        if playNumber < 10 and inputs[playNumber-1] == "-":  
            inputs[playNumber-1] = "X"
            isXturn = not isXturn
            show_board()
            isFinished = check_board_status()
        else:
            print("Given number is already filled or not in table!\nPlease give different number!")
            continue 
    else:
        playNumber = int(input("O's Turn!\nPlease input a nuber 1-9: "))
        if playNumber < 10 and inputs[playNumber-1] == "-":
            inputs[playNumber-1] = "O"
            isXturn = not isXturn
            show_board()
            isFinished = check_board_status()
        else:
            print("Given number is already filled or not in table!\nPlease give different number!")
            continue 
    if not "-" in inputs:
        isDraw = True
        isFinished = True

if isFinished and not isXturn and not isDraw:
    print("\nX is WON!")
elif isFinished and isXturn and not isDraw:
    print("\nO is WON!")
elif isFinished and isDraw:
    print("\nDraw!")