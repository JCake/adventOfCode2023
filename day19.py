import re;
input1 = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''
input2 = '''zsz{a<2141:R,s<3943:R,a>2353:ldm,R}
ctb{a<784:R,x>2521:R,x<1031:tlz,gl}
hvb{m<1363:nc,jz}
nh{m>662:px,R}
pmr{s<3424:A,s<3505:R,R}
lfd{a>2865:A,m>1362:xz,a<2730:ml,zg}
xx{m>2402:jh,x<3723:lhr,x<3825:hz,xpf}
msz{x>437:A,s<3250:dn,s>3613:A,nk}
xj{a>957:zd,a>563:ctb,s<1790:gfd,tsm}
ths{m<3198:A,x>3732:lfz,zr}
jsx{a>2308:A,x>1047:A,R}
qm{m<1969:dxg,m>2685:skh,vr}
dc{a>2195:A,x<3133:A,R}
krd{a>2069:mpt,bt}
bzf{s>3302:A,R}
zgd{x<520:A,R}
vx{a<2880:A,x<3486:A,s<753:A,A}
jn{s>2242:A,m<1380:lsq,a<2710:R,R}
qzr{s>3861:A,a>1625:A,xh}
tcv{x>1026:fgc,tbt}
php{m>1973:R,s>1053:R,A}
lmr{m<2677:R,R}
st{a<466:R,a>1034:A,x<3489:R,R}
fh{a<2918:R,a>2944:R,A}
tts{m<529:vck,m<788:nh,s<3643:ctq,txh}
nlg{x<872:A,R}
zxp{a>3928:kct,x>1393:R,s>3050:R,A}
cdg{x<1459:A,a>3788:R,R}
qkb{a<2683:R,lq}
tp{s<1041:hhn,np}
dz{s>2856:A,a>3512:vb,x<2980:A,grm}
qbg{m>301:nt,A}
sbg{x<3412:R,s<3721:A,A}
hhx{s<527:A,x>3144:php,a<1395:rlc,R}
sm{s<2062:R,R}
pk{x<2735:R,a>1071:R,x>2760:R,A}
mff{a<2407:A,x<2658:R,A}
kl{x>2694:A,R}
hqd{x<2635:R,s<2295:A,R}
glh{a>1215:R,R}
qpv{x<337:gzn,s<2598:rkz,m<662:dvd,hc}
ncp{a>3762:A,a>3745:R,A}
xr{a<2352:lsd,lmp}
sh{a<2351:R,A}
ss{a<2347:R,A}
hfb{x>2018:A,s>3006:R,A}
zsf{m>2665:ths,s<3430:gqg,a>2787:xvp,db}
nlh{m<728:R,m>837:sbs,a<1699:R,A}
brv{s>3042:A,A}
fg{x>2705:R,s>737:A,A}
xgd{x>557:vvl,sn}
sg{x>863:qz,s>1521:pn,s<929:lpl,pvf}
zx{m<1341:R,m<2683:A,x<715:A,R}
gcj{s>1156:R,m<854:A,s>1013:A,A}
dj{a<2194:dm,R}
gh{x>2453:mfg,x<1246:vgs,xt}
kp{x<3791:R,R}
cdr{x<2520:A,m<3415:A,x<2778:R,A}
sl{x>2242:R,R}
jvj{s<1968:hv,A}
rpt{a>3782:R,A}
kck{x>1294:A,x>1084:A,a<3858:R,R}
bch{s<1122:vsj,x<1486:vlf,a>3436:qt,bj}
jm{s<443:A,s>512:R,A}
xs{s<3528:R,m>2640:R,x>3042:R,A}
ch{a<1950:gxn,a>2226:R,x>1657:A,xvl}
lx{m<630:A,R}
zzc{m<1124:R,A}
fx{m<1347:A,R}
gt{a>2900:bg,x<3276:A,A}
grm{x>3575:A,s<2701:R,R}
kfl{m>1101:A,m<980:A,x<2760:A,A}
gqg{m>1492:lp,a<2757:ks,m>609:vqx,R}
lmp{s<3718:A,m<481:R,cxc}
lrg{m>2761:jc,m>1993:hnp,ms}
db{x<3762:nm,s<3711:vgh,grj}
nd{x>1223:cd,zm}
ng{s>2998:sv,mh}
xg{s<3814:R,R}
ht{s<3374:R,R}
xcp{s<2894:jvm,s<2996:R,a<2143:brv,pz}
rcp{s>3174:rph,a<1655:ksj,s>2925:A,fnk}
rvj{x<3249:R,a>1811:R,s<3474:A,A}
zg{x<2403:A,s<563:R,x<2657:A,A}
tz{s>3204:R,s<3156:A,tpr}
txh{x<1586:A,a>1878:phr,gs}
zkh{m<2430:dj,m<3326:pl,gls}
cms{a<373:R,A}
hhj{s<3380:gn,s<3575:fq,A}
kk{s>221:vbt,R}
ffv{a<270:A,A}
qpf{m>3344:R,x<1996:R,a<3690:A,R}
sv{s>3633:R,a<3753:A,m<1633:cdg,vd}
qhb{m<1272:ps,A}
zl{s>3175:A,R}
nhn{x>2042:xhg,x>1846:A,m<265:A,A}
ph{s<2097:R,m<3630:R,x>956:R,A}
dt{a>2966:A,R}
qmh{x>1389:A,x>738:A,s<567:fcr,rl}
nk{m>1534:R,A}
ssr{m>1063:R,R}
mgj{s>466:R,m>2416:R,s>458:R,R}
nn{x<1128:R,m<2501:R,R}
nz{a>2744:R,A}
kxn{x<3019:A,s<3436:A,a<3442:A,A}
rlq{m>191:spm,mn}
gx{x<1416:A,s>3286:A,m>2146:A,R}
gv{m<181:R,s>3541:R,s>3502:nrv,bjt}
js{x<863:R,m>2350:R,R}
nv{s>2840:R,a<2821:R,x<3326:R,A}
rmf{a<2391:R,x>1561:R,m<400:R,R}
zkb{a>2331:fsv,mzf}
px{a<2073:A,s>3630:A,A}
ld{x<2541:R,m>570:A,a<2995:A,A}
btk{m>3478:A,R}
tpl{s>2971:bd,s<2360:xj,x>1354:hvv,fbp}
tl{m<2872:A,R}
vg{a<1892:A,R}
ps{x<2420:A,a>1558:R,a>1512:A,A}
hz{a<927:pd,x>3765:cp,A}
cm{a>2376:tt,s>2714:sbl,a<2346:bh,ph}
mm{m>1173:A,m<1077:A,R}
rx{a>3197:A,a>3148:R,x>1636:tn,zx}
qxn{m>1810:A,a<1260:A,jl}
xbj{s<708:A,a>1765:A,R}
kqh{x<2590:zxp,a<3931:sd,zl}
pvf{m<2539:R,x>473:nz,tg}
dtx{s>3243:hcm,A}
sbs{a>1756:R,m>914:A,A}
zts{m>290:R,A}
rtp{a>3077:sx,dqn}
sk{a<322:R,a>582:tsz,s<2588:A,mnb}
rlc{m>1593:A,m<1024:R,m<1396:A,R}
fgc{m<2855:rt,R}
mfg{x<3203:A,m>3086:drf,R}
fj{s<1728:A,m<764:R,R}
hkl{a<402:A,R}
lp{a>2754:R,a<2663:R,A}
mpz{m>2341:fv,x<702:kr,lld}
hzd{a<1697:zzc,m<1156:tsn,a<1877:R,nlg}
cld{a>3920:R,A}
ln{a>3917:A,A}
prh{m>1220:R,R}
qz{s>1580:A,m>1985:xv,A}
bfr{m<3575:A,qdr}
rqf{x<2623:qv,cck}
xd{a>256:A,s<3677:R,rbc}
xgz{a>2348:R,m<2705:R,A}
gs{a>1600:R,m>938:R,x>2620:A,R}
kmb{a>1523:kk,a<994:df,x<1157:sfj,dcc}
mpt{a<2317:zkh,x>1742:cjj,a>2413:dh,cdt}
qt{x<2806:A,m<1984:A,psh}
hdv{s>497:A,A}
czc{x>2392:lnt,lkz}
br{m>3210:R,m>2829:A,s<3596:R,R}
lsd{x<2513:mtz,a>2222:R,x<3231:xtt,dp}
cq{m<793:kv,ttl}
xbc{m>2128:R,R}
fqr{a<2758:tck,mmq}
zs{m<1449:bsv,a<1703:tcv,x>1156:qp,mpz}
rbc{a<95:A,x<1457:R,a<162:A,A}
fjk{s<2662:ch,x<2165:xcp,m>436:gcl,gmx}
kqz{a>1044:R,a>425:R,A}
pgd{m>1538:R,R}
hf{x<3098:R,s<1612:R,A}
bc{x>2631:nns,lvk}
lkz{s>3076:A,x<2326:R,R}
skd{a>1580:A,A}
qvv{x>2639:A,R}
qkz{a<3922:R,s>2171:R,a>3963:A,A}
nns{x<3183:hg,hzq}
zc{x<652:R,A}
knq{m>1374:nv,s<2741:qsj,m>579:kdb,R}
xc{s<553:R,a>1325:A,s<1088:A,R}
qh{a<1461:xtk,m>1604:krd,s<3123:cq,qr}
hnp{s<2967:sm,x>2505:A,s>3575:nn,R}
zdd{s<3682:tts,a<2061:kvm,xr}
njx{a<3940:A,x>3117:R,mq}
lxl{m>1415:A,s<559:R,lk}
xcq{a>2134:R,s>1165:R,x<1925:A,A}
bh{x>901:R,s<1920:A,A}
kt{s>2880:dt,s<2299:xnb,A}
fsv{m<733:A,dqm}
vq{a<1837:jqn,pm}
xnb{s<1901:A,a<2945:R,s<2050:R,R}
qrc{a<3961:R,A}
gjr{a<1420:A,m<2657:A,s<146:A,R}
lql{x>1604:A,m>887:R,a>1806:A,A}
sx{a<3665:bk,s>2491:rs,gc}
nms{a>1906:R,R}
lpl{a>2687:tmk,R}
pbg{x<1261:R,s>3624:A,m>931:A,R}
hv{x>3011:A,a>2433:A,x>2190:R,A}
qzk{s>3241:vdr,R}
rkz{s>2505:R,s<2421:A,s>2450:R,R}
sfj{a>1286:gjr,a>1151:A,s>239:zp,fx}
frs{x>1362:R,x>859:R,R}
sr{a<3609:A,R}
gls{x<1470:A,phg}
ftp{a<1853:std,a>2002:ncb,x>533:btc,vld}
zz{a<3541:fz,x<1057:msz,s<3098:dsm,zgb}
gmx{s<2946:R,a<2045:pj,a>2287:sbt,sp}
nxb{s<3477:qbg,a<2375:gv,a<2473:bjx,clx}
frq{s>3220:bts,m<3436:R,m<3643:R,hk}
fnk{s<2641:R,A}
jj{m<846:R,s<2046:A,x<2913:A,A}
hq{a>2829:dbb,sg}
xvp{a>2926:ssr,x<3710:vf,sjr}
sjx{m<1352:ppf,kp}
nqn{m<3291:R,m>3685:A,R}
nc{s>3327:zpg,mm}
sb{x>765:R,A}
jvm{s<2785:A,s<2834:A,s<2864:R,A}
cxc{a<2487:R,m<696:R,A}
xl{s<2440:tmz,lmr}
xhg{a<2074:R,R}
tt{m>3658:R,R}
jqf{s>1068:nqn,m>3339:A,s<927:mnl,zgt}
cp{x<3803:R,s>1040:A,m>1005:R,R}
pxf{a<1521:R,s>1825:A,R}
qr{m>1018:ztl,s<3592:xhs,s>3774:jg,zdd}
vb{x<3164:R,a<3565:R,x<3525:A,R}
xtp{s<592:R,s>629:R,A}
gp{a<2405:R,x>1230:A,R}
pj{m>255:A,x<3203:R,R}
srp{x>2384:R,m>1385:A,A}
qrg{a<2966:fh,R}
btc{a>1943:R,a<1886:A,A}
mmq{x<2303:R,m>3379:A,A}
ml{s>458:A,R}
dfj{s<3065:A,A}
fcr{a<1219:A,R}
tmz{s<2045:R,R}
pg{a<2818:jn,sjx}
svh{a<781:rf,rg}
phg{s<2578:R,R}
lgx{s<1160:A,m<2465:R,A}
mzf{m<859:R,pmr}
fb{a<2983:A,s<2680:R,a<3020:ld,ht}
jxs{x>2951:R,x>2575:A,x<2292:R,A}
xtt{a>2160:R,m<441:R,R}
vc{m<1263:A,R}
fdn{s>604:A,s<574:A,m<1640:A,lv}
mq{m<698:A,x>2576:A,A}
kbh{x<1086:R,s>92:A,R}
kvm{m<389:czb,nlh}
rt{x>1620:R,m>2355:A,R}
zt{m>2816:A,s>2509:R,m<2676:R,R}
hm{x<3288:A,m>2088:R,R}
rd{m<379:A,s>485:R,R}
mbf{x<3376:R,R}
pm{s>1832:R,m>477:A,A}
qbp{s>2884:A,a>2970:hqd,cgb}
plj{s>3811:A,x<826:R,A}
zqt{m<1423:njx,nzb}
bdt{m>638:A,s>2916:R,s<2887:A,A}
xh{a<1569:A,A}
zp{m>1565:R,A}
mt{m<1097:A,m>1889:A,x<3056:R,A}
std{m<491:A,R}
nmx{x<3669:pc,a>3700:pcc,R}
zgb{m>2097:br,x<1441:kg,m>1126:sr,dx}
nr{x>1759:R,A}
cn{x>2031:mt,a<3681:tdj,x<1265:zgd,bzf}
ctq{x<2171:pbg,x>3019:A,zrv}
mh{s>2712:bs,rpt}
jjg{s<541:R,x<3043:R,s>851:A,R}
jdc{s>1571:qkz,A}
cck{m<2394:A,a>2402:R,m<2836:R,R}
zpg{m<1206:A,A}
ns{s<1096:qs,s>1753:hlp,R}
cb{m>1477:R,m<718:A,a>3713:A,R}
pcc{a<3708:R,a>3712:R,A}
gl{m<597:A,m>904:R,R}
bs{x>2294:R,m<1594:R,m<2822:R,R}
ks{a>2697:A,s<3174:A,A}
zbj{m>392:R,m>167:A,A}
tsz{x>2321:R,A}
jq{a>1617:A,a<1513:A,A}
zk{m>3198:R,R}
xz{a<2751:R,x>2480:A,R}
fq{a>1834:R,a<1759:A,a<1805:R,A}
hc{m<1077:A,x<431:R,R}
rf{x<2429:A,R}
pd{a>589:A,x>3767:R,R}
sj{a<1946:qzr,m>551:km,x<756:htp,rlq}
zrv{x>2630:R,s<3623:A,A}
zm{a<981:R,x>432:A,x<283:A,R}
qf{a<1784:R,m>544:R,m>186:R,R}
pz{m<344:R,a<2337:R,A}
xpf{x<3886:kph,gcj}
dp{s<3728:A,x>3622:R,s<3749:A,R}
nm{s<3672:R,m>1476:A,m<673:R,A}
crk{s>2573:qcb,R}
hms{x>2782:R,A}
gq{s<564:A,a<2120:R,s>607:A,A}
sbt{x>3246:R,R}
jv{x>989:R,x<710:A,m>3469:R,R}
rc{x<1773:R,m>631:R,bgj}
czb{x<2361:A,sbg}
kct{x<1548:A,m>2033:R,m>773:R,A}
xt{s>3379:qpf,x>1914:zk,a>3692:bzr,A}
bt{a>1760:lrg,x>1412:lzm,xn}
jh{s>1176:kqz,m<3121:R,m>3476:R,R}
df{s>236:R,a>490:kbh,ffv}
zvh{s<624:R,a<1652:hms,A}
ngh{a<1116:A,s<3107:R,x<2612:R,A}
bvs{x>937:A,A}
jl{a<1386:A,R}
xzf{s<2882:jq,x>915:R,s>3459:R,A}
kr{a<2287:nrd,a<2393:sh,R}
hg{x>2922:cf,a<1148:hxz,rnb}
lld{a>2253:cz,m>1874:A,s>1088:A,vg}
fbc{s>1476:rx,s<863:qxf,xqg}
td{x>2000:R,x<1615:A,x<1855:R,R}
dvd{x<453:A,A}
kph{a>1114:R,m<1071:A,R}
hhn{x<2851:lfd,s>565:vx,s>240:mk,gt}
phh{s<2871:cms,a<631:bdt,s>2909:R,R}
dd{x>2593:dc,s<3876:lbr,m>648:zsz,nhn}
jx{a>3703:R,x<1763:zc,m<1712:R,qn}
gvz{s>3641:A,s>3621:R,a<2322:R,R}
ltp{s<408:kmb,m<1521:bq,rpq}
cdt{m<2470:gcv,m>3101:cm,a<2352:gb,bvs}
fxx{a>1643:R,cct}
gd{x>2480:R,x>2288:R,R}
qp{m>2642:jqf,xcq}
tnf{x<3088:ns,a>3719:ncp,nmx}
hxz{a>717:hqg,lxl}
nps{m>1553:R,A}
gc{x<1587:bgt,a<3825:tnf,zqt}
vjx{x<3355:R,A}
vm{s>2934:A,R}
nbg{s>3152:kxn,mg}
bj{m>2438:A,m<916:R,A}
kg{s<3410:R,a>3622:R,A}
cx{m>603:mdx,zbj}
qdr{m>3737:A,a<2499:A,a<2548:R,A}
mnb{a<446:A,A}
rg{s<2432:R,m<3262:dkv,s>3460:rdf,ngh}
kpx{m<3072:A,a>1644:btk,kzk}
hx{m>1210:A,m<779:R,R}
jf{s<482:R,a<1100:A,rhv}
vk{a<142:A,s>1945:A,A}
htp{a<2324:zts,R}
bgj{a<1183:A,m>231:R,x<3231:R,A}
kgp{m>673:lql,s<3448:A,x>1641:R,A}
mc{a<2844:R,s>1162:R,R}
cpt{s<3839:mff,hl}
dg{a<1715:qhb,hhj}
sn{a<1718:R,m<1391:vc,x<350:R,A}
kjv{x>1960:tmv,x<1041:ftp,kgp}
jc{m>3400:R,jp}
cgb{m<3060:R,A}
psh{a<3563:R,R}
qsj{x<3342:R,m>876:A,a>2828:R,A}
kx{s>573:R,x<1561:A,R}
bqz{a>2885:qrg,a<2737:qkb,x>3229:knq,sc}
pds{a>744:R,a>278:R,A}
sjr{s>3626:A,m>1244:A,A}
fbp{a>966:lx,x<599:qpv,s>2748:phh,ndb}
bts{a>2398:A,x<3176:A,A}
xcg{a>2819:R,s<2438:A,R}
zr{m>3647:R,R}
jp{x>1936:R,x<941:A,A}
xpb{a<3833:A,a>3859:A,s<940:R,R}
hvv{x<2947:nb,a>768:cx,vjx}
ggc{a<1153:hfb,qxn}
jvl{m>2292:A,R}
dh{x>739:xl,m>2933:bfr,htq}
th{m>3142:R,a>1152:R,x<1166:R,A}
fv{m>3201:A,s<1010:A,R}
nb{s<2747:R,a>931:td,m<831:A,R}
rdf{x<1797:A,R}
hk{m<3843:A,m<3914:A,A}
fr{m>3137:A,s>2991:A,x>2974:R,A}
nvf{a<3572:R,m<2744:R,a>3580:R,A}
rs{a>3816:kqh,a>3718:ng,m<2622:mvp,gh}
pp{s<3385:R,A}
kb{x<2246:kt,m<1484:fb,x<2508:czc,qbp}
hbf{x<1163:A,A}
vlf{s>2060:ts,nzj}
gpz{a>1624:xbc,x<589:R,A}
zgt{a>2253:A,R}
lll{a>1978:jsx,hzd}
vf{m>1362:R,s>3803:A,R}
rpr{x>269:A,s<2281:R,a>2502:R,A}
fn{x>2984:A,s<3176:A,m<3654:cdr,A}
frp{m>1213:R,m<983:A,A}
krm{s>2829:R,s>2769:A,R}
phr{x<2941:A,m<886:R,m>952:R,A}
gfd{x<1339:R,a<258:sl,s<1672:smq,fj}
tmv{m>473:rvj,s>3407:R,s<3352:jxs,pp}
tbt{a>1032:R,R}
pjl{x<3527:R,x<3752:A,A}
vck{a>2120:gvz,frs}
lpz{s>3176:R,A}
sch{s>2532:kfl,a<2065:frp,x<3074:R,jt}
lk{a>244:R,A}
xv{m>3190:R,A}
bjt{m>369:R,m>297:R,R}
vbt{x<1318:A,R}
qn{x<2514:A,R}
bzr{m>3360:A,s>2833:R,A}
nx{m<2179:R,a>2525:R,A}
vd{a>3785:A,x>2238:A,R}
dcc{m<2359:A,a>1289:A,A}
md{m>1024:A,x<1516:R,a>3571:A,R}
cjj{s<2315:jvj,a>2474:dtx,m>3147:frq,rqf}
fxg{x<3483:bqz,s<2692:pg,zsf}
mnl{a>2172:A,A}
dx{a<3590:A,s>3591:R,a>3630:R,A}
in{a>2590:rtp,s<1459:bc,qh}
cz{a>2404:A,s<958:A,A}
htq{s>2389:nx,s>2078:rpr,krf}
tj{s<524:A,R}
mn{x>1287:R,s<3877:R,R}
smq{x<2919:A,R}
mdx{a>1164:A,R}
vld{a>1944:R,a>1897:R,m<595:R,R}
gxn{x>2167:R,x<875:A,x>1347:A,R}
bvg{x<2609:R,s<2643:A,a>1978:A,R}
dsm{a>3596:rm,m<1790:md,nvf}
skh{a>1688:tj,a>1031:A,hhz}
jqn{a<1624:pxf,x<2604:R,a<1741:hn,pjl}
kzk{x<2861:R,x>3539:A,s<2294:A,A}
fbd{s>623:R,A}
hl{x>2561:A,m>1352:A,m>1178:A,R}
vvl{x>1083:R,s>3324:A,s>3218:R,A}
ms{a<1948:R,a<2004:bvg,R}
ncb{a>2050:R,A}
ll{x<2674:xbj,fg}
fts{x>2814:ff,s>1525:gd,jvl}
mp{m>2533:R,m>2006:R,s>1618:R,A}
jr{m<603:R,R}
np{s<1384:mc,a<2776:fts,hgm}
brg{x>2720:A,s>1755:A,x<2245:mp,R}
mk{x>3577:vp,a<2778:dgf,jm}
vgh{s>3528:A,m>966:R,A}
fxb{m>506:R,a>3889:qrc,m<285:R,xpb}
ltj{x<3017:xc,a>1449:jjg,qjb}
lfz{a>2813:A,a<2670:A,x<3889:R,R}
krf{a>2503:R,x<420:A,R}
xn{m<2489:gpz,xzf}
nbq{m<2777:xs,A}
tg{a>2748:R,A}
fz{a>3464:A,pgd}
gn{s<3225:A,R}
hcm{a<2522:A,R}
lz{s>479:hdv,s>453:mgj,th}
gk{s<2803:R,x>2388:A,x<948:A,A}
gcl{a>2131:A,krm}
dxg{m<778:rd,a<955:dtp,A}
rnb{x<2741:ll,x>2805:flq,zvh}
nlc{a<2198:R,R}
bgt{a<3784:hr,x>846:kck,m<1446:fxb,jdc}
vdr{m>149:A,m<66:A,s<3265:A,A}
tlz{a>848:R,s>1876:R,A}
sp{x<3375:A,x<3683:R,R}
tck{x>2230:A,a>2666:A,A}
spm{x<1324:R,A}
clx{m>270:R,m<168:nr,R}
qv{x>2144:A,a<2375:R,x<2004:A,A}
hhz{a>354:A,A}
rhv{m<795:A,a>1776:A,s>500:R,A}
lvk{s>652:zs,ltp}
tbk{a>1933:A,A}
nzb{s<1165:ln,ljq}
qxf{s<522:qvv,A}
tsm{x<1670:A,a>287:jj,s<2052:vk,R}
bk{a<3316:fbc,s<2618:bch,x<2074:zz,ds}
rpq{s<517:lz,m>2407:qmh,m>1869:bb,fdn}
bb{m>2114:R,a>1218:gq,x>1046:xtp,pds}
xqg{s>1071:R,m>1984:tl,x>1848:A,hxp}
gzn{x<133:R,A}
grj{a>2714:R,s>3889:R,R}
nj{s>2128:sch,s>1778:nms,hf}
nrv{s>3518:R,a<2196:A,R}
cs{s<2334:R,m<1793:vm,x>2329:R,A}
mvp{a<3696:cn,a>3710:pzm,s<3053:zjg,jx}
mz{x<2948:nlc,R}
hxp{x<1060:R,s>939:A,a<3198:A,R}
xfj{a>2172:cpt,tbk}
gcv{s<3066:hng,s>3655:kz,x>813:gx,vff}
kz{m>2127:A,s<3777:A,m<1825:A,R}
lv{x<1540:R,a<1107:R,a<1993:A,A}
lhr{m>973:A,s<1135:A,R}
ppf{m<878:R,s<2255:R,A}
ts{x>536:A,R}
dm{a<2147:A,a<2163:R,s>2952:R,R}
sgb{m>2370:svh,a<925:xgc,ggc}
qs{a<3756:A,x>2203:R,A}
ndb{s<2606:R,s<2678:hkl,jr}
rl{s>612:R,R}
vr{m<2399:R,a<1384:st,R}
hzq{s>830:xx,qm}
mhn{m>407:xlz,x<1962:qzk,m>271:tz,mz}
lzm{s>2487:rcp,s>2055:kpx,brg}
vff{m>2105:A,A}
nzj{m<1440:R,R}
dbb{s<2390:hbf,sb}
tdj{m<1695:A,R}
dn{a<3599:R,R}
bq{s<524:jf,m<960:zgc,fk}
fk{a<1352:prh,kx}
ldm{m<887:A,R}
vgs{x<524:R,a<3695:jv,R}
hng{s<2339:R,R}
mg{a>3473:A,R}
zjg{a<3701:A,gk}
xvl{m<265:R,A}
sd{a<3883:A,x>3215:xfm,a<3911:A,cld}
flq{s>718:lgx,R}
xlz{s>3208:A,s<3155:R,a>2115:lpz,A}
pc{a<3696:A,R}
rm{a<3635:R,s>2790:R,R}
ztl{s>3688:xfj,a>1915:hvb,x<1402:xgd,dg}
jz{m>1461:nps,m>1418:R,srp}
hgm{s<1495:A,hm}
dtp{a>510:R,R}
vqx{a>2961:A,m>1104:R,m>880:R,R}
gb{a<2338:A,a<2344:A,s>2500:ss,xgz}
jk{a>2844:kb,vzf}
bg{a<2965:A,R}
km{s>3864:R,a<2268:plj,x<883:xg,gp}
qcb{a<352:R,a<593:A,A}
tmk{s>483:R,A}
jt{m>1243:R,a>2415:A,R}
nrd{a<2046:R,x<266:R,x<522:R,R}
pzm{x<1737:A,a>3714:R,A}
qjb{a>579:R,m<1462:R,a>382:R,R}
lsq{s<1911:R,s<2068:R,R}
dkv{s>3266:R,x<1445:R,R}
cct{x>1079:R,s>1320:R,m>769:A,A}
vp{m<2455:R,R}
sbl{s<3407:A,m<3553:A,A}
xgc{m>1966:sk,m>1667:cs,x>2611:mbf,crk}
kdb{s<3284:A,A}
vzf{m>2255:fqr,dfj}
bd{s<3514:fc,a>667:rc,xd}
bjx{a>2408:A,m<214:R,rmf}
dqn{x<1906:hq,s<1647:tp,x<2727:jk,fxg}
dgf{s>452:R,x<3286:R,x<3442:A,R}
dqm{a>2489:R,A}
bsv{s>1174:fxx,nd}
hlp{m>1501:R,R}
pl{x>1697:zt,R}
cf{x>3076:hhx,ltj}
tm{m>611:A,m<257:A,a<369:R,R}
lbr{a>1915:A,a<1623:R,x>2233:R,qf}
nt{s<3403:R,A}
cd{s<840:R,s<1018:A,A}
fc{a>872:glh,x>2163:R,R}
hr{x<653:R,x<1103:js,s<1312:R,cb}
hqg{x>2806:A,m<1886:kl,a<944:A,pk}
cpb{x<2168:R,a<3482:R,R}
rj{m>1697:R,a<2706:A,x<645:A,A}
ljq{m>2457:A,m>1995:R,m>1752:A,R}
ksj{x>2970:R,R}
drf{a>3683:A,m<3475:A,x<3643:R,R}
rph{s<3630:R,x>2997:A,s<3863:R,R}
jg{x<1736:sj,dd}
xfm{a>3910:A,x>3563:R,m<2652:R,R}
tn{a<3119:A,a<3137:R,R}
xhs{s<3301:mhn,a<2086:kjv,m<542:nxb,zkb}
mtz{x<1541:A,m<520:A,R}
lnt{a<2985:R,m>3068:A,a>3040:R,A}
ttl{x>1947:nj,lll}
pn{x>405:rj,s>2983:R,R}
zd{s>2030:A,x<2552:R,a>1148:R,A}
zgc{a<870:tm,s>605:fbd,skd}
ds{m<2522:nbg,m>3188:fn,s>3290:nbq,dz}
tsn{a>1826:R,a>1778:R,m>990:A,R}
lq{m<1414:A,x<3093:A,A}
hn{s<1796:A,m>421:A,s<1997:R,A}
tpr{m>330:A,A}
ff{m<2011:A,A}
xtk{m<1346:tpl,sgb}
vsj{m>2190:R,s>523:hx,cpb}
kv{s<2214:vq,fjk}
sc{a<2799:A,m>1492:fr,a>2838:R,xcg}

{x=128,m=1590,a=606,s=53}
{x=1604,m=505,a=1233,s=690}
{x=165,m=1071,a=3,s=1592}
{x=477,m=691,a=237,s=772}
{x=2637,m=164,a=3096,s=383}
{x=618,m=349,a=205,s=76}
{x=191,m=9,a=375,s=86}
{x=604,m=438,a=485,s=724}
{x=687,m=914,a=2217,s=471}
{x=910,m=173,a=402,s=419}
{x=2125,m=281,a=2016,s=17}
{x=793,m=634,a=254,s=384}
{x=877,m=435,a=122,s=106}
{x=1410,m=31,a=69,s=605}
{x=1307,m=1878,a=530,s=132}
{x=1466,m=2119,a=565,s=345}
{x=1874,m=1450,a=1410,s=888}
{x=962,m=842,a=661,s=1539}
{x=34,m=1218,a=1262,s=1335}
{x=42,m=565,a=596,s=728}
{x=1891,m=440,a=168,s=936}
{x=370,m=524,a=316,s=1966}
{x=1680,m=2136,a=2592,s=876}
{x=1943,m=1761,a=838,s=885}
{x=54,m=510,a=1969,s=831}
{x=870,m=274,a=1855,s=1939}
{x=1706,m=903,a=1261,s=322}
{x=1053,m=138,a=2131,s=1679}
{x=1373,m=813,a=3421,s=1493}
{x=1008,m=748,a=696,s=154}
{x=1000,m=1165,a=1862,s=59}
{x=543,m=879,a=78,s=737}
{x=60,m=830,a=293,s=2701}
{x=2204,m=1160,a=400,s=493}
{x=2556,m=125,a=2272,s=3184}
{x=1710,m=2846,a=163,s=2638}
{x=1735,m=202,a=164,s=1139}
{x=120,m=1221,a=1856,s=37}
{x=814,m=500,a=1915,s=1088}
{x=1084,m=729,a=983,s=363}
{x=149,m=2364,a=921,s=2036}
{x=1262,m=897,a=2020,s=1439}
{x=187,m=2171,a=471,s=83}
{x=1631,m=2507,a=830,s=1808}
{x=1,m=1657,a=386,s=1215}
{x=510,m=1617,a=772,s=1436}
{x=685,m=295,a=25,s=3098}
{x=14,m=463,a=2399,s=1219}
{x=1234,m=1798,a=454,s=1380}
{x=1744,m=185,a=984,s=565}
{x=873,m=2019,a=8,s=2266}
{x=788,m=1574,a=499,s=17}
{x=520,m=3119,a=559,s=40}
{x=209,m=1040,a=40,s=522}
{x=59,m=3306,a=53,s=914}
{x=911,m=100,a=1334,s=770}
{x=149,m=876,a=1312,s=1182}
{x=1408,m=677,a=106,s=411}
{x=519,m=2749,a=1483,s=21}
{x=29,m=1009,a=598,s=627}
{x=1762,m=478,a=148,s=1801}
{x=423,m=1887,a=192,s=576}
{x=601,m=111,a=52,s=1850}
{x=1378,m=1111,a=762,s=901}
{x=124,m=2574,a=11,s=458}
{x=1210,m=12,a=136,s=177}
{x=64,m=170,a=2015,s=232}
{x=382,m=640,a=713,s=252}
{x=328,m=2813,a=480,s=1431}
{x=2540,m=2957,a=887,s=784}
{x=437,m=116,a=362,s=754}
{x=2864,m=899,a=160,s=2893}
{x=500,m=174,a=1403,s=985}
{x=18,m=1006,a=6,s=773}
{x=277,m=5,a=1114,s=369}
{x=2355,m=2942,a=65,s=534}
{x=790,m=207,a=680,s=877}
{x=1497,m=58,a=458,s=150}
{x=2122,m=187,a=282,s=2088}
{x=1023,m=576,a=2501,s=220}
{x=132,m=821,a=850,s=1056}
{x=233,m=136,a=385,s=2084}
{x=955,m=25,a=1252,s=1264}
{x=504,m=1370,a=246,s=1704}
{x=1722,m=713,a=31,s=197}
{x=53,m=642,a=2880,s=1751}
{x=1082,m=397,a=1329,s=1757}
{x=1132,m=41,a=853,s=357}
{x=900,m=263,a=233,s=1837}
{x=1520,m=682,a=429,s=1570}
{x=2767,m=2027,a=170,s=933}
{x=2876,m=138,a=1348,s=1049}
{x=17,m=935,a=53,s=329}
{x=45,m=3487,a=1484,s=817}
{x=414,m=2,a=349,s=1523}
{x=220,m=122,a=53,s=2424}
{x=544,m=1697,a=715,s=97}
{x=2072,m=198,a=127,s=3522}
{x=120,m=449,a=1229,s=892}
{x=72,m=617,a=184,s=296}
{x=5,m=406,a=1124,s=3546}
{x=575,m=1856,a=32,s=727}
{x=548,m=215,a=645,s=175}
{x=1229,m=7,a=3749,s=687}
{x=191,m=1848,a=3121,s=1584}
{x=528,m=27,a=2356,s=1781}
{x=83,m=146,a=2422,s=302}
{x=1413,m=266,a=1484,s=217}
{x=2593,m=117,a=39,s=2732}
{x=1362,m=389,a=1788,s=789}
{x=79,m=1549,a=85,s=1222}
{x=28,m=743,a=89,s=522}
{x=73,m=1144,a=108,s=1429}
{x=397,m=654,a=1388,s=1070}
{x=2310,m=1939,a=114,s=843}
{x=280,m=3531,a=756,s=155}
{x=255,m=1589,a=3,s=54}
{x=1046,m=99,a=234,s=1300}
{x=1165,m=105,a=681,s=1984}
{x=89,m=470,a=81,s=35}
{x=91,m=931,a=1019,s=766}
{x=532,m=1707,a=944,s=109}
{x=145,m=2234,a=471,s=991}
{x=1076,m=611,a=129,s=654}
{x=857,m=1454,a=7,s=348}
{x=76,m=52,a=247,s=1621}
{x=1247,m=2182,a=46,s=1909}
{x=435,m=1268,a=1189,s=52}
{x=1863,m=775,a=274,s=44}
{x=614,m=5,a=604,s=2459}
{x=1138,m=183,a=223,s=353}
{x=195,m=3130,a=326,s=29}
{x=3446,m=5,a=6,s=510}
{x=2063,m=2346,a=218,s=251}
{x=2435,m=2438,a=1262,s=1141}
{x=1499,m=436,a=802,s=6}
{x=467,m=2159,a=307,s=209}
{x=1336,m=878,a=121,s=1154}
{x=433,m=1211,a=1059,s=1640}
{x=73,m=481,a=351,s=72}
{x=67,m=66,a=948,s=156}
{x=327,m=2039,a=983,s=563}
{x=1175,m=339,a=259,s=667}
{x=1950,m=2415,a=43,s=2835}
{x=791,m=4,a=1578,s=2156}
{x=660,m=326,a=141,s=87}
{x=90,m=69,a=443,s=157}
{x=169,m=1698,a=60,s=1387}
{x=50,m=408,a=1700,s=725}
{x=334,m=7,a=506,s=381}
{x=226,m=1321,a=602,s=2738}
{x=3175,m=1705,a=560,s=148}
{x=1642,m=1439,a=1214,s=1416}
{x=61,m=31,a=1180,s=218}
{x=2284,m=3174,a=790,s=432}
{x=199,m=316,a=442,s=124}
{x=480,m=410,a=3250,s=537}
{x=77,m=518,a=1480,s=310}
{x=414,m=242,a=487,s=1038}
{x=981,m=957,a=212,s=1222}
{x=3489,m=414,a=132,s=206}
{x=3701,m=35,a=67,s=2737}
{x=1752,m=1166,a=110,s=948}
{x=159,m=152,a=14,s=46}
{x=73,m=3262,a=334,s=462}
{x=2433,m=3012,a=2178,s=2191}
{x=949,m=241,a=2995,s=579}
{x=2,m=2224,a=2164,s=51}
{x=783,m=667,a=1334,s=151}
{x=1739,m=776,a=53,s=2446}
{x=3061,m=3,a=1187,s=1522}
{x=379,m=1421,a=24,s=618}
{x=229,m=378,a=64,s=2021}
{x=1493,m=669,a=207,s=38}
{x=1976,m=43,a=14,s=1687}
{x=56,m=871,a=2722,s=543}
{x=1141,m=101,a=10,s=577}
{x=60,m=1625,a=1050,s=331}
{x=1623,m=1723,a=2315,s=1450}
{x=73,m=1359,a=346,s=314}
{x=493,m=674,a=298,s=696}
{x=43,m=1667,a=1151,s=585}
{x=587,m=153,a=1266,s=1566}
{x=1546,m=656,a=76,s=917}
{x=1449,m=1598,a=402,s=120}
{x=1442,m=1848,a=1678,s=646}
{x=607,m=576,a=1139,s=33}
{x=907,m=29,a=2746,s=3466}
{x=1786,m=609,a=2902,s=2249}
{x=1249,m=81,a=936,s=985}
{x=241,m=3,a=3322,s=49}
{x=630,m=1090,a=1487,s=405}
{x=547,m=700,a=431,s=1587}
{x=698,m=119,a=1765,s=2553}
{x=762,m=203,a=435,s=769}
{x=2,m=292,a=812,s=713}
{x=735,m=6,a=315,s=307}
{x=567,m=39,a=400,s=1051}
{x=620,m=1559,a=51,s=816}
{x=286,m=195,a=797,s=2935}'''

