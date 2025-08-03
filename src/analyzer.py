# src/analyzer.py
def whale_score(trade):
    score = 0
    if trade['CongressPerson'] in ["Pelosi", "Schumer", "McConnell"]:
        score += 3
    if trade['Amount'] and ">$100K" in trade['Amount']:
        score += 2
    if trade['Type'] == "Purchase":
        score += 1
    return score

def confidence_score(ticker_trades):
    unique_people = set([t['CongressPerson'] for t in ticker_trades])
    avg_whale = sum(whale_score(t) for t in ticker_trades) / len(ticker_trades)
    return round(len(unique_people) * avg_whale / 10, 2)
