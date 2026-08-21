def evaluate(result):
    return {"review_gate":result.get("review",{}).get("decision")=="human_review_required","sections_present":all(k in result for k in ["problem","theory","computation","evidence","review"])}
