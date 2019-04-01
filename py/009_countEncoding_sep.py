#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:07:16 2019

@author: Kazuki
"""

import numpy as np
import pandas as pd
from tqdm import tqdm
import utils

PREF = 'f009'


def fe(df, name):
    
    feature = pd.DataFrame(index=df.index)
    
    for c in tqdm(df.columns):
        di = df[c].value_counts().to_dict()
        feature[c] = df[c].map(di)
    
    for i in [3,2,1]:
        for c in tqdm(df.columns):
            di = df[c].round(i).value_counts().to_dict()
            feature[f'{PREF}_{c}_r{i}'] = df[c].round(i).map(di)
    
    feature.to_pickle(f'../data/{name}_{PREF}.pkl')
    
    return


# =============================================================================
# main
# =============================================================================
if __name__ == "__main__":
    utils.start(__file__)
    
    tr = utils.load_train().drop(['ID_code', 'target'], axis=1)
    te = utils.load_test().drop(['ID_code'], axis=1)
    
    fe(tr, 'train')
    fe(te, 'test')
    
    
    utils.end(__file__)


