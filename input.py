
def SetPar():
    '''
    This function takes in input the values of the parameters gamma (healing probability)
    and beta (infection probability) used for the pandemic evolution.
    
    return:
    -gamma (float): healing probability between 0 and 1
    -beta (float): infection probability between 0 and 1
    '''

    gamma = float(input("Put in the healing probability (gamma):\n"))
    beta = float(input("Put in the infection probability (beta):\n"))
    
    return gamma, beta

def SetSIR():
    '''
    This function takes in input the parameters of the SIR model used
    for the pandemic evolution.
    
    return:
    -S (int): number of subsceptible people (population that can be infected)
    -I (int): number of infected people (infected population)
    -R (int): number of removed people (population healed or dead from the infection)
    '''
    
    s = int(input("Put in the numbers of susceptible (must be an integer!!!):\n"))
    i = int(input("Put in the numbers of infectious (must be an integer!!!):\n"))
    r = int(input("Put in the numbers of recovered (must be an integer!!!):\n"))
    
    return s, i, r

def SetVaccine():
    '''
    This function asks to user if a vaccine can be used in the simulation.
    This function takes in input a string that is used for the inizialization of a boolean
    variable that allow to run the script for the use of the vaccine.
    '''

    str=input("Do you want to use vaccine? (y/n)\n")

    if str == "yes" or str == "y":
        bol = True

    elif str == "no" or str == "n":
        bol = False

    else:
        raise TypeError("Only accepted answers are yes/y/no/n.")
    
    return bol

def Inspector(gamma, beta, s, i, r):
    '''
    This function checks if the parameters given by the user are compatible for the simulation.
    If not, this function interrupt the esecution of the code and raise the error with the 
    corresponding explanation.
    
    This function needs six parameters:
    -gamma (float): healing probability.
    -beta (float): infection probability. 
    -t (int): duration of the simulation.
    -S (int): number of subsceptible people.
    -I (int): number of infected people.
    -R (int): number of removed people.
    '''
        
    if beta < 0 or beta > 1:
        raise ValueError("Beta parameter must be between zero and one.")

    elif gamma < 0 or gamma > 1:
        raise ValueError("Gamma parameter must be between zero and one.")

    elif s < 0 or i < 0 or r < 0:
        raise ValueError("We can't have neagtive number of subsceptible, infected or recovered people.")
    
    elif s+i+r == 0:
        raise ValueError("Population must be greater than zero!!!")