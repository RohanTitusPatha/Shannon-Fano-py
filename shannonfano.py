import math

'''initialisation'''

class Node:
    def __init__(self):
        self.symbol = ''
        self.prob = 0.0
        self.arr = []
 
  
'''shanon main code part'''   
   
def shannon(l, h, p):
    if h == l  or l > h:
        return
    pack1 = sum(p[i].prob for i in range(l, h))
    pack2 = p[h].prob
    diff1 = abs(pack1 - pack2)
    k = h - 1
    while k < h:
        pack1 -= p[k].prob
        pack2 += p[k+1].prob
        diff2 = abs(pack1 - pack2)
        if diff2 >= diff1:
            break
        diff1 = diff2
        k -= 1

    for i in range(l, k + 1):
        p[i].arr.append(1)
    for i in range(k + 1, h + 1):
        p[i].arr.append(0)
    
    shannon(l, k, p)
    shannon(k + 1, h, p)
     
    
'''printing in order'''

codewords=[]   
def display(p):
    print("\nSymbol\tProbability\t\t\tCode")
    for node in p:
        print(f"{node.symbol}\t\t{node.prob}\t\t\t{''.join(map(str, node.arr))}")
        codewords.append(''.join(map(str, node.arr)))


'''calculating the frequencies of the letters'''

def calculate_letter_frequency(sentence):
    letter_frequency = {}
    for i in sentence:
        convert_lower = i.lower()
        if convert_lower in letter_frequency:
            letter_frequency[convert_lower] += 1
        else:
            letter_frequency[convert_lower] = 1
    return letter_frequency


'''sorting acc to frequencies'''

def sort_by_frequency_descending(letter_frequency):
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency


'''input part'''

input_sentence=input()
frequency = calculate_letter_frequency(input_sentence)
length = len(input_sentence)
temp=[]
probs=[]
symbs=[]
flag=0
frequency = sort_by_frequency_descending(frequency)
print("\nSorted Frequencies (Descending Order):")
for letter, freq in frequency:
    print(f"{letter}: {freq}") 
    temp.append(freq)
    symbs.append(letter)
    
for i in range(len(frequency)):
    flag = temp[i]/length
    probs.append(flag)
print(probs)


'''main function'''

if __name__ == '__main__':
    p = [Node() for _ in range(len(symbs))]
    symbols = symbs
    probabilities = probs
    
    for i in range(len(symbs)):
        p[i].symbol = symbols[i]
        p[i].prob = probabilities[i]    
        
    total = sum(i.prob for i in p)
    if total != 1:
        diff = 1 - total
        p[-1].prob += diff
    
    p.sort(key=lambda i: i.prob, reverse=True)
    for node in p:
        node.arr = []
    n= len(symbs) - 1
    shannon(0, n, p)
    display(p)
   
   
'''solutions'''

averagecw =0
entropy=0
variance=0
tp=0
for i in range(len(probs)):
    
    entropy -=  (probs[i]) * math.log((probs[i]),2)
    averagecw += (len(p[i].arr))*probs[i]
    tp += probs[i]*(((len(p[i].arr))-averagecw)**2)
variance = math.sqrt(tp)
effeciency = entropy / averagecw * 100
print("\nentropy:\t",entropy)
print("effeciency:\t",effeciency)
print("averagecw:\t",averagecw)
print("variance:\t",variance) 