def build_chain(endpoints, params):
    chains = []
    for ep in endpoints:
        for p in params:
            chains.append(f"{ep}?{p}=FUZZ")
    return chains
