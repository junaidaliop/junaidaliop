<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile/hero-dark.png">
  <img alt="Muhammad Junaid Ali Asif Raja — Fractional Deep Learning" src="assets/profile/hero-light.png" width="100%">
</picture>

<h1 align="center">Muhammad Junaid Ali Asif Raja</h1>

<p align="center">
  <b>Pioneering · Engineering · Crafting&nbsp; Fractional Deep Learning</b><br>
  <sub>Machine Learning Research &nbsp;·&nbsp; Direct PhD &nbsp;·&nbsp; Fractional Intelligent Computing Lab &nbsp;·&nbsp; National Yunlin University of Science &amp; Technology &nbsp;·&nbsp; Douliu, Taiwan</sub>
</p>

<p align="center">
  <a href="https://junaidaliop.github.io"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-junaidaliop.github.io-7C3AED?style=for-the-badge&logo=githubpages&logoColor=white"></a>
  <a href="https://scholar.google.com/citations?user=9VTFIJcAAAAJ"><img alt="Google Scholar" src="https://img.shields.io/badge/Scholar-profile-22D3EE?style=for-the-badge&logo=googlescholar&logoColor=white"></a>
  <a href="https://orcid.org/0009-0008-9249-9983"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-0009--0008--9249--9983-A78BFA?style=for-the-badge&logo=orcid&logoColor=white"></a>
  <a href="https://junaidaliop.github.io/assets/pdf/cv.pdf"><img alt="CV" src="https://img.shields.io/badge/CV-PDF-0E7490?style=for-the-badge&logo=adobeacrobatreader&logoColor=white"></a>
  <a href="mailto:muhammadjunaidaliasifraja@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-contact-7C3AED?style=for-the-badge&logo=protonmail&logoColor=white"></a>
</p>

<p align="center">
  <img alt="Citations"  src="https://img.shields.io/badge/citations-188-A78BFA?style=flat-square&labelColor=2D1F4A">
  <img alt="h-index"    src="https://img.shields.io/badge/h--index-9-A78BFA?style=flat-square&labelColor=2D1F4A">
  <img alt="i10-index"  src="https://img.shields.io/badge/i10--index-8-A78BFA?style=flat-square&labelColor=2D1F4A">
  <img alt="papers"     src="https://img.shields.io/badge/papers-27%2B-22D3EE?style=flat-square&labelColor=164E63">
  <img alt="repos"      src="https://img.shields.io/badge/public%20repos-16-22D3EE?style=flat-square&labelColor=164E63">
  <img alt="lang"       src="https://img.shields.io/badge/lang-Python%20%C2%B7%20Jupyter%20%C2%B7%20MATLAB-10B981?style=flat-square&labelColor=064E3B">
  <a href="mailto:muhammadjunaidaliasifraja@gmail.com"><img alt="Open to collaborations" src="https://img.shields.io/badge/open%20to%20collaborations-let's%20talk-F59E0B?style=for-the-badge&labelColor=78350F&logo=maildotru&logoColor=white"></a>
</p>

> [!IMPORTANT]
> **Thesis.** Classical solvers spend most of their budget evaluating memory kernels.
> Deep networks, given the right structure, can absorb those kernels in a single forward pass.

---

## Programme

I am **pioneering Fractional Deep Learning** — a coherent family of neural architectures, training objectives, and optimizers built around fractional-order operators. The class of systems under study is

$$ {}^{C}_{\,0}\mathcal{D}^{\alpha}_{t}\,x(t) \;=\; f\!\big(x(t),\,x(t-\tau),\,t\big), \qquad 0 < \alpha \leq 1, $$

and the trained surrogate $x_\theta$ minimises a fractional-residual criterion

$$ \mathcal{L}(\theta) \;=\; \sum_{t}\big\Vert\, x_\theta(t) - x(t)\,\big\Vert_{2}^{2} \;+\; \lambda\,\big\Vert\, {}^{C}_{\,0}\mathcal{D}^{\alpha}_{t}\,x_\theta(t) \,-\, f\!\big(x_\theta(t),\,x_\theta(t-\tau),\,t\big)\,\big\Vert_{2}^{2}, $$

so the network must be correct pointwise *and* correct under the fractional operator.

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class FractionalDeepLearning:
    """A coherent research programme around fractional-order operators."""
    vectors: list[str] = field(default_factory=lambda: [
        "fractional-aware optimizers for deep networks",
        "autoregressive neural emulators for fractional-order systems",
        "physics-informed losses with non-local memory kernels",
        "long-memory dynamics: cyber-physical, neuronal, ecological",
    ])
    alpha:   float = 0.95         # fractional order, Caputo sense
    horizon: int   = 1024         # rollout steps for long-memory rollouts
    kernel:  str   = "caputo"     # caputo | grunwald-letnikov | adams-bashforth
    solver:  str   = "L1-scheme"  # baseline against which surrogates compete
