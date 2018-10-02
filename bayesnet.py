'''
'' Assignment 5
'' Zeeshan Hyder Bhat
'' 12/15/2017
'''

import itertools


# Bayes Network class
class BayesNetwork:
    nodes = dict()
    node_names = []
    cpt_size = 0


    # adds new node to the network after reading from file
    def addNode(self,data):
        print("Reading Node: ")
        print(data['name'])
        newNode = dict()
        newNode['numparents'] = len(data['parents'])
        newNode['parents'] = data['parents']
        newNode['cpt'] = data['cpt']
        newNode['hcpt'] = data['hcpt']
        self.nodes[data['name']] = newNode
        self.node_names.append(data['name'])
        self.cpt_size += 2**newNode['numparents']
        
    
    # lists out all the nodes read from file
    def getNodeNames(self):
        return self.node_names

    # prints out total CPT of the network
    def totalCPT(self):
        return self.cpt_size
    
    # total multiplications done for the joint distribution
    def totalMultiplications(self):
        return len(self.node_names)*(2**len(self.node_names))

    # total additions done for the joint distribution
    def totalAdditions(self):
        total = 0
        for k,v in self.nodes.items():
            total += len(v['hcpt'])
        return total

    # calculate probability for each row in joint distribution table
    def getProbabilityFromTable(self,jd_table):
        '''
            First we go through each row and fetch the probability of each node given all other nodes, multiply them together
            and display the resulting probability row wise
        '''
        for jd_row in jd_table:
            pr = 1
            print(jd_row)
            for node in jd_row:
                if node[0] == 'n':
                    cpt_node = node[1:]
                else:
                    cpt_node = node

                parents = self.nodes[cpt_node]['parents']
                
                if(len(parents) > 0):
                    nots = map(lambda x:'n'+x,parents)
                    tp = parents+nots
                    given = list(filter(lambda x: x in jd_row, tp))
                else:
                    given = []

                if node[0] == 'n':
                    for probs in self.nodes[cpt_node]['hcpt']:
                        if set(probs['given']) == set(given):
                            pr *= probs['p']
                else:
                    for probs in self.nodes[cpt_node]['cpt']:
                        if set(probs['given']) == set(given):
                            pr *= probs['p']
                    
                
            print(pr)        

    def printJointDistribution(self):
        '''
        '' Print the whole distribution
        '' First we generate the truth table
        '''
        nodes = self.getNodeNames()
        k_map = list(itertools.product([0,1],repeat = len(nodes)))

        jd_table = []
        for i,k in enumerate(k_map):
            joint_dist_row = []
            for j,num in enumerate(k):
                char = nodes[j]
                if num == 1:
                    char = 'n'+char
                joint_dist_row.append(char)
            jd_table.append(joint_dist_row)
        '''
        '' and then calculate the probability for all the table
        '''
        self.getProbabilityFromTable(jd_table)




def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

'''
'' Creates the CPT for nodes after reading them
'''
def addToProTable(node,prob,parents=[]):
    cpt = []
    hcpt = []
    if len(parents) > 0:
        k_map = list(itertools.product([0,1],repeat = len(parents)))
        
        for i,k in enumerate(k_map):
            str = []
            for j,num in enumerate(k):
                char = parents[j]
                if num == 1:
                    char = 'n'+char
                str.append(char)
            
            cpt.append({
                'given': str,
                'p' : float(prob[i])
            })
            
            hcpt.append({
                'given': str,
                'p' : 1-float(prob[i])
            })
    else:
        cpt.append({
            'given': [],
            'p' : float(prob[0])
        })
        
        hcpt.append({
            'given': [],
            'p' : 1-float(prob[0])
        })
    return cpt,hcpt
    

# After reading each line from file, this function 
# process each line, reads them as a node and pushes on BayesNetwork
def processNode(node):
    node_data = dict()
    node_meta = node.split(' ')
    parent_probs = []
    node_data['name'] = node_meta[0]
    node_data['parents'] = []
    if node_meta[1] != 'NONE':
        head = 1
        while isFloat(node_meta[head]) == False:
            node_data['parents'].append(node_meta[head])
            head = head+1
        parent_probs = node_meta[head:]
        cpt,hcpt = addToProTable(node_data['name'],parent_probs,node_data['parents'])
    else:
        cpt,hcpt = addToProTable(node_data['name'],[node_meta[2]])
    node_data['cpt'] = cpt
    node_data['hcpt'] = hcpt
    return node_data

# main entry point for the program
def main():
    filename = raw_input("Enter filename:") 
    # read input file
    file = open(filename,'r')
    nodes = []
    bn = BayesNetwork()
    while True:
        line = file.readline().rstrip()
        if line == 'END':
            break
        node = processNode(line.rstrip())
        bn.addNode(node)
    jd_size = 2**len(bn.getNodeNames())
    cpt = bn.totalCPT()
    print("-----------------------------------------------")
    print("Bayes Network: ")
    print(filename)
    print("Number of lines in Joint Distribution:")
    print(jd_size)
    print("Number of CPT lines:")
    print(cpt)
    print("Compactness:")
    print(cpt/float(jd_size))
    print("Total Multiplications:")
    print(bn.totalMultiplications())
    print("Total Additions:")
    print(bn.totalAdditions())
    print("\n")
    
    # Print Joint Distribution
    bn.printJointDistribution()

# call the main function
main()