import re;
import math;
input1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""";
input2 = """seeds: 2276375722 160148132 3424292843 82110297 1692203766 342813967 3289792522 103516087 2590548294 590357761 1365412380 80084180 3574751516 584781136 4207087048 36194356 1515742281 174009980 6434225 291842774

seed-to-soil map:
4170452318 3837406401 124514978
2212408060 1593776674 105988696
3837406401 4016132523 278834773
1475766470 1699765370 492158296
3698488336 1475766470 118010204
2318396756 2191923666 46351359
4116241174 3961921379 54211144
2193579298 3791037069 18828762
2364748115 2578360543 354997036
3085506703 3439828590 106510622
1967924766 3546339212 219021823
2719745151 3765361035 25676034
2745421185 2238275025 340085518
2186946589 3809865831 6632709
3192017325 2933357579 506471011

soil-to-fertilizer map:
2067774073 3521970321 52706909
3338663639 285713733 377282283
4175452431 2125409520 119514865
3950920796 1900877885 224531635
285713733 3604616580 690350716
976064449 3368036703 153933618
2120480982 662996016 210956413
2763248642 1355402238 545475647
3715945922 873952429 49638562
3765584484 3182700391 185336312
2331437395 923590991 431811247
1129998067 2244924385 937776006
3308724289 3574677230 29939350

fertilizer-to-water map:
1898912715 0 159034880
0 781591504 125461131
4234890433 2427770485 8749678
176481534 1845116986 384152450
822014814 539693831 241897673
125461131 907052635 47763268
1476125220 244008638 19613711
3828547378 4170474998 124492298
2643114268 2457193301 126243103
173224399 2229269436 3257135
2916187764 3376015556 236473226
764735505 186729329 57279309
2427770485 3802085897 160735547
2895514626 2436520163 20673138
3152660990 2671736916 584987016
1495738931 1131222975 403173784
1339983969 1534396759 136141251
2588506032 3612488782 54608236
3737648006 2583436404 88300512
737041056 159034880 27694449
2057947595 1677521625 167595361
1063912487 263622349 276071482
3953039676 4041226796 129248202
2225542956 1670538010 6983615
560633984 954815903 176407072
2847762723 3328263653 47751903
2769357371 3962821444 78405352
3825948518 3256723932 2598860
4082287878 3667097018 134988879
4243640111 3276936468 51327185
4217276757 3259322792 17613676

water-to-light map:
527906959 2908176499 284796856
1306013866 0 139756297
500839409 1466481782 27067550
1269694476 139756297 36319390
0 778456518 2402633
4218077327 4154765934 76889969
812703815 4004150799 56130996
153843304 3657154694 8975056
2402633 905946004 132694584
3795108796 2776082693 132093806
3927202602 1422228955 44252827
1445770163 1493549332 1282533361
3794865694 780859151 243102
2728303524 176075687 602380831
162818360 3666129750 338021049
3330684355 3319846298 337308396
4154765934 4231655903 63311393
135097217 887199917 18746087
3667992751 3192973355 126872943
3971455429 781102253 88826366
1252423178 869928619 17271298
868834811 1038640588 383588367

light-to-temperature map:
2621973104 3678827401 230150807
1333642604 1531317439 615453278
3364444750 2854318675 314483239
2978187907 3908978208 107198609
1117308885 1110453605 216333719
1951157390 4016176817 152726483
4168382203 2717095112 26843204
0 312822387 5553076
287414983 245463475 67358912
1949095882 2597527252 2061508
3836867339 1522015715 9301724
648138229 2599588760 117506352
4132690450 1486323962 35691753
2852123911 4168903300 126063996
2468610361 3525464658 153362743
526108840 988424216 122029389
5553076 0 148736111
3265904462 1326787324 98540288
4195225407 716774234 17303853
181751976 318375463 105663007
843084177 3275513023 249951635
2214264232 734078087 254346129
154289187 218000686 27462789
3146382866 684048190 32726044
765644581 2433292104 77439596
3179108910 2510731700 86795552
3846169063 2146770717 286521387
2103883873 2743938316 110380359
3085386516 1425327612 60996350
3678927989 526108840 157939350
4212529260 3193074987 82438036
354773895 148736111 69264575
1093035812 3168801914 24273073

