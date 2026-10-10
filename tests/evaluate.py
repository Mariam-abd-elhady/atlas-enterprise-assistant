"""DeepEval evaluation. Owner: Person 4.

Reads tests/eval_cases.jsonl, runs each case through src.graph.run_question,
builds LLMTestCase objects, computes the 5 DeepEval metrics + routing accuracy,
and writes outputs/eval_report.json.
"""
