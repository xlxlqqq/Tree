import matplotlib.pyplot as plt

decisionNode = dict(boxstyle = "sawtooth", fc = "0.8")
leafNode = dict(boxstyle = "round4", fc = "0.8")
arrow_args = dict(arrowstyle = "<-")

#创建节点
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
#调用创建Node
    createPlot.ax1.annotate(nodeTxt, xy = parentPt, 
    xycoords = 'axes fraction', xytext = centerPt, 
    textcoords = 'axes fraction', va = "center", ha = "center",
    bbox = nodeType, arrowprops = arrow_args)

#创建文本框
# def createPlot():
#     fig = plt.figure(1, facecolor = 'white')
#     fig.clf()
#     createPlot.ax1 = plt.subplot(111, frameon = False)
#     plotNode('A decision node', (0.5,0.1), (0.1, 0.5), decisionNode)
#     plotNode('A leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
#     plt.show()

#获取leaf node的数目
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

#获取tree的层数/深度
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth: 
            maxDepth = thisDepth
    return maxDepth

#构建一个决策树
def retrieveTree(i):
    listOfTrees = [{'no surfacing':{0:'no', 1:{'flippers':\
        {0:'no',1:'yes'}}}},{'no surfacing':{0:'no',1:{'flippers':{0:\
            {'head':{0:'no',1:'yes'}},1:'no'}}}}]
    return listOfTrees[i]

#勾画文本
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[0] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)

#勾画决策树
def plotTree(myTree, parentPt, nodeTxt):
    #计算树的高，宽
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) \
        / 2.0 / plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    #减少y偏移
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.xOff + 1.0 / plotTree.totalD

#创建文本框
def createPlot(inTree):
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    axprops = dict(xticks = [], yticks = [])
    createPlot.ax1 = plt.subplot(111, frameon = False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()





