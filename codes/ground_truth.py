from pyscf import gto, scf

#gly-ala
geometry = """
O   -1.8905    1.6973    0.2100
O    1.7277   -1.1657   -0.8196
O   -3.2668    0.1023   -0.6122
N    0.2075    0.1284    0.3672
N    3.6993    0.6711   -0.2916
C   -0.9970   -0.5351   -0.0783
C   -1.3487   -1.6864    0.8516
C    1.4787   -0.2454   -0.0440
C   -2.1642    0.4318   -0.1879
C    2.5541    0.6018    0.6047
H   -0.8111   -0.9210   -1.0876
H    0.1082    0.8856    1.0375
H   -2.2438   -2.2144    0.5060
H   -0.5290   -2.4105    0.9106
H   -1.5484   -1.3260    1.8673
H    2.8402    0.1404    1.5546
H    2.1875    1.6133    0.8048
H    3.4171    1.0727   -1.1847
H    4.0410   -0.2681   -0.4915
H   -2.6688    2.2872    0.1178
"""

mol = gto.M(atom=geometry, basis='sto-3g')

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"gly-ala: {energy} Hartrees")

# gly-gly
geometry = """
O    1.1192   -0.9807    0.9350
O   -1.6980    1.2320    0.5903
O   -3.2962   -0.3376    0.2304
N    0.1194    0.0665   -0.8809
N    3.5584    0.0170    0.1638
C   -1.1505   -0.6217   -0.8231
C    1.1558   -0.1725    0.0097
C    2.3540    0.7121   -0.2674
C   -2.1620    0.0850    0.0422
H   -0.9953   -1.6290   -0.4254
H   -1.5383   -0.6729   -1.8442
H    0.2322    0.7805   -1.5946
H    2.2350    1.6486    0.2858
H    2.4304    0.9444   -1.3339
H    3.6446   -0.8687   -0.3332
H    3.4912   -0.2124    1.1546
H   -2.3743    1.6726    1.1478
"""

mol = gto.M(atom=geometry, basis='sto-3g')

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"gly-gly: {energy} Hartrees")

# gly-ser
geometry = """
O   -1.6104   -1.9191    0.8894
O   -2.7055    1.2947   -0.9551
O    1.9051   -0.3647   -1.3755
O   -2.0502    1.1089    1.2100
N    0.3449    0.0535    0.2933
N    3.8899    0.6451    0.2309
C   -0.8447   -0.1246   -0.5084
C   -1.3440   -1.5612   -0.4612
C    1.6300   -0.0826   -0.2113
C   -1.8972    0.8221    0.0297
C    2.6820    0.1281    0.8581
H   -0.6074    0.1581   -1.5405
H   -0.5904   -2.2503   -0.8561
H   -2.2684   -1.6750   -1.0367
H    0.2248    0.2518    1.2829
H    2.8851   -0.8303    1.3455
H    2.3337    0.8373    1.6153
H   -1.9256   -2.8390    0.8835
H    3.6847    1.5215   -0.2472
H    4.2159   -0.0049   -0.4832
H   -3.4007    1.8904   -0.6027
"""
mol = gto.M(atom=geometry, basis='sto-3g')

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"gly-ser: {energy} Hartrees")

# carnosine
geometry = """
O   -1.1827    2.8969   -0.5876
O   -1.8901    0.1543    1.4985
O    0.7136    3.5022    0.4837
N   -0.6950    0.3333   -0.4828
N    1.7643   -1.5529   -0.3956
N    3.7922   -1.9187    0.4324
N   -4.8172   -2.2295   -0.4376
C    0.3726    1.1474    0.0471
C    1.6855    0.9161   -0.7134
C    2.3783   -0.3605   -0.2965
C   -1.7519   -0.0994    0.3048
C   -2.7379   -0.9368   -0.4903
C    0.0023    2.6229    0.0089
C    3.6100   -0.5774    0.2062
C   -3.9062   -1.4202    0.3623
C    2.6623   -2.4776    0.0599
H    0.4928    0.8974    1.1094
H    2.3792    1.7478   -0.5340
H    1.5096    0.8913   -1.7969
H   -0.7045    0.1328   -1.4791
H   -3.1047   -0.3280   -1.3261
H   -2.1952   -1.7931   -0.9100
H    0.8301   -1.7409   -0.7360
H   -4.4492   -0.5662    0.7827
H   -3.5386   -2.0187    1.2031
H    4.3890    0.1382    0.4251
H    2.4323   -3.5331    0.0937
H   -5.1893   -1.6711   -1.2048
H   -5.6173   -2.5010    0.1323
H   -1.3805    3.8576   -0.5864
"""

