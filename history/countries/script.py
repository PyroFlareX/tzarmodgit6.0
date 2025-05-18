import os

# List of all tags
tags = [
    "LUX", "LIT", "EST", "LAT", "SER", "FIN", "IRE", "ARG", "BHU", "BOL", "BRA", "CHL", "COL", "COS",
    "ECU", "ELS", "ETH", "GUA", "HON", "KOR", "LIB", "MEN", "NEP", "NIC", "PAN", "PHI", "PRU", "SAU",
    "SIK", "TIB", "URG", "VEN", "YUN", "TAN", "PAR", "CUB", "DOM", "HAI", "YEM", "OMA", "SLO", "CRO",
    "GXC", "PRC", "SHX", "XSM", "LEB", "JOR", "SYR", "EGY", "LBA", "WGR", "DDR", "PAL", "ISR", "VIN",
    "CAM", "INS", "LAO", "MNT", "UKR", "GEO", "AZR", "ARM", "BLR", "ANG", "MZB", "ZIM", "COG", "KEN",
    "PAK", "BOT", "BAH", "BAN", "BLZ", "BRM", "CRC", "GDL", "GYA", "JAM", "JAN", "KYR", "MAD", "MOL",
    "PNG", "PUE", "QAT", "SCO", "SRL", "SUR", "TAJ", "TRI", "TMS", "UAE", "UZB", "KUW", "CYP", "MLT",
    "ALG", "MOR", "TUN", "SUD", "ERI", "DJI", "SOM", "UGA", "RWA", "BRD", "TZN", "ZAM", "MLW", "GAB",
    "RCG", "EQG", "CMR", "CAR", "CHA", "NGA", "DAH", "TOG", "GHA", "IVO", "VOL", "MLI", "SIE", "GNA",
    "GNB", "SEN", "GAM", "WLS", "NGR", "CSA", "USB", "MRT", "NMB", "WES", "BAS", "CAY", "MLD", "FIJ",
    "FSM", "TAH", "GUM", "SOL", "SAM", "HAW", "SLV", "BOS", "HRZ", "MAC", "NIR", "BAY", "MEK", "PRE",
    "SAX", "HAN", "WUR", "SHL", "CAT", "NAV", "GLC", "ADU", "BRI", "OCC", "COR", "KUR", "TRA", "DNZ",
    "SIL", "KSH", "DON", "KUB", "BUK", "ALT", "KAL", "KAR", "CRI", "TAT", "CIN", "DAG", "BYA", "CKK",
    "FER", "YAK", "VLA", "KKP", "YAM", "TAY", "OVO", "NEN", "KOM", "ABK", "KBK", "NOA", "VGE", "BSK",
    "KHI", "UDM", "CHU", "MEL", "RIF", "HAR", "TIG", "AFA", "BEG", "GBA", "SID", "ORO", "QEM", "KHA",
    "AOI", "LBV", "PAP", "TOS", "SPM", "TTS", "SMI", "GRN", "RAP", "YUC", "RIG", "QUE", "KAT", "BIA",
    "WLA", "CBV", "BAR", "EVE", "SOK", "THU", "HES", "RHI", "UBD", "KOS", "RKB", "RKN", "RKG", "RKU",
    "RKT", "RKL", "GEN", "RKH", "RKI", "RKC", "RGB", "RKA", "RNA", "RKV", "RAN", "RCO", "RUS", "RHD",
    "RAR", "ROA", "RAA", "GAR", "INC", "MIS", "MAY", "INU", "CHR", "ITZ", "NAH", "IAS", "DIP", "PSH",
    "HYD", "MYS", "RJP", "CIP", "RAS", "NWF", "KAS", "MPU", "WIS", "KOL", "KHL", "SIN", "KLT", "SKK",
    "FSA", "ASY", "BHR", "IMO", "BLC", "AMR"
]

# Create empty .txt files for each tag
for tag in tags:
    filename = f"{tag}.txt"
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            pass  # Create an empty file
        print(f"Created: {filename}")
    else:
        print(f"Already exists: {filename}")