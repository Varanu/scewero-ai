from pathlib import Path

DATA_DIR = Path('../data/unziped_data')
UAT_ID = '403'

FIGURE_WIDTH = 14
FIGURE_HEIGHT = 6
FONT_SIZE = 11
PLT_STYLE = 'seaborn-v0_8-whitegrid'

MORTALITY_RISK_THRESHOLD = 38  # °C – UTCI_MX or TX above this = extreme day
UTCI_HEAT_STRESS = 32          # °C – strong heat stress (UTCI)
TX_EXTREME = 35                # °C – extreme max temperature
HUMIDITY_HUMID_HEAT = 80       # % RH – humid heat (sweating ineffective)
HUMIDITY_DRY_HEAT = 50         # % RH – dry heat (dehydration risk)

UTCI_COMFORT_LOW = 9           # °C – lower bound of comfortable UTCI range
UTCI_COMFORT_HIGH = 26         # °C – upper bound of comfortable UTCI range

UTCI_REFERENCE = 'https://climate-adapt.eea.europa.eu/en/metadata/indicators/high-utci-days'

TOP_N_DAYS = 10                # number of extreme days to display

NUMERIC_COLS = [
    'CC', 'RH_AVG', 'RH_MN', 'RH_MX',
    'WS_AVG', 'WS_MX',
    'TG', 'TN', 'TX',
    'UTCI_MN', 'UTCI_MX',
]

