from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def compare_day_night(accidents):
    daytime_deaths = sum(item.dth_dnv_cnt for item in accidents if item.dght_cd == '1')
    nighttime_deaths = sum(item.dth_dnv_cnt for item in accidents if item.dght_cd == '2')

    daytime_minor_injuries = sum(item.sl_dnv_cnt for item in accidents if item.dght_cd == '1')
    nighttime_minor_injuries = sum(item.sl_dnv_cnt for item in accidents if item.dght_cd == '2')    

    labels = ['Daytime', 'Nighttime']
    deaths = [daytime_deaths, nighttime_deaths]
    minor_injuries = [daytime_minor_injuries, nighttime_minor_injuries] 
    x = range(len(labels))  
    fig, ax = plt.subplots()
    bar1 = ax.bar(x, deaths, width=0.4, label='Deaths', color='r', align='center')
    bar2 = ax.bar(x, minor_injuries, width=0.4, label='Minor Injuries', color='b', align='edge')    
    ax.set_xlabel('Time of Day')
    ax.set_ylabel('Count')
    ax.set_title('Comparison of Deaths and Minor Injuries by Time of Day')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend() 
    plt.show()
    
def plot_vehicle_stats_by_year(accidents):
    year_stats = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    for accident in accidents:
        if accident.wrngdo_isrty_vhcty_lclas_cd == "##":
            continue  # '##' 코드는 제외
        year_stats[accident.acc_year][accident.dmge_isrty_vhcty_lclas_cd][accident.wrngdo_isrty_vhcty_lclas_cd] += 1

    years = sorted(year_stats.keys())
    offender_types = set()
    victim_types = set()

    for year in years:
        for offender_type in year_stats[year].keys():
            offender_types.add(offender_type)
            victim_types.update(year_stats[year][offender_type].keys())

    offender_types = sorted(offender_types)
    victim_types = sorted(victim_types)
    ind = np.arange(len(years)) 

    bar_width = 0.1
    fig, ax = plt.subplots(figsize=(14, 8))

    for i, victim_type in enumerate(victim_types):
        counts = []
        for year in years:
            total_count = 0
            for offender_type in offender_types:
                total_count += year_stats[year][offender_type][victim_type]
            counts.append(total_count)
        
        ax.bar(ind + i * bar_width, counts, bar_width, label=f'Victim {victim_type}')

    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Accidents')
    ax.set_title('Yearly Accident Statistics by Offender and Victim Vehicle Types')
    ax.set_xticks(ind + bar_width * len(victim_types) / 2)
    ax.set_xticklabels(years)
    ax.legend()

    plt.show()
    
def plot_legal_violation_by_year(accidents):
    year_stats = defaultdict(lambda: defaultdict(int))

    for accident in accidents:
        year_stats[accident.acc_year][accident.aslt_vtr_cd] += 1

    years = sorted(year_stats.keys())
    violation_types = set()

    for year in years:
        violation_types.update(year_stats[year].keys())

    violation_types = sorted(violation_types)
    ind = np.arange(len(years)) 

    bar_width = 0.1
    fig, ax = plt.subplots(figsize=(14, 8))


    for i, violation_type in enumerate(violation_types):
        counts = []
        for year in years:
            counts.append(year_stats[year][violation_type])
        
        ax.bar(ind + i * bar_width, counts, bar_width, label=f'Violation {violation_type}')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Violations')
    ax.set_title('Yearly Legal Violations by Offender Vehicle Types')
    ax.set_xticks(ind + bar_width * len(violation_types) / 2)
    ax.set_xticklabels(years)
    ax.legend()

    plt.show()
    