temperature-to-humidity map:
1008510114 1939290935 27755995
2205283444 4197517502 16218189
1119061522 3123774174 108864966
1566495924 221087407 33939034
3089618547 3728555042 25452278
2341294643 3455988869 16076350
2286651827 3754007320 54642816
704748216 2542375745 76754089
445299830 3938069116 259448386
1036266109 1300576315 82795413
178337856 1565003866 40230920
2122934367 1605234786 81339593
1484902828 980285858 81593096
2823460240 1967046930 266158307
3827446421 1526750766 38253100
984919715 1161567987 23590399
218568776 1061878954 99689033
4049237602 3232639140 223349729
953670836 2233205237 3881060
318257809 3472065219 89705062
1727156113 3113814046 9960128
3733360236 444372828 94086185
4272587331 3688491436 22379965
910921285 178337856 42749551
781502305 3808650136 129418980
957551896 2798966448 27367819
1870217811 1686574379 252716556
407962871 2998327877 37336959
2508087592 2826334267 171993610
1600434958 3561770281 126721155
3865699521 812829188 167456670
1737116241 1185158386 115417929
1852534170 3710871401 17683641
3420360273 255026441 38629788
1227926488 2620139318 178827130
4033156191 4250190027 16081411
2204273960 2619129834 1009484
2250197491 4213735691 36454336
2680081202 1383371728 143379038
3458990061 538459013 274370175
3115070825 2237086297 305289448
2357370993 293656229 150716599
1406753618 3035664836 78149210
2221501633 4266271438 28695858

