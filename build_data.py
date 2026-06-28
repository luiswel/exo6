# -*- coding: utf-8 -*-
"""Build data.js for the EXO6 conference guide from hand-authored schedule data.
Run:  python3 build_data.py
Outputs: data.js  (window.SCHEDULE = {...})
"""
import json

TOPICS = {
    1: {"name": "Present-day results", "long": "Present day results in exoplanet research (setting the stage)", "color": "#3b82f6"},
    2: {"name": "Detection of small planets", "long": "Towards the detection of the lowest mass / smaller planets (methods, instrumentation, data analysis)", "color": "#10b981"},
    3: {"name": "Detailed characterisation", "long": "Towards their detailed characterisation (interiors, atmospheres, astrobiology)", "color": "#f59e0b"},
    4: {"name": "Astrophysical challenges", "long": "Astrophysical challenges (stellar characterisation, star-planet connection, stellar noise)", "color": "#a855f7"},
    0: {"name": "Special / plenary", "long": "Special sessions, keynotes & community events", "color": "#ec4899"},
}

DAYS = [
    ("Sunday", "2026-06-28"),
    ("Monday", "2026-06-29"),
    ("Tuesday", "2026-06-30"),
    ("Wednesday", "2026-07-01"),
    ("Thursday", "2026-07-02"),
    ("Friday", "2026-07-03"),
]

# Each session: dict(day, room, topic, chair, theme, kind, start, end, talks)
# talks: list of (start, speaker, title)
SESSIONS = []

def S(day, room, topic, chair, theme, kind, start, end, talks):
    SESSIONS.append(dict(day=day, room=room, topic=topic, chair=chair,
                         theme=theme, kind=kind, start=start, end=end, talks=talks))

