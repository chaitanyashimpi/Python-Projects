# import the necessary module
import speedtest

#create instance of Speedtest and call it
st = speedtest.Speedtest()

# fetch the download speed
download = st.download()

# fetch the upload speed
upload = st.upload()

# display the result
print("Your Download Speed is", download)
print("Your Upload Speed is", upload)

# fetch the ping
st.get_servers([])

ping = st.results.ping

# display the result
print("Your ping is", ping)
