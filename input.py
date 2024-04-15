def SetBeta():
    '''
    This function takes in input the values of the parameter beta
    (infection probability) used for the pandemic evolution.
    
    return:
    -beta (float): infection probability between 0 and 1.
    '''

    beta = float(input("Put in the infection probability (beta):\n"))

    if beta < 0 or beta > 1:
        raise ValueError("Beta parameter must be between zero and one.")
    
    return beta

def SetGamma():
    '''
    This function takes in input the values of the parameter gamma (healing probability)
    used for the pandemic evolution.
    
    return:
    -gamma (float): healing probability between 0 and 1.
    '''

    gamma = float(input("Put in the healing probability (gamma):\n"))
    
    if gamma < 0 or gamma > 1:
        raise ValueError("Gamma parameter must be between zero and one.")

    return gamma

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
    
    if s < 0 or i < 0 or r < 0:
        raise ValueError("We can't have neagtive number of subsceptible, infected or recovered people.")
    
    elif s+i+r == 0:
        raise ValueError("Population must be greater than zero!!!")

    return s, i, r

def SetVaccine():
    '''
    This function asks to user if a vaccine can be used in the simulation.
    This function takes in input a string that is used for the inizialization of a boolean
    variable that allow to run the script for the use of the vaccine.
    '''

    str=input("Do you want to apply some measures to mitigate the epidemic? (y/n)\n")

    if str == "yes" or str == "y":
        bol = True
        print("select one of the following number to use the corresponding action, press:")
        print("1: light lockdown, 20% reduction in the infection prob (beta).")
        print("2: heavy lockdown, 70% reduction in the infection prob (gamma).")
        print("3: weakly effective vaccine, 20% reduction in the infection prob and 50% reduction in the healing prob.")
        print("4: strongly effective vaccine, 60% reduction in the infection prob and 90% reduction in the healing prob.")
        scenario=int(input())
        
        if scenario == 1 or scenario == 2 or scenario == 3 or scenario == 4: 
            pass
        else:
            raise ValueError("Only accepted values are 1/2/3/4.") 

    elif str == "no" or str == "n":
        bol = False
        scenario = None
    else:
        raise TypeError("Only accepted answers are yes/y/no/n.")
    
    return bol, scenario