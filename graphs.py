# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns;
sns.set()
import pandas as pd


## Execution Times all Network Structures for the various Algorithms ###################################################
########################################################################################################################

def execution_time_all_NetworkStructures_for_Approximation_LINE():
    y1 = [0.00012,0.00012,0.00013,0.00034,0.0012,0.0221,0.0387,0.0977,0.444,1.993]
    y2 = [0.000131,0.00017,0.00015,0.00036,0.00110,0.0207,0.0342,0.0913,0.3236,1.312]
    y3 = [0.000121,0.000162,0.000175,  0.000436,0.00132 ,0.0227, 0.0438,0.0106,0.406, 1.87 ]
    y4 = [0,       0,       0,         0.00046, 0.0013,  0.0216, 0.0379,0.1936,1.3412,9.074 ]
    y5 = [0.00013,0.00014,0.00022,0.00051,0.0029,0.0243,0.05640,0.1614,0.5105,2.4698]
    y6 =[0.00013,0.00015,0.00015,0.0005,0.0019,0.0213, 0.0413, 0.122,0.468,4.192]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Balanced Tree", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Star", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Binomial", color="dimgray")
    plt.plot(x, y4, "--", label="Erdo-Renyi", color="peru")
    plt.plot(x, y5, "-p", label="Watts-Strogatz", color="powderblue")
    plt.plot(x, y6, "-.", label="Barabasi-Albert", color="silver")
    plt.legend(loc="upper left")

    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title("Approximation", fontsize=18)
    plt.ylabel("Execution time (seconds)", fontsize=18)
    plt.xlabel("Number of Vertices", fontsize=18)
    plt.legend(fontsize=15)
    plt.yscale('log')
    plt.tight_layout()
    plt.show()
    #plt.savefig("approximation_SC.pdf", dpi=300)


def execution_time_all_NetworkStructures_for_Greedy_LINE():
    y1 = [0.00014,0.00014,0.00021,0.00080,0.0015,0.0223,0.04617,0.113,0.4588,1.96]
    y2 = [0.000111,0.00011,0.00023,0.00045,0.00143,0.0190,0.03680,0.0900,0.3381,1.4089]
    y3 = [0.000130,0.000161,0.000286,0.000623,0.00182,0.0204,0.0412,0.102,0.441,1.836]
    y4 = [0,0,0,0.00053,0.0019,0.0288,0.0736,0.3496,2.479,22.3394]
    y5 = [0.00011,0.00016,0.00029,0.0007,0.0022,0.0283,0.0504,0.162,0.5051,2.368]
    y6 = [0.00011,0.00018,0.0003,0.0007,0.0022,0.0247,0.0509,0.142,0.509,2.407]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Balanced Tree", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Star", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Binomial", color="dimgray")
    plt.plot(x, y4, "--", label="Erdo-Renyi", color="peru")
    plt.plot(x, y5, "-p", label="Watts-Strogatz", color="powderblue")
    plt.plot(x, y6, "-.", label="Barabasi-Albert", color="silver")
    plt.legend(loc="upper left")

    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title("Greedy", fontsize=18)
    plt.ylabel("Execution time (seconds)", fontsize=18)
    plt.xlabel("Number of Vertices", fontsize=18)
    plt.legend(fontsize=15)
    plt.yscale('log')
    plt.tight_layout()
    plt.show()
    #plt.savefig("greedy_SC.pdf", dpi=300)


def execution_time_all_NetworkStructures_for_Genetic_LINE():
    y1 = [0.0176,0.0176,0.03386,0.0940,0.3064,0.9414,3.997,16.495,76.28,310.96]
    y2 = [0.00921,0.0204,0.0476,0.1268,0.4633,1.5824,7.015,22.812,107.366,443.81]
    y3 = [0.0096,0.0174,0.0313,2.61,0.6649,0.585,2.1467,8.377,36.002,147.58]
    y4 = [0,0,0,0.0842,0.145,0.3792,1.116,3.635,16.013,56.665]
    y5 = [0.0106,0.0168,0.0308,0.05177, 0.1502,0.4967,1.399,5.2896,25.899,110.31]
    y6 = [0.0117,0.028,0.0549,0.128,0.388, 1.366,7.533,22.392,87.12,368.45]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Balanced Tree", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Star", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Binomial", color="dimgray")
    plt.plot(x, y4, "--", label="Erdo-Renyi", color="peru")
    plt.plot(x, y5, "-p", label="Watts-Strogatz", color="powderblue")
    plt.plot(x, y6, "-.", label="Barabasi-Albert", color="silver")
    plt.legend(loc="upper left")
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title("Genetic", fontsize=18)
    plt.ylabel("Execution time (seconds)", fontsize=18)
    plt.xlabel("Number of Vertices", fontsize=18)
    plt.legend(fontsize=15)
    plt.yscale('log')
    plt.tight_layout()
    plt.show()



########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