```

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'ui-monospace,SFMono-Regular,Menlo,monospace','primaryColor':'#7C3AED','primaryTextColor':'#ffffff','primaryBorderColor':'#A78BFA','lineColor':'#A78BFA','secondaryColor':'#0F172A','tertiaryColor':'#1E293B','clusterBkg':'#0F172A','clusterBorder':'#334155'}}}%%
flowchart LR
    A["Fractional system<br/><b>𝒟<sup>α</sup>x = f</b>"]:::sys --> B["Discretise<br/>L1 · GL · Adams"]:::num
    B --> C["Neural surrogate<br/>NARX · cascade · PINN"]:::nn
    C --> D["Long-horizon<br/>prediction"]:::out
    A -. "fractional residual" .-> C
    classDef sys fill:#7C3AED,stroke:#C4B5FD,color:#ffffff,stroke-width:2px
    classDef num fill:#1E293B,stroke:#475569,color:#E2E8F0,stroke-width:2px
    classDef nn  fill:#06B6D4,stroke:#67E8F9,color:#0F172A,stroke-width:2px
    classDef out fill:#10B981,stroke:#6EE7B7,color:#022C22,stroke-width:2px
```

---

## Currently · 2026-Q2

| | Track | Open question |
|:-:|:--|:--|
| 🟣 | **Cyber-physical systems** | Fractional malware propagation on air-gapped industrial networks — what governs the long tail? |
| 🟣 | **Computational neuroscience** | Bursting transitions in fractional Hindmarsh–Rose & memristive neurons — recoverable from short windows? |
| 🔵 | **Aquatic ecology** | Toxin–plankton–nutrient dynamics under climate forcing — surrogate or stiff solver? |
| 🟢 | **Fractional optimization** | Memory-aware gradient updates — when do they outperform Adam, and on which loss landscapes? |

---

<p align="center">
  <picture>
    <img alt="Fractional Hindmarsh–Rose spike-train signature (animated SVG)" src="assets/profile/signature.svg" width="100%">
  </picture>
</p>
<p align="center"><sub><i>signature.svg — animated phase trace of a fractional bursting neuron, rendered live in your browser.</i></sub></p>

---

## Repositories

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/junaidaliop/optim">optim</a></h3>
      Fractional-calculus-inspired optimizers for deep networks. The empirical backbone of the <i>Fractional optimization</i> track above.
      <br><br>
      <img alt="lang" src="https://img.shields.io/badge/Python-7C3AED?style=flat-square&logo=python&logoColor=white">
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/junaidaliop/MobileNetV4">MobileNetV4</a></h3>
      Clean PyTorch replication of the MobileNetV4 architecture — for benchmarking surrogate backbones against modern efficient nets.
      <br><br>
      <img alt="stars" src="https://img.shields.io/github/stars/junaidaliop/MobileNetV4?style=flat-square&color=22D3EE&labelColor=164E63&logo=github">
      <img alt="lang" src="https://img.shields.io/badge/Python-22D3EE?style=flat-square&logo=python&logoColor=white">
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/junaidaliop/MNIST-SOPCNN">MNIST-SOPCNN</a></h3>
      Self-organizing polynomial CNN reference implementation. Useful when polynomial activations enter the fractional-network design space.
      <br><br>
      <img alt="stars" src="https://img.shields.io/github/stars/junaidaliop/MNIST-SOPCNN?style=flat-square&color=A78BFA&labelColor=2D1F4A&logo=github">
      <img alt="lang" src="https://img.shields.io/badge/Python-A78BFA?style=flat-square&logo=python&logoColor=white">
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/junaidaliop/daily-research-paper-recommender">daily-research-paper-recommender</a></h3>
      Personalised arXiv-style daily recommender — runs in-lab to surface fractional-calculus and SciML preprints worth reading.
      <br><br>
      <img alt="stars" src="https://img.shields.io/github/stars/junaidaliop/daily-research-paper-recommender?style=flat-square&color=10B981&labelColor=064E3B&logo=github">
      <img alt="lang" src="https://img.shields.io/badge/Python-10B981?style=flat-square&logo=python&logoColor=white">
    </td>
  </tr>
</table>

---

## Selected work

> [!NOTE]
> Eight papers, grouped by track. The full record lives on the <a href="https://junaidaliop.github.io/publications/">publications page</a>.

### Computational neuroscience — fractional & memristive neurons

