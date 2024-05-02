import pytest
import input as inp
import epidemic_class as epd
from unittest.mock import patch


def test_Inspector_NegativeBeta():
    '''
    This test checks if a negative value of beta is given to Inspector(...), the
    function will show the proper ValueError with the correct string explanation.
    '''

    with patch('builtins.input', return_value='-2'):
        with pytest.raises(ValueError) as excinfo:
            inp.SetBeta()
    
    assert str(excinfo.value) == "Beta parameter must be between zero and one."


def test_Inspector_BetaGreaterOne():
    '''
    This test checks if a beta greater than 1 given to Inspector(...), the
    function will show the proper ValueError with the correct string explanation.
    '''
    
    with patch('builtins.input', return_value='2'):
        with pytest.raises(ValueError) as excinfo:
            inp.SetBeta()
    
    assert str(excinfo.value) == "Beta parameter must be between zero and one."    


def test_Inspector_NegativeGamma():
    '''
    This test checks if a negative value of gamma is given to Inspector(...), the
    function will show the proper ValueError with the correct string explanation.
    '''

    with patch('builtins.input', return_value=-2):
        with pytest.raises(ValueError) as excinfo:
            inp.SetGamma()
    
    assert str(excinfo.value) == "Gamma parameter must be between zero and one."


def test_Inspector_GammaGreaterOne():
    '''
    This test checks if a gamma greater than 1 is given to Inspector(...), the
    function will show the proper ValueError with the correct string explanation.
    '''
    
    with patch('builtins.input', return_value='2'):
        with pytest.raises(ValueError) as excinfo:
            inp.SetGamma()
    
    assert str(excinfo.value) == "Gamma parameter must be between zero and one."


def test_Inspector_ZeroPopulation():
    '''
    This test checks if an empty size of the population is given to Inspector(...), the
    function will show the proper ValueError with the correct string explanation.
    '''
    
    with patch('builtins.input', side_effect=['0', '0', '0']):
        with pytest.raises(ValueError) as excinfo:
            inp.SetSIR()
    
    assert str(excinfo.value) == "Population must be greater than zero!!!"


def test_Inspector_NegativeS():
    '''
    This test checks if a negative value of subsceptible (S) is given to Inspector(...), the
    function will show the proper ValueError with the correct string explanation.
    '''
    
    with patch('builtins.input', side_effect=['-10', '1', '0']):
        with pytest.raises(ValueError) as excinfo:
            inp.SetSIR()
  
    assert str(excinfo.value) == "We can't have neagtive number of subsceptible, infected or recovered people."


def test_Inspector_NegativeI():
    '''
    This test checks if a negative value of infected (I) is given to Inspector(...), the
    function will show the proper ValueError with the correct string explanation.
    '''
    
    with patch('builtins.input', side_effect=['10', '-10', '0']):
        with pytest.raises(ValueError) as excinfo:
            inp.SetSIR()
  
    assert str(excinfo.value) == "We can't have neagtive number of subsceptible, infected or recovered people."


def test_Inspector_NegativeR():
    '''
    This test checks if a negative value of recovered (R) is given to Inspector(...), the
    function will show the proper ValueError with the correct string explanation.
    '''
    
    with patch('builtins.input', side_effect=['10', '1', '-10']):
        with pytest.raises(ValueError) as excinfo:
            inp.SetSIR()
    
    assert str(excinfo.value) == "We can't have neagtive number of subsceptible, infected or recovered people."


def test_VaccineTriggerOff():
    '''
    This test checks if the user does not want to use vaccine/isolation scenarios,
    boolean value that represent the activation of the restriction measures is setted
    to False and tha variable scenario doesn't have a value.
    '''
    with patch('builtins.input', side_effect=['no measures']):
        VaccineTrigger,scenario=inp.SetVaccine()

    assert(VaccineTrigger == False and scenario == "no measures")

def test_VaccineTriggerOn():
    '''
    This test checks if the vaccine option is triggered on if the user put
    the proper functionality in the shell.
    '''
    
    with patch('builtins.input', side_effect=['light lockdown']):
        VaccineTrigger,scenario=inp.SetVaccine()

    assert(VaccineTrigger == True)


