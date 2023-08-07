from datetime import date

def curr_year(request):
    curr_year = date.today().year
    curr_year_start = str(date(curr_year, 1, 1))

    return {'curr_year_start': curr_year_start}

