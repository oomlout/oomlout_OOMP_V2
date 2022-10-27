import OOMP
import OOMP_csv_BASE

def make():
    OOMP_csv_BASE.makeCSVSummaries()
    for item in OOMP.items:
        OOMP_csv_BASE.makeCSVFile(item)