mol = gto.M(atom=geometry, basis='sto-3g')

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"carnosine: {energy} Hartrees")

# aspartame
geometry = """
   O   -1.8337    2.9115   -0.4575
   O    2.1213   -0.0281   -1.6083
   O   -0.9281    2.0358    1.4665
   O    5.6253    0.4131   -0.4127
   O    4.1389    0.9708    1.2123
   N    0.5352    0.1671    0.0723
   N    1.9540   -2.5588    0.2571
   C   -0.3657    1.0282   -0.6567
   C   -1.3701    0.2130   -1.4846
   C    2.4857   -1.2131    0.4761
   C   -2.3150   -0.6407   -0.6694
   C    1.7229   -0.2954   -0.4765
   C   -1.0587    2.0398    0.2466
   C    3.9887   -1.2164    0.1958
   C   -1.9526   -1.9395   -0.3540
   C   -3.5233   -0.1063   -0.2544
   C   -2.8240   -2.7271    0.3982
   C   -4.3947   -0.8940    0.4979
   C    4.5756    0.1586    0.4068
   C   -4.0450   -2.2044    0.8242
   C   -2.5367    3.8858    0.3204
   H    0.2467    1.6211   -1.3488
   H   -1.9631    0.8843   -2.1203
   H   -0.8274   -0.4345   -2.1872
   H    0.2702   -0.1236    1.0091
   H    2.2977   -0.9132    1.5135
   H    4.5133   -1.9106    0.8620
   H    4.1856   -1.5215   -0.8397
   H   -1.0113   -2.3603   -0.6923
   H   -3.8117    0.9091   -0.5082
   H    0.9541   -2.5729    0.4494
   H    2.0719   -2.8319   -0.7176
   H   -2.5530   -3.7484    0.6495
   H   -5.3463   -0.4877    0.8280
   H   -4.7240   -2.8181    1.4089
   H   -3.2243    3.3922    1.0138
   H   -3.1171    4.5115   -0.3628
   H   -1.8289    4.5201    0.8624
   H    5.9882    1.3139   -0.2742
"""


mol = gto.M(atom=geometry, basis='sto-3g')

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"Aspartame: {energy} Hartrees")

# cystine
geometry = """
    S   -0.4126   -0.2308    0.9457
    S    0.4167   -0.2255   -0.9335
    O   -3.2409   -1.5942   -1.0036
    O    3.2471   -1.5935    1.0015
    O   -4.0463   -0.8876    0.9959
    O    4.0421   -0.8862   -1.0019
    N   -3.7666    1.6853   -0.4069
    N    3.7656    1.6866    0.4017
    C   -2.7275    0.6575   -0.3169
    C    2.7276    0.6574    0.3168
    C   -1.7150    1.0301    0.7677
    C    1.7095    1.0285   -0.7631
    C   -3.4158   -0.6642   -0.0311
    C    3.4162   -0.6634    0.0279
    H   -2.2525    0.6060   -1.3016
    H    2.2636    0.6043    1.3063
    H   -1.2455    1.9981    0.5588
    H   -2.2087    1.1165    1.7427
    H    1.2428    1.9974   -0.5517
    H    2.1990    1.1168   -1.7401
    H   -4.3813    1.4827   -1.1946
    H   -3.3379    2.5884   -0.6069
    H    3.3357    2.5849    0.6209
    H    4.2079    1.8067   -0.5093
    H   -3.6831   -2.4417   -0.7833
    H    3.6893   -2.4404    0.7792
"""

mol = gto.M(
    atom=geometry,
    basis='sto-3g'
)

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"cystine: {energy} Hartrees")

#glu-ser-gly

geometry = """
O   2.0407    1.8775    1.4292
O  -1.4526    2.3496   -1.3314
O  -1.2361   -1.0418   -0.4307
O   1.7165   -2.4817    0.0159
O   3.7108   -2.6965   -1.0496
O  -4.5020    0.3438   -0.8742
O  -5.7206   -1.4881   -0.3198
N   0.6661    0.8040   -0.1044
N   3.6506    2.0721   -0.9862
N  -2.7168    0.0218    1.0053
C   3.0549    0.8263   -0.5002
C   4.1191    0.0163    0.2553
C  -0.5948    1.0836    0.5440
C   1.8879    1.2279    0.3966
C   3.5765   -1.2643    0.8897
C  -1.1946    2.4026    0.0672
C  -1.5316   -0.0930    0.2928
C   3.0373   -2.2210   -0.1444
C  -3.7514   -0.9857    0.9703
C  -4.7598   -0.7535   -0.1254
H   2.7031    0.2533   -1.3650
H   4.9377   -0.2370   -0.4312
H   4.5570    0.6276    1.0555
H  -0.4163    1.1447    1.6248
H   0.6405    0.2941   -0.9827
H   4.3722   -1.7846    1.4350
H   2.7964   -1.0372    1.6247
H  -0.4948    3.2270    0.2400
H  -2.1299    2.6488    0.5789
H   2.9783    2.5659   -1.5725
H   4.4466    1.8594   -1.5865
H  -2.8707    0.8324    1.5972
H  -4.2684   -0.9522    1.9333
H  -3.2940   -1.9683    0.8210
H  -2.1629    1.7021   -1.4773
H   1.3774   -3.0933   -0.6720
H  -5.1711    0.4727   -1.5799
"""

