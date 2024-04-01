
def SetPar():
    
    gamma = float(input("Put in the healing probability (gamma):\n"))
    beta = float(input("Put in the infection probability (beta):\n"))
    
    return gamma, beta

def SetT():
    
    t= int(input("Put in the duration of the simulation (days) (must be an integer!!!):\n"))
    
    return t

def SetSIR():
    
    s = int(input("Put in the numbers of susceptible (must be an integer!!!):\n"))
    i = int(input("Put in the numbers of infectious (must be an integer!!!):\n"))
    r = int(input("Put in the numbers of recovered (must be an integer!!!):\n"))
    
    return s, i, r

def Inspector(gamma, beta, t,s,i,r):
    
    if t <= 0:
        raise ValueError("Simulation cannot take place with times less than or equal to zero.")
    
    elif beta < 0 or beta > 1:
        raise ValueError("Beta parameter must be between zero and one.")

    elif gamma < 0 or gamma > 1:
        raise ValueError("Gamma parameter must be between zero and one.")

    elif s < 0 or i < 0 or r < 0:
        raise ValueError("We can't have neagtive number of subsceptible, infected or recovered people.")
    
    elif s+i+r == 0:
        raise ValueError("Population must be greater than zero!!!")