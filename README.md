<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile/hero-dark.png">
  <img alt="Muhammad Junaid Ali Asif Raja — Fractional Deep Learning" src="assets/profile/hero-light.png" width="100%">
</picture>

<p align="center"><i>Networks should learn under fractional operators, not despite them.</i></p>

<h1 align="center">Muhammad Junaid Ali Asif Raja</h1>

<p align="center">
  <sub>Machine Learning Research &nbsp;·&nbsp; Direct-entry PhD &nbsp;·&nbsp; Fractional Intelligent Computing Lab &nbsp;·&nbsp; National Yunlin University of Science &amp; Technology &nbsp;·&nbsp; Douliu, Taiwan</sub>
</p>

<p align="center">
  <a href="https://junaidaliop.github.io"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-junaidaliop.github.io-7C3AED?style=flat-square&logo=githubpages&logoColor=white"></a>
  <a href="https://scholar.google.com/citations?user=9VTFIJcAAAAJ"><img alt="Google Scholar" src="https://img.shields.io/badge/Scholar-profile-22D3EE?style=flat-square&logo=googlescholar&logoColor=white"></a>
  <a href="https://orcid.org/0009-0008-9249-9983"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-0009--0008--9249--9983-A78BFA?style=flat-square&logo=orcid&logoColor=white"></a>
  <a href="https://junaidaliop.github.io/assets/pdf/cv.pdf"><img alt="CV" src="https://img.shields.io/badge/CV-PDF-22D3EE?style=flat-square&logo=adobeacrobatreader&logoColor=white"></a>
  <a href="mailto:muhammadjunaidaliasifraja@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-contact-7C3AED?style=flat-square&logo=protonmail&logoColor=white"></a>
</p>

---

## Fractional Deep Learning

I am working on **Fractional Deep Learning** — a thread within Scientific Machine Learning (SciML) that brings the tools of fractional calculus into deep learning. The hook is operators that encode long-range memory parametrically — Caputo, Grünwald–Letnikov, Riemann–Liouville — and the question is whether networks can *learn under* those operators rather than approximate them from outside.

The toolkit spans **physics-informed neural networks (PINNs)**, **neural operators**, **intelligent surrogates** for fractional-order systems, **fractional-aware optimizers**, and **fractional spiking neural networks (FSNNs)** — the leaky integrate-and-fire (LIF) cell lifted into Caputo-sense dynamics. The domains are wherever memory is the structure: computational neuroscience (Hindmarsh–Rose, FitzHugh–Nagumo, memristive neurons), cyber-physical systems (delay-differential malware propagation, SCADA security), aquatic ecology (toxin–plankton–nutrient dynamics), and climate-coupled forcing.

The shape of the field is still settling. That is the point.

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class FractionalDeepLearning:
    """A SciML thread bringing fractional calculus into deep learning."""
    methods:  tuple[str, ...] = (
        "physics-informed neural networks  (PINNs)",
        "neural operators",
        "intelligent surrogates",
        "fractional-order optimization",
        "fractional spiking neural networks  (FSNNs)",
    )
    domains:  tuple[str, ...] = (
        "fractional-order differential systems",
        "computational neuroscience",
        "cyber-physical systems",
        "aquatic ecology",
        "climate-coupled dynamics",
    )
    alpha:    float = 0.95          # fractional order, Caputo sense
    kernel:   str   = "caputo"      # caputo | grunwald-letnikov | riemann-liouville
    horizon:  int   = 1024          # rollout horizon for long-memory dynamics
    open:     bool  = True          # research direction still taking shape
```

---

## Selected work

1. **A Hybrid Neural-Computational Paradigm for Complex Firing Patterns and Excitability Transitions in Fractional Hindmarsh–Rose Neuronal Models.** *Chaos, Solitons & Fractals*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.chaos.2025.116149-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.chaos.2025.116149)
2. **Design of Intelligent Bayesian-Regularized Deep Cascaded NARX Neurostructure for Predictive Analysis of FitzHugh–Nagumo Bioelectrical Model in Neuronal Cell Membrane.** *Biomedical Signal Processing and Control*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.bspc.2024.107192-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.bspc.2024.107192)
3. **A Hybrid Intelligent Computational Framework for Diverse Firing Patterns in a Fractional-Order Locally Active Memristive Neuron Model.** *Chaos, Solitons & Fractals*, 2026. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.chaos.2026.118209-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.chaos.2026.118209)
4. **Neuro-Computational Surrogates for Aqueous Fractional-Order Nekton–Plankton Spatiotemporal Dynamics Under Toxicant Stress, Refuge Efficacy, and Nutrient Flux Modulation.** *Water Research*, 2026. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.watres.2025.124754-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.watres.2025.124754)
5. **Design of a Fractional-Order Environmental Toxin–Plankton System in Aquatic Ecosystems: A Novel Machine Predictive Expedition with Nonlinear Autoregressive Neuroarchitectures.** *Water Research*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.watres.2025.123640-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.watres.2025.123640)
6. **Design of Deep Learning Networks for Nonlinear Delay Differential System for Stuxnet Virus Spread in an Air-Gapped Critical Environment.** *Applied Soft Computing*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.asoc.2025.113091-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.asoc.2025.113091)
7. **Machine Learning Knowledge Driven Investigation for Immunity Infused Fractional Industrial Virus Transmission in SCADA Systems.** *Journal of Industrial Information Integration*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.jii.2025.100940-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.jii.2025.100940)
8. **Bayesian-Regularized Cascaded Neural Networks for Fractional Asymmetric Carbon–Thermal Nutrient–Plankton Dynamics Under Global Warming and Climatic Perturbations.** *Engineering Applications of Artificial Intelligence*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.engappai.2025.110739-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.engappai.2025.110739)

Full record on the [publications page](https://junaidaliop.github.io/publications/).

---

<p align="center">
  <img alt="Animated time series — fractional Hindmarsh–Rose ground truth vs neural surrogate prediction" src="assets/profile/signature.svg" width="100%">
</p>
<p align="center"><sub><i>signature.svg — fractional Hindmarsh–Rose bursting, ground truth vs neural surrogate, rendered live.</i></sub></p>
