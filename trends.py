from pytrends.request import TrendReq

def fetch_google_trends(keywords):
    pytrends = TrendReq()
    pytrends.build_payload(keywords, cat=0, timeframe='now 7-d', geo='', gprop='')
    data = pytrends.interest_over_time().reset_index()
    result = []
    for keyword in keywords:
        for i, row in data.iterrows():
            result.append({
                'date': row['date'],
                'value': row[keyword],
                'keyword': keyword
            })
    return result
