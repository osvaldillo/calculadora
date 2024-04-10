def getISR(income):
    #El diccionario isrTable fue obtenido de https://www.bbva.mx/educacion-financiera/impuestos-que-es-el-impuesto-sobre-la-renta.html
    isrTable = {(0.01, 746.04): (0, 0.0192),
                (746.05, 6332.05): (14.32, 0.064),
                (6332.06, 11128.01): (371.83, 0.1088),
                (11128.02,12935.82) : (893.63, 0.16),
                (12935.83, 15487.71): (1182.88, 0.1792),
                (15487.72, 31236.49): (1640.18, 0.2136),
                (31236.5, 49233): (5004.12, 0.2352),
                (49233.01, 93993.9): (9236.89, 0.3),
                (93993.91,125325.2): (22665.17, 0.32),
                (125325.21,375975.61):(32691.18, 0.34),
                (375975.62, 1000000000000000): (117912.32, 0.35)}
    for li, ls in isrTable.keys():
        if income > li and income < ls:
            tasa = isrTable[(li, ls)]
            return round((income - li) * tasa[1] + tasa[0], 2)