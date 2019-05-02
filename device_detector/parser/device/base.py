from ..parser import Parser

DEVICE_NAMES = [
    'desktop',
    'smartphone',
    'tablet',
    'feature phone',
    'console',
    'tv',
    'car browser',
    'smart display',
    'camera',
    'portable media player',
    'phablet',
]

DEVICE_TYPE_DESKTOP = 0
DEVICE_TYPE_SMARTPHONE = 1
DEVICE_TYPE_TABLET = 2
DEVICE_TYPE_FEATURE_PHONE = 3
DEVICE_TYPE_CONSOLE = 4
DEVICE_TYPE_TV = 5  # including set top boxes, blu-ray players
DEVICE_TYPE_CAR_BROWSER = 6
DEVICE_TYPE_SMART_DISPLAY = 7
DEVICE_TYPE_CAMERA = 8
DEVICE_TYPE_PORTABLE_MEDIA_PAYER = 9
DEVICE_TYPE_PHABLET = 10

DEVICE_TYPES = {
    'desktop': DEVICE_TYPE_DESKTOP,
    'smartphone': DEVICE_TYPE_SMARTPHONE,
    'tablet': DEVICE_TYPE_TABLET,
    'feature phone': DEVICE_TYPE_FEATURE_PHONE,
    'console': DEVICE_TYPE_CONSOLE,
    'tv': DEVICE_TYPE_TV,
    'car browser': DEVICE_TYPE_CAR_BROWSER,
    'smart display': DEVICE_TYPE_SMART_DISPLAY,
    'camera': DEVICE_TYPE_CAMERA,
    'portable media player': DEVICE_TYPE_PORTABLE_MEDIA_PAYER,
    'phablet': DEVICE_TYPE_PHABLET,
}

MOBILE_DEVICE_TYPES = {
    'camera',
    'feature phone',
    'phablet',
    'portable media player',
    'smartphone',
    'tablet',
}

