import nengo
import nengo_viz
import numpy as np

tau, r = 0.01, 4

def feedback(x):    
    return [-tau*r*x[1]+1.01*x[0], tau*r*x[0]+1.01*x[1]]
def osc_shape(x):
    theta = np.arctan2(x[1], x[0])
    r = (2 - 2 * np.sin(theta)
         + np.sin(theta)*np.sqrt(np.abs(np.cos(theta)))
         / (np.sin(theta)+1.4))
    return -r*np.cos(theta), r*np.sin(theta)

with nengo.Network('Oscillator', seed=1) as model:
    stim = nengo.Node(0)
    oscillator = nengo.Ensemble(1000, dimensions=2)
    shape = nengo.Ensemble(100, dimensions=2, radius=4)
    nengo.Connection(stim, oscillator[0])
    nengo.Connection(stim, oscillator[1])
    nengo.Connection(oscillator, oscillator,
                     function=feedback, synapse=tau)
    nengo.Connection(oscillator, shape,
                     function=osc_shape, synapse=tau)

if __name__ == '__main__':
    nengo_viz.Viz(__file__).start()