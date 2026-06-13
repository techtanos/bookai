def neuron(inputs,weights):
    output = 0
    for i in range(len(inputs)):
        output += inputs[i] * weights[i]
    return output
drone_data = [2.5, 10]
learned_weights = [0.3, 0.5]
result = neuron(drone_data, learned_weights)
print(f"Neuron output: {result}")
new_weights = [0.8, 0.2]
result2 = neuron(drone_data, new_weights)
print(f"With different weights: {result2}")

