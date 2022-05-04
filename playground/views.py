from unicodedata import category
from django.shortcuts import render
from playground.models import Category, Country, Ytchannel, Ytviews, Video

# Create your views here.
def home(request):
    return render(request, 'base.html')

def get_video_by_year(request, year):
    print('In the function')
    categories = Category.objects.all()
    for c in categories:
        print(c)
    return render(request, 'video_detail.html', {'categories': categories})

def get_videos(request):
    y = request.GET.get('year', '')
    c = request.GET.get('category', '')
    if ( y == 'all' and c == 'all' ) or (y == '' and c == ''):
        videos = Video.objects.raw('SELECT * FROM playground_video LIMIT 20')
    elif (y == 'all'):
        videos = Video.objects.aggregate(max_likes=max('Ytviews__view_count'), max_view_count=max('Ytviews__count')).filter(Video__country_code='US', Video__category_id=c)
    elif (c == 'all'):
        videos = Video.objects.aggregate(max_likes=max('Ytviews__view_count'), max_view_count=max('Ytviews__count')).filter(Video__country_code='US', Video__published_at__gte=y, Video__published_at__lt=y)
    else:
        videos = Video.objects.aggregate(max_likes=max('Ytviews__view_count'), max_view_count=max('Ytviews__count')).filter(Video__country_code='US', Video__published_at__gte=y, Video__published_at__lt=y, Video__category_id=c)
    return render(request, 'video_detail.html', {'videos': videos, 'y': y, 'c': c}) 