# ----------------------------- MONDAY 29 JUNE -----------------------------
S("Monday", "Main Room", 1, "Sérgio G. Sousa", "Planet demographics & forming giants", "plenary", "09:30", "10:30", [
    ("09:30", "Michelle Kunimoto", "Planetary Systems in Context: Demographic Insights from TESS"),
    ("10:00", "Gabriele Cugno", "Forming Planets and their Moons: Establishing an Observational View of Circumplanetary Disks"),
    ("10:15", "Chih-Chun Hsu", "Spins and Atmosphere Characterization of Infant and Adolescent Giant Exoplanets from Keck/KPIC High-resolution Spectroscopy"),
])
S("Monday", "Main Room", 1, "Andrew Collier Cameron", "The golden age of exoplanet atmospheres", "plenary", "11:00", "12:00", [
    ("11:00", "Laura Kreidberg", "The Golden Age of Exoplanet Atmospheres"),
    ("11:30", "Aniket Sanghi", "Mapping the Late Stages of Giant Planet Evolution with JWST Imaging of Benchmark Cold Planets Eps Ind Ab and Eps Eri b"),
    ("11:45", "Aidan Gibbs", "Discovery of a third Jovian planet around Beta Pictoris with JWST/NIRSpec"),
])
S("Monday", "Main Room", 1, "Eduardo Cristo", "Exotic worlds: debris, imaging & hot Jupiters", "parallel", "14:00", "16:00", [
    ("14:00", "Alexander Venner", "Extreme – But Not Extreme Enough? The Record-stretching Orbit of a Hidden “Failed Hot Jupiter”"),
    ("14:15", "Yifan Zhou", "JWST MIRI Time-Series as a Serendipitous Direct Imaging Survey: Wide-Orbit Planet Searches for Rocky Planet Hosts"),
    ("14:30", "Tim Cunningham", "A multi-wavelength view of planetary debris and accretion onto white dwarfs: the cornerstone system G29-38"),
    ("14:45", "Klaudia Jaworska", "The origins of Exocomets in Beta Pictoris"),
    ("15:00", "Chloe Lawlor", "Spectroscopic Confirmation of a Second Embedded Planet in the WISPIT 2 System"),
    ("15:15", "Luigi Mancini", "Unveiling the Diverse Architectures and Evolutionary Pathways of Neptune-sized Planets: Results from GAPS and HONEI"),
    ("15:30", "Taylor Bell", "WASP-12b: Diamond in the Rough, or Just Misunderstood?"),
    ("15:45", "Claire Finley", "Synthesizing Accretion and Circumplanetary Disk Properties of a Wide Orbit Planet with HST and JWST"),
])
S("Monday", "Main Room", 1, "William Dethier", "JWST atmospheres: hot Jupiters to rocky worlds", "parallel", "16:30", "18:30", [
    ("16:30", "Lisa Dang", "Mapping the Atmosphere of TOI-561 b: First JWST/NIRSpec Phase Curve of Ultra-Short Period Planet with a Thick Atmosphere"),
    ("16:45", "Stephen Schmidt", "A clear view of star–planet interactions in three ultra-hot jupiter systems using JWST"),
    ("17:00", "Beth Biller", "Imaging young, temperate sub-Jupiters: Early results from JWST direct imaging exoplanet searches"),
    ("17:15", "Prune August", "Is there an atmosphere on Hot Rock LHS 1478 b?"),
    ("17:30", "Kim Angelique Kahle", "A high refractory-to-volatile ratio for the ultra-hot Jupiter WASP-121 b from a panchromatic JWST dayside spectrum"),
    ("17:45", "Maël Voyer", "Atmospheric properties of planetary mass companions across L, T and Y types: a uniform JWST-MIRI analysis"),
    ("18:00", "Sydney Jenkins", "Searching for Frigid Worlds Around White Dwarfs with JWST"),
    ("18:15", "Cyril Gapp", "Phase-resolved transmission spectroscopy with JWST reveals the asymmetric atmosphere of WASP-121b"),
])
S("Monday", "Room 2", 4, "André Silva", "Host stars & demographics", "parallel", "14:00", "16:00", [
    ("14:00", "Jessie Christiansen", "The Next Decade of Exoplanet Demographics: Completing the Galactic Census of Exoplanets"),
    ("14:15", "Aneesh Baburaj", "Deviations from Solar Abundances for Host Stars of Wide Separation Companions and their Implications for Giant Planet Formation"),
    ("14:30", "Sergio Sousa", "Homogeneous Stellar Parameters as the Foundation of Exoplanet Demographics"),
    ("14:45", "Elisa Delgado Mena", "Unveiling planetary systems around intermediate mass evolved stars using NIRPS+HARPS"),
    ("15:00", "Emmanuel Greenfield", "The Impact of Mean Motion Resonances on the Astrometric Detection of Giant planets"),
    ("15:15", "Ekaterina Ilin", "Self-roast: Close-in planet induces flares on its host star"),
    ("15:30", "Yadira Gaibor", "Common Envelope Evolution Produces Rare, Massive, Close-In Planet Survivors"),
    ("15:45", "Yasmin Davis", "Inflation or inference? Revisiting the M dwarf radius inflation problem with eclipsing binaries"),
])
S("Monday", "Room 2", 2, "Khaled Al Moulla", "Pushing RV precision to Earth-twins", "parallel", "16:30", "18:30", [
    ("16:30", "André Silva", "Intrinsic limitations to template-based radial velocity extraction from high-resolution spectra"),
    ("16:45", "Ancy Anna John", "Towards Detecting Earth-Twins: Combining Optimised RV Extraction with Stellar-Variability Mitigation"),
    ("17:00", "Sara Tavella", "Reaching 40 cm/s RV precision on HARPS-N solar data with a PCA correction at the spectral level"),
    ("17:15", "Ben Lakeland", "Radial-velocity variability of the magnetically quiet Sun"),
    ("17:30", "Matteo Pinamonti", "The small planet-cold Jupiter connection: demographic insights from a targeted RV survey and the HD 29021 system"),
    ("17:45", "Salomé Grouffal", "Blind searches for exoplanets with NIRPS: results, limits, and synergies"),
    ("18:00", "Francisco J. Pozuelos", "Large-Scale Exoplanet Science Cases with Photonic E-MARCOT"),
    ("18:15", "Niamh O’Sullivan", "The Search for Supergranulation across Spectral Types"),
])
S("Monday", "Room 3", 3, "Olivier Demangeon", "Habitable worlds & biosignatures (future missions)", "parallel", "14:00", "16:00", [
    ("14:00", "David Charbonneau", "Habitable Worlds Observatory Project Status & Maturation Plans"),
    ("14:15", "Aaron Bello-Arufe", "Detecting biosignatures on habitable rocky worlds with ELT/ANDES"),
    ("14:30", "Sascha P. Quanz", "Decoding Other Worlds: Unlocking Planetary Habitability and Atmospheric Biosignatures with the LIFE Space Mission"),
    ("14:45", "Tyler Robinson", "Exo-Earth Science with Habitable Worlds Observatory"),
    ("15:00", "Nestor Espinoza", "The Rocky Worlds DDT Program"),
    ("15:15", "Qiao Xue", "Hot Rocks through JWST/NIRSpec’s eyes: What we learned from phase curves"),
    ("15:30", "Ryan Boukrouche", "Infrared heating hampers habitability around M stars"),
    ("15:45", "Afonso Mota", "A Biologically Defined Habitable Phase Space for Exoplanets"),
])
S("Monday", "Room 3", 3, "Clara Sousa-Silva", "JWST phase curves & resolved atmospheres", "parallel", "16:30", "18:30", [
    ("16:30", "Susana Barros", "Atmosphere and tidal deformation of WASP-103b from its JWST/NIRSpec-PRISM phase curve"),
    ("16:45", "Daphne Broski-Laing", "The best of both worlds: NIRSpec PRISM phase curves of two high-mass hot Jupiter analogs"),
    ("17:00", "Eva-Maria Ahrer", "Resolving the atmospheric limbs of HD 209458b with JWST/NIRCam"),
    ("17:15", "Jared Splinter", "Breaking Degeneracies in the Phase Curves of the Ultra-hot Jupiter WASP-121b with JWST NIRISS and NIRSpec"),
    ("17:30", "Michael Radica", "Unveiling the Nature of Super-Puffs: Early Results from a Panchromatic JWST Atmospheric Spectroscopy Survey"),
    ("17:45", "Anastasia Triantafillides", "The Panchromatic Transmission Spectrum of the Warm Jupiter WASP-80 b"),
    ("18:00", "Joost Wardenier", "Results from two ultra-hot Jupiter programs with JWST/NIRSpec: the phase curve of WASP-76b and the secondary eclipse of KELT-20b"),
    ("18:15", "Måns Holmberg", "Beyond a Homogeneous Terminator: Spatially and Temporally Resolved JWST Spectroscopy of Kepler-12 b"),
])

