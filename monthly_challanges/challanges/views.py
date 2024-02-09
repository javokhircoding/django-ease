from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthlychallanges = {
    "january" : "Eat no meat for the entire month!",
    "february" : "You know your birthday is in february",
    "march" : "Learn django for at least 20 minuts every day!",
    "april" : "Just don't be tired of typing!",
    "may" : "Who do you want to become?",
    "june" : "The actually trurh is on the next page!",
    "july" : "The actually truth is I can just copy them!",
    "august" : "And I'm gonna do that!",
    "september" : "Learn django for at least 20 minuts every day!",
    "october" : "Bruh, I missed october!",
    "november" : "I did a mistkake while typing october!",
    "december" : "Walk for at least 20 minuts every day!"
}


# Create your views here.

def monthly_challange_by_number(request, month):
    months = list(monthlychallanges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    else:
        forward_month = months[month - 1]
        return HttpResponseRedirect("/challanges/" + forward_month)


def monthly_challange(request, month):
    try:
        challange_text = monthlychallanges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challange_text)



'''
def monthly_challange(request, month):
    challange_text = None
    if month == "january":
        challange_text = "Eat no meat for the entire month!"
    elif month == "february":
        challange_text = "Walk for at least 20 minuts every day!"
    elif month == "march":
        challange_text = "Learn django for at least 20 minuts every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challange_text)
'''