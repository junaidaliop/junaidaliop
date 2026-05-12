<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile/hero-dark.png">
  <img alt="Muhammad Junaid Ali Asif Raja — Fractional Deep Learning" src="assets/profile/hero-light.png" width="100%">
</picture>

<h1 align="center">Muhammad Junaid Ali Asif Raja</h1>

<p align="center">
  <sub>Machine Learning Research &nbsp;·&nbsp; Direct-entry PhD &nbsp;·&nbsp; Fractional Intelligent Computing Lab &nbsp;·&nbsp; National Yunlin University of Science &amp; Technology &nbsp;·&nbsp; Douliu, Taiwan</sub>
</p>

<p align="center">
  <a href="https://junaidaliop.github.io"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-junaidaliop.github.io-7C3AED?style=for-the-badge&logo=githubpages&logoColor=white"></a>
  <a href="https://scholar.google.com/citations?user=9VTFIJcAAAAJ"><img alt="Google Scholar" src="https://img.shields.io/badge/Scholar-profile-22D3EE?style=for-the-badge&logo=googlescholar&logoColor=white"></a>
  <a href="https://orcid.org/0009-0008-9249-9983"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-0009--0008--9249--9983-A78BFA?style=for-the-badge&logo=orcid&logoColor=white"></a>
  <a href="https://junaidaliop.github.io/assets/pdf/cv.pdf"><img alt="CV" src="https://img.shields.io/badge/CV-PDF-22D3EE?style=for-the-badge&logo=adobeacrobatreader&logoColor=white"></a>
  <a href="mailto:muhammadjunaidaliasifraja@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-contact-7C3AED?style=for-the-badge&logo=protonmail&logoColor=white"></a>
</p>

<p align="center">
  <img alt="Citations" src="https://img.shields.io/badge/citations-188-A78BFA?style=flat-square&labelColor=2D1F4A">
  <img alt="h-index"   src="https://img.shields.io/badge/h--index-9-A78BFA?style=flat-square&labelColor=2D1F4A">
  <img alt="papers"    src="https://img.shields.io/badge/papers-27%2B-22D3EE?style=flat-square&labelColor=164E63">
</p>

> [!IMPORTANT]
> **Thesis.** Classical fractional solvers carry their full history at every step.
> A trained neural surrogate amortises that work into a single forward pass —
> without breaking the fractional constraint.

---

## Fractional Deep Learning

A direction I am working on — still finding its shape. Three threads.

**1 · Memory is structure, not noise.**
Long-range temporal dependence in real systems is captured natively by fractional operators. Networks should learn under that structure, not despite it.

**2 · Computation is spiking, not just smooth.**
Real neurons fire; real systems with memory accumulate. **Fractional spiking neural networks (FSNNs)** make discrete events first-class under a continuous memory kernel.

**3 · Optimisation is fractional.**
Memory-aware gradient updates — Caputo, Grünwald–Letnikov — change the training dynamics on non-smooth loss landscapes.

The class of systems under study and the criterion the surrogate $x_\theta$ minimises:

$$ {}^{C}_{\,0}\mathcal{D}^{\alpha}_{t}\,x(t) \;=\; f\!\big(x(t),\,x(t-\tau),\,t\big), \qquad 0 < \alpha \leq 1 $$

$$ \mathcal{L}(\theta) \;=\; \sum_{t}\big\Vert\, x_\theta(t) - x(t)\,\big\Vert_{2}^{2} \;+\; \lambda\,\big\Vert\, {}^{C}_{\,0}\mathcal{D}^{\alpha}_{t}\,x_\theta(t) \,-\, f\!\big(x_\theta(t),\,x_\theta(t-\tau),\,t\big)\,\big\Vert_{2}^{2} $$

Correct pointwise, *and* correct under the fractional operator.

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class FractionalDeepLearning:
    """An open research direction. Surface still being defined."""
    threads: list[str] = field(default_factory=lambda: [
        "fractional spiking neural networks",
        "fractional-order optimisation for deep networks",
        "neural emulators for fractional-order dynamics",
        "physics-informed losses with non-local memory kernels",
    ])
    alpha:  float = 0.95         # fractional order, Caputo sense
    kernel: str   = "caputo"     # caputo | grunwald-letnikov | riemann-liouville
    scheme: str   = "L1"         # L1 | adams-bashforth-moulton | grunwald-letnikov-direct
    horizon: int  = 1024         # rollout horizon for long-memory dynamics
