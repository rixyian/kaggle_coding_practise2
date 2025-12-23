import pandas as pd

'''df1 = pd.read_csv("orders.csv") #`.read_csv` is what pd uses for csv files
print(df1)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Country': ['USA', 'Canada', 'UK']
}

df2 = pd.DataFrame(data) #`.dataframe` is what pd uses for dictionaries
print(data)
print(df2)
print(df1)'''

#-----------looking into NN via numpy via youtube Sentdex tutorial series

inputs = [1, 2, 3, 2.5]

'''weights_seen_by_node1 = [0.2,   0.8,    -0.5,   1]
weights_seen_by_node2 = [0.5,   -0.91,  0.26,   -0.5]
weights_seen_by_node3 = [-0.26, -0.27,  0.17,   0.87]'''

weights_seen_by_nodes = [[0.2,   0.8,    -0.5,   1],
                         [0.5,   -0.91,  0.26,   -0.5],
                         [-0.26, -0.27,  0.17,   0.87]]
bias_on_nodes = [2, 3, 0.5]
'''bias_on_node1 = 2
bias_on_node2 = 3
bias_on_node3 = 0.5'''
layer_outputs = [] # list where current layer's output is stored
'''zip() combines 2+ lists, strings, dictionaries, etc into single array,
where each element in the array is a pair/list of the elements that shared
the same index in the original arrays'''
'''for n_weights, n_bias in zip(weights_seen_by_nodes, bias_on_nodes):
    n_output = 0 #initialise given nwurone (n)'s output
    for n_input, weight in zip(inputs, n_weights):
        n_output += n_input
    n_output += n_bias'''
what_zip_does = zip(weights_seen_by_nodes, bias_on_nodes)
print(weights_seen_by_nodes)
print(bias_on_nodes)
print(list(what_zip_does))

'''output = [inputs[0]*weights_seen_by_node1[0] + inputs[1]*weights_seen_by_node1[1] + inputs[2]*weights_seen_by_node1[2] + inputs[3]*weights_seen_by_node1[3] + bias_on_node1,
          inputs[0]*weights_seen_by_node2[0] + inputs[1]*weights_seen_by_node2[1] + inputs[2]*weights_seen_by_node2[2] + inputs[3]*weights_seen_by_node2[3] + bias_on_node2,
          inputs[0]*weights_seen_by_node3[0] + inputs[1]*weights_seen_by_node3[1] + inputs[2]*weights_seen_by_node3[2] + inputs[3]*weights_seen_by_node3[3] + bias_on_node3]'''

#print(output)

#for x in inputs