# ----------------------------- TUESDAY 30 JUNE -----------------------------
S("Tuesday", "Main Room", 2, "Heike Rauer (tbc)", "Future surveys: PLATO & Roman", "plenary", "09:00", "10:00", [
    ("09:00", "Don Pollacco", "The PLATO Mission"),
    ("09:30", "Scott Gaudi", "A Galactic Census of Exoplanets from the Nancy Grace Roman Space Telescope"),
    ("09:45", "Oscar Carrión-González", "Early observation plans for the Nancy Grace Roman Space Telescope Coronagraph Instrument"),
])
S("Tuesday", "Main Room", 2, "Nuno Santos", "Next-generation RV & detection", "plenary", "10:30", "12:00", [
    ("10:30", "René Doyon", "The Future of Precision Radial Velocities: From Small Planet Detection to Physical Characterization"),
    ("11:00", "Wei Wang", "Tianlin: a 6.6m UV-VIS-NIR space telescope for the exploration of exoplanet and biosignatures"),
    ("11:15", "Jonas Sauter", "Resolving the inner 1 AU of β Pictoris: planetary dynamics and close-in dust structures with VLTI/GRAVITY+"),
    ("11:30", "Florian Lienhard", "Earth-sized Planets Around the Smallest Stars: Occurrence Rates from SPECULOOS"),
    ("11:45", "Steven Giacalone", "A Stellar Obliquity Measurement for the Disintegrating Planet BD+05 4868 Ab"),
])
S("Tuesday", "Main Room", 3, "Susana Barros", "Giant planet structure & evolution", "parallel", "14:00", "16:00", [
    ("14:00", "Jonathan Fortney", "The Mass-Metallicity Relation for Giant Planets – A Revision and New Interpretation"),
    ("14:15", "Isobel Lockley", "Orbital Decay of Hot Neptunes"),
    ("14:30", "Arianna Nigioni", "The first population synthesis of planets in binaries (S-type)"),
    ("14:45", "Charles Law", "Witnessing Giant Planet Formation in the Act"),
    ("15:00", "Aaron Werlen", "Core-less Sub-Neptunes and Implications for the Mass–Radius Relation"),
    ("15:15", "Isabella Trierweiler", "Insights on exoplanetary compositions and structures from polluted white dwarfs"),
    ("15:30", "Rocio Kiman", "The Diversity of Cold Worlds: Age and Characterization of the Exoplanet COCONUTS-2b"),
    ("15:45", "Hinna Shivkumar", "Tracing the dynamical and atmospheric evolution of the young V1298 Tau planetary system"),
])
S("Tuesday", "Main Room", 3, "Amadeo Castro-González", "Sub-Neptunes, escape & retrievals", "parallel", "16:30", "18:30", [
    ("16:30", "Anna Ruth Taylor", "Exploring atmospheric escape from water-rich sub-Neptunes with full-atmosphere models"),
    ("16:45", "Matthäus Schulik", "Lifting the composition degeneracy of sub-Neptunes by understanding their molecular escape"),
    ("17:00", "Kevin Heng", "The Geoastronomy of Sub-Neptunes"),
    ("17:15", "Matthew Nixon", "Seriously, what is going on with K2-18 b?"),
    ("17:30", "Yoav Rotman", "A Matter of Perspective: How Model Construction Choices can Impact Inferences from JWST Observations"),
    ("17:45", "Divyansh Srivastava", "Time-domain atmospheric retrieval from JWST spectroscopic light curves"),
    ("18:00", "Avinash Verma", "Atmospheric Retrievals in the JWST Era: Lessons from HD 209458 b"),
    ("18:15", "Emily Omaya Garvin", "When the Likelihood Lies: Rethinking Exoplanet Atmospheric Retrievals Through Statistical Learning"),
])
S("Tuesday", "Room 2", 1, "David Armstrong", "Atmospheres across the radius valley", "parallel", "14:00", "16:00", [
    ("14:00", "James Rogers", "Using observations of escaping H/He to constrain the atmospheric composition of sub-Neptunes"),
    ("14:15", "Connor Cheverall", "Ground-based Atmospheric Characterization of Volcanic Super-Earth L 98-59 d at High Spectral Resolution"),
    ("14:30", "Pierre-Alexis Roy", "Is the hot Neptune desert populated by exposed giant planet interiors? Revealing the first thermal emission spectra of hot and super-dense sub-Neptunes"),
    ("14:45", "Adam Langeveld", "The 3D climate of WASP-121b probed with high-resolution spectroscopy"),
    ("15:00", "Björn Benneke", "Diversity in the Atmospheres of Planets near the Radius Valley"),
    ("15:15", "Brandon Coy", "A Thick Atmosphere on the Ultra-Short Period Lava World HD 3167 b"),
    ("15:30", "Jo Ann Egger", "Searching for hot water world candidates with CHEOPS"),
    ("15:45", "Thomas Beatty", "The Substellar Radius Problem: Directly Imaged Planets Are More Massive Than We Think"),
])
S("Tuesday", "Room 2", 1, "Vardan Adibekyan", "Architectures, obliquities & occurrence", "parallel", "16:30", "18:30", [
    ("16:30", "Julia Venturini", "Two stars rising: demographics, formation and characterisation of planets orbiting binary stars"),
    ("16:45", "Kaiming Cui", "Occurrence Rates of Close-in Planets and the Neptunian Desert Across Stellar Types from TESS"),
    ("17:00", "Madyson Barber", "TI-DYE: TESS Investigation - Demographics of Young Exoplanets"),
    ("17:15", "Lauren Biddle", "Spin-Orbit Alignment of Planetary Systems Through Space and Time"),
    ("17:30", "Sarah Ballard", "Exoplanet occurrence and dynamics in a galactic context"),
    ("17:45", "Domenico Barbato", "Unmasking the giants: the hunt for Gaia substellar candidates with HARPS-N"),
    ("18:00", "John Zanazzi", "Hot Jupiters, Obliquity Damping, and Resonance Locking"),
    ("18:15", "Peiwei Tu", "Planets Across Space and Time (PAST). VI. Age Dependence of the Occurrence and Architecture of Ultra-Short-Period Planet Systems"),
])
S("Tuesday", "Room 3", 4, "Pedro Viana", "Taming the Sun: stellar variability", "parallel", "14:00", "16:00", [
    ("14:00", "Ryan Rubenzahl", "Isolating pixel-level spectral variability in the Sun across time and space with multi-instrument EPRV datasets"),
    ("14:15", "Eric Ford", "Every Line Matters: Separating planetary and stellar signals via line-by-line analysis of EPRV surveys"),
    ("14:30", "Katlyn Hobbs", "Tracing the Spectral Fingerprints of Sunspots and Plage Across the Optical Spectrum"),
    ("14:45", "Angharad Weeks", "First Detection of Stellar Granulation and Oscillations from JWST Exoplanet Light Curves"),
    ("15:00", "Cis Lagae", "Stellar granulation-induced variability across the optical spectrum"),
    ("15:15", "Sabrina Sagynbayeva", "A hierarchical model for understanding stellar magnetic activity"),
    ("15:30", "Alba Barka", "Modeling Activity-Driven Signals in Photometry and Radial Velocities for Exoplanet Detection"),
    ("15:45", "Patrick McCreery", "Accurate, Precise, and Homogeneous Host Star Parameters Enable Unprecedented Age Precision from JWST Transit Light Curves"),
])
S("Tuesday", "Room 3", 2, "Solène Ulmer-Moll", "New instruments & high-contrast imaging", "parallel", "16:30", "18:30", [
    ("16:30", "Clark Baker", "Commissioning and First Light of HARPS3 on the Automated Isaac Newton Telescope"),
    ("16:45", "Jinglin Zhao", "Target Selection for the Second Earth Spectrograph (2ES): A Systematic Search for Earth Analogues"),
    ("17:00", "Mathilde Timmermans", "An update on the SPECULOOS survey: hunting small planets around the coolest stars"),
    ("17:15", "David Martin", "Small circumbinary planets are truly rarer than small single-star planets"),
    ("17:30", "Kaz Gary", "Masses of Directly-Imaged Planets via Ultra-High Precision Astrometry with the Habitable Worlds Observatory"),
    ("17:45", "Markus Bonse", "Use the 4S: A systematic re-analysis of VLT/NaCo data with Explainable Machine Learning"),
    ("18:00", "Adrien Simonnin", "High-contrast observations with ELT-ANDES: exoplanet yields with end-to-end simulations"),
    ("18:15", "Macarena Vega Pallauta", "CorGI-REx: Reference Star Vetting for the Roman Coronagraph Instrument with High-Contrast Imaging from VLT/SPHERE"),
])

