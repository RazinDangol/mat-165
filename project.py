import csv
import json
import requests

API_URL = "https://api.data.gov/ed/collegescorecard/v1/schools/?sort=2012.earnings.6_yrs_after_entry.percent_greater_than_25000%3Adesc&page={page}&school.operating=1&2014.student.size__range=0..&2014.academics.program_available.bachelors=true&school.ownership=1&school.degrees_awarded.predominant__range=1..3&school.degrees_awarded.highest__range=2..4&fields=id%2Cschool.name%2Cschool.city%2Cschool.state%2C2014.student.size%2Cschool.ownership%2Cschool.degrees_awarded.predominant%2C2014.cost.avg_net_price.overall%2C2014.completion.rate_suppressed.overall%2C2012.earnings.10_yrs_after_entry.median%2C2012.earnings.6_yrs_after_entry.percent_greater_than_25000%2Cschool.under_investigation&api_key=Xxf2NKtwfcXUd8K2hqawnlur6c0YY93xsNFwq0Dy"

page = 0
with open('data.csv','w+') as csvfile:
    fieldnames = ['school.name','school.state','school.city','2014.cost.avg_net_price.overall']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,lineterminator="\n")
    writer.writeheader()
    # Page loop
    while True:
        
        res = requests.get(API_URL.format(page=page))
        
        # request for json
        j = json.loads(res.text)

        # loop through result
        if len(j['results']) == 0:
            print("This is the end!!")
            break
        else:
             # append to csv with field school.name, school.state, school.city, 2014.cost.avg_net_price.overall
            print("Writing data of Page: {} {}".format(j['metadata']['page'],len(j['results'])))

            for item in j['results']:
                writer.writerow({'school.name':item['school.name'],'school.city':item['school.city'],'school.state':item['school.state'],'2014.cost.avg_net_price.overall':item['2014.cost.avg_net_price.overall']})
        page = page+1
       