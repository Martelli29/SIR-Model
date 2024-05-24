import config as cfg
import epidemic_class as cl
import plot as pl

if __name__ == "__main__":

    config = cfg.Configuration()
    
    SIR = cl.EpidemicSIR(config)
    SIR.Evolve()
    SIR.PrintResults()

    pl.plot(SIR.S_vector, SIR.I_vector, SIR.R_vector, SIR.vaccine_day)
