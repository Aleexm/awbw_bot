import os
HARD_DIR = os.path.join('assets', 'terrain')

TERRAIN_DICT = {
    1:  'plain',
    2:  'mountain',
    3:  'wood',
    4:  'hriver',
    5:  'vriver',
    6:  'criver',
    7:  'esriver',
    8:  'swriver',
    9:  'wnriver',
    10: 'neriver',
    11: 'eswriver',
    12: 'swnriver',
    13: 'wneriver',
    14: 'nesriver',
    15: 'hroad',
    16: 'vroad',
    17: 'croad',
    18: 'esroad',
    19: 'swroad',
    20: 'wnroad',
    21: 'neroad',
    22: 'eswroad',
    23: 'swnroad',
    24: 'wneroad',
    25: 'nesroad',
    26: 'hbridge',
    27: 'vbridge',
    28: 'sea',
    29: 'hshoal',
    30: 'hshoaln',
    31: 'vshoal',
    32: 'vshoale',
    33: 'reef',
    34: 'neutralcity',
    35: 'neutralbase',
    36: 'neutralairport',
    37: 'neutralport',
    38: 'orangestarcity',
    39: 'orangestarbase',
    40: 'orangestarairport',
    41: 'orangestarport',
    42: 'orangestarhq',
    43: 'bluemooncity',
    44: 'bluemoonbase',
    45: 'bluemoonairport',
    46: 'bluemoonport',
    47: 'bluemoonhq',
    48: 'greenearthcity',
    49: 'greenearthbase',
    50: 'greenearthairport',
    51: 'greenearthport',
    52: 'greenearthhq',
    53: 'yellowcometcity',
    54: 'yellowcometbase',
    55: 'yellowcometairport',
    56: 'yellowcometport',
    57: 'yellowcomethq',
    81: 'redfirecity',
    82: 'redfirebase',
    83: 'redfireairport',
    84: 'redfireport',
    85: 'redfirehq',
    86: 'greyskycity',
    87: 'greyskybase',
    88: 'greyskyairport',
    89: 'greyskyport',
    90: 'greyskyhq',
    91: 'blackholecity',
    92: 'blackholebase',
    93: 'blackholeairport',
    94: 'blackholeport',
    95: 'blackholehq',
    96: 'browndesertcity',
    97: 'browndesertbase',
    98: 'browndesertairport',
    99: 'browndesertport',
    100: 'browndeserthq',
    101: 'vpipe',
    102: 'hpipe',
    103: 'nepipe',
    104: 'espipe',
    105: 'swpipe',
    106: 'wnpipe',
    107: 'npipeend',
    108: 'epipeend',
    109: 'spipeend',
    110: 'wpipeend',
    111: 'missilesilo',
    112: 'missilesiloempty',
    113: 'hpipeseam',
    114: 'vpipeseam',
    115: 'hpiperubble',
    116: 'vpiperubble',
    117: 'amberblazeairport',
    118: 'amberblazebase',
    119: 'amberblazecity',
    120: 'amberblazehq',
    121: 'amberblazeport',
    122: 'jadesunairport',
    123: 'jadesunbase',
    124: 'jadesuncity',
    125: 'jadesunhq',
    126: 'jadesunport',
    127: 'amberblazecomtower',
    128: 'blackholecomtower',
    129: 'bluemooncomtower',
    130: 'browndesertcomtower',
    131: 'greenearthcomtower',
    132: 'jadesuncomtower',
    133: 'neutralcomtower',
    134: 'orangestarcomtower',
    135: 'redfirecomtower',
    136: 'yellowcometcomtower',
    137: 'greyskycomtower',
    138: 'amberblazelab',
    139: 'blackholelab',
    140: 'bluemoonlab',
    141: 'browndesertlab',
    142: 'greenearthlab',
    143: 'greyskylab',
    144: 'jadesunlab',
    145: 'neutrallab',
    146: 'orangestarlab',
    147: 'redfirelab',
    148: 'yellowcometlab',
    149: 'cobalticeairport',
    150: 'cobalticebase',
    151: 'cobalticecity',
    152: 'cobalticecomtower',
    153: 'cobalticehq',
    154: 'cobalticelab',
    155: 'cobalticeport',
    156: 'pinkcosmosairport',
    157: 'pinkcosmosbase',
    158: 'pinkcosmoscity',
    159: 'pinkcosmoscomtower',
    160: 'pinkcosmoshq',
    161: 'pinkcosmoslab',
    162: 'pinkcosmosport',
    163: 'tealgalaxyairport',
    164: 'tealgalaxybase',
    165: 'tealgalaxycity',
    166: 'tealgalaxycomtower',
    167: 'tealgalaxyhq',
    168: 'tealgalaxylab',
    169: 'tealgalaxyport',
    170: 'purplelightningairport',
    171: 'purplelightningbase',
    172: 'purplelightningcity',
    173: 'purplelightningcomtower',
    174: 'purplelightninghq',
    175: 'purplelightninglab',
    176: 'purplelightningport',
    181: 'acidrainairport',
    182: 'acidrainbase',
    183: 'acidraincity',
    184: 'acidraincomtower',
    185: 'acidrainhq',
    186: 'acidrainlab',
    187: 'acidrainport',
    188: 'whitenovaairport',
    189: 'whitenovabase',
    190: 'whitenovacity',
    191: 'whitenovacomtower',
    192: 'whitenovahq',
    193: 'whitenovalab',
    194: 'whitenovaport'
}
for k,v in TERRAIN_DICT.items():
    TERRAIN_DICT[k] = os.path.join(HARD_DIR, v+'.jpg')
