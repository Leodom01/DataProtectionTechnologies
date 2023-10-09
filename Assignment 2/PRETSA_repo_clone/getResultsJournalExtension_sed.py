import os
import sys
import pandas as pd
from calculateSEDBetweenEventLogs import get_sed_between_logs

dirPath = sys.argv[1]
dataset = sys.argv[2]
resultFilePath = os.path.join(dirPath, dataset + "_sed_results.csv")

df = pd.DataFrame()

filePathOriginalLog = os.path.join(dirPath, dataset + "_dataset.csv")
print(filePathOriginalLog)
event_log_original = pd.read_csv(filePathOriginalLog, delimiter=";")
distanceMatrix = dict()

for k in (4,8,16,32,64):
    for t in (1.0,2.0,3.0,4.0,5.0):
        for algorithm in ("pretsa","heuristic_pretsa","pretsa_star"):
            filePathAlgoLog = os.path.join(dirPath, dataset + "_dataset_t" + str(t) + "_k" + str(k) + "_" + algorithm + ".csv")
            data = dict()
            if os.path.exists(filePathAlgoLog):
                data["sed"] = \
                     get_sed_between_logs(event_log_original,filePathAlgoLog,distanceMatrix)
            else:
                data["sed"] = -1
            data["k"] = k
            data["t"] = t
            data["algorithm"] = algorithm
            data["dataset"] = dataset
            df = df.append(data, ignore_index=True)
df.to_csv(resultFilePath)