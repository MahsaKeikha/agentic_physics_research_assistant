def run(payload=None):
    payload = payload or {}
    return {"system":"F81","status":"reference_analysis_ready","input":payload,"human_review_required":True}

if __name__ == "__main__":
    print(run())
