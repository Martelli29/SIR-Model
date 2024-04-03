import input as inp

class EpidemicSIR:
    def __init__(self, t, S, I, R, gamma, beta):
        self.t = t  
        self.S = S  
        self.I = I  
        self.R = R  
        self.N = S + I + R  
        self.gamma = gamma  # healing probability
        self.beta = beta    # infection probability

        self.S_vector = []
        self.I_vector = []
        self.R_vector = []

    def Evolve(self):
        pass