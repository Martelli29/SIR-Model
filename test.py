import epidemic_class as epd
from unittest.mock import patch


def test_Vaccine_Scenario1():
    '''
    Checks if beta parameter (infection probability) is reduced by 20% due
    to the activation of scenario "light lockdown".
    '''

    test = epd.EpidemicSIR(1000, 1000, 0, 0.01, 0.5, "light lockdown")
    vax, gamma, beta = test.Vaccine(None, 0.01, 0.5)
    assert (beta == 0.4)


def test_Vaccine_Scenario2():
    '''
    Checks if beta parameter (infection probability) is reduced by 70% due
    to the activation of scenario "heavy lockdown".
    '''

    test = epd.EpidemicSIR(1000, 1000, 0, 0.01, 0.5, "heavy lockdown")

    vax, gamma, beta = test.Vaccine(None, 0.01, 0.9)
    assert (beta == 0.27)


def test_Vaccine_Scenario3():
    '''
    Checks if beta parameter (infection probability) is reduced by 20% and gamma
    parameter (healing probability) is increased by 50% due to the activation of scenario "weakly effective vaccine".
    '''

    test = epd.EpidemicSIR(1000, 1000, 0, 0.1, 0.5, "weakly effective vaccine")
    vax, gamma, beta = test.Vaccine(None, 0.1, 0.5)
    gamma = round(gamma, 5)

    assert (gamma == 0.15 and beta == 0.4)


def test_Vaccine_Scenario4():
    '''
    Checks if beta parameter (infection probability) is reduced by 60% and gamma
    parameter (healing probability) is increased by 90% due to the activation of scenario "strongly effective vaccine".
    '''

    test = epd.EpidemicSIR(1000, 1000, 0, 0.1, 0.5,
                           "strongly effective vaccine")
    vax, gamma, beta = test.Vaccine(None, 0.1, 0.5)
    gamma = round(gamma, 5)
    beta = round(beta, 5)

    assert (gamma == 0.19 and beta == 0.2)


def test_Vaccine_OnlyOnes():
    '''
    Checks the no modification of the parameters gamma and beta in a scenario 
    different from "no measures" if the parameters were already changed in a previous iteration
    of the cycle.
    We can check this by passing a value different from None to the Vaccine(..) method.
    '''

    test = epd.EpidemicSIR(1000, 1000, 0, 0.1, 0.5,
                           "strongly effective vaccine")
    vax, gamma, beta = test.Vaccine(True, 0.1, 0.5)

    assert (vax == True and gamma == 0.1 and beta == 0.5)


def test_Vaccine_NoMeasures():
    '''
    Checks the no modification of the parameters gamma and beta if the selected
    scenario is "no measures".
    '''

    test = epd.EpidemicSIR(1000, 1000, 0, 0.1, 0.5, "no measures")
    vax, gamma, beta = test.Vaccine(None, 0.1, 0.5)

    assert (vax == False and gamma == 0.1 and beta == 0.5)


def test_DiffEq_Float():
    '''
    Checks the correct type (float) of the returned variable S, I, R
    '''

    test = epd.EpidemicSIR(10000, 10000, 0, 0.1, 0.3, "no measures")
    S, I, R = test.DifferentialEq(10000, 10000, 0, 0.1, 0.3)

    assert (type(S) == float and type(I) == float and type(R) == float)


def test_DiffEq_ZeroBeta():
    '''
    Check the no variation of S if we use a value of beta equal to 0.
    '''

    test = epd.EpidemicSIR(10000, 10000, 0, 0.1, 0.0, "no measures")
    S, I, R = test.DifferentialEq(10000, 10000, 0, 0.1, 0.0)

    assert (S == 10000)


def test_DiffEq_ZeroGamma():
    '''
    Checks the no variation of R if we use a value of gamma equal to 0
    '''

    test = epd.EpidemicSIR(10000, 10000, 0, 0.0, 0.2, "no measures")
    S, I, R = test.DifferentialEq(10000, 10000, 0, 0.0, 0.2)

    assert (R == 0)


def test_DiffEq_NoEvolution():
    '''
    Checks the no variation of all parameters (S, I, R) if the values
    of gamma and beta are equal to 0.
    '''

    test = epd.EpidemicSIR(10000, 10000, 0, 0.0, 0.0, "no measures")
    S, I, R = test.DifferentialEq(10000, 10000, 0, 0.0, 0.0)

    assert (S == 10000 and I == 10000 and R == 0)


def test_DiffEq_StandardEvolution():
    '''
    Checks the correct variation of all parameters (S, I, R) for
    values of gamma and beta different than zero. 
    '''

    test = epd.EpidemicSIR(10000, 10000, 0, 1.0, 1.0, "no measures")
    S, I, R = test.DifferentialEq(10000, 10000, 0, 1.0, 1.0)

    assert (S == 5000 and I == 5000 and R == 10000)