mol = gto.M(
    atom=geometry,
    basis='sto-3g',
    charge=0,
    spin=0
)

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"glu-ser-gly: {energy} Hartrees")

# leu-thr
geometry = gto.M(
    atom='''
        O   3.2840   -1.0276   -1.5062
        O  -0.3006    0.7045    1.7152
        O   3.2362    2.1480    0.6383
        O   2.0587    1.8247   -1.2744
        N   0.8265   -0.3287   -0.0319
        N  -1.7495   -1.8508    0.5874
        C  -2.8147    0.3611    0.4154
        C  -4.1353   -0.1081   -0.2325
        C  -1.5892   -0.4946    0.0564
        C   2.1651    0.0324    0.3750
        C  -0.3052    0.0415    0.6796
        C   3.2223   -0.9780   -0.0816
        C  -3.9839   -0.1262   -1.7563
        C  -5.3240    0.7722    0.1563
        C   2.9622   -2.3833    0.4482
        C   2.4474    1.4129   -0.1889
        H  -2.9470    0.3829    1.5061
        H  -2.6166    1.4011    0.1221
        H  -4.3688   -1.1248    0.1043
        H  -1.4506   -0.5325   -1.0286
        H   2.1685    0.1045    1.4697
        H   4.2089   -0.6460    0.2613
        H   0.7106   -0.8302   -0.9073
        H  -4.9484   -0.3269   -2.2366
        H  -3.3026   -0.9150   -2.0880
        H  -3.6170    0.8338   -2.1349
        H  -5.4562    0.7822    1.2433
        H  -5.1770    1.8054   -0.1761
        H  -6.2513    0.3991   -0.2908
        H  -0.9402   -2.4149    0.3286
        H  -2.5496   -2.3027    0.1476
        H   2.0307   -2.7999    0.0501
        H   2.9138   -2.3922    1.5413
        H   3.7630   -3.0598    0.1301
        H   2.4444   -1.3916   -1.8331
        H   3.4350    3.0323    0.2631
    ''',
    unit='Angstrom',
    basis='sto-3g'
)

mf = scf.RHF(geometry)
energy = mf.kernel()

print(f"leu-thr: {energy} Hartrees")

# thr-lys
geometry = '''
O   2.7621   -0.4106    1.9741
O   1.8016   -0.0897   -1.7954
O   0.0879    3.3453   -0.8780
O   0.8868    2.4774    1.0606
N   0.3833   -0.0303    0.0367
N   2.6588   -2.5940   -1.0216
N  -6.2320   -1.4423    0.4920
C  -1.8499    1.0175    0.1520
C  -0.4331    1.0636   -0.4227
C  -2.6669   -0.2144   -0.2578
C  -4.0978   -0.2013    0.2907
C   2.1650   -1.6793    0.0075
C   3.3092   -1.1971    0.9161
C   1.4523   -0.5261   -0.6999
C  -4.8881   -1.4606   -0.0728
C   0.2671    2.3358    0.0143
C   4.3937   -0.3938    0.2042
H  -2.3905    1.9198   -0.1625
H  -1.8035    1.0601    1.2486
H  -0.4617    1.0376   -1.5185
H  -2.7026   -0.2747   -1.3524
H  -2.1593   -1.1206    0.0939
H  -4.0582   -0.1003    1.3829
H  -4.6224    0.6838   -0.0908
H   1.4258   -2.2165    0.6146
H   0.2102   -0.3996    0.9673
H   3.7787   -2.0666    1.3914
H  -4.9621   -1.5479   -1.1623
H  -4.3599   -2.3484    0.2924
H   5.1549   -0.0776    0.9266
H   4.8921   -0.9727   -0.5780
H   3.9931    0.5261   -0.2338
H   3.3232   -2.1183   -1.6301
H   3.1739   -3.3565   -0.5831
H   2.4190    0.4144    1.5908
H  -6.7013   -2.3211    0.2772
H  -6.1760   -1.3884    1.5082
H   0.5220    4.1743   -0.5835
'''

