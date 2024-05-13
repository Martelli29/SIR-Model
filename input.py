def SetBeta():
    """
    This function takes in input the values of the parameter beta
    (infection probability) used for the pandemic evolution.

    return:
    -beta (float): infection probability between 0 and 1.
    """

    beta = float(input("Put in the infection probability (beta):\n"))

    if beta < 0 or beta > 1:
        raise ValueError("Beta parameter must be between zero and one.")

    return beta


def SetGamma():
    """
    This function takes in input the values of the parameter gamma (healing probability)
    used for the pandemic evolution.

    return:
    -gamma (float): healing probability between 0 and 1.
    """

    gamma = float(input("Put in the healing probability (gamma):\n"))

    if gamma <= 0 or gamma > 1:
        raise ValueError("Gamma parameter must be between zero and one.")

    return gamma


def SetSIR():
    """
    This function takes in input the parameters of the SIR model used
    for the pandemic evolution.

    return:
    -S (int): number of subsceptible people (population that can be infected)
    -I (int): number of infected people (infected population)
    -R (int): number of removed people (population healed or dead from the infection)
    """

    s = int(input("Put in the numbers of susceptible (must be an integer!!!):\n"))
    i = int(input("Put in the numbers of infectious (must be an integer!!!):\n"))
    r = int(input("Put in the numbers of recovered (must be an integer!!!):\n"))

    if s < 0 or i < 0 or r < 0:
        raise ValueError(
            "We can't have neagtive number of subsceptible, infected or recovered people.")

    elif s+i+r == 0:
        raise ValueError("Population must be greater than zero!!!")

    return s, i, r


def SetVaccine():
    """
    This function control the implementation of the countermeasures.
    Takes in input a string that is stored in a variable that allow
    to run the script with the usege of the vaccine (or not).

    return:
    scenario (str): store the scenario selected by the user.
    """

    print()
    print("Digit one of the following scenario to activate the corresponding action:")
    print("no measures: No measures will be used.")
    print("light lockdown: 20% reduction in the infection prob (beta).")
    print("heavy lockdown: 70% reduction in the infection prob (gamma).")
    print("weakly effective vaccine: 20% reduction in the infection prob and 50% reduction in the healing prob.")
    print("strongly effective vaccine: 60% reduction in the infection prob and 90% reduction in the healing prob.")
    print()
    print("Mitigation measures will be activated only if 10% of population is infected on a current day.")

    scenario = input().lower()

    if scenario == "no measures" or "light lockdown" or "heavy lockdown" or "weakly effective vaccine" or "strongly effective vaccine":
        pass
    else:
        raise TypeError(
            "Only accepted answers are no measures/light lockdown/heavy lockdown/weakly effective vaccine/strongly effective vaccine.")

    return scenario
