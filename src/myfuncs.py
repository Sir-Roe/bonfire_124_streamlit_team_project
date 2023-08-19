#search for records with values that contain val
def locator (df,col,val):
    a_list=[]
    for i in range(len(df[col])):
        if len(df[col].iloc[i].split(','))>1:
            if val in df[col].iloc[i].split(','):
                a_list.append(i)
        else:
            if val == df[col].iloc[i]:
                a_list.append(i)
    #return the list of locations to be used as a .iloc filter
    return a_list

#create a list of unique possible values
def pos_values(df,col):
    p_list=[]
    for i in range(len(df[col])):
        if len(df[col].iloc[i].split(','))>1:
                s=df[col].iloc[i].split(',')
                for j in s:
                    p_list.append(j)
        else:
            p_list.append(df[col].loc[i].split(',')[0])
           
    p_list=list(set(p_list))
    p_list.sort()
    return p_list