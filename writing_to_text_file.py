#!/usr/bin/env python


cities = ['Middleton', 'Spring Green', 'Madison', 'Forest', 'Green Bay',
        'Rio', 'Kiel']

with open('wi_cities1.txt', 'w') as wi_cities1_out:
    with open('wi_cities2.txt', 'w') as wi_cities2_out:
        for city in cities:
            if len(city) > 6:
                wi_cities1_out.write(city + '\n')
            else:
                wi_cities2_out.write(city + '\n')


