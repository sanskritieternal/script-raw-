# Blockchain: versioned protocol-source checks (2026-10-24)

Candidate premises only. New BANK questions remain proposed with empty `verified_sources`.

## BANK-297-042: EIP-4844 and Dencun

- Ethereum Improvement Proposal, [EIP-4844: Shard Blob Transactions](https://eips.ethereum.org/EIPS/eip-4844), created 25 February 2022 and inspected 2026-10-24. The specification introduces a blob-carrying transaction type whose data is not directly accessible to EVM execution, while commitments can be accessed.
- Ethereum Foundation, [Dencun FAQ](https://ethereum.org/roadmap/dencun/), inspected 2026-10-24, dates mainnet activation to 13 March 2024 and explains temporary blob data availability for rollups.
- Limit: the current specification may reflect later parameter changes; anchor an episode's claim to the activated 2024 version or a dated commit. Temporary blob availability is not permanent archival storage or an automatic fee reduction for every transaction. Rollup-specific implementation, congestion and fee data require separate measurement.

## BANK-297-043: Fabric 2.5 private data collections

- Hyperledger Fabric project, [Private Data Architecture, release 2.5](https://hyperledger-fabric.readthedocs.io/en/release-2.5/private-data-arch.html), inspected 2026-10-24. It describes distribution of private payloads to authorized collection members and ledger hashes visible to channel peers. The versioned document flags brute-force guessing of low-entropy private data and describes access and purge controls.
- Limit: a hash can demonstrate consistency with a supplied value, not the truth of the real-world data or secrecy against guessing. Application policy, identities, collection configuration, versions and authorized peers determine actual behavior. The page is versioned documentation, not proof that a particular deployment enforced it correctly; inspect its configuration and transaction records before case-specific claims.
