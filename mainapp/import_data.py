import json
from models import Insight

def import_data():
    with open('json/jsondata.json', 'r') as file:
        json_data = json.load(file)

        for item in json_data:
            insight = Insight(
                end_year=item['end_year'],
                intensity=item['intensity'],
                sector=item['sector'],
                topic=item['topic'],
                insight=item['insight'],
                url=item['url'],
                region=item['region'],
                start_year=item['start_year'],
                impact=item['impact'],
                added=item['added'],
                published=item['published'],
                country=item['country'],
                relevance=item['relevance'],
                pestle=item['pestle'],
                source=item['source'],
                title=item['title'],
                likelihood=item['likelihood'],
            )
            insight.save()

if __name__ == "__main__":
    import_data()