# ----------------------------- WEDNESDAY 1 JULY -----------------------------
S("Wednesday", "Main Room", 3, "Kevin Heng (tbc)", "Interiors, atmospheres & the Solar System link", "plenary", "09:00", "10:30", [
    ("09:00", "Caroline Dorn", "Linking Interiors and Atmospheres in Super-Earths and Sub-Neptunes"),
    ("09:30", "Hilke Schlichting", "Bridging Solar System Evolution and Exoplanet Science"),
    ("09:45", "Tyler Fairnington", "A homogeneous survey of FGK-host Gas Giants with JWST"),
    ("10:00", "Marc Hon", "JWST’s First Look at the Disintegrating Terrestrial Planet BD+05 4868Ab"),
    ("10:15", "Kevin Ortiz Ceballos", "Magnetic radio emission from the β Pictoris exoplanetary system"),
])
S("Wednesday", "Main Room", 3, "Christianne Healing", "High-resolution spectroscopy of atmospheres", "plenary", "11:00", "13:00", [
    ("11:00", "Jayne Birkby", "From Gas Giants to Rocky Worlds: Advances from High Resolution Spectroscopy of Exoplanet Atmospheres"),
    ("11:30", "Francesco Amadori", "Joint High- and Low-Resolution Analysis of WASP-107b’s Atmosphere: Combined Strengths and Intrinsic Observational Limits"),
    ("11:45", "Romain Allart", "Three years of atmospheric characterization with The Near Infra-Red Planet Searcher (NIRPS)"),
    ("12:00", "Jaume Orell Miquel", "Probing atmospheric mass loss at disk dispersion timescales"),
    ("12:15", "Luke Parker", "Tracing cloud condensation and formation histories across the giant planet population with observations of silicon chemistry"),
    ("12:30", "Danya Alboslani", "Multi-epoch atmospheric variability of PSO J318: the first test case in a latitude-dependent study"),
    ("12:45", "Gavin Wang", "A JWST/NIRSpec Phase Curve of the Ultra-Short Period Rocky Planet K2-141 b"),
])
S("Wednesday", "Main Room", 0, "—", "PLATO mission special session", "special", "15:00", "17:00", [
    ("15:00", "Heike Rauer", "The PLATO Mission"),
    ("15:15", "Ana Heras", "PLATO status and planned data releases"),
    ("15:30", "Maximilian Guenther", "The PLATO Guest Observers Programme"),
    ("15:45", "Giampaolo Piotto", "The PLATO Input Catalog"),
    ("16:00", "Don Pollacco", "The PLATO Exoplanet Science"),
    ("16:15", "Jordan Philidet", "The PLATO Stellar Science"),
    ("16:30", "Stéphane Udry", "The Groundbased Observing Program"),
    ("16:45", "All", "Questions and discussion"),
])
S("Wednesday", "Room 3", 0, "Néstor Espinoza", "Rocky Worlds DDT data challenge", "special", "15:00", "17:00", [
    ("15:00", "Néstor Espinoza", "Rocky Worlds DDT Data Challenge – Special Session (part 1)"),
    ("16:00", "Néstor Espinoza", "Rocky Worlds DDT Data Challenge – Special Session (part 2)"),
])

