import pytest
import input as inp

def test_Inspector_NegativeTime():
  with pytest.raises(ValueError) as excinfo:
    inp.Inspector(0.5, 0.5, -1, 100, 1, 0)
  assert str(excinfo.value) == "Simulation cannot take place with times less than or equal to zero."

def test_Inspector_NegativeBeta():
  with pytest.raises(ValueError) as excinfo:
    inp.Inspector(0.5, -0.1, 1, 100, 1, 0)
  assert str(excinfo.value) == "Beta parameter must be between zero and one."

def test_Inspector_NegativeGamma():
  with pytest.raises(ValueError) as excinfo:
    inp.Inspector(-0.5, 0.1, 1, 100, 1, 0)
  assert str(excinfo.value) == "Gamma parameter must be between zero and one."

def test_Inspector_ZeroPopulation():
  with pytest.raises(ValueError) as excinfo:
    inp.Inspector(0.5, 0.1, 1, 0, 0, 0)
  assert str(excinfo.value) == "Population must be greater than zero!!!"

def test_Inspector_NegativeS():
  with pytest.raises(ValueError) as excinfo:
    inp.Inspector(0.5, 0.1, 1, -100, 2, 1)
  assert str(excinfo.value) == "We can't have neagtive number of subsceptible, infected or recovered people."

def test_Inspector_NegativeI():
  with pytest.raises(ValueError) as excinfo:
    inp.Inspector(0.5, 0.1, 1, 100, -2, 1)
  assert str(excinfo.value) == "We can't have neagtive number of subsceptible, infected or recovered people."

def test_Inspector_NegativeR():
  with pytest.raises(ValueError) as excinfo:
    inp.Inspector(0.5, 0.1, 1, 100, 2, -1)
  assert str(excinfo.value) == "We can't have neagtive number of subsceptible, infected or recovered people."