def test_Approximation_IncrementR():
    '''
    Checks the correct increment of R if it has the biggest decimal part.
    '''

    test = epd.EpidemicSIR(8, 1, 1, 0.1, 0.1, "no measures")
    S, I, R = test.Approximation(7.1, 1.2, 1.3)

    assert (S == 7 and I == 1 and R == 2)


def test_Approximation_IncrementI():
    '''
    Checks the correct increment of I if it has the biggest decimal part.
    '''

    test = epd.EpidemicSIR(8, 1, 1, 0.1, 0.1, "no measures")
    S, I, R = test.Approximation(7.1, 1.5, 1.3)

    assert (S == 7 and I == 2 and R == 1)


def test_Approximation_IncrementS():
    '''
    Checks the correct increment of S if it has the biggest decimal part and
    if, after the increment, it isn't bigger than the value of S before the evolution.
    '''

    test = epd.EpidemicSIR(8, 1, 1, 0.1, 0.1, "no measures")
    test.S_vector[-1] = 8
    S, I, R = test.Approximation(7.5, 1.2, 1.3)

    assert (S == 8)


def test_Approximation_NoIncrementS():
    '''
    Checks the no increment of S if it has the biggest decimal part
    but, after the increment, it is bigger than the value of S before the evolution.
    '''

    test = epd.EpidemicSIR(8, 1, 1, 0.1, 0.1, "no measures")
    test.S_vector[-1] = 7
    S, I, R = test.Approximation(7.5, 1.2, 1.3)

    assert (S == 7)


def test_Approximation_PopulationConservation():
    '''
    Checks if the total population is conserved after the approximation.
    '''

    test = epd.EpidemicSIR(10000, 10000, 0, 1.0, 1.0, "no measures")
    S, I, R = test.Approximation(10000, 10000, 0)

    assert (S+I+R == test.N)


def test_Approximation_type():
    '''
    Checks the correct type of the (S, I, R) parameters after the approximation (int).
    '''

    test = epd.EpidemicSIR(8, 1, 1, 0.1, 0.1, "no measures")
    S, I, R = test.Approximation(7.1, 1.5, 1.3)

    assert (type(S) == int and type(I) == int and type(R) == int)


def test_Evolve_ConservationOfN_1():
    '''
    Checks if the value of the total population (N) is conserved during the
    epidemic evolution.
    '''

    test = epd.EpidemicSIR(30000, 1, 0, 0.1, 0.3, "no measures")
    test.Evolve()
    for i in range(test.day):
        assert (test.S_vector[i] + test.I_vector[i] +
                test.R_vector[i] == test.N)


def test_Evolve_ConservationOfN_2():
    '''
    In this test we use a bigger number of subsecptible to check if N is
    conserved dureing the epidemic evolution.
    '''

    test = epd.EpidemicSIR(30000000, 1, 0, 0.1, 0.3, "no measures")
    test.Evolve()
    for i in range(test.day):
        assert (test.S_vector[i] + test.I_vector[i] +
                test.R_vector[i] == test.N)


