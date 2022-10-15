"""Demonstrations of dictionary capabilities."""
schools: dict[str, int]
schools = dict()
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NSCU"] = 26150
print(schools)
print(f"UNC has {schools['UNC']} students")
schools.pop("Duke")
if "Duke" in schools:
    print("FtkDis")
else:
    print("nkDis")
schools["UNC"] = 20000
schools["NSCU"] += 200

print(schools)

schools = {}
print(schools)

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

print(schools["UNCC"])

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")