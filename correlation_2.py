import pandas as pd
import pickle
import networkx as nx

#Import dict serially from the pickle
with open('readings.pickle', 'rb') as f: 
    dictCount = pickle.load(f)
    alcDictList = pickle.load(f)
    conDictList = pickle.load(f)
    readingsDataframeList = pickle.load(f)
                
posCorrPairsList = []
negCorrPairsList = []
#__________________higher correlation pairs__________________

def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_correlations(df, n=5):
    au_corr = df.corr().unstack()
    labels_to_drop = get_redundant_pairs(df)
    #reset index makes all pairs printable or some pairs are printed partially
    au_corr_pos = au_corr.drop(labels_to_drop).sort_values(ascending=False).reset_index()
    au_corr_neg = au_corr.drop(labels_to_drop).sort_values().reset_index()
    return au_corr_pos[0:n], au_corr_neg[0:n]

print("Top Correlation pairs:")
pairCount = 10

for dataframe in readingsDataframeList:
    posCorrPairs, negCorrPairs = get_top_correlations(dataframe, pairCount)
    posCorrPairsList.append(posCorrPairs)
    negCorrPairsList.append(negCorrPairs)
    #print('Positive Correlation pairs:',posCorrPairs,'Negative Correlation pairs:',negCorrPairs)

# this concats the 2 supplementary dfs row-wise into a single df
final_df = pd.concat(posCorrPairsList, ignore_index=True)
    
G = nx.from_pandas_dataframe(final_df,'level_0', 'level_1',True )

labeldict = {}
for nodes, u in G.nodes(data=True):
    labeldict[nodes]=nodes
nx.draw_networkx(G, labels=labeldict,with_labels=True)