def test_Evolve_DecresentS_1():
    '''
    Checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''

    test = epd.EpidemicSIR(30000, 1, 0, 0.1, 0.3, "no measures")
    test.Evolve()

    for i in range(1, test.day):
        assert (test.S_vector[i] <= test.S_vector[i-1])


def test_Evolve_DecresentS_2():
    '''
    Checks if the value of subsceptible population doesn't increase during
    the epidemic simulation using a very small numbers for gamma and beta.
    '''

    test = epd.EpidemicSIR(30000, 1, 0, 0.001, 0.003, "no measures")
    test.Evolve()

    for i in range(1, test.day):
        assert (test.S_vector[i] <= test.S_vector[i-1])


def test_Evolve_DecresentS_3():
    '''
    Checks if the value of subsceptible population doesn't increase during
    the epidemic simulation using a very small number of subscptible.
    '''

    test = epd.EpidemicSIR(100, 1, 0, 0.01, 0.03, "no measures")
    test.Evolve()

    for i in range(1, test.day):
        assert (test.S_vector[i] <= test.S_vector[i-1])


def test_Evolve_DecresentS_4():
    '''
    Checks if the value of subsceptible population doesn't increase during
    the epidemic simulation using a big numbers for gamma and beta.
    '''

    test = epd.EpidemicSIR(100000, 1, 0, 0.5, 0.6, "no measures")
    test.Evolve()

    for i in range(1, test.day):
        assert (test.S_vector[i] <= test.S_vector[i-1])


def test_Evolve_ZeroInfected():
    '''
    Checks if the value of subsecptible doesn't change if there are no
    infected population.
    '''

    test = epd.EpidemicSIR(1000, 0, 0, 0.2, 0.2, "no measures")
    test.Evolve()

    for i in range(test.day):
        assert (test.S_vector[i] == 1000 and test.I_vector[i]
                == 0 and test.R_vector[i] == 0)


def test_Evolve_SimulationTimeZero():
    '''
    Checks if the duration of the simulation is equal to 0 if the number of infected
    is equal to 0
    '''

    test = epd.EpidemicSIR(1000, 0, 0, 0.2, 0.2, "no measures")
    test.Evolve()

    assert (test.day-1 == 0)


def test_Evolve_SimulationTimeOne():
    '''
    Checks if the duration of the simulation is equal to 1 if the healing probability
    is equal to 1 and infection probability is equal to 0.
    '''

    test = epd.EpidemicSIR(1000, 10, 0, 1.0, 0.0, "no measures")
    test.Evolve()

    assert (test.day-1 == 1)


def test_Evolve_ZeroInfection():
    '''
    Checks if the values of subsceptible doesn't change if there are some
    infected population with 0.0% probability to infect. 
    '''

    test = epd.EpidemicSIR(1000, 10, 0, 0.2, 0.0, "no measures")
    test.Evolve()

    assert (test.S_vector[test.day-1] == 1000 and test.I_vector[test.day-1]
            == 0 and test.R_vector[test.day-1] == 10)


def test_Evolve_NoEpidemic():
    '''
    Checks if the values of subsceptible population remain unchanged if we have
    no infected people.
    '''

    test = epd.EpidemicSIR(1000, 0, 0, 0.5, 0.5, "strongly effective vaccine")
    test.Evolve()

    for i in range(test.day):
        assert (test.S_vector[i] == 1000 and test.I_vector[i]
                == 0 and test.R_vector[i] == 0)


def test_Evolve_NoVaccineNecessary_1():
    '''
    Checks the no activation of vaccine if light lockdown scenario is selected but
    the infected population doesn't reach a value equal to 10% of total population.
    '''

    test = epd.EpidemicSIR(10000, 10, 0, 0.05, 0.0, "light lockdown")
    v, gamma, beta = test.Vaccine(None, 0.05, 0.0)

    gamma = round(test.gamma, 5)
    beta = round(test.beta, 5)

    assert (gamma == 0.05 and beta == 0.0)


def test_Evolve_NoVaccineNecessary_2():
    '''
    Checks the no activation of vaccine if heavy lockdown scenario is selected but
    the infected population doesn't reach a value equal to 10% of total population.
    '''

    test = epd.EpidemicSIR(10000, 10, 0, 0.05, 0.0, "heavy lockdown")
    v, gamma, beta = test.Vaccine(None, 0.05, 0.0)

    gamma = round(test.gamma, 5)
    beta = round(test.beta, 5)

    assert (gamma == 0.05 and beta == 0.0)


def test_Evolve_NoVaccineNecessary_3():
    '''
    Checks the no activation of vaccine if weakly effective vaccine scenario is selected but
    the infected population doesn't reach a value equal to 10% of total population.
    '''

    test = epd.EpidemicSIR(10000, 10, 0, 0.05, 0.0, "weakly effective vaccine")
    v, gamma, beta = test.Vaccine(None, 0.05, 0.0)

    gamma = round(test.gamma, 5)
    beta = round(test.beta, 5)

    assert (gamma == 0.05 and beta == 0.0)


def test_Evolve_NoVaccineNecessary_4():
    '''
    Checks the no activation of vaccine if strongly effective vaccine scenario is selected but
    the infected population doesn't reach a value equal to 10% of total population.
    '''

    test = epd.EpidemicSIR(10000, 10, 0, 0.05, 0.0,
                           "strongly effective vaccine")
    v, gamma, beta = test.Vaccine(None, 0.05, 0.0)

    gamma = round(test.gamma, 5)
    beta = round(test.beta, 5)

    assert (gamma == 0.05 and beta == 0.0)


def test_NoVaccineDay():
    '''
    Checks the non activation of the vaccine/isolation day even if user has
    enabled the proper option but 10% of infected people is never reached.
    '''

    test = epd.EpidemicSIR(10000, 10, 0, 0.1, 0.1,
                           "strongly effective vaccine")
    test.Evolve()

    assert (test.triggerday == None)


def test_VaccineDay():  # giustoo, forse fare per ogni opzione
    '''
    Checks the activation of the vaccine/isolation day if user has
    enabled the proper option and 10% of people is infected.
    '''

    test = epd.EpidemicSIR(10000, 500, 0, 0.1, 1.0,
                           "strongly effective vaccine")
    test.Evolve()

    assert (test.triggerday == 2)
