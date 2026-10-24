"""Reproducible Semantic Scholar search for Deliverable 04.
Usage: python run_search.py  -> writes results/<search>_<UTC timestamp>.json and a log line.
"""
import json, time, datetime, pathlib, urllib.parse, urllib.request

BASE = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FIELDS = "paperId,title,abstract,year,venue,journal,publicationTypes,externalIds,authors"
YEAR = "2023-2026"

# Final string (v3). Plain words are used instead of most prefix wildcards: known-item testing showed that
# some wildcards (e.g. randomi*) silently fail in the bulk endpoint. See search_notes.md.
P = '("higher education" | university | universities | undergraduate | undergraduates | college)'
T = ('("generative AI" | GenAI | "generative artificial intelligence" | ChatGPT | "large language model" | '
     '"large language models" | LLM | LLMs | chatbot | chatbots | "conversational agent" | '
     '"conversational agents" | "conversational AI")')
M = '(Socratic | scaffolding | scaffold | "self-reflection" | reflection | metacognitive | metacognition | guidance | hints)'
O = ('("critical thinking" | "self-regulated learning" | reflection | dependence | dependency | '
     '"over-reliance" | overreliance | "academic integrity" | metacognitive)')
D = ('(randomized | randomised | "controlled trial" | "quasi-experimental" | "quasi-experiment" | experiment | '
     'experimental | "control group" | "within-domain" | conditions | compares)')

SEARCHES = {"C_final": f"+{P} +{T} +{M} +{O} +{D}"}

def get(params, tries=6):
    url = BASE + "?" + urllib.parse.urlencode(params)
    for k in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2 * (k + 1)); continue
            raise
    raise RuntimeError("rate limited")

def run(name, query):
    params = {"query": query, "year": YEAR, "fields": FIELDS}
    first = get(params); total = first.get("total"); data = list(first.get("data", []))
    token = first.get("token")
    while token:
        time.sleep(1.1)
        page = get({**params, "token": token}); data += page.get("data", []); token = page.get("token")
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = pathlib.Path("results"); out.mkdir(exist_ok=True)
    rec = {"search": name, "query": query, "year": YEAR, "executed_utc": stamp,
           "total_reported": total, "retrieved": len(data), "data": data}
    (out / f"{name}_{stamp}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    with open("search_log.tsv", "a") as f:
        f.write(f"{stamp}\t{name}\t{total}\t{len(data)}\t{query}\n")
    print(name, "total:", total, "retrieved:", len(data))
    return data

if __name__ == "__main__":
    for n, q in SEARCHES.items():
        run(n, q); time.sleep(1.5)
