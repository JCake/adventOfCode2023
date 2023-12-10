import re;
import math;
input1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)''';
input2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)''';
input3 = '''LRRLRRRLRLRLLRRLRLRLLRLRLRLLLLRRRLLRRRLRRRLRRRLLRLLRLRRLRLRLRRRLLLLRRLRLRRLRRLLRRRLRRLRLRRLRRLRRLRRLRLLRRLRRLLLLRLRLRRLLRRLLRRLRLLRLRRLRRLRRLRRRLRRLLLRRLRRRLRLRRRLLRLRRLRRRLRRLLRRRLRRLRLLRRLLRRLRRLRRRLRRLLRRLRRRLRLRLRLRLRLRRLRRLLRRRLRLRRLRRRLRLRLRLRLRLRRRLRRLRRRLLRRLRLLRRRLRRLRLLLLRRRLRRLRRRR

DRM = (DLQ, BGR)
PKD = (TNC, DKH)
FSM = (LKS, KPG)
NDS = (KGD, HNX)
KQQ = (DPF, GKD)
SBX = (DDL, MGH)
GCV = (KMG, GLP)
PCT = (JXN, XDR)
KHR = (QPK, FPQ)
FCK = (GLS, GGP)
MKR = (XPQ, TJX)
PFP = (RPR, LPS)
XPC = (SSS, FRX)
PTJ = (LSC, CND)
GVJ = (NRL, SHV)
QNF = (MBQ, GSR)
TMK = (DVM, BJM)
KTG = (QVG, LLX)
JMK = (BKF, XDK)
JQV = (DCM, RLT)
VFH = (FDD, GML)
XPN = (FKG, CXG)
GDX = (GRV, BPP)
GVP = (JLP, XNJ)
TCB = (RVR, QXQ)
DLP = (XDK, BKF)
FQG = (RMH, QHR)
XDD = (SMK, HMN)
TLL = (TVV, FXX)
NPT = (NGC, FQM)
XQK = (PQG, QTK)
DMQ = (RVS, KNQ)
QKR = (SJD, PLH)
XNV = (SJB, GCV)
SRP = (CDK, JFK)
FRP = (FFD, XPC)
PVC = (XVD, MGD)
DPP = (BFQ, XDD)
CNV = (LQC, JJH)
LLH = (CFP, BGF)
XCK = (VDX, GFC)
KGD = (LSF, FNK)
MJA = (FXB, QVX)
QLH = (KRM, KVD)
QCR = (TKN, RNB)
PSR = (FBL, HKJ)
MGK = (BVC, HVL)
PVK = (JRN, SMV)
JTD = (VNS, FGJ)
PMD = (HGN, NBM)
DRF = (CPR, RTX)
HJL = (CBR, VDR)
PPB = (GDX, DXB)
DVR = (LLT, GVJ)
JRN = (RLD, RSL)
NXM = (RBN, NVD)
RLV = (FRM, FJB)
SJB = (KMG, GLP)
KJM = (XJH, LQX)
GRB = (HHL, RGD)
LQC = (BMC, XSH)
NRB = (NQD, RFT)
SQH = (QJT, JXX)
JLX = (RJL, HHH)
HVR = (XPN, JFM)
FVD = (RXS, RHH)
KSX = (TCB, GDK)
GKJ = (TQF, HQJ)
HQL = (BMR, PBX)
QFP = (NJM, FSB)
TPH = (NXT, RKN)
SRL = (LSP, LFV)
SDL = (MGL, PSK)
MFX = (FSM, LQF)
RFT = (FLV, GMS)
BTG = (DRS, PVC)
HLR = (DSB, DPP)
DXB = (BPP, GRV)
NHS = (HQG, GVP)
GKK = (DCM, RLT)
MJT = (JNR, PGC)
KDS = (FFD, XPC)
TSS = (BGX, QQX)
FKC = (NBN, SJP)
HHQ = (GVP, HQG)
JKF = (QRR, GFD)
CXG = (SDD, TMN)
GCG = (TCC, TDT)
NQX = (DMQ, DPM)
GHX = (BJQ, CHJ)
JQC = (HNQ, RJF)
QBB = (GNH, XSC)
BJG = (VMH, FCN)
VMS = (KRX, VLQ)
GSF = (NQM, KBH)
JQQ = (PKD, GNB)
KFG = (BGX, QQX)
TTV = (SNB, JQF)
CXJ = (CND, LSC)
GGP = (PBH, XNG)
FCV = (NLP, QJK)
NSB = (KSX, SLL)
JBH = (RGK, NSS)
CQH = (HJL, FKR)
VRX = (HKJ, FBL)
HJZ = (QVX, FXB)
RLD = (BJP, RLV)
HHH = (PNJ, HPJ)
LSC = (NRP, DCF)
BVM = (RCG, QLL)
KGN = (PRB, MLT)
NTV = (MRQ, NHQ)
VXT = (VFH, MBX)
RLG = (MJQ, RNL)
JVX = (HJQ, FNV)
XGH = (HHK, JXT)
NHC = (HPX, LGG)
VPC = (XCL, HPQ)
HKJ = (RQC, TMK)
PGQ = (FTX, MNP)
MPF = (KNM, BJG)
MFT = (DRS, PVC)
XNG = (RCS, JNH)
RMH = (GHD, MPF)
PFM = (PGQ, XHJ)
TRN = (TCP, TCP)
NHP = (JMG, VGP)
JSK = (JBG, PVM)
FSB = (MGK, HTD)
BPR = (VFH, MBX)
RHM = (LHD, PTF)
PRV = (RJL, HHH)
GNC = (HVR, PSV)
PSV = (JFM, XPN)
KMG = (KDR, RTV)
RKL = (DPP, DSB)
GLN = (QJT, JXX)
FNK = (XXP, QDR)
JDP = (HVR, PSV)
HHD = (VPC, MDS)
XHJ = (MNP, FTX)
XVJ = (RGG, BCB)
DRH = (CDK, JFK)
BMC = (TTQ, KHR)
TCT = (JQD, QBB)
BCS = (HLV, MKR)
LFV = (GTL, NSX)
JCS = (JQC, NDG)
SBJ = (PHS, QMN)
HPZ = (DQD, PFP)
BFM = (PMD, JGB)
QBL = (KVC, TXK)
RGD = (NXH, KQQ)
PBX = (LBP, FPK)
FDD = (TCX, CSN)
RJT = (CQG, JSQ)
BMR = (FPK, LBP)
RBN = (DRF, VJB)
PHB = (NXR, LPM)
BPN = (PPX, PPX)
KVC = (NSF, TQK)
PXB = (GJH, JHM)
BCB = (NTR, KKB)
KXM = (NHS, HHQ)
VTT = (NCB, HCR)
SHP = (LQX, XJH)
RCG = (CLL, TCT)
LHG = (GSF, PRJ)
XCL = (JLX, PRV)
LXB = (RHH, RXS)
FKZ = (TJS, BJB)
NNH = (CFD, XMX)
NTD = (NCX, PVK)
DCF = (JHJ, VMN)
GJH = (JTD, CJD)
VBS = (CDQ, LFQ)
MGL = (GGB, QNN)
TXK = (NSF, TQK)
HRX = (QFP, BJR)
GMS = (GKJ, TNF)
RGA = (PFP, DQD)
KTS = (GSF, PRJ)
TPP = (VPC, MDS)
JNV = (BHV, XQK)
DXL = (HDP, KTG)
MBR = (GRS, GTG)
KVJ = (LPH, NGG)
HRG = (RNL, MJQ)
XHL = (JXF, FVH)
MMC = (FHM, HNF)
HGC = (SHT, HBF)
LPS = (NTV, CGR)
FKR = (CBR, VDR)
BHV = (PQG, QTK)
BKF = (SRP, DRH)
JMA = (BJB, TJS)
MPT = (HRX, VSD)
QHL = (NRB, HJG)
PDG = (KJM, SHP)
HFT = (HHQ, NHS)
SJD = (GPM, PPB)
NSF = (NRX, SRL)
MXG = (JVJ, BMF)
PHD = (BQK, VKV)
VBH = (TXK, KVC)
NJM = (HTD, MGK)
TVV = (LLH, HFB)
RPS = (GGQ, SNK)
HPR = (LJS, DJR)
FDR = (QKT, GRX)
LLT = (SHV, NRL)
VQC = (DPM, DMQ)
MJQ = (CLD, FCV)
BFG = (GJH, JHM)
GFS = (PMP, VXL)
LBP = (HRF, GRB)
BXC = (MFS, NRM)
CFD = (QMQ, HPR)
HPN = (JQC, NDG)
BBJ = (JTL, QQK)
VVL = (CDN, STB)
HFB = (CFP, BGF)
NNG = (XVP, CQH)
QKM = (KDS, FRP)
VJB = (CPR, RTX)
KQB = (XCK, BSF)
LKS = (LDJ, MXG)
GTL = (FVD, LXB)
PJS = (BGV, MLM)
KNM = (FCN, VMH)
FCN = (VGR, KHV)
RPJ = (XKD, BPM)
GLP = (KDR, RTV)
NXL = (VTS, SDL)
XDX = (MPT, FXH)
KRX = (DCD, DHH)
CTP = (CRQ, DPL)
SRG = (SKH, SLF)
QVX = (NDC, NPL)
XVK = (SNB, JQF)
RBT = (NSD, SBJ)
RXS = (FKC, JSS)
SFX = (PRB, MLT)
SRS = (FVH, JXF)
NRL = (RLG, HRG)
QKK = (PBX, BMR)
DPL = (PTQ, DBH)
PFD = (JQV, GKK)
VGR = (KMX, DVR)
FQX = (LHD, PTF)
LXT = (RHM, FQX)
JHV = (MBR, PHJ)
JNN = (VKG, SLT)
XDK = (DRH, SRP)
JBR = (BDR, GFS)
BNM = (VKG, SLT)
CJD = (VNS, FGJ)
FPK = (HRF, GRB)
PBH = (JNH, RCS)
FGV = (FDR, TMD)
LSF = (XXP, QDR)
RBM = (VHG, BDL)
TNF = (HQJ, TQF)
TRM = (JHT, BCG)
GBH = (XMJ, JFF)
DBH = (DSS, RQL)
PGB = (BXR, DXL)
QFR = (TDT, TCC)
HHL = (NXH, KQQ)
HGN = (BFG, PXB)
PXC = (BPN, BPN)
NDF = (VQC, NQX)
GSK = (BVV, SBX)
TCM = (VBS, HCN)
HTD = (BVC, HVL)
SHD = (MHG, HNG)
LQX = (QVF, LBV)
MSF = (FDF, VLP)
NRP = (VMN, JHJ)
TQF = (BXC, JCR)
MBX = (GML, FDD)
JCR = (MFS, NRM)
NTR = (PCN, RNT)
JHJ = (XMT, NPT)
SQX = (CDN, STB)
CSN = (GBJ, PGB)
GDJ = (GBM, GCJ)
XGL = (HJQ, FNV)
PLD = (BFL, BFL)
NRX = (LFV, LSP)
TFF = (HGQ, MJT)
JVJ = (TMS, HPK)
BSF = (VDX, GFC)
GML = (CSN, TCX)
BFJ = (GFD, QRR)
FGJ = (PGF, VMS)
TQK = (SRL, NRX)
GQD = (MDD, HLQ)
TJX = (XCG, DJH)
GRR = (LPM, NXR)
PTQ = (DSS, DSS)
HHK = (KLD, NNG)
FBR = (KXM, HFT)
RLT = (JMK, DLP)
PHL = (QHR, RMH)
DVM = (JTP, KDM)
MNF = (RPJ, RMF)
RMF = (BPM, XKD)
GGQ = (MFT, BTG)
CLD = (NLP, QJK)
NMR = (FNL, LXT)
CLX = (TRP, GMD)
QMQ = (DJR, LJS)
KDR = (PKC, NRF)
KKG = (VHG, BDL)
FBQ = (TPP, HHD)
QVV = (LNR, GSK)
VKV = (MFX, FDL)
HJG = (NQD, RFT)
XVD = (VXT, BPR)
NCX = (SMV, JRN)
QLN = (CDJ, TDK)
GFC = (CKR, LNC)
HGQ = (JNR, PGC)
NDG = (RJF, HNQ)
CBC = (NSD, SBJ)
BQK = (FDL, MFX)
VGV = (HGC, TQG)
VGP = (RJT, KPK)
VMN = (XMT, NPT)
PSH = (NSS, RGK)
PPL = (FXH, MPT)
DCD = (SBR, DTS)
MDD = (MQX, FQT)
XCG = (XVK, TTV)
LFQ = (SNS, VBL)
JHT = (FMN, HMC)
KNQ = (QKM, DPS)
PVM = (CHL, GLT)
JMG = (KPK, RJT)
XKD = (GQJ, NXL)
DGG = (CCB, CQX)
HNF = (MNC, FKZ)
QTL = (PSH, JBH)
RNL = (CLD, FCV)
BDR = (PMP, VXL)
GKH = (KXM, HFT)
RQC = (DVM, BJM)
GSR = (PPL, XDX)
JQD = (GNH, XSC)
GRS = (RTN, MPH)
BPP = (GBH, KQX)
XVP = (HJL, FKR)
PKZ = (NMR, KJK)
SLT = (BVM, KMJ)
XHA = (KJK, NMR)
BQQ = (FDR, TMD)
GGC = (CXJ, PTJ)
NBM = (PXB, BFG)
RQL = (BBH, NLT)
KJK = (FNL, LXT)
PSK = (GGB, QNN)
FQT = (DRL, NDS)
SJT = (VQC, NQX)
QHT = (GFS, BDR)
QJT = (PJS, DNG)
SVT = (PDG, GSS)
MBQ = (PPL, XDX)
VHL = (PVM, JBG)
QCJ = (JKK, JSR)
NQH = (LKQ, FBG)
XNJ = (QNF, LPL)
PQV = (CKJ, JHV)
FHM = (MNC, MNC)
FPN = (DLQ, BGR)
BJR = (NJM, FSB)
HPQ = (PRV, JLX)
KMJ = (QLL, RCG)
FTX = (TSM, PDR)
JXT = (KLD, NNG)
DPS = (KDS, FRP)
KKB = (RNT, PCN)
XCB = (TDM, HXC)
TCP = (PFP, DQD)
CDK = (NDF, SJT)
HCR = (HSP, PFD)
SNK = (BTG, MFT)
TKN = (QTL, HPL)
GSS = (KJM, SHP)
NRF = (SVT, RGV)
FLV = (GKJ, TNF)
QPK = (FPN, DRM)
RNB = (QTL, HPL)
HPJ = (XGL, JVX)
NSD = (QMN, PHS)
JXF = (DQV, XPX)
PRJ = (KBH, NQM)
XMT = (NGC, FQM)
JLP = (QNF, LPL)
RND = (HLV, MKR)
QRR = (GPQ, GLL)
LNR = (BVV, SBX)
PQG = (TXR, NTD)
JXX = (PJS, DNG)
QQX = (VTT, XKV)
RRJ = (GLS, GGP)
MLM = (VCD, BTQ)
QVG = (TMM, CTP)
KRM = (MSF, HVT)
XKV = (HCR, NCB)
LJX = (RNB, TKN)
CCB = (NXM, QSG)
RJF = (FQP, VDH)
XBN = (BJQ, CHJ)
JHM = (JTD, CJD)
SMV = (RSL, RLD)
PDR = (GHX, XBN)
JFK = (NDF, SJT)
HCN = (LFQ, CDQ)
SLL = (TCB, GDK)
VBL = (JBR, QHT)
SMK = (RBM, KKG)
GDK = (QXQ, RVR)
KQX = (XMJ, JFF)
LKQ = (HLN, VTD)
JSQ = (QXG, CLX)
FFD = (FRX, SSS)
NRM = (XBP, NQH)
SBR = (PQQ, SRG)
BKR = (MHG, HNG)
QQK = (GQK, STS)
HVL = (DLF, QLH)
NHT = (PTJ, CXJ)
GLL = (TLL, LRR)
GLS = (PBH, XNG)
NHB = (QQK, JTL)
PFS = (KFG, TSS)
PCN = (PFS, QFB)
CJV = (BFL, PKZ)
JFM = (FKG, CXG)
GFD = (GLL, GPQ)
MDS = (XCL, HPQ)
FXH = (VSD, HRX)
DQD = (RPR, LPS)
HPX = (RRJ, FCK)
JNR = (SQQ, SQQ)
BGR = (PQV, DKS)
BRN = (BSF, XCK)
RVS = (QKM, DPS)
PLH = (GPM, PPB)
XSM = (QFS, GQD)
TTH = (TQG, HGC)
KBJ = (KTS, LHG)
RKN = (PCX, NSB)
TPK = (PFM, RFN)
MNC = (BJB, TJS)
PMM = (GRR, PHB)
QKT = (BNK, QKR)
HQG = (JLP, XNJ)
RRD = (JGB, PMD)
CPR = (TGM, VXS)
GGM = (GCJ, GBM)
HBF = (FQG, PHL)
NXH = (DPF, GKD)
TMD = (GRX, QKT)
FBL = (RQC, TMK)
GNB = (DKH, TNC)
LQF = (LKS, KPG)
BKN = (TRN, TRN)
QJK = (BLT, XVJ)
HLV = (TJX, XPQ)
XPX = (TPK, HQN)
BJP = (FJB, FRM)
GHD = (KNM, BJG)
XMX = (HPR, QMQ)
FNV = (NHT, GGC)
JGB = (HGN, NBM)
PKH = (HHK, JXT)
JXN = (VRR, VRR)
CHJ = (TLF, QSN)
XBP = (LKQ, FBG)
QTK = (TXR, NTD)
PKC = (SVT, RGV)
JNH = (MGV, MPJ)
FXB = (NDC, NPL)
XHQ = (KTS, LHG)
MFS = (NQH, XBP)
FQM = (XJB, TXN)
QNN = (JQQ, GBG)
GBG = (PKD, GNB)
TMN = (GRC, BCV)
HMN = (KKG, RBM)
DHH = (SBR, DTS)
KPG = (LDJ, MXG)
FDL = (LQF, FSM)
FXX = (LLH, HFB)
VSD = (BJR, QFP)
HVT = (FDF, VLP)
FRM = (CBB, GMX)
GQK = (QVV, QBV)
CKJ = (PHJ, MBR)
JJH = (XSH, BMC)
SQQ = (PLD, PLD)
KPK = (JSQ, CQG)
VLP = (HHT, MMC)
NLP = (XVJ, BLT)
VTS = (MGL, PSK)
DTS = (SRG, PQQ)
VCD = (GDJ, GGM)
VRR = (HLR, RKL)
VXS = (BKN, SRB)
GMD = (PSR, VRX)
PFK = (HXC, TDM)
SJP = (VSM, NNH)
TDK = (SRS, XHL)
KRS = (GCV, SJB)
MRQ = (CJK, PQD)
XJB = (JRK, RPS)
BGF = (QCR, LJX)
MLT = (MMF, DGG)
TCC = (MNF, KKL)
QMN = (GLN, SQH)
GQJ = (VTS, SDL)
BFQ = (SMK, HMN)
NSS = (JPQ, HXV)
MHG = (VGV, TTH)
KBH = (GPL, XCV)
DRL = (KGD, HNX)
HMC = (QDF, RGR)
QSN = (FBR, GKH)
SDD = (GRC, BCV)
TGH = (BPN, SSQ)
HNG = (TTH, VGV)
RHH = (FKC, JSS)
DQA = (MVV, LQJ)
QFB = (KFG, TSS)
TQG = (SHT, HBF)
KDM = (QKK, HQL)
XHV = (PLD, CJV)
PQD = (TPH, PTN)
SSS = (SQX, VVL)
GPM = (DXB, GDX)
KLD = (CQH, XVP)
LRR = (FXX, TVV)
HPL = (JBH, PSH)
TMS = (BQQ, FGV)
MMF = (CCB, CQX)
DLQ = (PQV, DKS)
PHJ = (GTG, GRS)
TLF = (GKH, FBR)
FJB = (CBB, GMX)
PTF = (PSF, PHD)
NPL = (RTG, QHL)
XMJ = (XHQ, KBJ)
PMP = (TRM, PJK)
JPQ = (KLM, TCM)
BCG = (FMN, HMC)
DRS = (MGD, XVD)
RGT = (PKH, XGH)
TGM = (BKN, BKN)
BPM = (GQJ, NXL)
VDX = (CKR, LNC)
XJH = (QVF, LBV)
MGD = (BPR, VXT)
RGR = (JSK, VHL)
SNS = (QHT, JBR)
SRB = (TRN, DVK)
NRQ = (LQC, JJH)
PSF = (BQK, VKV)
BMF = (TMS, HPK)
LGG = (FCK, RRJ)
HPK = (FGV, BQQ)
QBV = (GSK, LNR)
FNF = (PHB, GRR)
GLT = (JDP, GNC)
DKS = (JHV, CKJ)
RGV = (GSS, PDG)
HQN = (PFM, RFN)
GKD = (BFJ, JKF)
HXC = (HPN, JCS)
MGH = (BVB, FBQ)
LBV = (XCB, PFK)
LHD = (PHD, PSF)
CDQ = (SNS, VBL)
BTQ = (GGM, GDJ)
HMS = (CBC, RBT)
VTD = (CNV, NRQ)
JBG = (GLT, CHL)
LCB = (NGG, LPH)
FKG = (SDD, TMN)
BVV = (DDL, MGH)
RGG = (KKB, NTR)
FBG = (HLN, VTD)
KMX = (GVJ, LLT)
HRF = (HHL, RGD)
DGM = (QFS, GQD)
LPM = (QFR, GCG)
QXQ = (BCS, RND)
BGV = (BTQ, VCD)
BGX = (XKV, VTT)
XDR = (VRR, ZZZ)
BJM = (JTP, KDM)
RFN = (PGQ, XHJ)
DDL = (FBQ, BVB)
XCV = (JNN, BNM)
TCX = (GBJ, PGB)
QXG = (TRP, GMD)
VKG = (BVM, KMJ)
RSL = (RLV, BJP)
CDN = (QLN, CNM)
RVR = (BCS, RND)
BBH = (BXJ, BXJ)
BXR = (KTG, HDP)
DJH = (XVK, TTV)
DVK = (TCP, HPZ)
SLF = (TFF, KQV)
DJR = (SFX, KGN)
HHT = (FHM, FHM)
JSR = (JXM, JNV)
DSB = (BFQ, XDD)
DPM = (RVS, KNQ)
HJQ = (NHT, GGC)
ZZZ = (RKL, HLR)
RJL = (HPJ, PNJ)
BJQ = (TLF, QSN)
HQJ = (BXC, JCR)
FQP = (HMS, SRH)
PGF = (VLQ, KRX)
LQJ = (FNF, PMM)
JXM = (BHV, XQK)
PNJ = (JVX, XGL)
STB = (CNM, QLN)
BBS = (JXN, JXN)
KKL = (RMF, RPJ)
SHV = (HRG, RLG)
FPQ = (FPN, DRM)
GBJ = (DXL, BXR)
QHR = (GHD, MPF)
MDG = (JKK, JSR)
CRQ = (PTQ, DBH)
BVB = (TPP, HHD)
GRC = (RGT, VDD)
SKH = (TFF, KQV)
DHZ = (LQJ, MVV)
LSP = (NSX, GTL)
MPJ = (QBL, VBH)
TDT = (KKL, MNF)
TXN = (JRK, RPS)
HSP = (GKK, JQV)
JTL = (STS, GQK)
GBM = (QCJ, MDG)
HDP = (LLX, QVG)
GMX = (KQB, BRN)
PJK = (JHT, BCG)
NDC = (RTG, QHL)
LPL = (GSR, MBQ)
VLQ = (DCD, DHH)
QLL = (CLL, TCT)
RTV = (NRF, PKC)
DKH = (BBJ, NHB)
NGC = (XJB, TXN)
CNM = (CDJ, TDK)
XXP = (BSP, NHC)
FNL = (RHM, FQX)
NBN = (VSM, NNH)
XSC = (BFM, RRD)
VXL = (PJK, TRM)
VSM = (XMX, CFD)
NQM = (GPL, XCV)
HLN = (CNV, NRQ)
GCJ = (QCJ, MDG)
FDF = (HHT, HHT)
PQQ = (SKH, SLF)
KVD = (MSF, HVT)
QSG = (NVD, RBN)
RGK = (HXV, JPQ)
NXR = (GCG, QFR)
QDR = (BSP, NHC)
TDM = (HPN, JCS)
MQX = (NDS, DRL)
JRK = (GGQ, SNK)
VMH = (VGR, KHV)
RPR = (NTV, CGR)
CFP = (LJX, QCR)
CLL = (JQD, QBB)
LLX = (CTP, TMM)
PRB = (DGG, MMF)
FVH = (XPX, DQV)
JKK = (JNV, JXM)
KLM = (VBS, HCN)
NHQ = (CJK, PQD)
BJB = (BKR, SHD)
CQX = (NXM, QSG)
KHV = (DVR, KMX)
SRH = (CBC, RBT)
DQV = (TPK, HQN)
NQD = (GMS, FLV)
PHS = (GLN, SQH)
GPL = (JNN, BNM)
JSS = (SJP, NBN)
CGR = (MRQ, NHQ)
PGC = (SQQ, XHV)
GPQ = (LRR, TLL)
HXV = (TCM, KLM)
BFL = (KJK, NMR)
PPX = (FXB, QVX)
AAA = (HLR, RKL)
DSS = (BBH, BBH)
VDD = (PKH, XGH)
NCB = (PFD, HSP)
SSQ = (PPX, HJZ)
DNG = (MLM, BGV)
CDJ = (XHL, SRS)
TNC = (NHB, BBJ)
QDF = (VHL, JSK)
GTG = (MPH, RTN)
FRX = (SQX, VVL)
MVV = (FNF, PMM)
QFS = (HLQ, MDD)
MNP = (PDR, TSM)
LDJ = (BMF, JVJ)
NSX = (FVD, LXB)
RNT = (PFS, QFB)
TJS = (SHD, BKR)
HNQ = (VDH, FQP)
BLT = (BCB, RGG)
KQV = (HGQ, MJT)
PTN = (NXT, RKN)
VDR = (BBS, PCT)
RCS = (MPJ, MGV)
GRX = (BNK, QKR)
JFF = (XHQ, KBJ)
RTG = (NRB, HJG)
CND = (DCF, NRP)
DCM = (JMK, DLP)
XPQ = (XCG, DJH)
RTX = (TGM, VXS)
DPF = (BFJ, JKF)
LNC = (PXC, TGH)
PCX = (SLL, KSX)
BSP = (HPX, LGG)
VHG = (LCH, NHP)
GRV = (KQX, GBH)
NGG = (DGM, XSM)
XSH = (TTQ, KHR)
MRH = (KVJ, LCB)
TXR = (NCX, PVK)
NVD = (VJB, DRF)
TTQ = (FPQ, QPK)
CKR = (PXC, PXC)
BVC = (DLF, QLH)
VDH = (SRH, HMS)
JQF = (SKC, MRH)
CBB = (BRN, KQB)
FMN = (RGR, QDF)
SHT = (FQG, PHL)
NLT = (BXJ, DHZ)
MPH = (KRS, XNV)
BXJ = (MVV, LQJ)
CHL = (JDP, GNC)
TSM = (XBN, GHX)
DLF = (KRM, KVD)
BCV = (RGT, VDD)
HNX = (FNK, LSF)
LJS = (SFX, KGN)
STS = (QBV, QVV)
SKC = (KVJ, LCB)
BNK = (SJD, PLH)
RTN = (KRS, XNV)
JTP = (QKK, HQL)
LCH = (VGP, JMG)
CBR = (BBS, BBS)
VNS = (VMS, PGF)
CQG = (CLX, QXG)
HLQ = (MQX, FQT)
TMM = (CRQ, DPL)
BDL = (NHP, LCH)
TRP = (VRX, PSR)
MGV = (VBH, QBL)
GNH = (BFM, RRD)
NXT = (NSB, PCX)
SNB = (SKC, MRH)
LPH = (XSM, DGM)
GGB = (GBG, JQQ)
CJK = (PTN, TPH)
QVF = (PFK, XCB)''';
input4 = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)''';
instructionsAndMap = re.split("\n\n+", input3)
instructions = instructionsAndMap[0];
mapPart = instructionsAndMap[1];
mapLines = re.split("\n",mapPart);
mapMap = {};
nodes = [];
for mapLine in mapLines:
    inAndOut = mapLine.split(' = ');
    node = inAndOut[0];
    nextNodes = inAndOut[1];
    mapMap[node]={'L':nextNodes[1:4],'R':nextNodes[6:9]}
    nodes.append(node);
instIndex = 0;
stepCount = 0;
def endsWithA(string):
    return string[len(string)-1] == 'A';
def endsWithZ(string):
    return string[len(string)-1] == 'Z';
aLocations = list(filter(endsWithA,nodes));
zLocations = list(filter(endsWithZ,nodes));
if 'AAA' in aLocations:
    # part 1
    location = 'AAA';
    while not location == 'ZZZ':
        nextDir = instructions[instIndex];
        location = mapMap[location][nextDir];
        stepCount += 1;
        instIndex = (instIndex + 1) % len(instructions);
    print(stepCount);
# part 2
stepCount = 0;
instIndex = 0;
locations = list(aLocations);
cycles = {}
for index, location in enumerate(aLocations):
    cycles[location] = {'ready': False};
    for endLocation in zLocations:
        cycles[location][endLocation] = [];
def allReady(cycles):
    for cycle in cycles:
        if not cycles[cycle]['ready']:
            return False;
    return True;
while not allReady(cycles):
    nextDir = instructions[instIndex];
    for index, location in enumerate(locations):
        locations[index] = mapMap[location][nextDir];
        if endsWithZ(locations[index]):
            thisCycle = cycles[aLocations[index]]
            thisCycle[locations[index]].append(stepCount + 1);
            if(len(thisCycle[locations[index]]) > 1):
                thisCycle['ready'] = True;
    stepCount += 1;
    instIndex = (instIndex + 1) % len(instructions);
print(cycles);
patterns = [];
for cycle in cycles:
    for endPoint in cycles[cycle]:
        if not endPoint == 'ready':
            if len(cycles[cycle][endPoint]) > 1:
                patterns.append(cycles[cycle][endPoint]);
print(patterns);
def allContain(listOfLists):
    for aList in listOfLists:
        for item in aList:
            allContain = True;
            for otherList in listOfLists[1:]:
                if not item in otherList:
                    allContain = False;
            if allContain:
                return item;
    return 0;
overlap = allContain(patterns);
for pattern in patterns:
    print(pattern[0] * 2 == pattern[1])
# Confirmed all are full loops, so can find LCM to solve:
factors = [];
for pattern in patterns:
    factors.append(pattern[0]);
print(math.lcm(*factors));