# Before using a new brand in on of the regex files, it needs to be added here
DEVICE_BRANDS = {
    '3Q': '3Q',
    '4G': '4Good',
    'AA': 'AllCall',
    'AC': 'Acer',
    'AD': 'Advance',
    'A3': 'AGM',
    'AZ': 'Ainol',
    'AI': 'Airness',
    'AW': 'Aiwa',
    'AK': 'Akai',
    'AL': 'Alcatel',
    'A2': 'Allview',
    'A1': 'Altech UEC',
    'A5': 'altron',
    'AN': 'Arnova',
    'KN': 'Amazon',
    'AG': 'AMGOO',
    'AO': 'Amoi',
    'AP': 'Apple',
    'AR': 'Archos',
    'AS': 'ARRIS',
    'AT': 'Airties',
    'A4': 'Ask',
    'AU': 'Asus',
    'AH': 'AVH',
    'AV': 'Avvio',
    'AX': 'Audiovox',
    'AY': 'Axxion',
    'AM': 'Azumi Mobile',
    'BB': 'BBK',
    'BE': 'Becker',
    'B5': 'Beeline',
    'BI': 'Bird',
    'BT': 'Bitel',
    'BG': 'BGH',
    'BL': 'Beetel',
    'BP': 'Blaupunkt',
    'B3': 'Bluboo',
    'BM': 'Bmobile',
    'BN': 'Barnes & Noble',
    'BO': 'BangOlufsen',
    'BQ': 'BenQ',
    'BS': 'BenQ-Siemens',
    'BU': 'Blu',
    'BD': 'Bluegood',
    'B2': 'Blackview',
    'B4': 'bogo',
    'BW': 'Boway',
    'BX': 'bq',
    'BV': 'Bravis',
    'BR': 'Brondi',
    'B1': 'Bush',
    'CB': 'CUBOT',
    'CF': 'Carrefour',
    'CP': 'Captiva',
    'CS': 'Casio',
    'CA': 'Cat',
    'C9': 'CAGI',
    'CE': 'Celkon',
    'CC': 'ConCorde',
    'C2': 'Changhong',
    'CH': 'Cherry Mobile',
    'CK': 'Cricket',
    'C1': 'Crosscall',
    'CL': 'Compal',
    'CN': 'CnM',
    'CM': 'Crius Mea',
    'C3': 'China Mobile',
    'CR': 'CreNova',
    'CT': 'Capitel',
    'CQ': 'Compaq',
    'CO': 'Coolpad',
    'C5': 'Condor',
    'CW': 'Cowon',
    'CU': 'Cube',
    'CY': 'Coby Kyros',
    'C6': 'Comio',
    'C7': 'ComTrade Tesla',
    'C8': 'Concord',
    'CX': 'Crescent',
    'C4': 'Cyrus',
    'DA': 'Danew',
    'DT': 'Datang',
    'D1': 'Datsun',
    'DE': 'Denver',
    'DX': 'DEXP',
    'DS': 'Desay',
    'DB': 'Dbtel',
    'DC': 'DoCoMo',
    'DG': 'Dialog',
    'DI': 'Dicam',
    'D3': 'Digicel',
    'DD': 'Digiland',
    'D2': 'Digma',
    'DL': 'Dell',
    'DN': 'DNS',
    'DM': 'DMM',
    'DO': 'Doogee',
    'DV': 'Doov',
    'DP': 'Dopod',
    'DR': 'Doro',
    'DU': 'Dune HD',
    'EB': 'E-Boda',
    'EA': 'EBEST',
    'EC': 'Ericsson',
    'ED': 'Energizer',
    'E4': 'Echo Mobiles',
    'ES': 'ECS',
    'E6': 'EE',
    'EI': 'Ezio',
    'EM': 'Eks Mobility',
    'EL': 'Elephone',
    'EP': 'Easypix',
    'EK': 'EKO',
    'E1': 'Energy Sistem',
    'ER': 'Ericy',
    'EE': 'Essential',
    'EN': 'Eton',
    'E2': 'Essentielb',
    'ET': 'eTouch',
    'EV': 'Evertek',
    'E3': 'Evolio',
    'EO': 'Evolveo',
    'EX': 'Explay',
    'E5': 'Extrem',
    'EZ': 'Ezze',
    'FA': 'Fairphone',
    'FI': 'FiGO',
    'FL': 'Fly',
    'FT': 'Freetel',
    'FR': 'Forstar',
    'FO': 'Foxconn',
    'FN': 'FNB',
    'FU': 'Fujitsu',
    'GT': 'G-TiDE',
    'GM': 'Garmin-Asus',
    'GA': 'Gateway',
    'GD': 'Gemini',
    'GE': 'Geotel',
    'GH': 'Ghia',
    'GI': 'Gionee',
    'GG': 'Gigabyte',
    'GS': 'Gigaset',
    'GC': 'GOCLEVER',
    'GL': 'Goly',
    'GO': 'Google',
    'G1': 'GoMobile',
    'GR': 'Gradiente',
    'GP': 'Grape',
    'GU': 'Grundig',
    'HF': 'Hafury',
    'HA': 'Haier',
    'HS': 'Hasee',
    'HE': 'HannSpree',
    'HI': 'Hisense',
    'HL': 'Hi-Level',
    'HM': 'Homtom',
    'HO': 'Hosin',
    'HP': 'HP',
    'HT': 'HTC',
    'HU': 'Huawei',
    'HX': 'Humax',
    'HY': 'Hyrican',
    'HN': 'Hyundai',
    'IA': 'Ikea',
    'IB': 'iBall',
    'IJ': 'i-Joy',
    'IY': 'iBerry',
    'IH': 'iHunt',
    'IK': 'iKoMo',
    'IE': 'iView',
    'IM': 'i-mate',
    'I1': 'iOcean',
    'I2': 'IconBIT',
    'IL': 'IMO Mobile',
    'IW': 'iNew',
    'IP': 'iPro',
    'IF': 'Infinix',
    'I5': 'InnJoo',
    'IN': 'Innostream',
    'I4': 'Inoi',
    'II': 'Inkti',
    'IX': 'Intex',
    'IO': 'i-mobile',
    'IQ': 'INQ',
    'IT': 'Intek',
    'IV': 'Inverto',
    'I3': 'Impression',
    'IZ': 'iTel',
    'JA': 'JAY-Tech',
    'JI': 'Jiayu',
    'JO': 'Jolla',
    'KL': 'Kalley',
    'KA': 'Karbonn',
    'KD': 'KDDI',
    'K1': 'Kiano',
    'KI': 'Kingsun',
    'KG': 'Kogan',
    'KO': 'Konka',
    'KM': 'Komu',
    'KB': 'Koobee',
    'KT': 'K-Touch',
    'KH': 'KT-Tech',
    'KK': 'Kodak',
    'KP': 'KOPO',
    'KW': 'Konrow',
    'KR': 'Koridy',
    'K2': 'KRONO',
    'KS': 'Kempler & Strauss',
    'KU': 'Kumai',
    'KY': 'Kyocera',
    'KZ': 'Kazam',
    'KE': 'Krüger&Matz',
    'LQ': 'LAIQ',
    'L2': 'Landvo',
    'LV': 'Lava',
    'LA': 'Lanix',
    'LC': 'LCT',
    'L5': 'Leagoo',
    'LD': 'Ledstar',
    'L1': 'LeEco',
    'L4': 'Lemhoov',
    'LE': 'Lenovo',
    'LN': 'Lenco',
    'LT': 'Leotec',
    'LP': 'Le Pan',
    'LG': 'LG',
    'LI': 'Lingwin',
    'LO': 'Loewe',
    'LM': 'Logicom',
    'L3': 'Lexand',
    'LX': 'Lexibook',
    'LY': 'LYF',
    'MN': 'M4tel',
    'MJ': 'Majestic',
    'MA': 'Manta Multimedia',
    'MW': 'Maxwest',
    'MB': 'Mobistel',
    'M3': 'Mecer',
    'MD': 'Medion',
    'M2': 'MEEG',
    'M1': 'Meizu',
    'ME': 'Metz',
    'MX': 'MEU',
    'MI': 'MicroMax',
    'M5': 'MIXC',
    'M6': 'Mobiistar',
    'MC': 'Mediacom',
    'MK': 'MediaTek',
    'MO': 'Mio',
    'M7': 'Miray',
    'MM': 'Mpman',
    'M4': 'Modecom',
    'MF': 'Mofut',
    'MR': 'Motorola',
    'MV': 'Movic',
    'MS': 'Microsoft',
    'M9': 'MTC',
    'MP': 'MegaFon',
    'MZ': 'MSI',
    'MU': 'Memup',
    'MT': 'Mitsubishi',
    'ML': 'MLLED',
    'MQ': 'M.T.T.',
    'N4': 'MTN',
    'MY': 'MyPhone',
    'MG': 'MyWigo',
    'M8': 'Myria',
    'N3': 'Navon',
    'NE': 'NEC',
    'NF': 'Neffos',
    'NA': 'Netgear',
    'NU': 'NeuImage',
    'NG': 'NGM',
    'NO': 'Nous',
    'NI': 'Nintendo',
    'N1': 'Noain',
    'N2': 'Nextbit',
    'NK': 'Nokia',
    'NV': 'Nvidia',
    'NB': 'Noblex',
    'NM': 'Nomi',
    'NL': 'NUU Mobile',
    'NY': 'NYX Mobile',
    'NN': 'Nikon',
    'NW': 'Newgen',
    'NX': 'Nexian',
    'NT': 'NextBook',
    'O3': 'O+',
    'OB': 'Obi',
    'O1': 'Odys',
    'OD': 'Onda',
    'ON': 'OnePlus',
    'OP': 'OPPO',
    'OR': 'Orange',
    'OT': 'O2',
    'OK': 'Ouki',
    'OU': 'OUYA',
    'OO': 'Opsson',
    'OV': 'Overmax',
    'OY': 'Oysters',
    'OW': 'öwn',
    'PN': 'Panacom',
    'PA': 'Panasonic',
    'PB': 'PCBOX',
    'PC': 'PCD',
    'PD': 'PCD Argentina',
    'PE': 'PEAQ',
    'PG': 'Pentagram',
    'PH': 'Philips',
    'PI': 'Pioneer',
    'PL': 'Polaroid',
    'P9': 'Primepad',
    'PM': 'Palm',
    'PO': 'phoneOne',
    'PT': 'Pantech',
    'PY': 'Ployer',
    'P4': 'Plum',
    'PV': 'Point of View',
    'PP': 'PolyPad',
    'P2': 'Pomp',
    'P3': 'PPTV',
    'PS': 'Positivo',
    'PR': 'Prestigio',
    'P1': 'ProScan',
    'PU': 'PULID',
    'QI': 'Qilive',
    'QT': 'Qtek',
    'QM': 'QMobile',
    'QA': 'Quantum',
    'QU': 'Quechua',
    'RA': 'Ramos',
    'RC': 'RCA Tablets',
    'RB': 'Readboy',
    'RI': 'Rikomagic',
    'RV': 'Riviera',
    'RM': 'RIM',
    'RK': 'Roku',
    'RO': 'Rover',
    'RT': 'RT Project',
    'SQ': 'Santin BiTBiZ',
    'SA': 'Samsung',
    'S0': 'Sanei',
    'SD': 'Sega',
    'SL': 'Selfix',
    'SE': 'Sony Ericsson',
    'S1': 'Sencor',
    'SF': 'Softbank',
    'SX': 'SFR',
    'SG': 'Sagem',
    'SH': 'Sharp',
    'SI': 'Siemens',
    'SJ': 'Silent Circle',
    'SN': 'Sendo',
    'S6': 'Senseit',
    'SW': 'Sky',
    'SK': 'Skyworth',
    'SC': 'Smartfren',
    'SO': 'Sony',
    'OI': 'Sonim',
    'SP': 'Spice',
    'SU': 'SuperSonic',
    'S5': 'Supra',
    'SV': 'Selevision',
    'SY': 'Sanyo',
    'SM': 'Symphony',
    'SR': 'Smart',
    'S7': 'Smartisan',
    'S4': 'Star',
    'SB': 'STF Mobile',
    'S8': 'STK',
    'S9': 'Savio',
    'ST': 'Storex',
    'S2': 'Stonex',
    'S3': 'SunVan',
    'SZ': 'Sumvision',
    'SS': 'SWISSMOBILITY',
    'TA': 'Tesla',
    'T5': 'TB Touch',
    'TC': 'TCL',
    'T7': 'Teclast',
    'TE': 'Telit',
    'T4': 'ThL',
    'TH': 'TiPhone',
    'TB': 'Tecno Mobile',
    'TP': 'TechPad',
    'TD': 'Tesco',
    'TI': 'TIANYU',
    'TG': 'Telego',
    'TL': 'Telefunken',
    'T2': 'Telenor',
    'TM': 'T-Mobile',
    'TN': 'Thomson',
    'TQ': 'Timovi',
    'T1': 'Tolino',
    'T9': 'Top House',
    'TO': 'Toplux',
    'T8': 'Touchmate',
    'TS': 'Toshiba',
    'TT': 'TechnoTrend',
    'T6': 'TrekStor',
    'T3': 'Trevi',
    'TU': 'Tunisie Telecom',
    'TR': 'Turbo-X',
    'TV': 'TVC',
    'TX': 'TechniSat',
    'TZ': 'teXet',
    'UC': 'U.S. Cellular',
    'UH': 'Uhappy',
    'UL': 'Ulefone',
    'UO': 'Unnecto',
    'UN': 'Unowhy',
    'US': 'Uniscope',
    'UX': 'Unimax',
    'UM': 'UMIDIGI',
    'UU': 'Unonu',
    'UT': 'UTStarcom',
    'VA': 'Vastking',
    'VD': 'Videocon',
    'VE': 'Vertu',
    'VI': 'Vitelcom',
    'VK': 'VK Mobile',
    'VS': 'ViewSonic',
    'VT': 'Vestel',
    'VR': 'Vernee',
    'VL': 'Verykool',
    'VV': 'Vivo',
    'VX': 'Vertex',
    'V3': 'Vinsoc',
    'V2': 'Vonino',
    'VG': 'Vorago',
    'V1': 'Voto',
    'VO': 'Voxtel',
    'VF': 'Vodafone',
    'VZ': 'Vizio',
    'VW': 'Videoweb',
    'VU': 'Vulcan',
    'WA': 'Walton',
    'WF': 'Wileyfox',
    'WN': 'Wink',
    'WM': 'Weimei',
    'WE': 'WellcoM',
    'WY': 'Wexler',
    'WI': 'Wiko',
    'WL': 'Wolder',
    'WG': 'Wolfgang',
    'WO': 'Wonu',
    'W1': 'Woo',
    'WX': 'Woxter',
    'XV': 'X-View',
    'XI': 'Xiaomi',
    'XN': 'Xion',
    'XO': 'Xolo',
    'YA': 'Yarvik',
    'Y2': 'Yes',
    'YE': 'Yezz',
    'Y1': 'Yu',
    'YU': 'Yuandao',
    'YS': 'Yusun',
    'YT': 'Ytone',
    'ZE': 'Zeemi',
    'ZK': 'Zenek',
    'ZO': 'Zonda',
    'ZP': 'Zopo',
    'ZT': 'ZTE',
    'ZU': 'Zuum',
    'ZN': 'Zen',
    'ZY': 'Zync',
    # legacy brands, might be removed in future versions
    'WB': 'Web TV',
    'XX': 'Unknown',
}

