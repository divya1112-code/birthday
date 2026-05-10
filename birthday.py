import streamlit as st
import time

# 🖤 Fake lock screen
st.markdown("## 🔒 Private Access System")
st.markdown("### Unauthorized access is prohibited")

name_check = st.text_input("Who is this for? 💖")
password = st.text_input("Enter Secret Code 🔐", type="password")

if name_check.lower() == "yashika" and password == "davuni":

    st.success("Access Granted 💖")
    
    # ⏳ Fake loading
    with st.spinner("Decrypting memories... 💭"):
        time.sleep(2)

    st.balloons()

    st.markdown("## 💖 I made this just for you… click slowly 💖")
    st.markdown("🎶 Make sure your sound is on 💖")

    if st.button("Start 🎬"):

        audio_file = open("song.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        countdown = st.empty()
        for i in range(3, 0, -1):
            countdown.markdown(f"## 💖 {i} 💖")
            time.sleep(1)

        countdown.empty()

        messages = [
            """💖 Happy Birthday Yashika 💖
I still remember how everything started…
how randomly you came to my house to give an invite,
and then one day you asked about admission…
And just like that… our friendship began 💕""",

            """🥺
From random laughs to deep talks,
everything feels so special with you 💖""",

            """✨
You understand me without words…
I’m really lucky to have you in my life 💕""",

            """🌸
You stayed when everyone else left…
even when I didn’t ask you to.
I’ll never forget that 💖""",
            """🎂
Happy Birthday Yashika 🎉
You are my forever person 💕
Love you always 💖"""
        ]
        images = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg", "img5.jpg"]
        for i in range(len(images)):
            st.image(images[i], use_column_width=True)
            text_placeholder = st.empty()
            text = messages[i]
            display = ""
            for ch in text:
                display += ch
                text_placeholder.markdown(display)
                time.sleep(0.025)
            time.sleep(2)
        st.success("🎉 Happy Birthday Yashika 💖")
        st.balloons()
        st.markdown("### 💌 You are my home 💖")
elif name_check or password:
    st.error("❌ Access Denied")