rulesAndParts = re.split('\n\n',input1)
rules = rulesAndParts[0]
partsSection = rulesAndParts[1]
rawParts = [part[1:-1].split(',') for part in re.split('\n',partsSection)]
parts = [];
for rawPart in rawParts:
    part = {};
    for field in rawPart:
        fieldParts = field.split('=')
        part[fieldParts[0]] = int(fieldParts[1])
    parts.append(part)

rulesMap = {};
for ruleLine in re.split('\n',rules):
    labelAndRules = ruleLine.split('{')
    label = labelAndRules[0];
    rules = labelAndRules[1][:-1].split(',')
    rulesMap[label] = rules;

def conditionMet(condition, part):
    if '>' in condition:
        fieldAndValue = condition.split('>');
        field = fieldAndValue[0];
        value = int(fieldAndValue[1])
        return part[field] > value;
    else:
        fieldAndValue = condition.split('<');
        field = fieldAndValue[0];
        value = int(fieldAndValue[1])
        return part[field] < value;
def findNextOutcome(part):
    for rule in rules:
        if ':' in rule:
            checkAndOutcome = rule.split(':')
            if conditionMet(checkAndOutcome[0], part):
                return checkAndOutcome[1]
        else:
            return rule;
acceptedSum = 0
for part in parts:
    outcome = 'in';
    while not outcome == 'R' and not outcome == 'A':
        rules = rulesMap[outcome]
        outcome = findNextOutcome(part);
    if outcome == 'A':
        acceptedSum += (part['x'] + part['m'] + part['a'] + part['s'])