# ----------------------------- THURSDAY 2 JULY -----------------------------
S("Thursday", "Main Room", 4, "Susanne Aigrain (tbc)", "Biosignatures & stellar systematics", "plenary", "09:00", "10:00", [
    ("09:00", "Daniel Apai", "Biosignature Detection and Interpretation: Challenges and Pathways"),
    ("09:30", "Nadiia Kostogryz", "Small-Scale Stellar Magnetism as a Systematic in Exoplanet Transits: Limb Darkening and Ingress–Egress Asymmetries"),
    ("09:45", "Charles Cadieux", "Sub-Kelvin Temperature Time Series of the Sun over 10 years with HARPS-N"),
])
S("Thursday", "Main Room", 4, "Jennifer Burt", "The star is the signal", "plenary", "10:30", "12:00", [
    ("10:30", "Ignasi Ribas", "The Star is the Signal: Taming Stellar Activity for Exoplanet Detection and Characterisation"),
    ("11:00", "Nuno Santos", "PoET: looking at the Sun, finding other Earths"),
    ("11:15", "Diego Munoz", "The Curious Orbits of Eccentric Warm Jupiters"),
    ("11:30", "Jared Kolecki", "Stellar [O/Si] Enhancement is a Predictor of Giant Planets"),
    ("11:45", "Jean-Michel Desert", "Responses of Exoplanet Atmospheres to Stellar Flares and Variability"),
])
S("Thursday", "Main Room", 4, "Elisa Delgado-Mena", "Stellar contamination in transit spectra", "parallel", "14:00", "16:00", [
    ("14:00", "Ben Hord", "An Overview and Early Performance Update of NASA’s Pandora SmallSat Mission to Characterize Exoplanets and Their Host Stars"),
    ("14:15", "Emily Calamari", "Connecting the Atmospheres of the Coldest Worlds and Hottest Planets"),
    ("14:30", "Vigneshwaran Krishnamurthy", "Know Thy Star, Know Thy Planet: Probing Transit Light Source Effects in an Active Late K-star"),
    ("14:45", "Giuseppe Morello", "Disentangling Stellar Activity in High-Precision Exoplanet Transmission Spectroscopy"),
    ("15:00", "Nina-Elisabeth Nemec", "The influence of stellar spectral libraries on transmission spectra"),
    ("15:15", "Gloria Canocchi", "Challenging Exoplanet Atmospheric Detections with 3D Non-LTE Stellar Spectra"),
    ("15:30", "Carmen San Nicolas Martinez", "Granulation-Driven Radial Velocity Variability: First Results from PoET"),
    ("15:45", "Mark Fortune", "New, scalable extensions of celerite to 2D data and their applications to exoplanet science"),
])
S("Thursday", "Main Room", 2, "Daniel Folha", "Detection methods: imaging, ML & pipelines", "parallel", "16:30", "18:30", [
    ("16:30", "Rachel Bowens-Rubin", "The Coolest Planets in the Neighborhood: The direct detection of frigid ice & gas giants orbiting nearby systems with JWST"),
    ("16:45", "Rodrigo Ferrer Chavez", "From data-driven to physics-based: An algorithm for 2-10x improvement in JWST exoplanet imaging sensitivity"),
    ("17:00", "Maddy Scott", "A novel Bayesian framework to compute a dataset’s sensitivity to transiting planets, with applications to occurrence rates"),
    ("17:15", "Hugo Vivien", "Automated exploration of TESS archival data with deep learning"),
    ("17:30", "Marina Ventikos", "Early-stage classifying of TESS light curves with machine learning"),
    ("17:45", "Juliana Garcia-Mejia", "A Ground-Based Transit Observation of the Long-Period Extremely Low-Density Planet HIP 41378 f"),
    ("18:00", "David Degen", "Signal or stochasticity? A human-validated dataset for single-transit detection"),
    ("18:15", "Jennifer Burt", "A Community EPRV Data Standard"),
])
S("Thursday", "Room 2", 3, "Caroline Dorn", "Ultra-hot Jupiters & atmospheric dynamics", "parallel", "14:00", "16:00", [
    ("14:00", "Engin Keles", "Detection of a Lava World atmosphere on 55 Cnc e"),
    ("14:15", "Guo Chen", "From dayside to nightside: insights from high-resolution near-infrared spectroscopy of ultrahot Jupiters"),
    ("14:30", "Julia V. Seidel", "Atmospheric Wind Measurements as Probes of Magnetic Fields in Ultra-Hot Jupiters"),
    ("14:45", "Dario Gonzalez Picos", "Clouds, Chemistry and Isotopes in β Pictoris b's Atmosphere"),
    ("15:00", "Georgia Mraz", "High Resolution Emission Phase Curve of the Ultra Hot Jupiter WASP-33 b"),
    ("15:15", "Morgan Saidel", "Tails, Torii, and Tidal Decay: Observing the Most Violent Atmospheric Outflows"),
    ("15:30", "Gaia Lacedelli", "Linking migration to atmospheric escape: first results from the ATREIDES survey of exo-Neptunes"),
    ("15:45", "Niamh Mallaghan", "Probing the unique giant exoring candidate ASASSN-21js"),
])
S("Thursday", "Room 2", 3, "Julia Seidel", "Sub-Neptunes & temperate worlds (JWST)", "parallel", "16:30", "18:30", [
    ("16:30", "Nikku Madhusudhan", "A JWST Survey of the Sub-Neptune Regime: New insights into uncharted territory"),
    ("16:45", "Lukas Felix", "Competing chemical signatures in the atmosphere of TOI-270 d"),
    ("17:00", "Alexandre Souza", "Atmospheric Characterization of K2-18 b from Combined JWST Transmission Spectroscopy"),
    ("17:15", "Achrene Dyrek", "Hot Hosts and Cool Neptunes: JWST observations of HD106315c around an F-type star"),
    ("17:30", "Lorenzo Pica-Ciamarra", "JWST Transmission Spectrum of a Benchmark Temperate Sub-Neptune"),
    ("17:45", "James Kirk", "BOWIE-ALIGN: A Population-Level Comparison of Aligned and Misaligned Hot Jupiter Atmospheres"),
    ("18:00", "Edouard Barrier", "The 3D runaway greenhouse effect on temperate sub-Neptunes"),
    ("18:15", "Jerry Xuan", "The First Spectrum of a Mature Cold Jupiter in our Backyard and the First Exoplanetary Detections of CH3D and 15NH3"),
])
S("Thursday", "Room 3", 1, "Yolanda Frensch", "Formation, abundances & dynamical origins", "parallel", "14:00", "16:00", [
    ("14:00", "Kamil Kalinowski", "Gaia Astrometric Substellar Companions: DR3 RV Follow-Up and DR4/DR5 Forecasts for Mutual Inclinations"),
    ("14:15", "Lina Messamah", "In the Company of Two: NIRPS Hunts Planets in Binary Systems"),
    ("14:30", "Nicole Wallack", "A JWST NIRSpec Phase Curve of the Ultra-Hot Super-Jupiter TOI-2109b"),
    ("14:45", "Amadeo Castro-González", "The Neptunian ridge: a dynamical fingerprint of close-in planet evolution"),
    ("15:00", "Robin Canup", "Formation of compact systems during disk infall"),
    ("15:15", "Jean-Baptiste Ruffio", "Elemental abundances of the HR 8799 planets reveal hallmarks of pebble formation"),
    ("15:30", "Alice Booth", "The Chemical Landscape of Giant Planet Formation"),
    ("15:45", "Juan Espinoza-Retamal", "POSEIDON: The Dynamical Origins of Hot and Warm Neptunes"),
])
S("Thursday", "Room 3", 1, "Hugh Osborn", "Orbital architectures & migration", "parallel", "16:30", "18:30", [
    ("16:30", "Pietro Leonardi", "Observing and modeling the orbit of a 542-Day transiting giant with large Transit Timing Variations"),
    ("16:45", "Xian-Yu Wang", "Distinct Eccentricity - Stellar Obliquity Trends in Three Gas-Giant Mass Regimes"),
    ("17:00", "Samuel Grunblatt", "Doubling the Sample of Asteroseismic Masses, Radii, and Ages for Transiting Planet Systems Observed by TESS"),
    ("17:15", "Joshua Roth", "The T16 Planet Hunt: 10,000 Newly Identified TESS Exoplanet Candidates"),
    ("17:30", "Richelle van Capelleveen", "Results from the WIde Separation Planets In Time (WISPIT) survey"),
    ("17:45", "Samuel Yee", "Not so Lonely: Hot Jupiters with Near-Resonant Companions"),
    ("18:00", "Songhu Wang", "Misaligned Cool Stars with ‘‘In-Between’’ Jupiters: Smoking-Gun Evidence for High-e Migration and Tidal Realignment"),
    ("18:15", "Jonathan Roberts", "Two Populations, Two Histories: Orbital Eccentricities of Exoplanets and Brown Dwarfs"),
])

