import csv
import traceback
class minMaxNormalization:
    """
    Minmax normalization is a normalization strategy which linearly transforms x to y= (x-min)/(max-min), where min and max are the minimum and maximum values in X, where X is the set of observed values of x. So, the entire range of values of X from min to max are mapped to the range 0 to 1.
    For more infomation You may look at below given post on stack-overflow
    http://stats.stackexchange.com/a/70807
    :return:
    """
    def minMaxCalculator(self,dataset):
        """
        :param dataset: data set is expected to be 2D matrix
        :return: minMax ==> list of list, e.g. [[12, 435], [13, 545], [5, 13424], [34, 454], [5, 2343], [4, 343]]

        To run this individual function for testing use below given code
        minMaxNormalizationInstance = minMaxNormalization()
        minMaxNormalizationInstance.minMaxCalculator([[12,13,13424,34,2343,343],[435,545,5,454,5,4],[43,56,67,87,89,8]])
        """
        minMax = list()
        for columnNo in range(len(dataset[0])):
            """
            len(dataset[0]) is number of elements present in the row e.g. columns
            iterating by column
            e.g. this is the column  then, [[12,13,13424,34,2343,343],[435,545,5,454,5,4],[43,56,67,87,89,8]]
            """
            columnvalues = []
            for row in dataset:
                """
                going to each row for particular column
                """
                columnvalues.append(row[columnNo])
            """
            e.g. columnvalues [12, 435, 43] at the end
            """
            minimumInColumn = min(columnvalues)
            maximumInColumn = max(columnvalues)
            """
            this will be the min and max value for first column  12 435
            """
            minMax.append([minimumInColumn,maximumInColumn])
            """
            This will be in minMax list at the end of all iteration on all column
            where each sublist represent min and max value for that column respectively
            [[12, 435], [13, 545], [5, 13424], [34, 454], [5, 2343], [4, 343]]
            """
        return minMax

    def normalizeDatasetUsingMinmax(self,dataset,minMax):
        """
        Actual implementation of min max normalization where it accepts data set and minmax value for each column
        y= (x-min)/(max-min)
        :param dataset: dataset in 2d array
        :param minMax: [[12, 435], [13, 545], [5, 13424], [34, 454], [5, 2343], [4, 343]]
        :return: will return min max value e.g. [[0.0, 0.0, 1.0, 0.0, 1.0, 1.0], [1.0, 1.0, 0.0, 1.0, 0.0, 0.0], [0.07328605200945626, 0.08082706766917293, 0.004620314479469409, 0.1261904761904762, 0.03592814371257485, 0.011799410029498525]]

        This snippet of code can be tested using following code
        minMaxNormalizationInstance = minMaxNormalization()
        dataset = [[12, 13, 13424, 34, 2343, 343], [435, 545, 5, 454, 5, 4], [43, 56, 67, 87, 89, 8]]
        minmax = minMaxNormalizationInstance.minMaxCalculator(dataset)
        print minMaxNormalizationInstance.normalizeDatasetUsingMinmax(dataset, minmax)

        """
        for row in dataset:
            for eachColumnNo in range(len(row)):
                """
                where
                minMax[eachColumnNo][1] = max for the given column
                minMax[eachColumnNo][0] = min for the given column
                """
                row[eachColumnNo] = float((row[eachColumnNo]-minMax[eachColumnNo][0]))/float((minMax[eachColumnNo][1]-minMax[eachColumnNo][0]))
        return dataset

