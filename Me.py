from urllib.parse import parse_qsl, urlencode
from collections import defaultdict

def reorder_query(query_string):
    pairs = parse_qsl(query_string, keep_blank_values=True)

    grouped = defaultdict(list)

    # collect all values per key
    for k, v in pairs:
        grouped[k].append(v)

    # sort values for each key (custom rule)
    for k in grouped:
        grouped[k].sort(reverse=True)

    # rebuild while preserving original key order appearance
    seen = set()
    result = []

    for k, v in pairs:
        if k not in seen:
            seen.add(k)
            for val in grouped[k]:
                result.append((k, val))

    return urlencode(result, doseq=True)