mol = gto.Mole()
mol.atom = geometry
mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"thr-lys: {energy} Hartrees")

# trp-his
geometry = '''
O   -0.8812   -0.9656   -1.5931
O    0.5680    2.0185    1.0333
O   -0.8999    3.4923    0.1484
N   -0.9031   -0.0851    0.5517
N    4.2035   -0.9585    1.3352
N   -0.8108   -3.4188   -0.0035
N   -3.9090   -0.7927    0.2743
N   -5.8925   -0.1820   -0.5159
C    1.4388   -2.5157   -0.4713
C    0.0795   -2.2752    0.2047
C    2.5372   -1.6551    0.0886
C   -1.5417    1.1603    0.1994
C    2.8964   -0.3762   -0.3763
C   -0.6225   -1.0601   -0.3942
C   -2.8557    1.3548    0.9684
C    3.9559    0.0476    0.4287
C    3.3396   -2.0009    1.1316
C   -3.9913    0.5448    0.3871
C    2.4378    0.4778   -1.3989
C    4.5824    1.2877    0.2615
C   -0.6124    2.3389    0.4511
C    3.0549    1.7213   -1.5779
C    4.1105    2.1180   -0.7592
C   -5.1939    0.9205   -0.0918
C   -5.0906   -1.1969   -0.2819
H    1.7399   -3.5636   -0.3301
H    1.3724   -2.3703   -1.5574
H    0.2157   -2.1491    1.2851
H   -1.7325    1.1685   -0.8812
H   -2.7291    1.0862    2.0254
H   -3.1533    2.4114    0.9525
H   -0.6157   -0.2177    1.5167
H    3.3857   -2.8837    1.7538
H    4.9196   -0.9307    2.0478
H    1.6214    0.1854   -2.0519
H   -0.3809   -4.2607    0.3781
H   -1.6736   -3.2799    0.5216
H    5.4041    1.5975    0.8985
H    2.7056    2.3839   -2.3653
H    4.5750    3.0883   -0.9157
H   -3.1443   -1.3922    0.5551
H   -5.6154    1.9124   -0.1643
H   -5.3027   -2.2366   -0.4867
H    1.1371    2.8059    1.1687
'''

mol = gto.Mole()
mol.atom = geometry
mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"trp-his: {energy} Hartrees")

# phe-ile
geometry = '''
O   -0.4186   -2.0495   -0.2435
O   -0.0572    1.6500    1.7555
O   -2.0462   -2.6445    1.2092
N   -0.9071    0.5227   -0.0846
N    0.4975    3.5954   -0.3498
C   -3.3081   -0.0648    0.2229
C   -1.8377   -0.2978    0.6480
C   -3.5415   -0.6119   -1.2022
C   -3.7285    1.4065    0.3434
C    0.8359    2.1742   -0.4350
C   -0.0799    1.4446    0.5429
C    2.3102    1.9646   -0.0595
C   -4.9837   -0.4873   -1.6745
C   -1.4623   -1.7725    0.5746
C    2.7344    0.5167   -0.1371
C    2.6080   -0.2881    0.9835
C    3.2412    0.0212   -1.3275
C    2.9994   -1.6250    0.9120
C    3.6325   -1.3158   -1.3990
C    3.5116   -2.1388   -0.2792
H   -3.9457   -0.6438    0.9054
H   -1.7501   -0.0387    1.7109
H   -2.8978   -0.0924   -1.9218
H   -3.2744   -1.6736   -1.2478
H   -4.8123    1.5187    0.2399
H   -3.2478    2.0266   -0.4204
H   -3.4555    1.8045    1.3266
H   -0.8218    0.3718   -1.0851
H    0.6557    1.8323   -1.4602
H    2.9538    2.5615   -0.7203
H    2.5112    2.3373    0.9549
H   -5.6734   -0.9453   -0.9586
H   -5.1076   -0.9961   -2.6362
H   -5.2721    0.5580   -1.8186
H    0.7219    3.9498    0.5798
H    1.0847    4.1226   -0.9955
H    2.2205    0.1004    1.9204
H    3.3366    0.6537   -2.2052
H   -0.2053   -3.0068   -0.2560
H    2.9064   -2.2655    1.7842
H    4.0304   -1.7164   -2.3268
H    3.8160   -3.1798   -0.3350
'''

mol = gto.Mole()
mol.atom = geometry
mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"phe-ile: {energy} Hartrees")

