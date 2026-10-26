# 062 selected source inspection — 2026-10-24

These are bounded research leads for proposed PC episodes. Specifications, firmware revisions, model numbers and test conditions must be named before a performance or reliability claim becomes actionable.

## PCIe lanes — BANK-062-053

The [PCI-SIG PCIe 5.0 FAQ](https://pcisig.com/what-bit-rates-does-pcie-50-specification-support-and-how-does-it-compare-prior-pcie-generations) distinguishes per-lane transfer rate, lane count and bandwidth in each direction. The archived “64 GB/s across the motherboard” claim has no fixed meaning without PCIe generation, link width, encoding overhead and whether one or both directions are counted. Use a specific CPU, chipset, motherboard manual and device slot map for the case.

## GPU power excursions — BANK-062-056

Intel's [ATX 3.0 power-supply excursion design guide](https://edc.intel.com/content/www/pl/pl/design/ipla/software-development-platforms/client/platforms/alder-lake-desktop/atx-version-3-0-multi-rail-desktop-platform-power-supply-design-guide/2.01/psu-power-excursion/) specifies short-duration add-in-card and PSU budget behavior beyond a steady wattage label. A 450 W GPU and 1,000 W PSU anecdote needs actual PSU revision, connector, rail behavior, excursion duration and failure log; the two numbers alone do not diagnose the trip.

## Intel desktop instability — BANK-062-058

Intel's [September 2024 root-cause update](https://community.intel.com/t5/Blogs/Tech-Innovation/Client/Intel-Core-13th-and-14th-Gen-Desktop-Instability-Root-Cause/post/1633239/highlight/true?profile.language=en) describes Vmin shift, affected 13th and 14th generation **desktop** processors, operating scenarios and BIOS-delivered microcode 0x12B. A [later Intel 0x12F update](https://community.intel.com/t5/Mobile-and-Desktop-Processors/Intel-Core-13th-and-14th-Gen-Vmin-Shift-Instabilty-Update-New/m-p/1686948) supplements that mitigation without changing the root-cause determination. Scope the board BIOS, processor SKU and update date; do not merge an oxidation report into a single cause or imply an update repairs already degraded silicon.

## Apple M1 architecture — BANK-062-055

[Apple's November 2020 M1 announcement](https://www.apple.com/newsroom/2020/11/apple-unleashes-m1/) describes an integrated SoC and unified memory, while the [M1 MacBook Air technical record](https://support.apple.com/en-us/111883) provides one shipping system configuration. These are manufacturer sources for design and model facts, not independent proof that ARM always beats x86. Compare named computers, workload, power limits, software compatibility and release date.

## EXPO/XMP memory profiles — BANK-062-060

[AMD's EXPO documentation](https://www.amd.com/en/products/processors/technologies/expo.html) identifies it as a DDR5 overclocking profile and provides compatibility information. [Intel's XMP guide](https://www.intel.com/content/www/us/en/gaming/extreme-memory-profile-xmp.html) describes profile use on supported platforms. An enabled profile is a configuration, not a guaranteed speedup. Measure a named workload with CPU, board, BIOS, DIMM kit and stability conditions fixed.

## Semantic and neighboring-scope review

New `051`–`061` select a dated architecture, interface, component behavior, fault class or market change. Existing `014`–`020` cover general CPU/GPU mechanisms; `021`–`028` storage, cooling and power; `029`–`032` diagnosis; `049` cache/bandwidth; `050` firmware recovery. A case requires model/version evidence rather than repeating those generic explanations. The JSON crosswalk routes all 27 archived pitches; the two Intel instability pitches share `058`.

Niche `511` owns semiconductor fabrication and chiplet interfaces; `512` owns quantum computing devices and benchmarking. Niche `061` owns software/programming and `063` consumer-product decisions. Those active banks were inspected. The quantum-chip pitch routes to verified `BANK-512-036`; the chiplet pitch routes to verified `BANK-511-041`. No numerical market-cap, universal performance or 2040 prediction is treated as established.

Only the listed primary sources were inspected. Other cases still need model-specific technical manuals, independent test protocols and dated compatibility records before production.
