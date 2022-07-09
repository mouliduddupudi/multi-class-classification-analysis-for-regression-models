def muli_class(actual, predictions):
    """
    Confusion matrix
		The inputs should be numpy array
    """
    act = actual.copy() #numpy array
    pred = predictions.copy() #numpy array
    lb = min(min(act), min(pred))
    ub = max(max(act), max(pred))
    print(f"The min and max values are {lb} & {ub}")
    diff = float(input("Enter the difference between two values: "))
    r = np.arange(round(lb),round(ub), diff)
    label = np.arange(1,len(r)+1,1)


    for j in range(2):
        if j == 0:
            f = act
        else:
            f = pred
        for i in range(len(act)):
            for k in range(len(r)):
                if k == 0 and (f[i] <= r[k+1]):
                    f[i] = label[k]
                    break
                elif k > 0 and (k < (len(r)-1)) and (f[i] > r[k]) and (f[i]<=r[k+1]):
                    f[i] = label[k]
                    break
                elif k == (len(r)-1) and (f[i]> r[k]):
                    f[i] = label[k]
                    break


    x_labels = ['recall']
    y_labels = ['precision']
    for i in range(2):
        if i == 0:
            lol = x_labels
        else:
            lol = y_labels
        for k in range(len(r)):
            if k == 0:
                lol.insert(k,str(r[k+1]))
            if k >0 and (k < (len(r)-1)):
                lol.insert(k,str(r[k])+'-'+str(r[k+1]))
            if k == len(r)-1:
                lol.insert(k,str(r[k]))


    from sklearn.metrics import confusion_matrix
    import matplotlib.pyplot as plt
    import seaborn as sns

    cm = confusion_matrix(act, pred)
    cmn = cm / cm.astype(np.float).sum(axis = 0)
    recall = np.diag(cmn) / np.sum(cmn, axis = 1)
    precision = np.diag(cmn) / np.sum(cmn, axis = 0)
    cm_extended = np.append(cmn, [precision], axis=0)
    recall = recall.reshape((-1,1))
    z = np.zeros((1,1))
    recall = np.append(recall, z, axis=0)
    cm_extended = np.append(cm_extended, recall, axis=1)

    # Normalise
    fig, ax = plt.subplots(figsize=(10,10))
    sns.heatmap(cm_extended, annot=True, fmt='.2f', xticklabels=x_labels, yticklabels=y_labels)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.show(block=False)
