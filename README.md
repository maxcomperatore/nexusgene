# Nexusedit (NEXUS-880)
### In Vivo Base-Editing Therapeutic Platform
#### Preclinical Investigation & Target Product Profile (TPP) Data Room

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Target](https://img.shields.io/badge/Target-TTR%20(ENSG00000118271)-emerald.svg)](https://platform.opentargets.org/target/ENSG00000118271)
[![Modality](https://img.shields.io/badge/Modality-In%20Vivo%20Base%20Editor-cyan.svg)](#mechanism-of-action)
[![Delivery](https://img.shields.io/badge/Delivery-ApoE--LNP-purple.svg)](#lipid-nanoparticle-delivery)

---

## 1. Executive Summary

**Nexusedit (NEXUS-880)** is a novel in vivo base-editing candidate designed to target Transthyretin (TTR) amyloidosis. 

Unlike standard CRISPR-Cas systems that introduce double-stranded DNA breaks, NEXUS-880 utilizes a precision deaminase tethered to a catalytically modified Cas12a complex to perform direct single-base transitions without cleaving the DNA backbone, mitigating the risk of chromosomal translocations.

---

## 2. Market Opportunity

* **Addressable Market**: Global in vivo gene editing is projected to grow substantially by 2034.
* **Clinical Need**: Current standard of care requires lifelong continuous therapy. A one-time in vivo base-editing approach offers permanent genetic silencing.

---

## 3. Genetic Validation & OpenTargets Evidence

Data sourced from OpenTargets (`ENSG00000118271`):
* Strong genetic causality between mutant TTR variants and amyloid disease.
* High biological tolerance for circulating TTR reduction in adult human populations.

---

## 4. Mechanism of Action

1. **Cellular Uptake**: Ionizable lipid nanoparticles enter hepatocytes via endogenous ApoE-mediated receptor uptake.
2. **Precision Deamination**: The engineered ribonucleoprotein complex targets the splice junction, permanently silencing protein output.
3. **Genomic Integrity**: Zero double-stranded cuts prevents non-homologous end-joining errors.

---

## 5. Structural Biology

* **Structure**: Based on the Cas12a / crRNA complex (PDB: 5XUS).
* **PAM Engineering**: Modified PAM-interacting loop enables targeted binding to previously inaccessible non-canonical splice junctions.

---

## 6. Reproducibility

```bash
# Clone the repository
git clone https://github.com/maxcomperatore/nexusgene.git
cd nexusgene

# Run analysis scripts
uv run --with requests --with matplotlib python fetch_ttr_genetics.py
```

---

## License
Released under the MIT License for research and computational benchmarking.