#arg-met
geometry = '''
S    5.6759    1.9712   -0.1186
O    0.3158    0.1736   -1.5551
O    2.8337   -2.4479    1.4186
O    4.2608   -2.7998   -0.2997
N    1.6055   -0.4138    0.2804
N   -0.1369    2.0144    0.9516
N   -4.8830    0.0714    0.3726
N   -6.7323   -0.5307   -1.0372
N   -7.0047    0.9556    0.6691
C   -0.5444    0.6384    0.6614
C   -1.9757    0.6169    0.1053
C    2.7158   -0.9439   -0.4743
C   -2.5977   -0.7850    0.1734
C    3.7366    0.1484   -0.8225
C    0.4791    0.1095   -0.3379
C   -4.0130   -0.8221   -0.3942
C    4.5014    0.6818    0.3911
C    3.3646   -2.1370    0.2116
C    4.5215    3.3596   -0.1960
C   -6.1232    0.1393    0.0003
H   -0.4985    0.0551    1.5885
H   -2.0046    0.9869   -0.9271
H   -2.5986    1.2986    0.6989
H    2.3029   -1.3383   -1.4120
H   -1.9743   -1.4936   -0.3845
H   -2.6160   -1.1224    1.2172
H    4.4557   -0.2677   -1.5409
H    3.2141    0.9655   -1.3345
H    1.6715   -0.4043    1.2941
H   -3.9846   -0.5205   -1.4484
H   -4.3820   -1.8532   -0.3367
H    3.8258    1.0759    1.1569
H    5.0857   -0.1205    0.8525
H   -0.7805    2.4271    1.6258
H    0.7785    2.0123    1.4011
H    3.2623   -3.2358    1.8157
H    5.0757    4.2691   -0.4444
H    4.0340    3.5090    0.7710
H    3.7666    3.1995   -0.9691
H   -7.7178   -0.3984   -1.2374
H   -6.2280   -1.1756   -1.6350
H   -7.9783    1.0236    0.3934
H   -6.7035    1.5155    1.4593
'''

mol = gto.Mole()
mol.atom = geometry
mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"arg-met: {energy} Hartrees")

#ser-cys
geometry = '''
S   -2.5863    2.1687   -0.6708
O    3.5498   -1.6701   -0.0420
O    1.2290    0.2282    1.6474
O   -1.9556   -1.4848   -1.3215
O   -3.4602   -1.3353    0.3682
N   -0.1601    0.0209   -0.1980
N    2.3405    1.6783   -0.9142
C   -1.3964   -0.0747    0.5416
C    2.2227    0.2640   -0.5642
C    1.0693    0.1669    0.4300
C   -2.0027    1.3021    0.8239
C    3.5355   -0.2482    0.0249
C   -2.3854   -1.0160   -0.1255
H   -1.1537   -0.5442    1.5039
H    1.9750   -0.3161   -1.4615
H   -0.2054    0.0098   -1.2128
H   -1.2728    1.9487    1.3225
H   -2.8643    1.2002    1.4926
H    3.6821    0.0581    1.0659
H    4.3902    0.1062   -0.5622
H    1.4913    1.9855   -1.3875
H    3.0978    1.8035   -1.5850
H   -3.0338    3.2665   -0.0440
H    4.3993   -1.9645    0.3286
H   -2.6053   -2.0950   -1.7312
'''
mol = gto.Mole()
mol.atom = geometry
mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"ser-cys: {energy} Hartrees")

#tyr-asp
geometry = '''
O   -0.9523    1.2444    1.6587
O    0.1533   -2.1349   -0.5970
O   -1.2760   -3.4205    0.6028
O   -4.9851   -0.0298   -1.2960
O    4.6971   -2.0060   -0.2123
O   -4.1238    0.6784    0.6814
N   -1.1814    0.0625   -0.3234
N   -0.9095    3.4379   -0.2677
C   -0.0939    2.2284   -0.3823
C    1.3196    2.4983    0.1540
C   -1.8362   -1.0870    0.2539
C   -0.7884    1.1497    0.4433
C    2.2238    1.2921    0.0557
C   -3.2098   -1.3159   -0.3830
C    2.2792    0.3986    1.1126
C    2.9801    1.1034   -1.0894
C   -0.9806   -2.3355    0.1165
C    3.1144   -0.7149    1.0220
C    3.8152   -0.0102   -1.1802
C   -4.1280   -0.1196   -0.2453
C    3.8823   -0.9195   -0.1245
H   -0.0409    1.9367   -1.4376
H    1.2810    2.8282    1.2018
H    1.7763    3.3328   -0.3958
H   -1.9553   -0.9182    1.3307
H   -0.9681    0.0399   -1.3162
H   -3.7125   -2.1787    0.0683
H   -3.0788   -1.5306   -1.4515
H   -1.8177    3.2793   -0.7031
H   -0.4727    4.1954   -0.7916
H    1.6953    0.5500    2.0153
H    2.9323    1.8049   -1.9173
H    3.1635   -1.4188    1.8483
H    4.4077   -0.1584   -2.0790
H    0.6922   -2.9515   -0.6682
H   -5.5841    0.7427   -1.2138
H    5.1526   -1.9895   -1.0715

'''
mol = gto.Mole()
mol.atom = geometry
mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"tyr-asp: {energy} Hartrees")

