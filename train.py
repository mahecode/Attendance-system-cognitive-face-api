import cognitive_face as CF
from global_variables import personGroupId

Key = 'd2285796756f4c62981c3f3c7dd45273'
CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

res = CF.person_group.train(personGroupId)
print(res)
