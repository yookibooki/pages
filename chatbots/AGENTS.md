# Pass Criteria
| criterion | requirement | pass when |
|---|---|---|
| autoscale | grid adapts to viewport | all cards visible at any viewport size, zero scroll h or v, updates live on resize |
| square | cards square | aspect 1:1 (±1px) at all times, incl. immediately after add/remove/resize |
| gap | uniform spacing | every measured gap h and v identical; content/logo never alters spacing |
| logo | contained logos | proportional, fully visible, centered both axes, never sizes card, stays clear of badges |
| badges | chips per card | score top-left, model bottom-right, above logo, zero layout impact |
| dynamic | count-agnostic | add/remove refits with no reload; code has no hardcoded counts/cols |
| coverage | max area use | no column count yields a larger card (small tolerance), grid stays centered |
| ordering | score sort | data-score non-increasing down the list after any edit |
| style | visual baseline | dark theme, rounded cards, glass chips w/ white text, as in current file |
| stack | zero-dep vanilla | single self-contained index.html, no framework/build/CDN, icons/* only external |

NOTE: Claude card is hidden during peak hours, Monday-Friday 05:00-11:00 Pacific Time (America/Los_Angeles, DST-aware).

# Mapping
Scores are the Artificial Analysis Intelligence Index at **high** reasoning effort (not max); models with no index on AA are left unchanged.

| website | best model |
|---|---|
| chatgpt.com | GPT-6 Luna |
| claude.ai | Sonnet 5.5 |
| meta.ai | Muse Spark 1.3 |
| chat.together.ai | GLM-5.3 |
| chat.z.ai | GLM-5.3 |
| chat.qwen.ai | Qwen4 Max |
| aistudio.tencent.ai | Hy4 |
| chat.deepseek.com | DeepSeek V4.1 |
| chat.stepfun.com | Step 5 Preview |
| chat.mistral.ai | GLM-5.3 |
| agent.minimax.io | M3.1 Flash |
| chat.ant-ling.com | Ling-3.2-flash |
| longcat.ai | LongCat-2.5 |