humidity-to-location map:
2849843584 4147982382 56632112
3849085050 3618212322 355529444
1632881348 407047779 65646492
3056274757 2246063521 686771203
2729873863 4028012661 26534599
3779070915 1543896540 70014135
2571854216 2932834724 91402738
2192942437 1028113266 378911779
2960746591 932585100 95528166
765942740 0 407047779
2663256954 1441254676 66616909
2756408462 4054547260 93435122
1698527840 1407025045 34229631
0 3024237462 156854744
3743045960 1507871585 36024955
156854744 3181092206 437120116
1172990519 472694271 459890829
2906475696 3973741766 54270895
593974860 2074095641 171967880
1732757471 1613910675 460184966""";
sections = re.split("\n\n+", input2)
seeds = re.split(r"\s+",sections[0].split(": ")[1])
minLocation = 46294181; # starting with value found in previous runs, but not correct
def findSourceStart(aSection):
    return aSection['sourceStart']
def findDestStart(aSection):
    return aSection['destStart']
sortedSections = [];
for section in sections[1:]:
    mapLines = re.split("\n+", section)[1:]
    sortedSection = [];
    for mapLine in mapLines:
        mapLineParts = re.split(r"\s+", mapLine);
        destStart = int(mapLineParts[0])
        sourceStart = int(mapLineParts[1])
        mapRange = int(mapLineParts[2])
        sourceEnd = sourceStart + mapRange
        diff = destStart - sourceStart
        sortedSection.append({'sourceStart':sourceStart,'sourceEnd':sourceEnd,'diff':diff,'destStart':destStart,'destEnd':destStart+diff});
    sortedSection.sort(key=findSourceStart)
    sortedSections.append(sortedSection)
    print('one update done')
print('made overallMap')

# overallSortedMap = list(sortedSections[0]);
# for section in sortedSections[1:2]:
#     
#     for overallEntry in overallSortedMap:
#         if overallEntry['destStart'] > overallEntry['destEnd']:
#             destSwap = overallEntry['destStart'];
#             overallEntry['destStart'] = overallEntry['destEnd'];
#             overallEntry['destEnd'] = destSwap;
#             sourceSwap = overallEntry['sourceStart'];
#             overallEntry['sourceStart'] = overallEntry['sourceEnd'];
#             overallEntry['sourceEnd'] = sourceSwap;
#     overallSortedMap.sort(key=findDestStart);
# 
#     for sectionEntry in section:
#         if sectionEntry['sourceStart'] > sectionEntry['sourceEnd']:
#             destSwap = sectionEntry['destStart'];
#             sectionEntry['destStart'] = sectionEntry['destEnd'];
#             sectionEntry['destEnd'] = sectionEntry;
#             sourceSwap = sectionEntry['sourceStart'];
#             sectionEntry['sourceStart'] = sectionEntry['sourceEnd'];
#             sectionEntry['sourceEnd'] = sourceSwap;
#     section.sort(key=findSourceStart);
#     
#     updatedOverallMap = [];
#     overallIndex = 0;
#     overallValue = overallSortedMap[overallIndex]['destStart'];
#     sectionIndex = 0;
#     nextSectionValue = section[sectionIndex]['sourceStart'];
#     while sectionIndex < len(section) and overallIndex < len(overallSortedMap):
#         if overallValue < nextSectionValue:
#             sourceStart = overallSortedMap[overallIndex]['sourceStart'] + (overallValue - overallSortedMap[overallIndex]['destStart']);
#             sourceEnd = min(nextSectionValue, overallSortedMap[overallIndex]['sourceEnd']);
#             destStart = overallValue;
#             destEnd = destStart + (sourceEnd - sourceStart);
#             updatedOverallMap.append({'sourceStart':sourceStart,'sourceEnd':sourceEnd,'destStart':destStart,'destEnd':destEnd});
#             if destEnd > overallValue:
#                 overallValue = destEnd + 1
#             else:
#                 overallValue = overallValue + 1;
#         elif nextSectionValue < overallValue:
#             sourceStart = nextSectionValue;
#             sourceEnd = min(section[sectionIndex]['sourceEnd'], overallValue);
#             destStart = section[sectionIndex]['destStart'];
#             destEnd = destStart + (sourceEnd - sourceStart);
#             updatedOverallMap.append({'sourceStart':sourceStart,'sourceEnd':sourceEnd,'destStart':destStart,'destEnd':destEnd});
#             if sourceEnd > nextSectionValue:
#                 nextSectionValue = sourceEnd + 1;
#             else:
#                 nextSectionValue += 1;
#         else:
#             # equal
#             sourceStart = overallSortedMap[overallIndex]['sourceStart'] + (overallValue - overallSortedMap[overallIndex]['destStart']);
#             sourceEnd = sourceStart + min(overallSortedMap[overallIndex]['destEnd'] - overallValue, section[sectionIndex]['sourceEnd'] - nextSectionValue);
#             destStart = section[sectionIndex]['destStart'] + (nextSectionValue - section[sectionIndex]['sourceStart']);
#             destEnd = destStart + (sourceEnd - sourceStart);
#             updatedOverallMap.append({'sourceStart':sourceStart,'sourceEnd':sourceEnd,'destStart':destStart,'destEnd':destEnd});
#             if sourceEnd > nextSectionValue:
#                 nextSectionValue = sourceEnd + 1;
#             else:
#                 nextSectionValue += 1;
#             if destEnd > overallValue:
#                 overallValue = destEnd + 1
#             else:
#                 overallValue += 1;
#         if nextSectionValue >= section[sectionIndex]['sourceEnd']:
#             sectionIndex += 1;
#             if sectionIndex < len(section):
#                 nextSectionValue = section[sectionIndex]['sourceStart'];
#             else:
#                 nextSectionValue = 9999999999999999; # really big number
#         if overallValue >= overallSortedMap[overallIndex]['destEnd']:
#             overallIndex += 1;
#             if overallIndex < len(overallSortedMap):
#                 overallValue = overallSortedMap[overallIndex]['destStart'];
#             else:
#                 overallValue = 99999999999999; # really big number
#     overallSortedMap = updatedOverallMap;
#     print('one update done')
# overallSortedMap.sort(key=findDestStart);
# print('made overallMap')
#    
# def findStart(seedRange):
#     return seedRange['start'];
# seedRanges = []
# for seedRangeIndex in range(0,int(len(seeds)/2)):
#     seedStart = int(seeds[seedRangeIndex * 2]);
#     seedRange = int(seeds[seedRangeIndex * 2 + 1]);
#     seedRanges.append({'start': seedStart,'end':seedStart + seedRange})
# seedRanges.sort(key=findStart);
#    
# print(overallSortedMap);
# for part in overallSortedMap:
#     found = False;
#     for i in range(part['sourceStart'], part['sourceEnd']):
#         j = 0;
#         while j < len(seedRanges) and seedRanges[j]['start'] < i:
#             j += 1;
#         if j < len(seedRanges) and seedRanges[j]['end'] < i:
#             print(part['destEnd'] + i - part['sourceStart']);
#             found = True;
#             break;
#     if found:
#         break;
        

def findModifier(seed, sortedSection):
    if(len(sortedSection) == 0):
        return 0
    middleIndex = math.floor(len(sortedSection)/2);
    middle = sortedSection[middleIndex]
    if seed >= middle['sourceStart']:
        if seed < middle['sourceEnd']:
            return middle['diff']
        else:
            return findModifier(seed,sortedSection[middleIndex+1:])
    else:
        return findModifier(seed,sortedSection[:middleIndex])
for seedRangeIndex in range(0,int(len(seeds)/2)):
    seedStart = int(seeds[seedRangeIndex * 2]);
    seedRange = int(seeds[seedRangeIndex * 2 + 1]);
    # part 1 just iterated over each item in 'seeds', unlike this code for part 2
    # playing with the range to try to more quickly find most likely smallest result
    for seed in range(seedStart+17, seedStart + seedRange, 19):
        curVal = int(seed)
        for sortedSection in sortedSections:
            curVal += findModifier(curVal, sortedSection)
        if curVal < 0:
            print(curVal)
            print(seed)
        elif curVal < minLocation:
            minLocation = curVal
            print(minLocation)
print(minLocation)
# Got the answer of 46294175 - this was correct            
    