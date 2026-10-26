# Selected primary-source research: data-center infrastructure cases

Checked 2026-10-24. These checks bound two new cases and one routed archived power-deal premise. They do not verify other capacity, cable, uptime, cooling-cost or water claims.

## GB200 NVL72 rack design — BANK-160-042

- Primary designer sources: NVIDIA, [15 October 2024 OCP design description](https://developer.nvidia.com/blog/nvidia-contributes-nvidia-gb200-nvl72-designs-to-open-compute-project/) and [DGX GB rack hardware guide](https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html).
- NVIDIA describes a GB200 NVL72 configuration with 72 GPUs and roughly 120 kW rack power/cooling demand, using direct liquid cooling for selected components plus air cooling for others.
- Limit: These are manufacturer reference designs and specifications, not measurements of every deployed rack or a finding that air cooling universally fails at 100 kW. Facility-level heat rejection, water use and actual load depend on configuration and operating conditions. Do not derive an electrical or cooling installation procedure from the public design.

## Northern Virginia completed connections — BANK-160-043

- Primary utility record: Dominion Energy, [2024 Sustainability and Corporate Responsibility Report](https://sustainability.dominionenergy.com/SCR-Report-2024.pdf). It reports connecting 15 data centers in 2024 with combined capacity of nearly 1 GW.
- Limit: Connected capacity is not the same as measured annual consumption, pending applications, a seven-year queue, a regional shortage or a global share of internet traffic. The record is Dominion’s own report for a specified year; a bottleneck episode would need dated utility/regulator queue and grid studies.

## Three Mile Island Unit 1 power agreement — BANK-160-021

- Primary company record: Constellation, [20 September 2024 announcement of its 20-year Microsoft power purchase agreement](https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html). It described a plan to restart the retired Unit 1 as Crane Clean Energy Center, subject to the relevant regulatory and operational steps.
- Limit: A purchase agreement and planned restart did not, on that date, mean power was already delivered to a Microsoft data center. Keep Unit 1 separate from the 1979 Unit 2 accident. The agreement’s timing boundary is already scoped in [BANK-001-205](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-205), so no duplicate case was added here. For any current-status episode, recheck licensing, commissioning and delivered-energy records as of its script date.

## Semantic homes

This niche covers rack integration, regional utility connections and facility procurement. [General AI server heat paths](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-206), [SMR energy investment](../113_energy_power/IN_DEPTH_TOPIC_BANK.md#bank-113-025), [indirect water accounting](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-203) and [undersea internet history](../129_internet_history/IN_DEPTH_TOPIC_BANK.md#bank-129-035) remain distinct questions.
