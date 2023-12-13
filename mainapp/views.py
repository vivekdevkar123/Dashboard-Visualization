# views.py

import json
from datetime import datetime
from django.shortcuts import HttpResponse
from rest_framework import generics
from .models import Insight
from .serializers import InsightSerializer

class InsightList(generics.ListCreateAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

class InsightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer

def import_data_view(request):
    try:
        with open('mainapp/static/json/jsondata.json', 'r') as file:
            json_data = json.load(file)

            for item in json_data:
                # Convert the 'added' date string to the correct format
                added_date_str = item.get('added', '')
                added_date = datetime.strptime(added_date_str, '%B, %d %Y %H:%M:%S') if added_date_str else None

                # Convert the 'published' date string to the correct format
                published_date_str = item.get('published', '')
                published_date = datetime.strptime(published_date_str, '%B, %d %Y %H:%M:%S') if published_date_str else None

                try:
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
                        added=added_date,
                        published=published_date,
                        country=item['country'],
                        relevance=item['relevance'],
                        pestle=item['pestle'],
                        source=item['source'],
                        title=item['title'],
                        likelihood=item['likelihood'],
                    )
                    insight.save()
                except Exception as e:
                    print(f"Error saving record: {item}")
                    print(f"Exception: {e}")

        return HttpResponse("Data import successful.")
    except Exception as e:
        return HttpResponse(f"Error: {e}")
