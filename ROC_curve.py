import matplotlib.pyplot as plt
from sklearn.metrics import  roc_curve, auc

def ROCCurve(reg, X, y):
    y_pred_proba = reg.predict_proba(X=X)[:,1]
    [fpr, tpr, thr] = roc_curve(y, y_pred_proba)
    auc (fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, color='coral', label = 'ROC Curve with Area Under Curve ='+str(auc (fpr, tpr)))
    plt.xlabel('False positive Rate (1 - specificity)')
    plt.ylabel('True Positive Rate ')
    plt.legend(loc='lower right')
    plt.savefig("./static/roccurve.jpg")
    # plt.show()