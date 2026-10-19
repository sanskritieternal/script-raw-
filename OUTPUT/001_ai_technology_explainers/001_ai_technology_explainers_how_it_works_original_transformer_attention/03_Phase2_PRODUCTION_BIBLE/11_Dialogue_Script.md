# Master narration — revision P2-2
This is the complete proposed EN voiceover, divided into 75 planned eight-second cues. Text inside the Spoken column is spoken; cue numbers, timing and claim IDs are production annotations. No researcher quotations or impersonations are used.

1448 whitespace-delimited words. Planned delivery approximately 150–175 words/minute with visual holds. Timing is an estimate; actual audio must fit each slot before media acceptance. Numerical expressions and proper names can expand spoken duration, so rehearse rather than inferring fit from word count. Retain final visual reading space and revise a cue if needed.

| Cue / planned scene | Time | Spoken narration | Claims |
|---|---|---|---|
| 001 | 00:00–00:08 | Look at a diagram filled with bright connections. What, exactly, would you need to know before trusting its explanation? | Editorial framing/question; no new factual assertion |
| 002 | 00:08–00:16 | Our question is deliberately narrow: how does attention combine information, and where should an explanation of that operation stop? | Editorial framing/question; no new factual assertion |
| 003 | 00:16–00:24 | We will use the original Transformer paper, first submitted to arXiv in June two thousand seventeen. | C001 |
| 004 | 00:24–00:32 | We will also work through invented numbers. They are teaching materials, never measurements collected from a trained model. | C011, C012 |
| 005 | 00:32–00:40 | Keep three questions separate: what is being calculated, what system contains that calculation, and what evidence supports an interpretation? | Editorial framing/question; no new factual assertion |
| 006 | 00:40–00:48 | A useful explanation should let you inspect the steps. It should also tell you which conclusions those steps cannot establish. | Editorial framing/question; no new factual assertion |
| 007 | 00:48–00:56 | Our small example will have three positions, which we will call A, B, and C. The labels carry no word meanings. | C011 |
| 008 | 00:56–01:04 | Instead of showing a mysterious machine, we will show supplied inputs, a calculation, and its resulting vector. | C011, C012 |
| 009 | 01:04–01:12 | Later, we will change which positions are allowed into that calculation. Watch the normalization, rather than just the colored arrows. | C013 |
| 010 | 01:12–01:20 | Finally, we will ask why describing an operation and explaining a model's prediction require different kinds of evidence. | C009, C010 |
| 011 | 01:20–01:28 | First, locate the operation. The original Transformer has an encoder and a decoder; this is our historical architecture. | C002 |
| 012 | 01:28–01:36 | Its attention appears in three settings: encoder self-attention, decoder self-attention, and attention connecting the decoder with the encoder. | C005 |
| 013 | 01:36–01:44 | Keep those settings distinct. A rule for one should not quietly become a rule for every part of the diagram. | C005, C006 |
| 014 | 01:44–01:52 | For now, isolate one calculation. In scaled dot-product attention, query and key scores are scaled and normalized before values are combined. | C003 |
| 015 | 01:52–02:00 | Think of query, key, and value as labels for mathematical roles. Our diagram should preserve those labels throughout the demonstration. | C003 |
| 016 | 02:00–02:08 | A score is not the final combined result. Follow each stage rather than treating every highlighted connection as the same quantity. | C003 |
| 017 | 02:08–02:16 | The normalization step belongs between scoring and combining. We will make its arithmetic visible rather than hiding it behind an animation. | C003, C011 |
| 018 | 02:16–02:24 | Our supplied vectors are already prepared for this operation. We are not demonstrating how a trained model learned them. | C011 |
| 019 | 02:24–02:32 | That boundary matters: checking an example's arithmetic cannot tell us which words a real model would connect in a real task. | C011, C012 |
| 020 | 02:32–02:40 | We can inspect each quantity slowly while keeping the limit clear: this example does not observe an actual model. | C011, C012 |
| 021 | 02:40–02:48 | Here are invented inputs. The label reminds us that these numbers were chosen for teaching, rather than measured from a model. | C011 |
| 022 | 02:48–02:56 | The query is square root of two times natural log of two, followed by zero. The exact expression stays on screen. | C011 |
| 023 | 02:56–03:04 | The keys for A, B, and C are one, zero; zero, one; and zero, zero, respectively. | C011 |
| 024 | 03:04–03:12 | For each key, take its dot product with the query, then divide by the square root of two. | C003, C011 |
| 025 | 03:12–03:20 | The resulting scores are natural log of two, zero, and zero. These are intermediate scores, not the final weights. | C011 |
| 026 | 03:20–03:28 | Now exponentiate those scores. For our chosen numbers, the three contributions are two, one, and one. | C011 |
| 027 | 03:28–03:36 | Their total is four. Divide each contribution by that total so we can inspect the normalized weights. | C011 |
| 028 | 03:36–03:44 | A receives one half. B receives one quarter. C receives one quarter. In this invented example, those weights sum to one. | C011 |
| 029 | 03:44–03:52 | Pause on the fractions. The colors should help you follow the calculation, while the labels preserve its exact values. | C011 |
| 030 | 03:52–04:00 | Nothing here was discovered by asking a model a question. We selected the inputs so that you could check every step. | C011 |
| 031 | 04:00–04:08 | Next come the values. A has the vector two, zero. B has zero, four. C has zero, zero. | C012 |
| 032 | 04:08–04:16 | Multiply A's value by its weight of one half. Its contribution to the combined vector is one, zero. | C011, C012 |
| 033 | 04:16–04:24 | Multiply B's value by one quarter. Its contribution is zero, one. C's weighted contribution remains zero, zero. | C011, C012 |
| 034 | 04:24–04:32 | Adding these contributions gives the combined vector one, one. The result follows directly from the supplied values and weights. | C012 |
| 035 | 04:32–04:40 | This distinction is worth keeping: a weight describes a coefficient in the combination; the combined vector is a different object. | C003, C012 |
| 036 | 04:40–04:48 | The output is two numbers. Our illustration has neither a prediction head nor a trained network interpreting a sentence. | C012 |
| 037 | 04:48–04:56 | Try tracing the result backward on the diagram. Which value contributed to the first coordinate, and which to the second? | C012 |
| 038 | 04:56–05:04 | In these invented numbers, A supplies the first coordinate and B supplies the second. The labels make the calculation inspectable. | C012 |
| 039 | 05:04–05:12 | You can verify that arithmetic without making a claim about language understanding, conscious attention, or the cause of a model's prediction. | C012 |
| 040 | 05:12–05:20 | Now keep the same supplied vectors. We will change the allowed positions and calculate the weights again. | C013 |
| 041 | 05:20–05:28 | The original decoder's self-attention masks future positions before softmax. This does not describe every attention setting in the architecture. | C006 |
| 042 | 05:28–05:36 | For our separate masking illustration, place the query at B. Allow A and B, and exclude C from the combination. | C013 |
| 043 | 05:36–05:44 | The allowed exponential contributions are now two and one. The excluded position contributes zero to their normalization total. | C013 |
| 044 | 05:44–05:52 | The total is three. The new weights are two thirds, one third, and zero, in the order A, B, C. | C013 |
| 045 | 05:52–06:00 | Notice the important change: we normalized again over allowed positions. We did not simply erase the old quarter assigned to C. | C013 |
| 046 | 06:00–06:08 | If we erased that old weight without normalizing again, the remaining weights would total three quarters rather than one. | C011, C013 |
| 047 | 06:08–06:16 | Using the new weights, A contributes four thirds to the first coordinate. B contributes four thirds to the second. | C013 |
| 048 | 06:16–06:24 | The masked example therefore produces four thirds, four thirds. Both its weights and its result are shown as exact fractions. | C013 |
| 049 | 06:24–06:32 | These are two versions of an invented calculation, not an experiment showing that masking improves a trained model's performance. | C013 |
| 050 | 06:32–06:40 | What you can inspect is the operation: the allowed positions changed, the normalization changed, and the weighted sum changed. | C013 |
| 051 | 06:40–06:48 | Before leaving the diagram, put the operation back in context. This small calculation does not represent the whole original architecture. | C002, C008 |
| 052 | 06:48–06:56 | Multi-head attention joins projected head outputs and projects their concatenation. Our single-query illustration leaves that larger structure out. | C004 |
| 053 | 06:56–07:04 | Avoid giving a head a permanent human-like job based on a decorative illustration. This episode has not measured such a job. | Editorial framing/question; no new factual assertion |
| 054 | 07:04–07:12 | The original design also adds positional encodings to input embeddings. Keep this architectural step separate from our supplied toy inputs. | C007 |
| 055 | 07:12–07:20 | Feed-forward sublayers, residual connections, and normalization also belong to the architecture. An attention-only picture needs that visible boundary. | C008 |
| 056 | 07:20–07:28 | A simplified drawing is useful when you can identify both the operation it shows and the parts it leaves out. | Editorial framing/question; no new factual assertion |
| 057 | 07:28–07:36 | Remember the three attention settings. Their different places in the architecture help you keep the described operations distinct. | C005 |
| 058 | 07:36–07:44 | Return to the full diagram with the same labels. Keep the historical system identified throughout the architecture explanation. | C002 |
| 059 | 07:44–07:52 | The explanation remains about a selected design and a selected operation. It is not a specification for every product using AI. | Editorial framing/question; no new factual assertion |
| 060 | 07:52–08:00 | That prepares the final question: even with the mechanism visible, what would justify treating its attention weights as an explanation? | C009, C010 |
| 061 | 08:00–08:08 | Jain and Wallace investigated that question in studied attention-based NLP models. Their model scope must travel with their reported result. | C009 |
| 062 | 08:08–08:16 | They found substantially different attention distributions that could accompany similar predictions. Their finding concerns the systems studied in their experiments. | C009 |
| 063 | 08:16–08:24 | Our invented arithmetic does not reproduce that experiment. It cannot independently confirm or refute their conclusions about model explanations. | C009, C011, C012 |
| 064 | 08:24–08:32 | Wiegreffe and Pinter argued that assessing attention as explanation depends on a definition of explanation and model-aware testing. | C010 |
| 065 | 08:32–08:40 | That response asks us to define what would count as an explanation before deciding how to test it. | C010 |
| 066 | 08:40–08:48 | Read the two positions together. Ask which model, which prediction, and which criterion of explanation each discussion concerns. | C009, C010 |
| 067 | 08:48–08:56 | Neither title should become a universal slogan about every attention head. Keep the claim as narrow as the evidence inspected here. | C009, C010 |
| 068 | 08:56–09:04 | A bright heatmap can invite a story. Before accepting that story, ask what test connects the diagram to the interpretation. | Editorial framing/question; no new factual assertion |
| 069 | 09:04–09:12 | For this episode, the result is a careful question rather than a claim that a mathematical picture reveals human-like thought. | Editorial framing/question; no new factual assertion |
| 070 | 09:12–09:20 | We can describe an operation, check an example, and still require further evidence before making a claim about a model's reasoning. | C009, C010, C012 |
| 071 | 09:20–09:28 | Ask three questions of the next diagram: what system is shown, what quantity appears, and what evidence supports its meaning? | Editorial framing/question; no new factual assertion |
| 072 | 09:28–09:36 | Keep the synthetic label on invented examples. Keep the source and its limits with any result reported by a study. | C009, C010, C011 |
| 073 | 09:36–09:44 | Our arithmetic showed supplied weights combining supplied values. It did not measure a trained model's understanding or settle the explanation debate. | C011, C012, C013 |
| 074 | 09:44–09:52 | The source links let you inspect the historical design and both research positions. Follow them when you want the precise context. | C001, C009, C010 |
| 075 | 09:52–10:00 | Understanding the steps is useful. Knowing exactly where those steps stop supporting a conclusion is part of understanding them well. | Editorial framing/question; no new factual assertion |

## Synchronization rules
PRODUCTION_MANIFEST.json (narration_plan) preserves the same cue text, claim references and timing inputs for Phase 3. Edit both together and repeat integrity checks. The scene breakdown later carries these claim IDs and exact source locators. All visual numerical text must agree with the synthetic calculation. No actual captions, recorded voice files or measured delivery durations exist yet.
