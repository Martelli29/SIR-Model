import epidemic_class as epd


def test_Vaccine_Scenario1():
    """
    Checks if beta parameter (infection probability) is reduced by 20% due
    to the activation of scenario "light lockdown".
    """

    config_test = {"S": 1000, "I": 1000, "R": 0, "gamma": 0.01,
                   "beta": 0.5, "scenario": "light lockdown"}
    test = epd.EpidemicSIR(config_test)
    vax, gamma, beta = test.Vaccine(None, 0.01, 0.5)

    assert (beta == 0.4)


def test_Vaccine_Scenario2():
    """
    Checks if beta parameter (infection probability) is reduced by 70% due
    to the activation of scenario "heavy lockdown".
    """

    config_test = {"S": 1000, "I": 1000, "R": 0, "gamma": 0.01,
                   "beta": 0.5, "scenario": "heavy lockdown"}
    test = epd.EpidemicSIR(config_test)
    vax, gamma, beta = test.Vaccine(None, 0.01, 0.9)

    assert (beta == 0.27)


def test_Vaccine_Scenario3():
    """
    Checks if beta parameter (infection probability) is reduced by 20% and gamma
    parameter (healing probability) is increased by 50% due to the activation of scenario "weakly effective vaccine".
    """

    config_test = {"S": 1000, "I": 1000, "R": 0, "gamma": 0.01,
                   "beta": 0.5, "scenario": "weakly effective vaccine"}

    test = epd.EpidemicSIR(config_test)
    vax, gamma, beta = test.Vaccine(None, 0.1, 0.5)
    gamma = round(gamma, 5)

    assert (gamma == 0.15 and beta == 0.4)


def test_Vaccine_Scenario4():
    """
    Checks if beta parameter (infection probability) is reduced by 60% and gamma
    parameter (healing probability) is increased by 90% due to the activation of scenario "strongly effective vaccine".
    """

    config_test = {"S": 1000, "I": 1000, "R": 0, "gamma": 0.01,
                   "beta": 0.5, "scenario": "strongly effective vaccine"}

    test = epd.EpidemicSIR(config_test)
    vax, gamma, beta = test.Vaccine(None, 0.1, 0.5)
    gamma = round(gamma, 5)
    beta = round(beta, 5)

    assert (gamma == 0.19 and beta == 0.2)


def test_Vaccine_OnlyOnes():
    """
    Checks the no modification of the parameters gamma and beta in a scenario
    different from "no measures" if the parameters were already changed in a previous iteration
    of the cycle.
    We can check this by passing a value different from None to the Vaccine(..) method.
    """

    config_test = {"S": 1000, "I": 1000, "R": 0, "gamma": 0.01,
                   "beta": 0.5, "scenario": "strongly effective vaccine"}

    test = epd.EpidemicSIR(config_test)
    vax, gamma, beta = test.Vaccine(True, 0.1, 0.5)

    assert (vax == True and gamma == 0.1 and beta == 0.5)


