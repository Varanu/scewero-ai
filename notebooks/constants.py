from pathlib import Path

# ── Base directory (resolved relative to this file, not CWD) ─────────────────
_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR        = _ROOT / 'data' / 'unziped_data'
FIRST_PHASE_DIR = _ROOT / 'data' / 'first_phase'
FIGURES_DIR     = _ROOT / 'data' / 'first_phase' / 'figures'

UAT_ID_CLUJ_NAPOCA = '54975'

# ── Plot defaults ─────────────────────────────────────────────────────────────
FIGURE_WIDTH  = 14
FIGURE_HEIGHT = 6
FONT_SIZE     = 11
PLT_STYLE     = 'seaborn-v0_8-whitegrid'

# ── Climate thresholds ────────────────────────────────────────────────────────
MORTALITY_RISK_THRESHOLD = 38   # °C – UTCI_MX or TX above this = extreme day
UTCI_HEAT_STRESS         = 32   # °C – strong heat stress (UTCI)
TX_EXTREME               = 35   # °C – extreme max temperature
HUMIDITY_HUMID_HEAT      = 80   # % RH – humid heat (sweating ineffective)
HUMIDITY_DRY_HEAT        = 50   # % RH – dry heat (dehydration risk)

UTCI_COMFORT_LOW  = 9           # °C – lower bound of comfortable UTCI range
UTCI_COMFORT_HIGH = 26          # °C – upper bound of comfortable UTCI range

UTCI_REFERENCE = 'https://climate-adapt.eea.europa.eu/en/metadata/indicators/high-utci-days'

TOP_N_DAYS = 10                 # number of extreme days to display

NUMERIC_COLS = [
    'CC', 'RH_AVG', 'RH_MN', 'RH_MX',
    'WS_AVG', 'WS_MX',
    'TG', 'TN', 'TX',
    'UTCI_MN', 'UTCI_MX',
]

# ── Mortality data constants ─────────────────────────────────────────────────
MORTA_DIR        = _ROOT / 'data' / 'raw' / 'Mortalitati'
MORTA_OUTPUT_DIR = FIRST_PHASE_DIR
SIRUTA_CODE      = int(UAT_ID_CLUJ_NAPOCA)
DBF_ENCODINGS    = ['cp852', 'cp1250', 'latin-1']   # fallback chain for Romanian DBFs

# ── Analysis period ───────────────────────────────────────────────────────────
ANALYSIS_YEAR_START = 1995
ANALYSIS_YEAR_END   = 2024
ANALYSIS_PERIOD     = f'{ANALYSIS_YEAR_START}–{ANALYSIS_YEAR_END}'

# ── Mortality EDA constants ──────────────────────────────────────────────────
SUMMER_MONTHS  = [6, 7, 8]
AGE_BINS       = [0, 1, 18, 40, 60, 75, 120]
AGE_LABELS     = ['infant', '1–17', '18–39', '40–59', '60–74', '75+']
MORTALITY_COLS = ['DAT_DEC', 'DAT_NAS', 'SEX', 'CODB', 'source_year']