# ----------------------------- FRIDAY 3 JULY -----------------------------
S("Friday", "Main Room", 3, "Monika Lendl", "Young & cool sub-Neptunes", "plenary", "09:00", "10:30", [
    ("09:00", "Luis Welbanks", "KRONOS: Young Sub-Neptunes and the Origins of the Galaxy’s Most Common Planets"),
    ("09:15", "Matthew Murphy", "Planetary Evolution in Progress: The Feature-rich Atmosphere of the 23 Myr Sub-Neptune Progenitor V1298 Tau c"),
    ("09:30", "Frances Rigby", "Thinking Outside the Plane-Parallel Box for Young Sub-Neptunes"),
    ("09:45", "Helena Kühnle", "Cool worlds: Unlocking the secrets of two frigid atmospheres using JWST/MIRI"),
    ("10:00", "Caroline Piaulet-Ghorayeb", "The Carbon Key: First Detailed Chemical Inventory of the Steam World Planet GJ 9827 d"),
    ("10:15", "Evert Nasedkin", "Near-Infrared Spectra of the HR 8799 planets with JWST"),
])
S("Friday", "Main Room", 1, "Ignas Snellen", "From rocky worlds to giants: latest results", "plenary", "11:00", "13:00", [
    ("11:00", "Kimberly Paragas", "LHS 3844 b’s Surface: Insights from the Highest SNR Emission Spectrum of Any Rocky Exoplanet"),
    ("11:15", "Niall Whiteford", "Weather on other worlds: JWST observes silicate cloud variability on a giant exoplanet"),
    ("11:30", "Carlos Gascon Alvarez", "First Results from the JWST Exoplanet Grand Tour Spectroscopic Survey"),
    ("11:45", "Jeehyun Yang", "A new molecule on a temperate giant orbiting a late M dwarf"),
    ("12:00", "Melissa Hobson", "ESPRESSO characterizes the small transiting exoplanet population with extreme precision radial velocities"),
    ("12:15", "Alejandro Suárez Mascareño", "Diving into the planetary system of Proxima with NIRPS"),
    ("12:30", "Allona Vazan", "Forming Water-Rich Planets from Dry Building Blocks"),
    ("12:45", "Yolanda Frensch", "Revealing uncommon gas giants transiting low-mass stars"),
])