#glu-gly
geometry = '''
O   -0.5119    1.9097    1.0960
O    0.9748   -2.6954   -0.0656
O    2.7225   -1.5681   -0.9790
O   -1.8613   -1.3346    0.3966
O   -4.0474   -0.7642    0.1874
N    1.7803    2.6903   -0.5167
N   -0.9448    0.7566   -0.8731
C    1.3498    1.3040   -0.3264
C    2.2183    0.6472    0.7570
C    1.7894   -0.7785    1.1036
C   -0.1231    1.3604    0.0671
C   -2.3837    0.7021   -0.7490
C    1.9007   -1.7050   -0.0817
C   -2.8635   -0.5243   -0.0163
H    1.4734    0.7806   -1.2795
H    3.2676    0.6469    0.4338
H    2.1766    1.2397    1.6809
H    2.4307   -1.1785    1.8967
H    0.7594   -0.7851    1.4748
H    2.7610    2.7062   -0.7957
H    1.7367    3.1923    0.3699
H   -0.5317    0.3096   -1.6860
H   -2.7959    0.6883   -1.7616
H   -2.7319    1.5883   -0.2101
H    1.0513   -3.2811   -0.8489
H   -2.1984   -2.1242    0.8712
'''
mol = gto.Mole()
mol.atom = geometry
mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"glu-gly: {energy} Hartrees")

# gly-val-ala
mol = gto.Mole()
mol.atom = '''
O   -0.1077   -1.0953   -1.3663
O    3.0557   -0.7161    1.4988
O   -3.7900    1.0741    0.6520
O   -5.1078   -0.5329   -0.2401
N    2.0239    0.1698   -0.3846
N   -1.5434   -0.2154    0.2321
N    5.0116   -1.8064   -0.0993
C    0.4402    2.0183    0.1425
C    0.7650    0.5118    0.2275
C   -0.3219   -0.3504   -0.4122
C    1.5015    2.9008    0.8080
C    0.2373    2.4563   -1.3114
C   -2.7283   -0.9488   -0.1511
C    3.0754   -0.4210    0.3059
C   -2.8056   -2.2698    0.5995
C    4.2856   -0.6392   -0.5789
C   -3.9915   -0.1360    0.0774
H   -0.5031    2.2086    0.6697
H    0.8060    0.2303    1.2877
H    2.4646    2.8342    0.2912
H    1.1905    3.9509    0.8024
H    1.6523    2.6019    1.8505
H    1.1465    2.3275   -1.9076
H   -0.5724    1.9020   -1.7957
H   -0.0325    3.5178   -1.3534
H    2.1259    0.3384   -1.3811
H   -1.6088    0.3839    1.0495
H   -2.6670   -1.1409   -1.2288
H   -2.8766   -2.1054    1.6809
H   -3.6848   -2.8470    0.2941
H   -1.9164   -2.8817    0.4137
H    4.9164    0.2541   -0.5375
H    3.9788   -0.8062   -1.6160
H    5.3633   -1.6283    0.8410
H    5.8340   -1.9544   -0.6831
H   -4.6298    1.5658    0.7760
'''

mol.basis = 'sto-3g'
mol.charge = 0

mol.build()
mf = scf.RHF(mol)

energy = mf.kernel()

print(f"gly-val-ala: {energy} Hartrees")