## Cost Function all Network Structures for the various Algorithms #####################################################
########################################################################################################################
def costfunction_all_NetworkStructures_for_Approximation():
    # Balanced Tree -> r = 2 -- h = increased by 1 in every run, starts with 1
    # Erdo Renyi -> p=0.2
    # Watts - Strogatz -> k=2
    # Barabasi-Albert -> m=1

    sns.set_style("ticks")

    data = [["2",     0 ,        2.0,2,0,2.0,2.0],
            ["4",     2.16,      125.04,4,0,4.0,4.0 ],
            ["8",     250.083,   372.097,8,0,8.0,129.68],
            ["16",    379.86,    372.097,8,259.76,16.0,504.69 ],
            ["32",    886.69,    2607.007,32,519.52,32.0,1264.73 ],
            ["64",    1903.46,   5630.31,64,307.76,64.0,3752.51 ],
            ["128",   4433.25,   5630.31,128,1162.52,128.0,6217.07 ],
            ["256",   7342.22,   24003.90,256,6552.64,256.0,12096.63 ],
            ["512",   17542.49 , 53895.35,512,8951.86,512.0,25169.55],
            ["1024",   56812.17, 168392.52,1024,68618.70,1024.0,81269.18 ],
            ]
    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'], width = 0.6)
    plt.xticks(rotation=0, fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Approximation", fontsize=20)
    plt.ylabel("Cost Function", fontsize=20)
    plt.xlabel("Number of Vertices", fontsize=20)
    plt.legend(fontsize=16)
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def costfunction_all_NetworkStructures_for_Greedy():
    sns.set_style("ticks")

    data = [["2",124.04,1.161,1.16,0,1.161,1.16 ],
            ["4",124.04,246.92,125.04,0,125.52,125.04 ],
            ["8",371.28,493.97,250.73,0,252.75, 372.65],
            ["16",745.11,1235.35,382.19,388.85,747.28,748.45 ],
            ["32",1746.77,2728.88,1500.48,1158.90,1388.81,1753.92 ],
            ["64",3269.75,5752.19,3217.71,1708.70,2821.53, 4732.42 ],
            ["128",8583.57,12639.10,6510.32,5041.98,5147.98,8244.56 ],
            ["256",13074.54,24125.78,12099.31,23343.71,11187.54,16346.34 ],
            ["512", 36131.69,54017.23,27427.64,110230.25,27571.52,36592.49],
            ["1024",98694.95,168556.29,84872.029,440389.58,109849.121,116151.27 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'], width = 0.6)

    plt.xticks(rotation=0, fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Greedy", fontsize=20)
    plt.ylabel("Cost Function", fontsize=20)
    plt.xlabel("Number of Vertices", fontsize=20)
    plt.legend(fontsize=16)

    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def costfunction_all_NetworkStructures_for_Genetic():
    sns.set_style("ticks")

    data = [["2",124.04,1.161,1.16,0,1.161,1.16 ],
            ["4",124.04,246.92,125.04,0,3.3233,125.04 ],
            ["8",249.40,493.97,250.73,0,129.09,372.65 ],
            ["16",624.23,1235.35,382.19,147.86,148.84,748.45 ],
            ["32",1506.15,2728.88,1503.81,1086.42,1273.89, 1753.92],
            ["64",3400.336,5752.19,3623.29,3498.15,2514.96,4734.80 ],
            ["128",8012.42,12639.10,7171.00,23480.76,6212.21,8393.66 ],
            ["256",15039.79,24125.78,14766.39,229235.27,14206.98,17062.14 ],
            ["512",35542.64,54017.23,34354.79,1942119.08,35845.13,39449.045 ],
            ["1024",114932.21,168556.29,108433.52,16359885.61,149304.38,124501.55 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'], width = 0.6)
    plt.xticks(rotation=0, fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Genetic", fontsize=20)
    plt.ylabel("Cost Function", fontsize=20)
    plt.xlabel("Number of Vertices", fontsize=20)
    plt.legend(fontsize=16)
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def costfunction_all_NetworkStructures_for_ILP():
    sns.set_style("ticks")

    data = [["2", 124.04,124.04,1.161, 0,1.161,1.161,],
            ["4", 124.04,246.92,125.04,0,124.84,125.04],
            ["8", 371.287,493.97,250.73,0,494.79,372.65],
            ["16", 745.73,1235.35,382.19,516.82,632.51,870.33],
            ["32", 1745.06,2728.88,1503.81,1706.56,1712.23,1756.54],
            ["64", 3770.035,5752.19,3371.40,0,0,4854.30],
            ["128",8527.22 ,12639.10,6510.04,0,0,8280.75],
            ["256", 15417.41,24125.78,12099.31,0,0,16260.24],
            ["512", 0,54017.23,27427.64,0,0,36950.95],
            ["1024",0 ,168556.29,84872.03,0,0,117625.16],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'],
            width=0.6)
    plt.xticks(rotation=0, fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("ILP", fontsize=20)
    plt.ylabel("Cost Function", fontsize=20)
    plt.xlabel("Number of Vertices", fontsize=20)
    plt.legend(fontsize=16)
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


## NumberofNodesinVC all Network Structures for the various Algorithms #################################################
########################################################################################################################
def NumberofNodesinVC_all_NetworkStructures_for_Approximation():
    # Balanced Tree -> r = 2 -- h = increased by 1 in every run, starts with 1
    # Erdo Renyi -> p=0.2
    # Watts - Strogatz -> k=2
    # Barabasi-Albert -> m=1

    sns.set_style("ticks")

    data = [["2",2,2,2,0,2,2 ],
            ["4",2,2,4,0,4,4 ],
            ["8",4,2,8,0,8,6 ],
            ["16",10,2,8,14,16,8 ],
            ["32",20,2,32,28,32,16 ],
            ["64",42,2,64,62,64,28 ],
            ["128",84,2,128,124,128,60 ],
            ["256",170,2,256,250,256,126 ],
            ["512",340,2,512,510,512,272 ],
            ["1024",682,2,1024,1020,1024,534 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'], width=0.6)
    plt.xticks(rotation=0, fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Approximation", fontsize=20)
    plt.ylabel("VC Set", fontsize=20)
    plt.xlabel("Number of Vertices", fontsize=20)
    plt.legend(fontsize=16)
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def NumberofNodesinVC_all_NetworkStructures_for_Greedy():
    sns.set_style("ticks")

    data = [["2",1,1,1,0,1,1 ],
            ["4",1,1,1,0,2,2 ],
            ["8",2,1,4,0,4,3 ],
            ["16",6,1,4,9,10,6 ],
            ["32",10,1,8,21,18,10 ],
            ["64",26,1,32,48,35,18 ],
            ["128",42,1,64,109,72,37 ],
            ["256",106,1,128,234,154,80 ],
            ["512",170,1,256,486,290,163 ],
            ["1024",426,1,512,998,580,321 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'], width=0.6)
    plt.xticks(rotation=0, fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Greedy", fontsize=20)
    plt.ylabel("VC Set", fontsize=20)
    plt.xlabel("Number of Vertices", fontsize=20)
    plt.legend(fontsize=16)
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def NumberofNodesinVC_all_NetworkStructures_for_Genetic():
    sns.set_style("ticks")

    data = [["2", 1,1,1,0,1,1],
            ["4",1,1,2,0,3,2],
            ["8", 3,1,4,0,6,3],
            ["16", 8,1,8,11,12,6],
            ["32", 16,1,8,25,21,10],
            ["64", 36,1,32,55,41,19],
            ["128", 69,1,64,114,81,47],
            ["256", 138,1,128,239,330,99],
            ["512", 285,1,256,490,330,217],
            ["1024", 532,1,512,999,659,433],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'], width=0.6)
    plt.xticks(rotation=0, fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Genetic", fontsize=20)
    plt.ylabel("VC Set", fontsize=20)
    plt.xlabel("Number of Vertices", fontsize=20)
    plt.legend(fontsize=16)
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def NumberofNodesinVC_all_NetworkStructures_for_ILP():
    sns.set_style("ticks")

    data = [["2", 1, 1, 1, 0, 1, 1],
            ["4", 1,1,2,0,1,2],
            ["8", 2,1,4,0,2,3],
            ["16", 5,1,8,3,5,5],
            ["32", 10,1,16,6,11,9],
            ["64", 20,1,32,0,0,17],
            ["128", 38,1,64,0,0,34],
            ["256", 81,1,128,0,0,78],
            ["512", 0,1,256,0,0,158],
            ["1024", 0,1,512,0,0,312],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'],
            width=0.6)
    plt.xticks(rotation=0, fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("ILP", fontsize=20)
    plt.ylabel("VC Set", fontsize=20)
    plt.xlabel("Number of Vertices", fontsize=20)
    plt.legend(fontsize=16)
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################


if __name__ == '__main__':

    ## Execution Times all Network Structures for the various Algorithms ###################################################
    execution_time_all_NetworkStructures_for_Approximation_LINE()
    execution_time_all_NetworkStructures_for_Greedy_LINE()
    execution_time_all_NetworkStructures_for_Genetic_LINE()
    ########################################################################################################################
    ########################################################################################################################

    ## Cost Function all Network Structures for the various Algorithms #####################################################  
    costfunction_all_NetworkStructures_for_Approximation()
    costfunction_all_NetworkStructures_for_Greedy()
    costfunction_all_NetworkStructures_for_Genetic()
    costfunction_all_NetworkStructures_for_ILP()
    ########################################################################################################################
    ########################################################################################################################

    # NumberofNodesinVC all Network Structures for the various Algorithms ##################################################  
    NumberofNodesinVC_all_NetworkStructures_for_Approximation()
    NumberofNodesinVC_all_NetworkStructures_for_Greedy()
    NumberofNodesinVC_all_NetworkStructures_for_Genetic()
    NumberofNodesinVC_all_NetworkStructures_for_ILP()
    ########################################################################################################################
    ########################################################################################################################
