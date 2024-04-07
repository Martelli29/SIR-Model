import matplotlib.pyplot as plt

def plot(S, I, R):
    '''
    This function takes as input three lists and uses the functionality of matplotlib
    to plot them in a graph.
    '''
    
    plt.plot(S, color="blue")
    plt.plot(I, color="red")
    plt.plot(R, color="black")

    plt.xlabel("Days")
    plt.ylabel("Population")
    
    plt.title("SIR model")
    plt.legend(["Subsceptible", "Infected", "Revomed"])
    
    plt.show()