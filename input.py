
def SetPar():
    beta = float(input("Put in the infection probability (beta):\n"))
    gamma = float(input("Put in the healing probability (gamma):\n"))
    return beta, gamma

def SetT():
    
    t= int(input("Put in the duration of the simulation (days):\n"))
    return t

def SetSIR():
    s = (int, input("Put in the numbers of susceptible:\n"))
    i = (int, input("Put in the numbers of infectious:\n"))
    r = (int, input("Put in the numbers of recovered:\n"))
    return s, i, r

if __name__=="__main__":
    SetPar()
    SetT()
    SetSIR()