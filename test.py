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

def test_Evolve_ConservationOfN():
    '''
    This test checks if the value of the total population (N) is conserved during the
    epidemic evolution.
    '''

    epidemictest=epd.EpidemicSIR(300, 30000, 1, 0, 0.1, 0.3)
    epidemictest.Evolve()
    for i in range(300):
        assert(epidemictest.S_vector[i]+ epidemictest.I_vector[i]+ epidemictest.R_vector[i] == epidemictest.N)

def test_Evolve_DecresentS():
    '''
    This test checks if the value of subsceptible population doesn't increase during
    the epidemic simulation.
    '''
    epidemictest=epd.EpidemicSIR(300, 30000, 1, 0, 0.1, 0.3)
    epidemictest.Evolve()

    for i in range(1, 300):
        assert(epidemictest.S_vector[i] <= epidemictest.S_vector[i-1])