# ----------------------------- NON-TALK EVENTS -----------------------------
EVENTS = [
    ("Sunday", "16:00", "18:30", "Registration", "logistics"),
    ("Sunday", "17:00", "19:00", "Welcome Reception", "social"),
    ("Monday", "08:15", "09:00", "Registration", "logistics"),
    ("Monday", "09:00", "09:30", "Welcome Session to Exoplanets 6", "plenary"),
    ("Monday", "10:30", "11:00", "Coffee Break", "break"),
    ("Monday", "12:00", "13:00", "Lunch", "break"),
    ("Monday", "16:00", "16:30", "Coffee Break", "break"),
    ("Tuesday", "10:00", "10:30", "Coffee Break", "break"),
    ("Tuesday", "12:00", "13:00", "Lunch", "break"),
    ("Tuesday", "16:00", "16:30", "Coffee Break", "break"),
    ("Tuesday", "20:45", "22:30", "Music Concert at Casa da Música", "social"),
    ("Wednesday", "10:30", "11:00", "Coffee Break", "break"),
    ("Wednesday", "13:00", "14:00", "Lunch", "break"),
    ("Wednesday", "18:30", "19:45", "Public Talk — Heike Rauer: Finding Other Worlds with PLATO (Rectory of the University of Porto)", "social"),
    ("Thursday", "10:00", "10:30", "Coffee Break", "break"),
    ("Thursday", "12:00", "13:00", "Lunch", "break"),
    ("Thursday", "16:00", "16:30", "Coffee Break", "break"),
    ("Friday", "10:30", "11:00", "Coffee Break", "break"),
    ("Friday", "13:00", "13:15", "Farewell", "social"),
]