class loadData:
    def loadFromcsv(self,fileName):
        """
        load a file and conver to 2d python list and return it
        :param fileName: csv file name with absolute path

        Example file  - pima-indians-diabetes.data
        Test the script using following code
        loadDataInstance =  loadData()
        print loadDataInstance.loadFromcsv('pima-indians-diabetes.data')
        e.g. https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data
        :return: 2D arrat [list of [list]]
        e.g. [['6', '148', '72', '35', '0', '33.6', '0.627', '50', '1'], ['1', '85', '66',...]..[]...]
        """
        try:
            data = list(csv.reader(open(fileName)))
            return data
        except:
            return (traceback.print_exc())

    def convertDataToFloat(self,dataset):
        """
        loadFromcsv function returns data as list of list of  strings,
        It must be converted to floats for further processing
        code can be tested through below given snippet

        loadDataInstance = loadData()
        dataset = loadDataInstance.loadFromcsv('pima-indians-diabetes.data')
        print loadDataInstance.convertDataToFloat(dataset)

        :param dataset:
        :return: dataset in floats
        """
        for row in dataset:
            for i in range(len(row)):
                row[i] = float(row[i])
        return dataset

class splitToTrainTest:
    def basicSplitter(self,dataset):
        """
        Just take the dataset and split it in to 70% and 30% ration
        :param dataset:

        use following code to run this code snippet

        loadDataInstance = loadData()
        dataset = loadDataInstance.loadFromcsv('pima-indians-diabetes.data')
        dataset =  loadDataInstance.convertDataToFloat(dataset)
        splitToTrainTestInstance =  splitToTrainTest()


        :return: test and train 2d array
        """
        trainDataSize = int(len(dataset)*0.7)
        testDataSize = int(len(dataset) - len(dataset)*0.7)
        print ("Train data size : ",trainDataSize," | Test data size : ",testDataSize)
        train = dataset[:int(len(dataset)*0.7)]
        test = dataset[int(len(dataset) * 0.7):]
        return train, test

    def advanceSplitter(self,classDict):
        positiveClassSize = len(classDict[1.0])
        negativeClassSize = len(classDict[0.0])
        print "Total number of positive cases : ", positiveClassSize
        print "Total number of negative cases : ", negativeClassSize
        Xtrain = []
        Xtrain.extend(classDict[1.0][:int(positiveClassSize * 0.7)])
        Xtrain.extend(classDict[0.0][:int(negativeClassSize * 0.7)])

        Xtest = []
        Xtest.extend(classDict[1.0][int(positiveClassSize * 0.3):])
        Xtest.extend(classDict[0.0][int(negativeClassSize * 0.3):])

        Ytrain = []
        for i in range(0, int(positiveClassSize * 0.7)):
            Ytrain.append(1)
        for i in range(0, int(negativeClassSize * 0.7)):
            Ytrain.append(0)

        Ytest = []
        for i in range(int(positiveClassSize * 0.3), positiveClassSize):
            Ytest.append(1)
        for i in range(int(negativeClassSize * 0.3), negativeClassSize):
            Ytest.append(0)

        return  Xtrain, Xtest, Ytrain, Ytest


class functionalTesting():
    """
    for testing performance of classification
    """
    def createConfusionMatrix(self,actual, predicted, threshold):
        """
        will create confusion matrix for given set of actual and predicted array
        Sometime insted of 1 and 0, we have probabilistic value [any float between 1 and 0], so threshold is required
        :param actual: Array of Actual sample
        :param predicted: Array of predicted sample
        :param threshold:  Any number between 0-1
        :return:
        """
        fp = 0
        fn = 0
        tp = 0
        tn = 0
        for i in range(len(predicted)):
            # if  predicted value is greater than threshold, predicted value = 1 else predicted value = 0
            if predicted[i] > threshold:
                predicted[i] = 1
            else:
                predicted[i] = 0
        for no in range(0, len(predicted)):
            if predicted[no] == 1 and actual[no] == 1:
                tp += 1
            elif predicted[no] == 0 and actual[no] == 0:
                tn += 1
            elif predicted[no] == 1 and actual[no] == 0:
                fn += 1
            elif predicted[no] == 0 and actual[no] == 1:
                fp += 1
        # calculating accuracy
        ACC = float((tp + tn))/ float((fp + tp + tn + fn))
        # calculating f1 measure
        F1 = float(2*tp)/ float(2*tp + fp + fn)
        print "False Positive : ",fp,", False Negative : ", fn,", True Positive : ", tp,", " \
                                                "True Negative : ", tn,", Accuracy : ",ACC ,", F1 Score : ",F1
