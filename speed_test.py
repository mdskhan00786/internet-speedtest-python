from speedtest import Speedtest
st = Speedtest()

print("Your connection downloading speed is : ",st.download())
print("Your connection uploading speed is : ",st.upload())