from django.shortcuts import render

# Create your views here.

lots = [
    {
        'id' : 1,
        'title' : '1',
        'description' : '1',
        'start_price' : 1,
        'current_price' : 1,
        'end_price' : 1,
    },
    {
        'id' : 2,
        'title' : '2',
        'description' : '2',
        'start_price' : 2,
        'current_price' : 2,
        'end_price' : 2,
    },
]

def lots_list(request):
    return render(request, "lots/list.html", {'lots' : lots})


def lots_detail(request, id):
    return render(request, "lots/detail.html", {'lot' : lots[id - 1]})