import time
import rsa
def gen_certificate(uav_public):
    second = time.time()#represent with number
    timestamp = time.ctime(second)#represent with char
    expired = second + 60*60*24 # one day 
    expired_time = time.ctime(expired)
    device = ['AA','AB','AC']
    gcs_public = "45,7988" #public for people to varified never change
    certificate = "SIGNTIME: " + timestamp + "\n" + "EXPIREDTIME: " + expired_time + "\n" + "DEVICE: " + " ".join(device) + "\n" + "GCS: " + gcs_public+ "\n" + "UAV: " + uav_public + "\n"
    sign = "kadhjfhsalkfhsoak"#use function to sign
    return certificate + sign
