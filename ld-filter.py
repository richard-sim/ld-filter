import json
import re

data = json.load(open('ld41.json'))
ideas = data["ideas"]

reduced = {}
for k, idea in ideas.items():
    sanitizedIdea = idea.lower()
    sanitizedIdea = re.sub(r"[.,!/_]", " ", sanitizedIdea)
    sanitizedIdea = re.sub(r"['\"-\\]", "", sanitizedIdea)
    sanitizedIdea = re.sub(r"\s+", " ", sanitizedIdea)
    sanitizedIdea = sanitizedIdea.strip()

    if sanitizedIdea not in reduced:
        reduced[sanitizedIdea] = (idea, [k])
    else:
        reduced[sanitizedIdea][1].append(k)

counts = []
for k, v in reduced.items():
    sanitizedIdeas = v[1]
    while len(counts) <= len(sanitizedIdeas):
        counts.append([])

    counts[len(sanitizedIdeas)].append(k)

duplicateCount = len(ideas) - len(reduced)
print("%d duplicates found (%.1f%%):" % (duplicateCount, 100.0 * duplicateCount / len(ideas)))
print("\t%d original ideas" % len(ideas))
print("\t%d sanitized ideas" % len(reduced))
for i, keys in enumerate(counts):
    if len(keys) > 0:
        print(str(i) + " items: " + ', '.join([reduced[k][0] for k in keys]))
