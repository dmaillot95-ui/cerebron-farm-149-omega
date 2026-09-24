import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parent; NAME="OMEGA"
required=[ROOT/"architecture"/"OMEGA_ARCHITECTURE_V1.json",ROOT/"memory"/"OMEGA_MEMORY_CONTRACT_V1.json",ROOT/"benchmarks"/"OMEGA_BENCHMARK_V1.json",ROOT/"config"/"model-candidates.json",ROOT/"training"/"OMEGA_TRAINING_READINESS_GATES_V1.json"]
missing=[str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing: print(json.dumps({"status":"FAIL","missing":missing})); raise SystemExit(1)
b=json.loads((ROOT/"benchmarks"/"OMEGA_BENCHMARK_V1.json").read_text()); m=json.loads((ROOT/"memory"/"OMEGA_MEMORY_CONTRACT_V1.json").read_text()); a=json.loads((ROOT/"architecture"/"OMEGA_ARCHITECTURE_V1.json").read_text())
assert b["m6_rule"]=="M6_NEVER_IN_TRAIN"; assert "M6_COLD_BENCHMARK" in m["training_forbidden"]; assert a["runtime_changed"] is False
print(json.dumps({"status":"PASS","name":NAME,"m6_guard":True,"runtime_changed":False,"required_files":len(required)}))
