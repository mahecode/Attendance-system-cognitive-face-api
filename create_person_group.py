import cognitive_face as CF
from global_variables import personGroupId
import sys

Key = 'd2285796756f4c62981c3f3c7dd45273'
CF.Key.set(Key)

personGroups = CF.person_group.lists()
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print(personGroupId + " already exists.")
        sys.exit()

res = CF.person_group.create(personGroupId)
print(res)
