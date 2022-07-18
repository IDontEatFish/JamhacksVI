from webscrapping.webscrapper import tracker

global gloal_info
global_info = tracker()

def global_data_dict(global_info):

   
    global_data = {}
    info_list = ['Total Cases', 'New Cases', 'Total Deaths', 'Total Recovered', 'New Recovered', 'Active Cases', 'Serious Critical', 'Total Cases/ 1M population', 'Deaths/ 1M population', 'Total Tests', 'Total Tests', 'Tests / 1M population', 'Population' ]


    for x in global_info:
            global_data[x[0].capitalize()] = {info_list[0]: x[1], 
            info_list[1]: x[2], 
            info_list[2]: x[3], 
            info_list[3]: x[4], 
            info_list[4]: x[5], 
            info_list[5]: x[6], 
            info_list[6]: x[7],
            info_list[7]: x[8],
            info_list[8]: x[9],
            info_list[9]: x[10],
            info_list[10]: x[11],
            info_list[11]: x[12],
            info_list[12]: x[13]}   
            
    return(global_data)

def sorted_countries(global_info):
    countries_sorted = []
    for x in global_info:
        countries_sorted.append(x[0])
    return countries_sorted

        