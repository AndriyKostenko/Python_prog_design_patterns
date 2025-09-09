# Implementation of the Composite design pattern for neural networks.
# This allows treating individual neurons and layers of neurons uniformly.

from abc import ABC
from collections.abc import Iterable

# Abstract base class for connectable objects, implementing Iterable for uniform iteration.
class Connectable(Iterable, ABC):
    # Connects this object to another, establishing inputs and outputs between all pairs.
    def connect_to(self, other):
        if self == other:
            return
        
        for s in self:
            for o in other:
                s.outputs.append(0)
                o.inputs.append(s)
    

# Represents a single neuron with inputs and outputs.
class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []
        
    def __str__(self):
        return f"{self.name}, "\
            f"{len(self.inputs)} inputs, " \
            f"{len(self.outputs)} outputs"
            
    # Makes the neuron iterable, yielding itself for uniform handling.
    def __iter__(self):
        yield self
            
        

        
# Represents a layer of neurons, inheriting from list and Connectable.
class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))
            
    def __str__(self):
        return f"{self.name} with {len(self)} neurons"
    

# Main section to demonstrate the composite pattern.
if __name__ == "__main__":
    neuron1 = Neuron('n1')
    neuron2 = Neuron("n2")
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 4)
    
    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    
    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)