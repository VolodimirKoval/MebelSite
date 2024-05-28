from datetime import datetime


def site_name(request):
    return {'site_name': 'Mebel of your dream'}


def footer_name_date(request):
    current_date = datetime.now()
    return {'footer_name_date': f'Copyright Mebel {current_date.year}'}
    