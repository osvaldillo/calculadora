def conv(mag, convertion):
    dic = {'in-cm': mag*2.54,
           'cm-in': mag/2.54,
           'ft-m': mag*0.3048,
           'm-ft': mag/0.3048,
           'mille-km': mag*1.609344,
           'km-mille': mag/1.609344, #0-5 longitud
           'kg-oz':mag*35.27396584,
           'oz-kg':mag/35.27396584,
           'lb-kg':mag * 0.4535924,
           'kg-lb':mag / 0.4535924, #5-9 masa
           'atm-pa':mag * 101325,
           'pa-atm':mag/ 101325,
           'mmHg-pa': mag * 133.3224,
           'pa-mmHg': mag / 133.3224,
           'kgf/cm2-pa': mag*98066.5,
           'pa-kgf/cm2': mag/98066.5, #9-15 presion
           '°f-°c': (mag - 32)/1.8,
           '°c-°f': mag*1.8 + 32, #15-17 temperatura
           'rad-°':mag * 57.29577951,
           '°-rad': mag / 57.29577951,#17-19 angulo
           'hp-kw': mag*0.7457,
           'kw-hp': mag/0.7457} #19-21 potencia
    return dic[convertion]