def test_Vaccine_Scenario1():
    '''
    This test checks if the correct scenario (in this case scenario 1) 
    is setted if the user put the proper functionality in the shell.
    '''

    with patch('builtins.input', side_effect=['light lockdown']):
        VaccineTrigger,scenario=inp.SetVaccine()

    assert(scenario == "light lockdown")

def test_Vaccine_Scenario2():
    '''
    This test checks if the correct scenario (in this case scenario 2) 
    is setted if the user put the proper functionality in the shell.
    '''

    with patch('builtins.input', side_effect=['heavy lockdown']):
        VaccineTrigger,scenario=inp.SetVaccine()

    assert(scenario == "heavy lockdown")


def test_Vaccine_Scenario3():   
    '''
    This test checks if the correct scenario (in this case scenario 3) 
    is setted if the user put the proper functionality in the shell.
    '''

    with patch('builtins.input', side_effect=['weakly effective vaccine']):
        VaccineTrigger,scenario=inp.SetVaccine()

    assert(scenario == "weakly effective vaccine")


def test_Vaccine_Scenario4():
    '''
    This test checks if the correct scenario (in this case scenario 4) 
    is setted if the user put the proper functionality in the shell.
    '''
        
    with patch('builtins.input', side_effect=['strongly effective vaccine']):
        VaccineTrigger,scenario=inp.SetVaccine()

    assert(scenario == "strongly effective vaccine")


def test_Evolve_ConservationOfN_1():
    '''
    This test checks if the value of the total population (N) is conserved during the
    epidemic evolution.
    '''

    test=epd.EpidemicSIR(30000, 1, 0, 0.1, 0.3)
    test.Evolve(False, 0)
    for i in range(test.t):
        assert(test.S_vector[i]+ test.I_vector[i]+ test.R_vector[i] == test.N)

def test_Evolve_ConservationOfN_2():
    '''
    This test checks if the value of the total population (N) is conserved during the
    epidemic evolution.
    '''

    test=epd.EpidemicSIR(3000000, 1, 0, 0.1, 0.3)
    test.Evolve(False, 0)
    for i in range(test.t):
        assert(test.S_vector[i]+ test.I_vector[i]+ test.R_vector[i] == test.N)


def test_Evolve_DecresentS_1():
    '''
    This test checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''

    test=epd.EpidemicSIR(30000, 1, 0, 0.1, 0.3)
    test.Evolve(False, 0)

    for i in range(1, test.t):
        assert(test.S_vector[i] <= test.S_vector[i-1])


def test_Evolve_DecresentS_2():
    '''
    This test checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''

    test=epd.EpidemicSIR(30000, 1, 0, 0.01, 0.03)
    test.Evolve(False, 0)

    for i in range(1, test.t):
        assert(test.S_vector[i] <= test.S_vector[i-1])


def test_Evolve_DecresentS_3():
    '''
    This test checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''

    test=epd.EpidemicSIR(100, 1, 0, 0.01, 0.03)
    test.Evolve(False, 0)

    for i in range(1, test.t):
        assert(test.S_vector[i] <= test.S_vector[i-1])


def test_Evolve_DecresentS_4():
    '''
    This test checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''

    test=epd.EpidemicSIR(100000, 1, 0, 0.5, 0.6)
    test.Evolve(False, 0)

    for i in range(1, test.t):
        assert(test.S_vector[i] <= test.S_vector[i-1])


def test_Evolve_ZeroInfected():
    '''
    This test checks if the value of subsecptible doesn't change if there are no
    infected population.
    '''

    test=epd.EpidemicSIR(1000, 0, 0, 0.2, 0.2)
    test.Evolve(False, 0)

    for i in range(test.t):
        assert(test.S_vector[i]==1000 and test.I_vector[i]==0 and test.R_vector[i]==0)


def test_Evolve_SimulationTime1():
    '''
    This test checks if the duration of the simulation is equal to 0 if the number of infected
    is equal to 0
    '''

    test=epd.EpidemicSIR(1000, 0, 0, 0.2, 0.2)
    test.Evolve(False, 0)

    assert(test.t-1==0)