def test_Vaccine_NoMeasures():
    """
    Checks the no modification of the parameters gamma and beta if the selected
    scenario is "no measures".
    """

    config_test = {"S": 1000, "I": 1000, "R": 0, "gamma": 0.01,
                   "beta": 0.5, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    vax, gamma, beta = test.Vaccine(None, 0.1, 0.5)

    assert (vax == False and gamma == 0.1 and beta == 0.5)


def test_DiffEq_Float():
    """
    Checks the correct type (float) of the returned variable S, I, R
    """

    config_test = {"S": 1000, "I": 1000, "R": 0, "gamma": 0.1,
                   "beta": 0.3, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    S, I, R = test.DifferentialEq(10000, 10000, 0, 0.1, 0.3)

    assert (type(S) == float and type(I) == float and type(R) == float)


def test_DiffEq_ZeroBeta():
    """
    Check the no variation of S if we use a value of beta equal to 0.
    """

    config_test = {"S": 10000, "I": 10000, "R": 0, "gamma": 0.1,
                   "beta": 0.0, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    S, I, R = test.DifferentialEq(10000, 10000, 0, 0.1, 0.0)

    assert (S == 10000)


def test_DiffEq_ZeroGamma():
    """
    Checks the no variation of R if we use a value of gamma equal to 0
    """

    config_test = {"S": 10000, "I": 10000, "R": 0, "gamma": 0.0,
                   "beta": 0.2, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    S, I, R = test.DifferentialEq(10000, 10000, 0, 0.0, 0.2)

    assert (R == 0)


def test_DiffEq_NoEvolution():
    """
    Checks the no variation of all parameters (S, I, R) if the values
    of gamma and beta are equal to 0.
    """

    config_test = {"S": 10000, "I": 10000, "R": 0, "gamma": 0.0,
                   "beta": 0.0, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    S, I, R = test.DifferentialEq(10000, 10000, 0, 0.0, 0.0)

    assert (S == 10000 and I == 10000 and R == 0)


def test_DiffEq_StandardEvolution():
    """
    Checks the correct variation of all parameters (S, I, R) for
    values of gamma and beta different from zero.
    """

    config_test = {"S": 10000, "I": 10000, "R": 0, "gamma": 1.0,
                   "beta": 1.0, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    S, I, R = test.DifferentialEq(10000, 10000, 0, 1.0, 1.0)

    assert (S == 5000 and I == 5000 and R == 10000)


def test_Approximation_IncrementR():
    """
    Checks the correct increment of R if it has the biggest decimal part.
    """

    config_test = {"S": 8, "I": 1, "R": 1, "gamma": 0.1,
                   "beta": 0.1, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    S, I, R = test.Approximation(7.1, 1.2, 1.3)

    assert (S == 7 and I == 1 and R == 2)


def test_Approximation_IncrementI():
    """
    Checks the correct increment of I if it has the biggest decimal part.
    """

    config_test = {"S": 8, "I": 1, "R": 1, "gamma": 0.1,
                   "beta": 0.1, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    S, I, R = test.Approximation(7.1, 1.5, 1.3)

    assert (S == 7 and I == 2 and R == 1)


def test_Approximation_IncrementS():
    """
    Checks the correct increment of S if it has the biggest decimal part and
    if, after the increment, it isn't bigger than the value of S before the evolution.
    """

    config_test = {"S": 8, "I": 1, "R": 1, "gamma": 0.1,
                   "beta": 0.1, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.S_vector[-1] = 8
    S, I, R = test.Approximation(7.5, 1.2, 1.3)

    assert (S == 8)


def test_Approximation_NoIncrementS():
    """
    Checks the no increment of S if it has the biggest decimal part
    but, after the increment, it is bigger than the value of S before the evolution.
    """

    config_test = {"S": 8, "I": 1, "R": 1, "gamma": 0.1,
                   "beta": 0.1, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.S_vector[-1] = 7
    S, I, R = test.Approximation(7.5, 1.2, 1.3)

    assert (S == 7)


def test_Approximation_PopulationConservation():
    """
    Checks if the total population is conserved after the approximation.
    """

    config_test = {"S": 10000, "I": 10000, "R": 0, "gamma": 1.0,
                   "beta": 1.0, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    S, I, R = test.Approximation(10000, 10000, 0)

    assert (S + I + R == test.N)


def test_Approximation_type():
    """
    Checks the correct type of the (S, I, R) parameters after the approximation (int).
    """

    config_test = {"S": 8, "I": 1, "R": 1, "gamma": 0.1,
                   "beta": 0.1, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    S, I, R = test.Approximation(7.1, 1.5, 1.3)

    assert (type(S) == int and type(I) == int and type(R) == int)


def test_Evolve_ConservationOfN_1():
    """
    Checks if the value of the total population (N) is conserved during the
    epidemic evolution.
    """

    config_test = {"S": 30000, "I": 1, "R": 0, "gamma": 0.1,
                   "beta": 0.3, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()
    for i in range(test.day):
        assert (test.S_vector[i] + test.I_vector[i] +
                test.R_vector[i] == test.N)


def test_Evolve_ConservationOfN_2():
    """
    In this test we use a bigger number of susceptible to check if N is
    conserved during the epidemic evolution.
    """

    config_test = {"S": 30000000, "I": 1, "R": 0, "gamma": 0.1,
                   "beta": 0.3, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()
    for i in range(test.day):
        assert (test.S_vector[i] + test.I_vector[i] +
                test.R_vector[i] == test.N)


def test_Evolve_DecresentS_1():
    """
    Checks if the value of susceptible population doesn't increase during
    the epidemic simulation.
    """

    config_test = {"S": 30000, "I": 1, "R": 0, "gamma": 0.1,
                   "beta": 0.3, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    for i in range(1, test.day):
        assert (test.S_vector[i] <= test.S_vector[i - 1])


def test_Evolve_DecresentS_2():
    """
    Checks if the value of susceptible population doesn't increase during
    the epidemic simulation using a very small numbers for gamma and beta.
    """

    config_test = {"S": 30000, "I": 1, "R": 0, "gamma": 0.001,
                   "beta": 0.003, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    for i in range(1, test.day):
        assert (test.S_vector[i] <= test.S_vector[i - 1])


def test_Evolve_DecresentS_3():
    """
    Checks if the value of susceptible population doesn't increase during
    the epidemic simulation using a very small number of susceptible.
    """

    config_test = {"S": 100, "I": 1, "R": 0, "gamma": 0.01,
                   "beta": 0.03, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    for i in range(1, test.day):
        assert (test.S_vector[i] <= test.S_vector[i - 1])


def test_Evolve_DecresentS_4():
    """
    Checks if the value of susceptible population doesn't increase during
    the epidemic simulation using a big numbers for gamma and beta.
    """

    config_test = {"S": 100000, "I": 1, "R": 0, "gamma": 0.5,
                   "beta": 0.6, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    for i in range(1, test.day):
        assert (test.S_vector[i] <= test.S_vector[i - 1])


def test_Evolve_ZeroInfected():
    """
    Checks if the value of susceptible doesn't change if there are no
    infected population.
    """

    config_test = {"S": 1000, "I": 0, "R": 0, "gamma": 0.2,
                   "beta": 0.2, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    for i in range(test.day):
        assert (test.S_vector[i] == 1000 and test.I_vector[i]
                == 0 and test.R_vector[i] == 0)


def test_Evolve_SimulationTimeZero():
    """
    Checks if the duration of the simulation is equal to 0 if the number of infected
    is equal to 0
    """

    config_test = {"S": 1000, "I": 0, "R": 0, "gamma": 0.2,
                   "beta": 0.2, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    assert (test.day - 1 == 0)


def test_Evolve_SimulationTimeOne():
    """
    Checks if the duration of the simulation is equal to 1 if the healing probability
    is equal to 1 and infection probability is equal to 0.
    """

    config_test = {"S": 1000, "I": 10, "R": 0, "gamma": 1.0,
                   "beta": 0.0, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    assert (test.day - 1 == 1)


def test_Evolve_ZeroInfection():
    """
    Checks if the values of susceptible doesn't change if there are some
    infected population with 0.0% probability to infect. 
    """

    config_test = {"S": 1000, "I": 10, "R": 0, "gamma": 0.2,
                   "beta": 0.0, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    assert (test.S_vector[-1] == 1000 and test.I_vector[-1]
            == 0 and test.R_vector[-1] == 10)


def test_Evolve_NoEpidemic():
    """
    Checks if the values of susceptible population remain unchanged if we have
    no infected people.
    """

    config_test = {"S": 1000, "I": 0, "R": 0, "gamma": 0.5,
                   "beta": 0.5, "scenario": "strongly effective vaccine"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    for i in range(test.day):
        assert (test.S_vector[i] == 1000 and test.I_vector[i]
                == 0 and test.R_vector[i] == 0)


def test_Evolve_NoVaccineNecessary_1():
    """
    Checks the no activation of vaccine if light lockdown scenario is selected but
    the infected population doesn't reach a value equal to 10% of total population.
    """

    config_test = {"S": 10000, "I": 10, "R": 0, "gamma": 0.05,
                   "beta": 0.0, "scenario": "light lockdown"}

    test = epd.EpidemicSIR(config_test)
    v, gamma, beta = test.Vaccine(None, 0.05, 0.0)

    gamma = round(test.gamma, 5)
    beta = round(test.beta, 5)

    assert (gamma == 0.05 and beta == 0.0)


def test_Evolve_NoVaccineNecessary_2():
    """
    Checks the no activation of vaccine if heavy lockdown scenario is selected but
    the infected population doesn't reach a value equal to 10% of total population.
    """

    config_test = {"S": 10000, "I": 10, "R": 0, "gamma": 0.05,
                   "beta": 0.0, "scenario": "heavy lockdown"}

    test = epd.EpidemicSIR(config_test)
    v, gamma, beta = test.Vaccine(None, 0.05, 0.0)

    gamma = round(test.gamma, 5)
    beta = round(test.beta, 5)

    assert (gamma == 0.05 and beta == 0.0)


def test_Evolve_NoVaccineNecessary_3():
    """
    Checks the no activation of vaccine if weakly effective vaccine scenario is selected but
    the infected population doesn't reach a value equal to 10% of total population.
    """

    config_test = {"S": 10000, "I": 10, "R": 0, "gamma": 0.05,
                   "beta": 0.0, "scenario": "weakly effective vaccine"}

    test = epd.EpidemicSIR(config_test)
    v, gamma, beta = test.Vaccine(None, 0.05, 0.0)

    gamma = round(test.gamma, 5)
    beta = round(test.beta, 5)

    assert (gamma == 0.05 and beta == 0.0)


def test_Evolve_NoVaccineNecessary_4():
    """
    Checks the no activation of vaccine if strongly effective vaccine scenario is selected but
    the infected population doesn't reach a value equal to 10% of total population.
    """

    config_test = {"S": 10000, "I": 10, "R": 0, "gamma": 0.05,
                   "beta": 0.0, "scenario": "strongly effective vaccine"}

    test = epd.EpidemicSIR(config_test)
    v, gamma, beta = test.Vaccine(None, 0.05, 0.0)

    gamma = round(test.gamma, 5)
    beta = round(test.beta, 5)

    assert (gamma == 0.05 and beta == 0.0)


def test_Evolve_VectorsLength():
    """
    Checks if the size of the S/I/R vectors are equal to the duration of the simulation.
    """

    config_test = {"S": 30000, "I": 1, "R": 0, "gamma": 0.1,
                   "beta": 0.3, "scenario": "no measures"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    assert (len(test.S_vector) == len(test.I_vector)
            == len(test.R_vector) == test.day)


def test_NoVaccineDay():
    """
    Checks the non activation of the vaccine/isolation day even if user has
    enabled the proper option but 10% of infected people is never reached.
    """

    config_test = {"S": 10000, "I": 10, "R": 0, "gamma": 0.1,
                   "beta": 0.1, "scenario": "strongly effective vaccine"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    assert (test.triggerday == None)


def test_VaccineDay():
    """
    Checks the activation of the vaccine/isolation day if user has
    enabled the proper option and 10% of people is infected.
    """

    config_test = {"S": 10000, "I": 500, "R": 0, "gamma": 0.1,
                   "beta": 1.0, "scenario": "strongly effective vaccine"}

    test = epd.EpidemicSIR(config_test)
    test.Evolve()

    assert (test.triggerday == 2)
