def build_chain(endpoints, params):
    return [f"{ep}?{p}=FUZZ" for ep in endpoints for p in params]
