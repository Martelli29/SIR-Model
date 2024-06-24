import json


def load_config() -> None:
    """
    Loading of the configuration file named 'config.json', if the file name is different,
    an error is raised.

    return:
        None 
    """

    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found.")


def CheckBeta(beta : float) -> None:
    """
    Checks if the parameter beta (infection probability) given as input
    by the user has a value between 0 and 1 and that it is float type.

    1 parameter needed:
        -beta (float): infection probability.

    return:
        None
    """

    if type(beta) != float:
        raise TypeError("Beta parameter must be float type.")

    elif beta < 0 or beta > 1:
        raise ValueError("Beta parameter must be between zero and one.")


def CheckGamma(gamma : float) -> None:
    """
    Checks if the parameter gamma (healing probability) given as input
    by the user has a value between 0 and 1 and that it is float type.

    1 parameter needed:
        -gamma (float): healing probability.

    return:
        None
    """

    if type(gamma) != float:
        raise TypeError("Beta parameter must be float type.")

    elif gamma <= 0 or gamma > 1:
        raise ValueError("Gamma parameter must be between zero and one.")


def CheckSIR(s : int, i : int, r : int) -> None:
    """
    Checks if the user gives proper values through the configuration file.
    They must be non negative whole number and the total population must be
    bigger then 0.

    3 parameters needed:
        -S (int): number of susceptible people (population that can be infected).
        -I (int): number of infected people (infected population).
        -R (int): number of removed people (population healed or dead from the infection).

    return:
        None
    """

    if type(s) != int or type(i) != int or type(r) != int:
        raise TypeError("s/i/r population must be whole numbers.")

    elif s < 0 or i < 0 or r < 0:
        raise ValueError(
            "We can't have neagtive number of subsceptible, infected or recovered people.")

    elif s + i + r == 0:
        raise ValueError("Population must be greater than zero!!!")


def CheckVaccine(scenario : str) -> None:
    """
    Checks the correct selection and syntax of the selected scenario.
    Are available five different scenarios (no measures, light lockdown,
    heavy lockdown, weakly effective vaccine, strongly effective vaccine.)

    1 parameter needed:
        scenario (str): store the scenario selected by the user.

    return:
        None
    """

    if type(scenario) == str:
        scenario = scenario.lower()

    if scenario == "no measures" or scenario == "light lockdown" or scenario == "heavy lockdown" or scenario == "weakly effective vaccine" or scenario == "strongly effective vaccine":
        pass
    else:
        raise TypeError(
            "Only accepted answers are the strings:\n-no measures\n-light lockdown\n-heavy lockdown\n-weakly effective vaccine\n-strongly effective vaccine")


def Configuration() -> dict[int, int, int, float, float, str]:
    """
    In this file we have the creation of the epidemic variable that are 
    inizialized through the access of the configuration file.
    Then the checker functions are called to verify that all the parameters
    given by the user are suitable for the program.

    return:
        "S" (int): number of the initial susceptible population.
        "I" (int): number of the initial infected population.
        "R" (int): number of the initial removed population.
        "gamma" (float): healing probability after each day of the simulation.
        "beta" (float): infection probability after each day of the simulation.
        "scenario" (str): selected scenario for the simulation.
    """

    config = load_config()  # loading of the config file

    gamma = config["gamma"]["value"]
    beta = config["beta"]["value"]
    s = config["SIR"]["S"]["value"]
    i = config["SIR"]["I"]["value"]
    r = config["SIR"]["R"]["value"]
    scenario = config["vaccine_scenario"]["value"]

    CheckBeta(beta)
    CheckGamma(gamma)
    CheckSIR(s, i, r)
    CheckVaccine(scenario)

    return {"S": s, "I": i, "R": r, "gamma": gamma, "beta": beta, "scenario": scenario}