```

---

## Currently · 2026-Q2

| Track | Open question |
|:--|:--|
| **Cyber-physical systems** | What mechanisms shape the heavy-tailed infection-time distribution of fractional malware propagation on air-gapped industrial networks? |
| **Computational neuroscience** | Are bursting transitions in fractional Hindmarsh–Rose and memristive neurons recoverable from short observation windows? |
| **Aquatic ecology** | Can a neural surrogate match a stiff implicit solver on toxin–plankton–nutrient dynamics under non-stationary climate forcing? |
| **Fractional optimisation** | When do memory-aware gradient updates outperform Adam, and on which loss landscapes? |

---

## Selected work

Eight papers, four tracks. Full record on the [publications page](https://junaidaliop.github.io/publications/) — selected here, not exhaustive.

1. *[computational neuroscience]* &nbsp; **A Hybrid Neural-Computational Paradigm for Complex Firing Patterns and Excitability Transitions in Fractional Hindmarsh–Rose Neuronal Models.** *Chaos, Solitons & Fractals*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.chaos.2025.116149-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.chaos.2025.116149)
2. *[computational neuroscience]* &nbsp; **Design of Intelligent Bayesian-Regularized Deep Cascaded NARX Neurostructure for Predictive Analysis of FitzHugh–Nagumo Bioelectrical Model in Neuronal Cell Membrane.** *Biomedical Signal Processing and Control*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.bspc.2024.107192-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.bspc.2024.107192)
3. *[computational neuroscience]* &nbsp; **A Hybrid Intelligent Computational Framework for Diverse Firing Patterns in a Fractional-Order Locally Active Memristive Neuron Model.** *Chaos, Solitons & Fractals*, 2026. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.chaos.2026.118209-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.chaos.2026.118209)
4. *[aquatic ecology]* &nbsp; **Neuro-Computational Surrogates for Aqueous Fractional-Order Nekton–Plankton Spatiotemporal Dynamics Under Toxicant Stress, Refuge Efficacy, and Nutrient Flux Modulation.** *Water Research*, 2026. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.watres.2025.124754-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.watres.2025.124754)
5. *[aquatic ecology]* &nbsp; **Design of a Fractional-Order Environmental Toxin–Plankton System in Aquatic Ecosystems: A Novel Machine Predictive Expedition with Nonlinear Autoregressive Neuroarchitectures.** *Water Research*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.watres.2025.123640-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.watres.2025.123640)
6. *[cyber-physical systems]* &nbsp; **Design of Deep Learning Networks for Nonlinear Delay Differential System for Stuxnet Virus Spread in an Air-Gapped Critical Environment.** *Applied Soft Computing*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.asoc.2025.113091-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.asoc.2025.113091)
7. *[cyber-physical systems]* &nbsp; **Machine Learning Knowledge Driven Investigation for Immunity Infused Fractional Industrial Virus Transmission in SCADA Systems.** *Journal of Industrial Information Integration*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.jii.2025.100940-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.jii.2025.100940)
8. *[climate-coupled dynamics]* &nbsp; **Bayesian-Regularized Cascaded Neural Networks for Fractional Asymmetric Carbon–Thermal Nutrient–Plankton Dynamics Under Global Warming and Climatic Perturbations.** *Engineering Applications of Artificial Intelligence*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.engappai.2025.110739-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.engappai.2025.110739)

---

## Repositories

- **[optim](https://github.com/junaidaliop/optim)** — fractional-calculus-inspired optimizers for deep networks; the code behind the *fractional optimisation* thread above.
- **[MobileNetV4](https://github.com/junaidaliop/MobileNetV4)** — a clean PyTorch port of the MobileNetV4 architecture; used as a baseline backbone for surrogate-architecture experiments.
- **[MNIST-SOPCNN](https://github.com/junaidaliop/MNIST-SOPCNN)** — self-organizing polynomial CNN reference implementation.
- **[daily-research-paper-recommender](https://github.com/junaidaliop/daily-research-paper-recommender)** — a personal arXiv recommender for fractional-calculus and SciML preprints.

---

<p align="center">
  <img alt="Animated spike-train signature — fractional Hindmarsh–Rose, α = 0.95, bursting regime" src="assets/profile/signature.svg" width="100%">
</p>
<p align="center"><sub><i>signature.svg — animated time series of a fractional bursting neuron, rendered live in your browser.</i></sub></p>

<p align="center"><sub>Open to collaborations &nbsp;·&nbsp; <a href="mailto:muhammadjunaidaliasifraja@gmail.com">muhammadjunaidaliasifraja@gmail.com</a></sub></p>
