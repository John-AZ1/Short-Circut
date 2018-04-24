sRadi = ['S1', 'S1', 'S3']
purge = False
sid = 1
if purge is True:
    sRadi = [x for x in sRadi if x != "S%d"%sid]
else:
    sRadi = [x for x in sRadi if x != "S%d"%sid]
    sRadi.append("S%d"%sid)
print(sRadi)
