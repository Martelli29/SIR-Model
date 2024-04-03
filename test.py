import pytest
import input as inp

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

def test_Inspector_NegativeGamma():
    '''
    This test checks if a negative value of gamma is given to Inspector(...), the
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
