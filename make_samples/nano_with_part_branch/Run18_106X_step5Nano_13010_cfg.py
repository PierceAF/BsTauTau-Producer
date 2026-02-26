# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_upgrade2018_realistic_v16_L1v1 --step NANO --era Run2_2018,run2_nanoAOD_106Xv2 --python_filename Run18_106X_step5Nano_13010_cfg.py --fileout file:step5.root --filein /store/mc/RunIISummer20UL18MiniAODv2/ttbarToBsToTauTau_BsFilter_TauTauFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2810000/01B61B6C-3245-824E-874A-643BAE58C6C1.root --no_exec --mc -n -1
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2
from PhysicsTools.NanoAOD.common_cff import *


process = cms.Process('NANO',Run2_2018,run2_nanoAOD_106Xv2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("RecoJets.JetProducers.PileupJetID_cfi")
process.pileupJetId.jets = cms.InputTag("slimmedJets")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('/store/mc/RunIISummer20UL18MiniAODv2/ttbarToBsToTauTau_BsFilter_TauTauFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2810000/01B61B6C-3245-824E-874A-643BAE58C6C1.root'),
    fileNames = cms.untracked.vstring('file:/eos/cms/store/group/phys_bphys/ytakahas/bstautau/01B61B6C-3245-824E-874A-643BAE58C6C1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

process.myTauCandidates = cms.EDProducer('TauProducer',
    isMC = cms.bool(True),
    jets = cms.InputTag("slimmedJets"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    muons = cms.InputTag("slimmedMuons"),
    electrons = cms.InputTag("slimmedElectrons"),
    genParticles = cms.InputTag("prunedGenParticles")
)


def get_3prong_vars(prefix):
    """
    Returns a PSet containing all 3-prong specific variables.
    The prefix ('leg1' or 'leg2') must match the keys used in C++ UserFloats/Ints.
    """
    return cms.PSet(
        # Standard Kinematics (Visible)
        **{prefix+"_pt":     Var(f"userFloat('{prefix}_pt')",     float, doc=f"{prefix} visible Pt")},
        **{prefix+"_eta":    Var(f"userFloat('{prefix}_eta')",    float, doc=f"{prefix} visible Eta")},
        **{prefix+"_phi":    Var(f"userFloat('{prefix}_phi')",    float, doc=f"{prefix} visible Phi")},
        **{prefix+"_mass":   Var(f"userFloat('{prefix}_m')",      float, doc=f"{prefix} visible mass")},
        **{prefix+"_charge": Var(f"userInt('{prefix}_charge')",   int,   doc=f"{prefix} charge")},

        # Vertex Quality and Displacement
        **{prefix+"_vtxProb":   Var(f"userFloat('{prefix}_vtxProb')",   float, doc=f"{prefix} 3-track vertex probability")},
        **{prefix+"_l3dSig":    Var(f"userFloat('{prefix}_l3dSig')",    float, doc=f"{prefix} 3D decay length significance")},
        **{prefix+"_flightLen": Var(f"userFloat('{prefix}_flightLen')", float, doc=f"{prefix} 3D decay length in cm")},
        **{prefix+"_pvips":     Var(f"userFloat('{prefix}_pvips')",     float, doc=f"{prefix} IP significance wrt PV")},
        **{prefix+"_alpha":     Var(f"userFloat('{prefix}_alpha')",     float, doc=f"{prefix} cosine of angle between p and decay length")},
        
        # DOCA (Distance of Closest Approach)
        **{prefix+"_maxDoca": Var(f"userFloat('{prefix}_maxDoca')", float, doc=f"{prefix} max distance between tracks")},
        **{prefix+"_minDoca": Var(f"userFloat('{prefix}_minDoca')", float, doc=f"{prefix} min distance between tracks")},

        # Kinematic Fit Derived Variables
        **{prefix+"_fitMass": Var(f"userFloat('{prefix}_fitMass')", float, doc=f"{prefix} tau mass after kin-fit")},
        **{prefix+"_fitPt":   Var(f"userFloat('{prefix}_fitPt')",   float, doc=f"{prefix} tau Pt after kin-fit")},

        # SV and PV Positions
        **{prefix+"_svX": Var(f"userFloat('{prefix}_svX')", float, doc=f"{prefix} SV X position")},
        **{prefix+"_svY": Var(f"userFloat('{prefix}_svY')", float, doc=f"{prefix} SV Y position")},
        **{prefix+"_svZ": Var(f"userFloat('{prefix}_svZ')", float, doc=f"{prefix} SV Z position")},
        **{prefix+"_pvX": Var(f"userFloat('{prefix}_pvX')", float, doc=f"{prefix} refitted PV X")},
        **{prefix+"_pvY": Var(f"userFloat('{prefix}_pvY')", float, doc=f"{prefix} refitted PV Y")},
        **{prefix+"_pvZ": Var(f"userFloat('{prefix}_pvZ')", float, doc=f"{prefix} refitted PV Z")},
        **{prefix+"_origPvX": Var(f"userFloat('{prefix}_origPvX')", float, doc=f"{prefix} original PV X")},
        **{prefix+"_origPvY": Var(f"userFloat('{prefix}_origPvY')", float, doc=f"{prefix} original PV Y")},
        **{prefix+"_origPvZ": Var(f"userFloat('{prefix}_origPvZ')", float, doc=f"{prefix} original PV Z")},

        # Background Rejection
        **{prefix+"_nExtra":    Var(f"userFloat('{prefix}_nExtra')",    float, doc=f"{prefix} number of extra tracks at SV")},
        **{prefix+"_vweight":   Var(f"userFloat('{prefix}_vweight')",   float, doc=f"{prefix} PV refit weight")},
        **{prefix+"_deltaChi2": Var(f"userFloat('{prefix}_deltaChi2')", float, doc=f"{prefix} PV chi2 diff (orig - refit)")},

        # Gen Matching
        **{prefix+"_genMatchId":  Var(f"userInt('{prefix}_genMatchId')",  int, doc=f"{prefix} matched gen-tau ID")},
        **{prefix+"_isFromBsTau": Var(f"userInt('{prefix}_isFromBsTau')", int, doc=f"{prefix} 1 if from Bs->TauTau")},

        # Track Indices
        **{prefix+"_trkIdx1": Var(f"userInt('{prefix}_trkIdx1')", int, doc=f"{prefix} index of 1st pion")},
        **{prefix+"_trkIdx2": Var(f"userInt('{prefix}_trkIdx2')", int, doc=f"{prefix} index of 2nd pion")},
        **{prefix+"_trkIdx3": Var(f"userInt('{prefix}_trkIdx3')", int, doc=f"{prefix} index of 3rd pion")},

        **{prefix+"_m_rho": Var(f"userFloat('{prefix}_m_rho')", float)},
        
        # Daughter Pion Kinematics
        **{prefix+"_pion1_pt": Var(f"userFloat('{prefix}_pion1_pt')", float)},
        **{prefix+"_pion2_pt": Var(f"userFloat('{prefix}_pion2_pt')", float)},
        **{prefix+"_pion3_pt": Var(f"userFloat('{prefix}_pion3_pt')", float)},
        **{prefix+"_pion1_eta": Var(f"userFloat('{prefix}_pion1_eta')", float)},
        **{prefix+"_pion2_eta": Var(f"userFloat('{prefix}_pion2_eta')", float)},
        **{prefix+"_pion3_eta": Var(f"userFloat('{prefix}_pion3_eta')", float)},
        **{prefix+"_pion1_phi": Var(f"userFloat('{prefix}_pion1_phi')", float)},
        **{prefix+"_pion2_phi": Var(f"userFloat('{prefix}_pion2_phi')", float)},
        **{prefix+"_pion3_phi": Var(f"userFloat('{prefix}_pion3_phi')", float)},

        # Parent Jet Information
        **{prefix+"_jetPt":      Var(f"userFloat('{prefix}_jetPt')",      float, doc=f"{prefix} parent jet Pt")},
        **{prefix+"_jetEta":     Var(f"userFloat('{prefix}_jetEta')",     float, doc=f"{prefix} parent jet Eta")},
        **{prefix+"_jetPhi":     Var(f"userFloat('{prefix}_jetPhi')",     float, doc=f"{prefix} parent jet Phi")},
        **{prefix+"_jetMass":    Var(f"userFloat('{prefix}_jetMass')",    float, doc=f"{prefix} parent jet mass")},
        **{prefix+"_energyFrac": Var(f"userFloat('{prefix}_energyFraction')", float, doc=f"{prefix} energy fraction in jet")},
        **{prefix+"_jetNCharged": Var(f"userInt('{prefix}_jetNCharged')", int,   doc=f"{prefix} jet charged mult")},
        **{prefix+"_jetNNeutral": Var(f"userInt('{prefix}_jetNNeutral')", int,   doc=f"{prefix} jet neutral mult")},
        **{prefix+"_jetIdx":     Var(f"userInt('{prefix}_counter_jet')",  int,   doc=f"{prefix} jet collection index")},


        # English comment: Added Jet ID, PU ID, and Flavour details
        **{prefix+"_jetId":      Var(f"userInt('{prefix}_jetId')",        int,   doc=f"{prefix} Jet ID (1: Tight)")},
        **{prefix+"_puId":       Var(f"userInt('{prefix}_puId')",         int,   doc=f"{prefix} Pileup Jet ID (fullId)")},
        **{prefix+"_puScore":    Var(f"userFloat('{prefix}_puScore')",    float, doc=f"{prefix} Pileup Jet ID score")},
        **{prefix+"_hadronFlavour": Var(f"userInt('{prefix}_hadronFlavour')", int, doc=f"{prefix} Jet hadron flavour")},

        # B-tagging (Updated for consistency)
        **{prefix+"_jetBTag":    Var(f"userFloat('{prefix}_jetBTag')",    float, doc=f"{prefix} jet DeepFlavour B-tag (probb+probbb)")},
        **{prefix+"_deepFlavB":  Var(f"userFloat('{prefix}_deepFlavB')",  float, doc=f"{prefix} DeepFlavour probb")},
        **{prefix+"_deepFlavBB": Var(f"userFloat('{prefix}_deepFlavBB')", float, doc=f"{prefix} DeepFlavour probbbb")},
        **{prefix+"_deepFlavLep": Var(f"userFloat('{prefix}_deepFlavLep')", float, doc=f"{prefix} DeepFlavour problepb")},
        
        
    )

# --- 1-prong Leg2 specific variables (Used for Had3P, Mu3P, Ele3P) ---
leg2_1p_vars = cms.PSet(
    leg2_pt   = Var("userFloat('leg2_pt')", float),
    leg2_eta  = Var("userFloat('leg2_eta')", float),
    leg2_phi  = Var("userFloat('leg2_phi')", float),
    leg2_mass = Var("userFloat('leg2_m')", float),
    leg2_charge = Var("userInt('leg2_charge')", float),
    leg2_pdgId = Var("userInt('leg2_pdgId')", int),
    leg2_genMatchId = Var("userInt('leg2_genMatchId')", int),
    leg2_isFromBsTau = Var("userInt('leg2_isFromBsTau')", int),
    leg2_id   = Var("userFloat('leg2_id')",   float, doc="Lepton ID score (e.g. MVA valuel)"),
    leg2_iso  = Var("userFloat('leg2_iso')",  float, doc="Relative isolation"),
    leg2_dxy  = Var("userFloat('leg2_dxy')",  float, doc="dxy w.r.t. PV"),
    leg2_dz   = Var("userFloat('leg2_dz')",   float, doc="dz w.r.t. PV"),

#    leg2_jetPt     = Var("userFloat('leg2_jetPt')",     float, doc="Leg2 parent jet Pt"),
#    leg2_jetEta    = Var("userFloat('leg2_jetEta')",    float, doc="Leg2 parent jet Eta"),
#    leg2_jetPhi    = Var("userFloat('leg2_jetPhi')",    float, doc="Leg2 parent jet Phi"),
#    leg2_jetMass   = Var("userFloat('leg2_jetMass')",   float, doc="Leg2 parent jet mass"),
#    leg2_jetId     = Var("userInt('leg2_jetId')",       int,   doc="Leg2 Jet ID (1: Tight)"),
#    leg2_puId      = Var("userInt('leg2_puId')",        int,   doc="Leg2 Pileup Jet ID (fullId)"),
#    leg2_puScore   = Var("userFloat('leg2_puScore')",   float, doc="Leg2 Pileup Jet ID score"),
#    leg2_hadronFlavour = Var("userInt('leg2_hadronFlavour')", int, doc="Leg2 Jet hadron flavour"),

    # B-tagging for Leg2
#    leg2_jetBTag    = Var("userFloat('leg2_jetBTag')",    float, doc="Leg2 jet DeepFlavour B-tag (probb+probbb)"),
#    leg2_deepFlavB  = Var("userFloat('leg2_deepFlavB')",  float, doc="Leg2 DeepFlavour probb"),
#    leg2_deepFlavBB = Var("userFloat('leg2_deepFlavBB')", float, doc="Leg2 DeepFlavour probbbb"),
#    leg2_deepFlavLep= Var("userFloat('leg2_deepFlavLep')",float, doc="Leg2 DeepFlavour problepb"),
    
    # Correlations between 1p and 3p
    lp_doca_sv3p      = Var("userFloat('lp_doca_sv3p')", float, doc="DOCA of 1-prong to 3-prong SV"),
    sip3d_sig_1p_sv3p = Var("userFloat('sip3d_sig_1p_sv3p')", float, doc="Signed IP significance of 1-prong wrt 3-prong SV"),
)

# --- Di-Tau System common variables (Bs candidate level) ---
ditau_common_vars = cms.PSet(
    P4Vars, # visible p4 of the whole system
    pairType       = Var("userInt('pairType')", int, doc="1=Had3P, 2=Mu3P, 3=Ele3P, 4=3P3P"),
    m_vis          = Var("userFloat('m_vis')", float, doc="Visible invariant mass"),
    dr_taus        = Var("userFloat('dr_taus')", float, doc="DeltaR between the two tau candidates"),
    dz_taus        = Var("userFloat('dz_taus')", float, doc="DeltaZ between the two tau candidates"),
    vtxProb_bs     = Var("userFloat('vtxProb_bs')", float, doc="Vertex probability of the Bs fit (all tracks)"),
    iso_ratio      = Var("userFloat('iso_ratio')", float, doc="Sum pT of di-tau pair over jet pT"),
    is_true_signal = Var("userInt('is_true_signal')", int, doc="1 if both taus matched to same Bs"),
    bsX = Var("userFloat('bsX')", float, doc="Bs vertex X"),
    bsY = Var("userFloat('bsY')", float, doc="Bs vertex Y"),
    bsZ = Var("userFloat('bsZ')", float, doc="Bs vertex Z"),
)

# --- Table Creation ---

def make_channel_table(label, tableName, is_3p3p=False):
    # Start with the common system variables
    all_vars = ditau_common_vars.clone()
    
    # Add Leg 1 (always a 3-prong)
    leg1_pset = get_3prong_vars("leg1")
    for name in leg1_pset.parameterNames_():
        setattr(all_vars, name, getattr(leg1_pset, name))
    
    if is_3p3p:
        # Add Leg 2 as a 3-prong
        leg2_pset = get_3prong_vars("leg2")
        for name in leg2_pset.parameterNames_():
            setattr(all_vars, name, getattr(leg2_pset, name))
            
        # Add 3P3P specific exact mass variables
        all_vars.m_exact = Var("userFloat('m_exact')", float, doc="Exact mass from collinear approximation")
        all_vars.x1      = Var("userFloat('x1')", float, doc="Energy fraction x1")
        all_vars.x2      = Var("userFloat('x2')", float, doc="Energy fraction x2")
        all_vars.alpha1      = Var("userFloat('alpha1')", float, doc="Alpha 1")
        all_vars.alpha2      = Var("userFloat('alpha2')", float, doc="Alpha 2")
    else:
        # Add Leg 2 as a 1-prong (Had/Mu/Ele)
        for name in leg2_1p_vars.parameterNames_():
            setattr(all_vars, name, getattr(leg2_1p_vars, name))
        
    return cms.EDProducer("SimpleCandidateFlatTableProducer",
        src = cms.InputTag("myTauCandidates", label),
        cut = cms.string(""),
        name = cms.string(tableName),
        doc  = cms.string(f"Custom candidates for {label} channel"),
        singleton = cms.bool(False),
        extension = cms.bool(False),
        variables = all_vars
    )

# --- Instantiate tables for each output collection ---
process.tauTableHad3P = make_channel_table("DiTausHad3P", "BsTau3pTau1p")
process.tauTableMu3P  = make_channel_table("DiTausMu3P",  "BsTau3pTauMu")
process.tauTableEle3P = make_channel_table("DiTausEle3P", "BsTau3pTauEle")
process.tauTable3P3P  = make_channel_table("DiTaus3P3P",  "BsTau3pTau3p", is_3p3p=True)

    

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--eventcontent nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
#    fileName = cms.untracked.string('file:/eos/user/y/ytakahas/step5.root'),
    fileName = cms.untracked.string('step5.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)






# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v16_L1v1', '')

# Path and EndPath definitions

process.myTauSequence = cms.Sequence(
    process.myTauCandidates + 
    process.tauTableHad3P + 
    process.tauTableMu3P + 
    process.tauTableEle3P + 
    process.tauTable3P3P
)

process.nanoAOD_step = cms.Path(process.myTauSequence + process.nanoSequenceMC)



process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

process.NANOAODSIMoutput.outputCommands.extend([
    'keep *_tauTableHad3P_*_*',
    'keep *_tauTableMu3P_*_*',
    'keep *_tauTableEle3P_*_*',
    'keep *_tauTable3P3P_*_*',

])


# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeCommon 

#call to customisation function nanoAOD_customizeCommon imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeCommon(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