print(acceptedSum)

# TODO part 2 - find what combos can map to A
class Node:
  def __init__(self,name):
    self.ranges = {};
    self.name = name;
initialNode = Node('in')
allNodes = [initialNode]
allRulesForAccepting = [];
allRulesForRejecting = [];
def findChildNodes(parentNode):
    rules = rulesMap[parentNode.name]
    rangesSoFar = parentNode.ranges.copy()
    for rule in rules:
        if ':' in rule:
            checkAndOutcome = rule.split(':')
            check = checkAndOutcome[0];
            outcome = checkAndOutcome[1];
            if '<' in check or '>' in check:
                fieldAndValue = re.split(r'[<>]', check);
                field = fieldAndValue[0];
                value = int(fieldAndValue[1])
                if outcome == 'A':
                    allRulesForAccepting.append(f'{rangesSoFar.copy()}')
                elif outcome == 'R':
                    allRulesForRejecting.append(f'{rangesSoFar.copy()}')
                else:
                    nextNode = Node(outcome)
                    nextNode.ranges = rangesSoFar.copy();
                    if field in nextNode.ranges:
                        fieldRange = nextNode.ranges[field];
                        if '<' in check:
                            nextNode.ranges[field] = (fieldRange[0], min(value-1, fieldRange[1]))
                        else:
                            nextNode.ranges[field] = (max(value+1, fieldRange[0]), fieldRange[1])
                    else:
                        nextNode.ranges[field] = (0,value-1) if '<' in check else (value+1,4000)
                    allNodes.append(nextNode);
                    findChildNodes(nextNode);
                    if field in rangesSoFar:
                        fieldRange = rangesSoFar[field];
                        if '>' in check:
                            rangesSoFar[field] = (fieldRange[0], min(value, fieldRange[1]))
                        else:
                            rangesSoFar[field] = (max(value, fieldRange[0]), fieldRange[1])
                    else:
                        rangesSoFar[field] = (0,value) if '>' in check else (value,4000)
        else:
            outcome = rule;
            if outcome == 'A':
                allRulesForAccepting.append(f'{rangesSoFar.copy()}')
            elif outcome == 'R':
                allRulesForRejecting.append(f'{rangesSoFar.copy()}')
            else:
                nextNode = Node(outcome);
                nextNode.ranges = rangesSoFar.copy();
                allNodes.append(nextNode);
                findChildNodes(nextNode);
                
            
findChildNodes(initialNode)
for node in allNodes:
    print(f'{node.name} : {node.ranges}');
print('acceptance:')
for successCombos in set(allRulesForAccepting):
    print(successCombos)
print('rejection:')
for failureCombos in set(allRulesForRejecting):
    print(failureCombos)