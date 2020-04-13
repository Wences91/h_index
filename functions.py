#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def h_index(df):
    df = df[df.Citations != 0]
    df = df.sort_values(by=['Citations'])
    df['h_index'] = range(1, len(df)+1)

    if(len(df) > 0):
        # itero sobre el número de publicaciones que tiene (el máximo de h-index)
        for cites in range(1, len(df)+1):
            if len(df[df.Citations >= cites]) >= cites:
                aux_h_index = cites
        res = aux_h_index
    else:
        res = 0
    return res