# val-ala-ser
mol = gto.Mole()
mol.build(
    atom = '''
    O  2.6617  -1.0062  -1.5480
    O -0.7574  -0.1708   1.8963
    O -2.9973   2.1513  -1.1695
    O -5.4638  -0.2815   0.5415
    O -4.3859  -0.5810  -1.4332
    N  1.4976  -0.7915   0.4460
    N  5.0151  -0.9217  -0.1462
    N -1.9955  -0.2650  -0.0642
    C  4.0420   1.3117   0.3518
    C  3.8555  -0.2229   0.4133
    C  0.2161  -1.2366  -0.0505
    C  2.6280  -0.7122  -0.3541
    C  4.2948   1.7977  -1.0787
    C  2.8859   2.1052   0.9710
    C -0.8695  -0.4916   0.7149
    C  0.0551  -2.7409   0.1040
    C -3.1789   0.3865   0.4468
    C -3.1331   1.8906   0.2221
    C -4.3706  -0.2209  -0.2632
    H  4.9391   1.5553   0.9384
    H  3.7624  -0.5237   1.4643
    H  0.1547  -0.9771  -1.1141
    H  5.1691   1.3160  -1.5273
    H  4.4872   2.8767  -1.0841
    H  3.4317   1.6179  -1.7276
    H  2.6830   1.7616   1.9906
    H  3.1343   3.1708   1.0213
    H  1.9667   2.0068   0.3848
    H  1.5698  -0.5472   1.4297
    H  5.8590  -0.6298   0.3454
    H  4.9228  -1.9235   0.0188
    H -3.2570   0.1680   1.5181
    H  0.1206  -3.0401   1.1563
    H -0.9178  -3.0722  -0.2741
    H  0.8366  -3.2785  -0.4435
    H -1.9914  -0.5577  -1.0374
    H -2.2779   2.3375   0.7394
    H -4.0529   2.3687   0.5742
    H -2.9703   3.1174  -1.2771
    H -6.2413  -0.6548   0.0741
    ''',
    basis = 'sto3g'
)

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"val-ala-ser: {energy} Hartrees")

#gly-his-lys
mol.build(
    atom = '''
    O  -0.9514    0.7191   -2.1819
    O   1.2167   -2.4567   -3.2242
    O   0.0294   -3.0383   -1.3799
    O  -0.3533    3.2697    0.8076
    N   0.2304   -0.4223   -0.5396
    N  -2.1453    2.1788   -0.1901
    N  -2.7619   -2.6275    0.4858
    N   6.3869    0.7178    2.0608
    N  -1.9841   -2.9095    2.5468
    N  -1.0709    5.5956   -0.4748
    C   2.5737   -1.1979   -0.6148
    C   1.2754   -0.9435   -1.3825
    C   3.2162    0.0571   -0.0104
    C  -1.7390    0.8281    0.1080
    C   4.5418   -0.2262    0.7042
    C  -2.9380   -0.1210    0.2230
    C  -0.8077    0.3738   -1.0109
    C   5.1474    1.0196    1.3551
    C  -2.6081   -1.3719    1.0027
    C   0.7502   -2.2411   -1.9659
    C  -1.4137    3.2984    0.1869
    C  -2.1275   -1.5718    2.2755
    C  -2.0921    4.5871   -0.2303
    C  -2.3750   -3.5175    1.4488
    H   3.2974   -1.6748   -1.2887
    H   2.3890   -1.9215    0.1907
    H   1.4423   -0.2331   -2.2009
    H   3.3870    0.7927   -0.8060
    H   2.5190    0.5154    0.7013
    H  -1.1798    0.8634    1.0512
    H   5.2548   -0.6485   -0.0152
    H   4.3757   -0.9917    1.4729
    H  -3.7605    0.3823    0.7481
    H  -3.3187   -0.3859   -0.7718
    H   0.2291   -0.7030    0.4368
    H  -2.9854    2.3055   -0.7473
    H   5.3443    1.7786    0.5898
    H   4.4336    1.4487    2.0668
    H  -3.0980   -2.8593   -0.4396
    H  -1.8769   -0.8223    3.0123
    H   7.0706    0.3400    1.4060
    H   6.7869    1.5809    2.4263
    H  -2.7664    4.9046    0.5712
    H  -2.6762    4.4366   -1.1434
    H  -2.4009   -4.5857    1.2869
    H   0.8948   -3.3070   -3.5922
    H  -1.5194    6.4697   -0.7460
    H  -0.5709    5.7936    0.3913
    '''
)
mf = scf.RHF(mol)
energy = mf.kernel()

print(f"gly-his-lys: {energy} Hartrees")