1. **A Hybrid Neural-Computational Paradigm for Complex Firing Patterns and Excitability Transitions in Fractional Hindmarsh–Rose Neuronal Models.** *Chaos, Solitons & Fractals*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.chaos.2025.116149-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.chaos.2025.116149)
2. **Design of Intelligent Bayesian-Regularized Deep Cascaded NARX Neurostructure for Predictive Analysis of FitzHugh-Nagumo Bioelectrical Model in Neuronal Cell Membrane.** *Biomedical Signal Processing and Control*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.bspc.2024.107192-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.bspc.2024.107192)
3. **A Hybrid Intelligent Computational Framework for Diverse Firing Patterns in a Fractional-Order Locally Active Memristive Neuron Model.** *Chaos, Solitons & Fractals*, 2026. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.chaos.2026.118209-A78BFA?style=flat-square&labelColor=2D1F4A)](https://doi.org/10.1016/j.chaos.2026.118209)

### Aquatic ecology — *Water Research*

4. **Neuro-Computational Surrogates for Aqueous Fractional-Order Nekton-Plankton Spatiotemporal Dynamics Under Toxicant Stress, Refuge Efficacy, and Nutrient Flux Modulation.** *Water Research*, 2026. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.watres.2025.124754-22D3EE?style=flat-square&labelColor=164E63)](https://doi.org/10.1016/j.watres.2025.124754)
5. **Design of a Fractional-Order Environmental Toxin-Plankton System in Aquatic Ecosystems: A Novel Machine Predictive Expedition with Nonlinear Autoregressive Neuroarchitectures.** *Water Research*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.watres.2025.123640-22D3EE?style=flat-square&labelColor=164E63)](https://doi.org/10.1016/j.watres.2025.123640)

### Cyber-physical systems — fractional malware propagation

6. **Design of Deep Learning Networks for Nonlinear Delay Differential System for Stuxnet Virus Spread in an Air-Gapped Critical Environment.** *Applied Soft Computing*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.asoc.2025.113091-F59E0B?style=flat-square&labelColor=78350F)](https://doi.org/10.1016/j.asoc.2025.113091)
7. **Machine Learning Knowledge Driven Investigation for Immunity Infused Fractional Industrial Virus Transmission in SCADA Systems.** *Journal of Industrial Information Integration*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.jii.2025.100940-F59E0B?style=flat-square&labelColor=78350F)](https://doi.org/10.1016/j.jii.2025.100940)

### Climate-coupled dynamics — *Engineering Applications of AI*

8. **Bayesian-Regularized Cascaded Neural Networks for Fractional Asymmetric Carbon–Thermal Nutrient–Plankton Dynamics Under Global Warming and Climatic Perturbations.** *Engineering Applications of Artificial Intelligence*, 2025. &nbsp; [![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.engappai.2025.110739-10B981?style=flat-square&labelColor=064E3B)](https://doi.org/10.1016/j.engappai.2025.110739)

<details>
<summary><b>Full record</b> — 27&#43; papers · talks · awards</summary>

&nbsp;

The complete list lives on the [publications page](https://junaidaliop.github.io/publications/); citation metrics on [Google Scholar](https://scholar.google.com/citations?user=9VTFIJcAAAAJ).

</details>

---

## Research mindmap

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'ui-monospace,SFMono-Regular,Menlo,monospace','primaryColor':'#7C3AED','primaryTextColor':'#ffffff','primaryBorderColor':'#A78BFA','lineColor':'#A78BFA'}}}%%
mindmap
  root((Fractional<br/>Deep Learning))
    Operators
      Caputo
      Grünwald–Letnikov
      Adams–Bashforth
    Methods
      NARX emulators
      Bayesian cascades
      PINN variants
      Fractional optimizers
    Systems
      Hindmarsh–Rose
      FitzHugh–Nagumo
      Memristive neurons
      Malware propagation
      Plankton dynamics
    Applications
      Cyber-physical
      Computational neuroscience
      Aquatic ecology
      Climate-coupled
```

---

<p align="center">
  <img alt="Abstract phase-portrait artwork — generative visualisation of fractional-order attractor traces" src="assets/profile/artwork-dark.jpg" width="100%">
</p>
<p align="center"><sub><i>Generative phase-portrait — produced via Codex image generation, post-processed for the README backplate.</i></sub></p>

---

```toml
[profile]
name      = "Muhammad Junaid Ali Asif Raja"
role      = "Machine Learning Research, Direct PhD"
programme = "Fractional Deep Learning"
lab       = "Fractional Intelligent Computing Lab"
affiliation = "National Yunlin University of Science & Technology"
location  = "Douliu, Taiwan"

[contact]
email      = "muhammadjunaidaliasifraja@gmail.com"
portfolio  = "https://junaidaliop.github.io"
scholar    = "https://scholar.google.com/citations?user=9VTFIJcAAAAJ"
orcid      = "https://orcid.org/0009-0008-9249-9983"
cv         = "https://junaidaliop.github.io/assets/pdf/cv.pdf"

[status]
open-to    = ["collaborations", "internships", "fractional-DL discussions"]
updated    = "2026-05"
```
