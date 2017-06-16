def calc(x):
    ver_var_Debetovaya = {0:0.1, 1:1, 2:0, 3:0, 6:0, 7:1}
    ver_var_Classic = {0:0.1, 1:1, 2:0, 3:0, 6:1, 7:1}
    ver_var_Bonusnaya = {0:0.3, 1:1, 2:0, 3:0, 6:1, 7:1}
    ver_var_CashBack = {0:0.1, 1:0, 2:1, 3:0, 6:0, 8:1}
    ver_var_Rubls = {0:0.1, 1:0, 2:1, 3:0, 6:1, 8:1}
    ver_var_Na_ur_litso = {0:0.1, 1:0, 2:0, 3:1, 6:0, 7:1}
    ver_var_Korporativnaya = {0:0.1, 1:0, 2:0, 3:1, 6:1, 7:1}
    
    for i in range(0,len(x)-1):
        for j in range(0,len(ver_var_Debetovaya)-1):
            if i==list(ver_var_Debetovaya.keys())[j]:
                Debetovaya = x[i]*list(ver_var_Debetovaya.values())[j]
        for k in range(0,len(ver_var_Classic)-1):
            if i==list(ver_var_Classic.keys())[k]:
                Classic = x[i]*list(ver_var_Classic())[k]
        for l in range(0,len(ver_var_Bonusnaya)-1):
            if i==list(ver_var_Bonusnaya.keys())[l]:
                Bonusnaya = x[i]*list(ver_var_Sams_S7.values())[l]
        for m in range(0,len(ver_var_CashBack)-1):
            if i==list(ver_var_CashBack.keys())[m]:
                CashBack = x[i]*list(ver_var_CashBack.values())[m]
        for n in range(0,len(ver_var_Rubls)-1):
            if i==list(ver_var_Rubls.keys())[n]:
                Rubls = x[i]*list(ver_var_Rubls.values())[n]
        for o in range(0,len(ver_var_Na_ur_litso)-1):
            if i==list(ver_var_Na_ur_litso.keys())[o]:
                Na_ur_litso = x[i]*list(ver_var_Na_ur_litso.values())[o]
        for p in range(0,len(ver_var_Korporativnaya)-1):
            if i==list(ver_var_Korporativnaya.keys())[p]:
                Korporativnaya = x[i]*list(ver_var_Korporativnaya.values())[p]
        
    y=[str(Debetovaya),str(Classic),str(Bonusnaya),str(CashBack),str(Rubls),str(Na_ur_litso),str(Korporativnaya)]
    return y
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