# flip Abbrev / Brand for fast membership testing
BRAND_TO_ABBREV = {brand.lower(): abbrev for abbrev, brand in DEVICE_BRANDS.items()}


class BaseDeviceParser(Parser):

    DEVICE_NAMES = DEVICE_NAMES

    DEVICE_TYPE_DESKTOP = DEVICE_TYPE_DESKTOP
    DEVICE_TYPE_SMARTPHONE = DEVICE_TYPE_SMARTPHONE
    DEVICE_TYPE_TABLET = DEVICE_TYPE_TABLET
    DEVICE_TYPE_FEATURE_PHONE = DEVICE_TYPE_FEATURE_PHONE
    DEVICE_TYPE_CONSOLE = DEVICE_TYPE_CONSOLE
    DEVICE_TYPE_TV = DEVICE_TYPE_TV
    DEVICE_TYPE_CAR_BROWSER = DEVICE_TYPE_CAR_BROWSER
    DEVICE_TYPE_SMART_DISPLAY = DEVICE_TYPE_SMART_DISPLAY
    DEVICE_TYPE_CAMERA = DEVICE_TYPE_CAMERA
    DEVICE_TYPE_PORTABLE_MEDIA_PAYER = DEVICE_TYPE_PORTABLE_MEDIA_PAYER
    DEVICE_TYPE_PHABLET = DEVICE_TYPE_PHABLET

    DEVICE_TYPES = DEVICE_TYPES

    DEVICE_BRANDS = DEVICE_BRANDS

    BRAND_TO_ABBREV = BRAND_TO_ABBREV


__all__ = (
    'BaseDeviceParser',
    'DEVICE_BRANDS',
    'MOBILE_DEVICE_TYPES',
)