def test_Evolve_SimulationTime2():
    '''
    This test checks if the duration of the simulation is equal to 1 if the heaing probability
    is equal to 1 and infection probability is equal to 0.
    '''

    test=epd.EpidemicSIR(1000, 10, 0, 1.0, 0.0)
    test.Evolve(False, 0)
    
    assert(test.t-1==1)


def test_Evolve_ZeroInfection():
    '''
    This test checks if the values of subsceptible doesn't change if there are some
    infected population with 0.0% probability to infect. 
    '''

    test=epd.EpidemicSIR(1000, 10, 0, 0.2, 0.0)
    test.Evolve(False, 0)

    assert(test.S_vector[test.t-1]==1000 and test.I_vector[test.t-1]==0 and test.R_vector[test.t-1]==10)


def test_Evolve_NoEpidemic():
    '''
    This test checks if the values of subsceptible population remain unchanged if we have
    no infected people.
    '''

    test=epd.EpidemicSIR(1000, 0, 0, 0.5, 0.5)
    test.Evolve(False, 0)

    assert(test.S_vector[test.t-1]==1000 and test.I_vector[test.t-1]==0 and test.R_vector[test.t-1]==0)


def test_Evolve_NoVaccineNecessary():
    '''
    This test checks the no activation of vaccine if the infected population never reach
    a value equal to 10% of total population.
    '''

    test=epd.EpidemicSIR(10000, 10, 0, 0.05, 0.0)
    test.Evolve(True, 4)

    test.gamma = round(test.gamma, 5)
    test.beta = round(test.beta, 5)

    assert(test.gamma == 0.05 and test.beta == 0.0)


def test_Evolve_Scenario1():
    '''
    This test checks if beta parameter (infection probability) is reduced by 20% due
    to the activation of scenario 1.
    '''

    test=epd.EpidemicSIR(10000, 1, 0, 0.01, 0.5)
    test.Evolve(True, "light lockdown")

    assert(test.beta==0.4)


def test_Evolve_Scenario2():
    '''
    This test checks if beta parameter (infection probability) is reduced by 70% due
    to the activation of scenario 2.
    '''

    test=epd.EpidemicSIR(10000, 1, 0, 0.01, 0.9)
    test.Evolve(True, "heavy lockdown")

    assert(test.beta==0.27)


def test_Evolve_Scenario3():
    '''
    This test checks if beta parameter (infection probability) is reduced by 20% and gamma
    parameter (healing probability) is increased by 50% due to the activation of scenario 3.
    '''

    test=epd.EpidemicSIR(10000, 1, 0, 0.1, 0.5)
    test.Evolve(True, "weakly effective vaccine")
    test.gamma = round(test.gamma, 5)

    assert(test.gamma == 0.15 and test.beta == 0.4)


def test_Evolve_Scenario4():
    '''
    This test checks if beta parameter (infection probability) is reduced by 60% and gamma
    parameter (healing probability) is increased by 90% due to the activation of scenario 4.
    '''

    test=epd.EpidemicSIR(10000, 1, 0, 0.1, 0.5)
    test.Evolve(True, "strongly effective vaccine")
    test.gamma = round(test.gamma, 5)
    test.beta = round(test.beta, 5)
    
    assert(test.gamma == 0.19 and test.beta == 0.2)


def test_NoVaccineDay():
    '''
    This test checks the non activation of the vaccine/isolation day even if user has
    enabled the proper option but 10% of infected people is never reached.
    '''

    test=epd.EpidemicSIR(10000, 10, 0, 0.1, 0.1)
    test.Evolve(True, 4)

    assert(test.triggerday == None)


def test_VaccineDay():
    '''
    This test checks the activation of the vaccine/isolation day if user has
    enabled the proper option and 10% of people is infected.
    '''
        
    test=epd.EpidemicSIR(10000, 500, 0, 0.1, 1.0)
    test.Evolve(True, "strongly effective vaccine")

    assert(test.triggerday == 2)