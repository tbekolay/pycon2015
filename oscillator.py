
import nengo
import numpy as np

model = nengo.Network('Oscillator', seed=1)

tau = 0.01
r = 4

def feedback(x):    
    return [-tau*r*x[1]+x[0], tau*r*x[0]+x[1]]

def osc_shape(x):
    theta = np.arctan2(x[1], x[0])
    r = 2 - 2 * np.sin(theta) + np.sin(theta)*np.sqrt(np.abs(np.cos(theta)))/(np.sin(theta)+1.4)
    return -r*np.cos(theta), r*np.sin(theta)

with model:
    stim = nengo.Node(lambda t: [.5,.5] if t<.02 else [0,0])    
    oscillator = nengo.Ensemble(1000, dimensions=2)
    shape = nengo.Ensemble(100, dimensions=2, radius=4)
    
    nengo.Connection(stim, oscillator)
    nengo.Connection(oscillator, oscillator, function=feedback, synapse=tau)
    nengo.Connection(oscillator, shape, function=osc_shape, synapse=tau)