# his-arg-val
mol = gto.Mole()
mol.atom = '''
O   0.4167    1.1213    1.4803
O   2.1182   -1.9682   -1.7099
O  -3.6223    1.7282    0.4876
O  -3.5415    3.8063    1.3642
N  -1.1046    1.6522   -0.1897
N   1.2174   -1.1261    0.2546
N   3.1237   -3.9288    0.2064
N  -3.9652   -2.0222   -0.0424
N   5.5955    0.2339   -0.7202
N   4.7604    1.6607    0.7627
N  -6.1183   -2.0655   -0.8991
N  -5.3382   -3.9916    0.0374
C   0.1188   -0.4276   -0.3610
C  -1.1182   -1.3224   -0.5095
C  -1.5183    2.9283    0.3464
C  -1.1713    4.0602   -0.6446
C  -0.1604    0.8466    0.4302
C  -1.6821   -1.8367    0.8238
C   3.2284   -2.4797    0.3823
C   2.1423   -1.8514   -0.4856
C   0.3150    4.1058   -1.0124
C  -2.0291    4.0036   -1.9116
C  -2.8877   -2.7514    0.6286
C   4.6199   -1.9996   -0.0550
C  -2.9835    2.8899    0.7714
C   4.8052   -0.5095    0.1105
C   4.3008    0.3928    1.0172
C   5.5374    1.5303   -0.2896
C  -5.0590   -2.6793   -0.2730
H   0.4376   -0.1149   -1.3641
H  -1.9010   -0.7835   -1.0549
H  -0.8543   -2.1881   -1.1312
H  -0.9579    3.1006    1.2741
H  -1.4113    5.0098   -0.1467
H  -1.9760   -0.9867    1.4511
H  -0.9095   -2.3903    1.3694
H  -1.5433    1.3360   -1.0487
H   1.3004   -1.0932    1.2666
H   3.0660   -2.2469    1.4407
H   0.6170    3.2294   -1.5951
H   0.5356    4.9954   -1.6121
H   0.9358    4.1486   -0.1114
H  -1.8419    3.0920   -2.4882
H  -1.8062    4.8566   -2.5621
H  -3.0972    4.0459   -1.6766
H  -2.5847   -3.6228    0.0353
H  -3.2209   -3.0996    1.6137
H   5.3927   -2.5039    0.5395
H   4.8004   -2.2641   -1.1058
H   2.2315   -4.2538    0.5777
H   3.8455   -4.3927    0.7566
H   6.1271   -0.1090   -1.5093
H   3.6330    0.2007    1.8445
H  -4.5529    1.7361    0.7975
H   6.0801    2.3240   -0.7827
H  -6.0640   -1.0953   -1.1897
H  -6.9823   -2.5615   -1.0885
H  -4.6672   -4.5921    0.5029
H  -6.2362   -4.4032   -0.1931
'''

mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
energy = mf.kernel()

print(f'his-arg-val: {energy} Ha')

# val-asp-ser
atoms = '''
O   2.8608  -1.1126  -1.1524
O  -0.5884   0.9845   1.6605
O  -3.7018   0.9120  -2.2961
O  -2.2149  -2.9715   0.5745
O  -0.9198  -3.0254  -1.2928
O  -4.5004   1.7140   1.3982
O  -4.1726  -0.3340   0.4768
N   1.6434  -0.2438   0.6198
N   5.1468  -0.8665   0.3389
N  -1.6734   0.5432  -0.3432
C   4.4072   1.4993   0.1413
C   4.0491   0.0669   0.6032
C   0.3428  -0.6855   0.1720
C   2.8088  -0.4973  -0.0887
C   3.3208   2.5394   0.4375
C   4.7734   1.5432  -1.3454
C  -0.0161  -2.0602   0.7300
C  -0.6780   0.3586   0.6062
C  -2.7315   1.5134  -0.1850
C  -3.2380   2.0161  -1.5287
C  -1.0700  -2.7352  -0.1131
C  -3.8482   0.8414   0.5864
H   5.2998   1.8097   0.7026
H   3.8782   0.0796   1.6869
H   0.3726  -0.7185  -0.9243
H   1.6999   0.2557   1.5029
H   0.8536  -2.7284   0.7427
H  -0.3654  -1.9859   1.7671
H   2.4223   2.3700  -0.1645
H   3.0376   2.5129   1.4947
H   3.6836   3.5486   0.2145
H   3.9242   1.2733  -1.9814
H   5.0844   2.5551  -1.6295
H   5.6072   0.8753  -1.5826
H  -2.3461   2.3488   0.4107
H   4.9368  -1.7697   0.7624
H   5.9960  -0.5313   0.7922
H  -1.7041  -0.0649  -1.1566
H  -2.4347   2.5080  -2.0869
H  -4.0671   2.7192  -1.3991
H  -4.0147   1.2670  -3.1457
H  -2.8962  -3.4011   0.0146
H  -5.2375   1.2828   1.8810
'''

mol = gto.Mole()
mol.atom = atoms
mol.basis = 'sto-3g'
mol.build()

mf = scf.RHF(mol)
energy = mf.kernel()

print(f"val-asp-ser: {energy} Hartrees")