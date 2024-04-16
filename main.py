import input as inp
import epidemic_class as cl 
import plot as dr

if __name__=="__main__":
    
    gamma=inp.SetGamma()
    beta=inp.SetBeta()
    s,i,r = inp.SetSIR()
    bol, scenario = inp.SetVaccine()
    SIR=cl.EpidemicSIR(s, i, r, gamma, beta)
    SIR.Vaccine(scenario)
    SIR.Evolve(bol, scenario)
    
    dr.plot(SIR.S_vector, SIR.I_vector, SIR.R_vector, SIR.triggerday)
