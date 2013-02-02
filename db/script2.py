#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from BeautifulSoup import BeautifulSoup
import urllib2 

teams = {u'GSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2247&wjb=&wjb=', u'SIU': u'http://m.espn.go.com/ncf/clubhouse?teamId=79&wjb=&wjb=', u'BC': u'http://m.espn.go.com/ncf/clubhouse?teamId=103&wjb=&wjb=', u'MIA': u'http://m.espn.go.com/ncf/clubhouse?teamId=2390&wjb=&wjb=', u'SJSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=23&wjb=&wjb=', u'SHSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2534&wjb=&wjb=', u'MICH': u'http://m.espn.go.com/ncf/clubhouse?teamId=130&wjb=&wjb=', u'UTEP': u'http://m.espn.go.com/ncf/clubhouse?teamId=2638&wjb=&wjb=', u'NDSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2449&wjb=&wjb=', u'CONN': u'http://m.espn.go.com/ncf/clubhouse?teamId=41&wjb=&wjb=', u'PRE': u'http://m.espn.go.com/ncf/clubhouse?teamId=2506&wjb=&wjb=', u'LIB': u'http://m.espn.go.com/ncf/clubhouse?teamId=2335&wjb=&wjb=', u'SAM': u'http://m.espn.go.com/ncf/clubhouse?teamId=2535&wjb=&wjb=', u'PITT': u'http://m.espn.go.com/ncf/clubhouse?teamId=221&wjb=&wjb=', u'ELON': u'http://m.espn.go.com/ncf/clubhouse?teamId=2210&wjb=&wjb=', u'ARIZ': u'http://m.espn.go.com/ncf/clubhouse?teamId=12&wjb=&wjb=', u'OKST': u'http://m.espn.go.com/ncf/clubhouse?teamId=197&wjb=&wjb=', u'IDHO': u'http://m.espn.go.com/ncf/clubhouse?teamId=70&wjb=&wjb=', u'UAB': u'http://m.espn.go.com/ncf/clubhouse?teamId=5&wjb=&wjb=', u'SMU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2567&wjb=&wjb=', u'OKLA': u'http://m.espn.go.com/ncf/clubhouse?teamId=201&wjb=&wjb=', u'WEB': u'http://m.espn.go.com/ncf/clubhouse?teamId=2692&wjb=&wjb=', u'GT': u'http://m.espn.go.com/ncf/clubhouse?teamId=59&wjb=&wjb=', u'VAN': u'http://m.espn.go.com/ncf/clubhouse?teamId=238&wjb=&wjb=', u'FIU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2229&wjb=&wjb=', u'UTAH': u'http://m.espn.go.com/ncf/clubhouse?teamId=254&wjb=&wjb=', u'BYU': u'http://m.espn.go.com/ncf/clubhouse?teamId=252&wjb=&wjb=', u'FAMU': u'http://m.espn.go.com/ncf/clubhouse?teamId=50&wjb=&wjb=', u'WMU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2711&wjb=&wjb=', u'UNH': u'http://m.espn.go.com/ncf/clubhouse?teamId=160&wjb=&wjb=', u'NAVY': u'http://m.espn.go.com/ncf/clubhouse?teamId=2426&wjb=&wjb=', u'MURR': u'http://m.espn.go.com/ncf/clubhouse?teamId=93&wjb=&wjb=', u'HAW': u'http://m.espn.go.com/ncf/clubhouse?teamId=62&wjb=&wjb=', u'BGSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=189&wjb=&wjb=', u'APP': u'http://m.espn.go.com/ncf/clubhouse?teamId=2026&wjb=&wjb=', u'MIZZ': u'http://m.espn.go.com/ncf/clubhouse?teamId=142&wjb=&wjb=', u'TULN': u'http://m.espn.go.com/ncf/clubhouse?teamId=2655&wjb=&wjb=', u'SYR': u'http://m.espn.go.com/ncf/clubhouse?teamId=183&wjb=&wjb=', u'RICH': u'http://m.espn.go.com/ncf/clubhouse?teamId=257&wjb=&wjb=', u'RICE': u'http://m.espn.go.com/ncf/clubhouse?teamId=242&wjb=&wjb=', u'TOWS': u'http://m.espn.go.com/ncf/clubhouse?teamId=119&wjb=&wjb=', u'NIU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2459&wjb=&wjb=', u'KSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2306&wjb=&wjb=', u'CHAT': u'http://m.espn.go.com/ncf/clubhouse?teamId=236&wjb=&wjb=', u'GASO': u'http://m.espn.go.com/ncf/clubhouse?teamId=290&wjb=&wjb=', u'PEAY': u'http://m.espn.go.com/ncf/clubhouse?teamId=2046&wjb=&wjb=', u'CLEM': u'http://m.espn.go.com/ncf/clubhouse?teamId=228&wjb=&wjb=', u'EMU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2199&wjb=&wjb=', u'COLO': u'http://m.espn.go.com/ncf/clubhouse?teamId=38&wjb=&wjb=', u'ILST': u'http://m.espn.go.com/ncf/clubhouse?teamId=2287&wjb=&wjb=', u'FLA': u'http://m.espn.go.com/ncf/clubhouse?teamId=57&wjb=&wjb=', u'WCU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2717&wjb=&wjb=', u'CMU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2117&wjb=&wjb=', u'UCD': u'http://m.espn.go.com/ncf/clubhouse?teamId=302&wjb=&wjb=', u'YSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2754&wjb=&wjb=', u'MCNS': u'http://m.espn.go.com/ncf/clubhouse?teamId=2377&wjb=&wjb=', u'UGA': u'http://m.espn.go.com/ncf/clubhouse?teamId=61&wjb=&wjb=', u'TCU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2628&wjb=&wjb=', u'OSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=194&wjb=&wjb=', u'TXST': u'http://m.espn.go.com/ncf/clubhouse?teamId=326&wjb=&wjb=', u'TTU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2641&wjb=&wjb=', u'WVU': u'http://m.espn.go.com/ncf/clubhouse?teamId=277&wjb=&wjb=', u'LSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=99&wjb=&wjb=', u'TXSO': u'http://m.espn.go.com/ncf/clubhouse?teamId=2640&wjb=&wjb=', u'UVA': u'http://m.espn.go.com/ncf/clubhouse?teamId=258&wjb=&wjb=', u'NWST': u'http://m.espn.go.com/ncf/clubhouse?teamId=2466&wjb=&wjb=', u'UTM': u'http://m.espn.go.com/ncf/clubhouse?teamId=2630&wjb=&wjb=', u'TLSA': u'http://m.espn.go.com/ncf/clubhouse?teamId=202&wjb=&wjb=', u'AFA': u'http://m.espn.go.com/ncf/clubhouse?teamId=2005&wjb=&wjb=', u'VILL': u'http://m.espn.go.com/ncf/clubhouse?teamId=222&wjb=&wjb=', u'JKST': u'http://m.espn.go.com/ncf/clubhouse?teamId=2296&wjb=&wjb=', u'CSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=36&wjb=&wjb=', u'WOF': u'http://m.espn.go.com/ncf/clubhouse?teamId=2747&wjb=&wjb=', u'MISS': u'http://m.espn.go.com/ncf/clubhouse?teamId=145&wjb=&wjb=', u'EWU': u'http://m.espn.go.com/ncf/clubhouse?teamId=331&wjb=&wjb=', u'ME': u'http://m.espn.go.com/ncf/clubhouse?teamId=311&wjb=&wjb=', u'MD': u'http://m.espn.go.com/ncf/clubhouse?teamId=120&wjb=&wjb=', u'TENN': u'http://m.espn.go.com/ncf/clubhouse?teamId=2633&wjb=&wjb=', u'W&M;': u'http://m.espn.go.com/ncf/clubhouse?teamId=2729&wjb=&wjb=', u'UK': u'http://m.espn.go.com/ncf/clubhouse?teamId=96&wjb=&wjb=', u'IND': u'http://m.espn.go.com/ncf/clubhouse?teamId=84&wjb=&wjb=', u'WAKE': u'http://m.espn.go.com/ncf/clubhouse?teamId=154&wjb=&wjb=', u'IDST': u'http://m.espn.go.com/ncf/clubhouse?teamId=304&wjb=&wjb=', u'SFA': u'http://m.espn.go.com/ncf/clubhouse?teamId=2617&wjb=&wjb=', u'SDST': u'http://m.espn.go.com/ncf/clubhouse?teamId=2571&wjb=&wjb=', u'SDSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=21&wjb=&wjb=', u'PSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=213&wjb=&wjb=', u'IOWA': u'http://m.espn.go.com/ncf/clubhouse?teamId=2294&wjb=&wjb=', u'CSUS': u'http://m.espn.go.com/ncf/clubhouse?teamId=16&wjb=&wjb=', u'DUKE': u'http://m.espn.go.com/ncf/clubhouse?teamId=150&wjb=&wjb=', u'AKR': u'http://m.espn.go.com/ncf/clubhouse?teamId=2006&wjb=&wjb=', u'ILL': u'http://m.espn.go.com/ncf/clubhouse?teamId=356&wjb=&wjb=', u'NEB': u'http://m.espn.go.com/ncf/clubhouse?teamId=158&wjb=&wjb=', u'ISU': u'http://m.espn.go.com/ncf/clubhouse?teamId=66&wjb=&wjb=', u'SUU': u'http://m.espn.go.com/ncf/clubhouse?teamId=253&wjb=&wjb=', u'FSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=52&wjb=&wjb=', u'EKY': u'http://m.espn.go.com/ncf/clubhouse?teamId=2198&wjb=&wjb=', u'WYO': u'http://m.espn.go.com/ncf/clubhouse?teamId=2751&wjb=&wjb=', u'EIU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2197&wjb=&wjb=', u'AAMU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2010&wjb=&wjb=', u'TEM': u'http://m.espn.go.com/ncf/clubhouse?teamId=218&wjb=&wjb=', u'ASU': u'http://m.espn.go.com/ncf/clubhouse?teamId=9&wjb=&wjb=', u'ARMY': u'http://m.espn.go.com/ncf/clubhouse?teamId=349&wjb=&wjb=', u'NAU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2464&wjb=&wjb=', u'BSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=68&wjb=&wjb=', u'ND': u'http://m.espn.go.com/ncf/clubhouse?teamId=87&wjb=&wjb=', u'MSST': u'http://m.espn.go.com/ncf/clubhouse?teamId=344&wjb=&wjb=', u'TEX': u'http://m.espn.go.com/ncf/clubhouse?teamId=251&wjb=&wjb=', u'ECU': u'http://m.espn.go.com/ncf/clubhouse?teamId=151&wjb=&wjb=', u'MASS': u'http://m.espn.go.com/ncf/clubhouse?teamId=113&wjb=&wjb=', u'GRAM': u'http://m.espn.go.com/ncf/clubhouse?teamId=2755&wjb=&wjb=', u'STAN': u'http://m.espn.go.com/ncf/clubhouse?teamId=24&wjb=&wjb=', u'USM': u'http://m.espn.go.com/ncf/clubhouse?teamId=2572&wjb=&wjb=', u'NW': u'http://m.espn.go.com/ncf/clubhouse?teamId=77&wjb=&wjb=', u'BALL': u'http://m.espn.go.com/ncf/clubhouse?teamId=2050&wjb=&wjb=', u'UNT': u'http://m.espn.go.com/ncf/clubhouse?teamId=249&wjb=&wjb=', u'MINN': u'http://m.espn.go.com/ncf/clubhouse?teamId=135&wjb=&wjb=', u'WAG': u'http://m.espn.go.com/ncf/clubhouse?teamId=2681&wjb=&wjb=', u'CARK': u'http://m.espn.go.com/ncf/clubhouse?teamId=2110&wjb=&wjb=', u'UNC': u'http://m.espn.go.com/ncf/clubhouse?teamId=153&wjb=&wjb=', u'FRES': u'http://m.espn.go.com/ncf/clubhouse?teamId=278&wjb=&wjb=', u'UNI': u'http://m.espn.go.com/ncf/clubhouse?teamId=2460&wjb=&wjb=', u'UNLV': u'http://m.espn.go.com/ncf/clubhouse?teamId=2439&wjb=&wjb=', u'UNM': u'http://m.espn.go.com/ncf/clubhouse?teamId=167&wjb=&wjb=', u'MEM': u'http://m.espn.go.com/ncf/clubhouse?teamId=235&wjb=&wjb=', u'UCLA': u'http://m.espn.go.com/ncf/clubhouse?teamId=26&wjb=&wjb=', u'ALA': u'http://m.espn.go.com/ncf/clubhouse?teamId=333&wjb=&wjb=', u'WIS': u'http://m.espn.go.com/ncf/clubhouse?teamId=275&wjb=&wjb=', u'KU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2305&wjb=&wjb=', u'INST': u'http://m.espn.go.com/ncf/clubhouse?teamId=282&wjb=&wjb=', u'ORE': u'http://m.espn.go.com/ncf/clubhouse?teamId=2483&wjb=&wjb=', u'MORG': u'http://m.espn.go.com/ncf/clubhouse?teamId=2415&wjb=&wjb=', u'PUR': u'http://m.espn.go.com/ncf/clubhouse?teamId=2509&wjb=&wjb=', u'M-OH': u'http://m.espn.go.com/ncf/clubhouse?teamId=193&wjb=&wjb=', u'USF': u'http://m.espn.go.com/ncf/clubhouse?teamId=58&wjb=&wjb=', u'USC': u'http://m.espn.go.com/ncf/clubhouse?teamId=30&wjb=&wjb=', u'MSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=127&wjb=&wjb=', u'CAL': u'http://m.espn.go.com/ncf/clubhouse?teamId=25&wjb=&wjb=', u'CIN': u'http://m.espn.go.com/ncf/clubhouse?teamId=2132&wjb=&wjb=', u'NEV': u'http://m.espn.go.com/ncf/clubhouse?teamId=2440&wjb=&wjb=', u'BAY': u'http://m.espn.go.com/ncf/clubhouse?teamId=239&wjb=&wjb=', u'WASH': u'http://m.espn.go.com/ncf/clubhouse?teamId=264&wjb=&wjb=', u'USU': u'http://m.espn.go.com/ncf/clubhouse?teamId=328&wjb=&wjb=', u'AUB': u'http://m.espn.go.com/ncf/clubhouse?teamId=2&wjb=&wjb=', u'WSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=265&wjb=&wjb=', u'TOL': u'http://m.espn.go.com/ncf/clubhouse?teamId=2649&wjb=&wjb=', u'LOU': u'http://m.espn.go.com/ncf/clubhouse?teamId=97&wjb=&wjb=', u'ORST': u'http://m.espn.go.com/ncf/clubhouse?teamId=204&wjb=&wjb=', u'SCAR': u'http://m.espn.go.com/ncf/clubhouse?teamId=2579&wjb=&wjb=', u'SEMO': u'http://m.espn.go.com/ncf/clubhouse?teamId=2546&wjb=&wjb=', u'LAMR': u'http://m.espn.go.com/ncf/clubhouse?teamId=2320&wjb=&wjb=', u'MRSH': u'http://m.espn.go.com/ncf/clubhouse?teamId=276&wjb=&wjb=', u'SAV': u'http://m.espn.go.com/ncf/clubhouse?teamId=2542&wjb=&wjb=', u'TXA': u'http://m.espn.go.com/ncf/clubhouse?teamId=2837&wjb=&wjb=', u'FAU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2226&wjb=&wjb=', u'UCF': u'http://m.espn.go.com/ncf/clubhouse?teamId=2116&wjb=&wjb=', u'LT': u'http://m.espn.go.com/ncf/clubhouse?teamId=2348&wjb=&wjb=', u'UTSA': u'http://m.espn.go.com/ncf/clubhouse?teamId=2636&wjb=&wjb=', u'SOU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2582&wjb=&wjb=', u'OHIO': u'http://m.espn.go.com/ncf/clubhouse?teamId=195&wjb=&wjb=', u'UNCO': u'http://m.espn.go.com/ncf/clubhouse?teamId=2458&wjb=&wjb=', u'BUFF': u'http://m.espn.go.com/ncf/clubhouse?teamId=2084&wjb=&wjb=', u'TA&M;': u'http://m.espn.go.com/ncf/clubhouse?teamId=245&wjb=&wjb=', u'KENT': u'http://m.espn.go.com/ncf/clubhouse?teamId=2309&wjb=&wjb=', u'MTU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2393&wjb=&wjb=', u'MOSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=2623&wjb=&wjb=', u'HOW': u'http://m.espn.go.com/ncf/clubhouse?teamId=47&wjb=&wjb=', u'TROY': u'http://m.espn.go.com/ncf/clubhouse?teamId=2653&wjb=&wjb=', u'HOU': u'http://m.espn.go.com/ncf/clubhouse?teamId=248&wjb=&wjb=', u'VT': u'http://m.espn.go.com/ncf/clubhouse?teamId=259&wjb=&wjb=', u'ULL': u'http://m.espn.go.com/ncf/clubhouse?teamId=309&wjb=&wjb=', u'ULM': u'http://m.espn.go.com/ncf/clubhouse?teamId=2433&wjb=&wjb=', u'SOAL': u'http://m.espn.go.com/ncf/clubhouse?teamId=6&wjb=&wjb=', u'NMSU': u'http://m.espn.go.com/ncf/clubhouse?teamId=166&wjb=&wjb=', u'NCST': u'http://m.espn.go.com/ncf/clubhouse?teamId=152&wjb=&wjb=', u'SELA': u'http://m.espn.go.com/ncf/clubhouse?teamId=2545&wjb=&wjb=', u'ARST': u'http://m.espn.go.com/ncf/clubhouse?teamId=2032&wjb=&wjb=', u'JVST': u'http://m.espn.go.com/ncf/clubhouse?teamId=55&wjb=&wjb=', u'NICH': u'http://m.espn.go.com/ncf/clubhouse?teamId=2447&wjb=&wjb=', u'RUTG': u'http://m.espn.go.com/ncf/clubhouse?teamId=164&wjb=&wjb=', u'ARK': u'http://m.espn.go.com/ncf/clubhouse?teamId=8&wjb=&wjb=', u'WKU': u'http://m.espn.go.com/ncf/clubhouse?teamId=98&wjb=&wjb='}

#print len(teams)

for k,url in teams.items():
    req = urllib2.Request(url)
    html = (urllib2.urlopen(req)).read()
    soup = BeautifulSoup(html)
    tn = soup.find('td', attrs={'class':'teamHeader', 'valign':'middle'}).find('b').getText()
    print "INSERT INTO teams (sport,full,short) VALUES ('ncf','{0}','{1}');".format(tn,k)