# ----------------------------- THEME / TAG ENGINE -----------------------------
TAG_RULES = [
    ("JWST", ["jwst", "nirspec", "niriss", "nircam", "miri", "prism"]),
    ("RV/EPRV", ["radial velocit", "eprv", " rv ", "rv ", "harps", "espresso", "nirps", "spectrograph", "doppler", "poet"]),
    ("High-res spectroscopy", ["high-resolution", "high resolution", "high-res", "high spectral resolution"]),
    ("Direct imaging", ["imaging", "high-contrast", "high contrast", "coronagraph", "direct detection", "directly imaged", "directly-imaged"]),
    ("Astrometry", ["astrometr"]),
    ("Stellar activity", ["stellar activit", "granulation", "flare", "sunspot", "plage", "magnet", "limb darkening", "supergranulation", "oscillation", "the sun", " sun ", "solar", "stellar magnetism", "activity"]),
    ("Demographics", ["demographic", "occurrence", "census", "population synthesis", "occurrence rate"]),
    ("Interiors", ["interior", "mass-metallicity", "mass–metallicity", "mass-radius", "mass–radius", "core", "composition", "structure", "radius valley", "density"]),
    ("Atmospheres", ["atmospher", "phase curve", "transmission", "emission spectr", "retrieval", "cloud", "biosignature", "spectrum", "spectra", "chemistr", "molecule", "isotope", "escape", "outflow", "wind"]),
    ("Formation & dynamics", ["formation", "disk", "migration", "dynamic", "eccentric", "obliquity", "resonan", "circumplanetary", "tidal", "spin-orbit", "spin–orbit", "ttv", "transit timing"]),
    ("Sub-Neptunes", ["sub-neptune", "sub neptune", "neptun", "super-earth", "super earth"]),
    ("Rocky & habitable", ["rocky", "habitab", "terrestrial", "lava", "earth-twin", "earth analog", "exo-earth", "water world", "steam world"]),
    ("Missions & surveys", ["plato", "roman", "ariel", "hwo", "habitable worlds observatory", "life space", " life ", "tess", "cheops", "speculoos", "elt", "andes", "pandora", "tianlin", "mission", "telescope", "survey", "harps3"]),
    ("White dwarfs & debris", ["white dwarf", "polluted", "debris", "exocomet"]),
    ("Machine learning", ["machine learning", "deep learning", "neural", "data-driven", "explainable", "statistical learning"]),
    ("Brown dwarfs", ["brown dwarf", "l, t and y", "l t y", "substellar", "pso j318", "coconuts"]),
]

def tags_for(title):
    t = (" " + title.lower() + " ")
    out = []
    for name, kws in TAG_RULES:
        if any(k in t for k in kws):
            out.append(name)
    return out[:4]

def mins(hhmm):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)

# Build flat list of talks with derived fields + stable ids
talks_out = []
sessions_out = []
counter = 0
for si, s in enumerate(SESSIONS):
    block_end = s["end"]
    times = [t[0] for t in s["talks"]]
    sess_id = f"S{si:02d}"
    talk_ids = []
    for ti, (start, speaker, title) in enumerate(s["talks"]):
        end = s["talks"][ti + 1][0] if ti + 1 < len(s["talks"]) else block_end
        dur = mins(end) - mins(start)
        invited = dur >= 30
        counter += 1
        tid = f"t{counter:03d}"
        talk_ids.append(tid)
        talks_out.append(dict(
            id=tid, sid=sess_id, day=s["day"], room=s["room"], topic=s["topic"],
            chair=s["chair"], theme=s["theme"], kind=s["kind"],
            start=start, end=end, speaker=speaker, title=title,
            invited=invited, tags=tags_for(title),
        ))
    sessions_out.append(dict(
        id=sess_id, day=s["day"], room=s["room"], topic=s["topic"], chair=s["chair"],
        theme=s["theme"], kind=s["kind"], start=s["start"], end=block_end, talks=talk_ids,
    ))

events_out = [dict(day=d, start=st, end=en, label=lab, type=ty) for (d, st, en, lab, ty) in EVENTS]

data = dict(
    meta=dict(
        title="Exoplanets 6 — Porto 2026",
        subtitle="28 June – 3 July 2026 · Personal conference guide",
        rooms=["Main Room", "Room 2", "Room 3"],
    ),
    topics=TOPICS,
    days=[dict(name=n, date=d) for (n, d) in DAYS],
    sessions=sessions_out,
    talks=talks_out,
    events=events_out,
)

with open("data.js", "w", encoding="utf-8") as f:
    f.write("window.SCHEDULE = ")
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write(";\n")

# Summary
from collections import Counter
print("Talks:", len(talks_out), "| Sessions:", len(sessions_out), "| Events:", len(events_out))
tagc = Counter(t for tk in talks_out for t in tk["tags"])
print("Top tags:", tagc.most_common(8))
notag = [tk["speaker"] for tk in talks_out if not tk["tags"]]
print("Talks with no tag:", len(notag), notag[:10])
