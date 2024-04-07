import pytest
import input as inp
import epidemic_class as epd

def test_Inspector_NegativeTime():
    '''
    This test checks if a negative value of time is given to Inspector(...), the function
    will raise the ValueError with the correct string explanation.
    '''
    
    with pytest.raises(ValueError) as excinfo:
        inp.Inspector(0.5, 0.5, -1, 100, 1, 0)
    
    assert str(excinfo.value) == "Simulation cannot take place with times less than or equal to zero."

def test_Inspector_NegativeBeta():
    '''
    This test checks if a negative value of beta is given to Inspector(...), the
    function will raise the ValueError with the correct string explanation.
    '''
    
    with pytest.raises(ValueError) as excinfo:
        inp.Inspector(0.5, -0.1, 1, 100, 1, 0)
    
    assert str(excinfo.value) == "Beta parameter must be between zero and one."
    
def test_Inspector_BetaGreaterOne():
    '''
    This test checks if a beta greater than 1 given to Inspector(...), the
    function will raise the ValueError with the correct string explanation.
    '''
    
    with pytest.raises(ValueError) as excinfo:
        inp.Inspector(0.5, -0.1, 1, 100, 1, 0)
    
    assert str(excinfo.value) == "Beta parameter must be between zero and one."    

def test_Inspector_NegativeGamma():
    '''
    This test checks if a negative value of gamma is given to Inspector(...), the
    function will raise the ValueError with the correct string explanation.
    '''
    
    with pytest.raises(ValueError) as excinfo:
        inp.Inspector(-0.5, 0.1, 1, 100, 1, 0)
    
    assert str(excinfo.value) == "Gamma parameter must be between zero and one."

def test_Inspector_GammaGreaterOne():
    '''
    This test checks if a gamma greater than 1 is given to Inspector(...), the
    function will raise the ValueError with the correct string explanation.
    '''
    
    with pytest.raises(ValueError) as excinfo:
        inp.Inspector(-0.5, 0.1, 1, 100, 1, 0)
    
    assert str(excinfo.value) == "Gamma parameter must be between zero and one."

def test_Inspector_ZeroPopulation():
    '''
    This test checks if an empty size of the population is given to Inspector(...), the
    function will raise the ValueError with the correct string explanation.
    '''
    
    with pytest.raises(ValueError) as excinfo:
        inp.Inspector(0.5, 0.1, 1, 0, 0, 0)
    
    assert str(excinfo.value) == "Population must be greater than zero!!!"

def test_Inspector_NegativeS():
    '''
    This test checks if a negative value of subsceptible (S) is given to Inspector(...), the
    function will raise the ValueError with the correct string explanation.
    '''
    
    with pytest.raises(ValueError) as excinfo:
        inp.Inspector(0.5, 0.1, 1, -100, 2, 1)
  
    assert str(excinfo.value) == "We can't have neagtive number of subsceptible, infected or recovered people."

def test_Inspector_NegativeI():
    '''
    This test checks if a negative value of infected (I) is given to Inspector(...), the
    function will raise the ValueError with the correct string explanation.
    '''
    
    with pytest.raises(ValueError) as excinfo:
        inp.Inspector(0.5, 0.1, 1, 100, -2, 1)
  
    assert str(excinfo.value) == "We can't have neagtive number of subsceptible, infected or recovered people."

def test_Inspector_NegativeR():
    '''
    This test checks if a negative value of recovered (R) is given to Inspector(...), the
    function will raise the ValueError with the correct string explanation.
    '''
    
    with pytest.raises(ValueError) as excinfo:
        inp.Inspector(0.5, 0.1, 1, 100, 2, -1)
    
    assert str(excinfo.value) == "We can't have neagtive number of subsceptible, infected or recovered people."

def test_Evolve_ConservationOfN1():
    '''
    This test checks if the value of the total population (N) is conserved during the
    epidemic evolution.
    '''

    test=epd.EpidemicSIR(300, 30000, 1, 0, 0.1, 0.3)
    test.Evolve()
    for i in range(300):
        assert(test.S_vector[i]+ test.I_vector[i]+ test.R_vector[i] == test.N)

def test_Evolve_ConservationOfN2():
    '''
    This test checks if the value of the total population (N) is conserved during the
    epidemic evolution.
    '''

    test=epd.EpidemicSIR(3000, 3000000, 1, 0, 0.1, 0.3)
    test.Evolve()
    for i in range(300):
        assert(test.S_vector[i]+ test.I_vector[i]+ test.R_vector[i] == test.N)

def test_Evolve_DecresentS1():
    '''
    This test checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''

    test=epd.EpidemicSIR(300, 30000, 1, 0, 0.1, 0.3)
    test.Evolve()

    for i in range(1, 300):
        assert(test.S_vector[i] <= test.S_vector[i-1])

def test_Evolve_DecresentS2():
    '''
    This test checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''

    test=epd.EpidemicSIR(300, 30000, 1, 0, 0.01, 0.03)
    test.Evolve()

    for i in range(1, 300):
        assert(test.S_vector[i] <= test.S_vector[i-1])

def test_Evolve_DecresentS3():
    '''
    This test checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''

    test=epd.EpidemicSIR(300, 100, 1, 0, 0.01, 0.03)
    test.Evolve()

    for i in range(1, 300):
        assert(test.S_vector[i] <= test.S_vector[i-1])

def test_Evolve_DecresentS4():
    '''
    This test checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''

    test=epd.EpidemicSIR(300, 100000, 1, 0, 0.5, 0.6)
    test.Evolve()

    for i in range(1, 300):
        assert(test.S_vector[i] <= test.S_vector[i-1])


def test_Evolve_ZeroInfected():
    '''
    This test checks if the value of subsecptible doesn't change if there are no
    infected population.
    '''

    test=epd.EpidemicSIR(100, 1000, 0, 0, 0.2, 0.2)
    test.Evolve()

    for i in range(100):
        assert(test.S_vector[i]==1000 and test.I_vector[i]==0 and test.R_vector[i]==0)

def test_Evolve_ZeroInfection():
    '''
    This test checks if the values of subsceptible doesn't change if there are some
    infected population with 0.0% probability to infect. 
    '''

    test=epd.EpidemicSIR(100, 1000, 10, 0, 0.2, 0.0)
    test.Evolve()

    assert(test.S_vector[99]==1000 and test.I_vector[99]==0 and test.R_vector[99]==10)

def test_Evolve_ZeroHealing():
    '''
    This test checks if the values of removed population remain unchanged during the simulation
    if healing probability is 0.0%.
    '''

    test=epd.EpidemicSIR(100, 1000, 10, 0, 0.0, 0.2)
    test.Evolve()

    assert(test.S_vector[99]==0 and test.I_vector[99]==1010 and test.R_vector[99]==0)

def test_Evolve_NoEpidemic():
    '''
    This test checks if the values of subsceptible population remain unchanged if we have
    no infected people.
    '''

    test=epd.EpidemicSIR(100, 1000, 0, 0, 0.5, 0.5)
    test.Evolve()

    assert(test.S_vector[99]==1000 and test.I_vector[99]==0 and test.R_vector[99]==0)