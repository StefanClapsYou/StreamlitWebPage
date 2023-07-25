from PIL import Image
import requests
from streamlit_lottie import st_lottie
import streamlit as st
from typing_extensions import Literal

st.set_page_config(page_title="My webpage", page_icon=":fleur_de_lis:", layout="wide")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(r"C:\Users\libri\Desktop\Python\WebPage\Style\style.css")

lottie_coding = load_lottieur1("https://lottie.host/86fbe299-971f-400c-9b33-7e85b5704839/3j5iD2aVfd.json")
img_lottie_animation = Image.open("C:\\Users\\libri\\Desktop\\Python\\WebPage\\Images\\mqdefault_6s.png")
img_BedWars_Video = Image.open("C:\\Users\\libri\\Desktop\\Python\\WebPage\\Images\\BedWars2.png")

st.subheader("Hi, I am Stefan :wave:")
st.title("A student in a small country named Albania")
st.write("I am a student in progress in learning python with the goal of being a web designer")
st.write("I also produce some music! [Learn More >](https://soundcloud.com/stefan-cakoni)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Hello! So I don't really have a job YET. I am still learning how to use python for web designing!
            Here's some stuff I do in my free time: I play soccer/football, I play the guitar,
            and I study with Cisco Academy with Professor Ardi, learning python essentials, etc!

            If this sounds interesting to you, consider subscribing to my YouTube channel (Link below).
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/channel/UC-9pb_cMw6IKIdBHkeZyH1w)")

with right_column:
    st_lottie(lottie_coding, height=300, key='Coding')

with st.container():
    st.write("---")
    st.header("My videos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Watch me react to Dhar Mann!")
        st.write(
            """
            Watch me react to Dhar Mann's probably most cringe-worthy video so far.
            No hate to him, just the whole purpose of his channel is to change lives while that video does the complete opposite...
            Anyways, don't mind my voice, I was kinda sick :skull:
            """
        )
        st.markdown("[Watch Video >](https://www.youtube.com/watch?v=tMeL2g8Uupk&t=209s)")

    with image_column:
        st.image(img_BedWars_Video)
    with text_column:
        st.subheader("Watch me play bedwars on minecraft!")
        st.write(
            """
            Watch me play BedWars on a Minecraft server called Herobrine.org. The audio is kinda bad, but still, it's something...
            Anyways, watch that video and make me some backaroonies RN!!!!
            """
        )
        st.markdown("[Watch Video >](https://www.youtube.com/watch?v=mg4sD5rV9Qo&t=4s)")

with st.container():
    st.write("---")
    st.header("Get In touch with me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/libriim72@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()





    
