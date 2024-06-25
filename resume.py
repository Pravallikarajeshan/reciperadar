import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_about = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_oGlWy5.json")
lottie_education = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_hvwgi2fk.json")
lottie_skills = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_kyu4i2kk.json")
lottie_projects = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_rsggjc3o.json")
lottie_contact = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_nuwbvx2f.json")

# Function to load CSS style
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS file from local directory
local_css("abc.css")

def main():
    st.set_page_config(page_title="Resume-Professional Passport", page_icon=":briefcase:", layout="wide")
    
    st.title("Resume-Professional Passport")
    st.sidebar.title("Navigation Panel")
    page = st.sidebar.radio("Go to", ["About me", "Education", "Skills", "Projects", "Publishment", "Contact"])

    if page == "About me":
        st_lottie(lottie_about, height=300, key="about")
        st.header("About me")
        st.write("Hello! I'm Pravallika K.R, a dedicated professional eager to explore new opportunities in the field of AI engineering. With a fervent passion for innovation and problem-solving, I am driven by the prospect of contributing to cutting-edge projects that push the boundaries of technology. I thrive in collaborative environments, where my strong work ethic and commitment to excellence align seamlessly with team goals. Beyond my academic and professional pursuits, I find fulfillment in the melodic intricacies of Carnatic singing, a cherished hobby that adds depth and balance to my life. As I embark on this journey, I am excited to leverage my skills and expertise to make meaningful contributions in the dynamic landscape of artificial intelligence.")
    
    elif page == "Education":
        st_lottie(lottie_education, height=300, key="education")
        st.header("Education")
        st.subheader("BTech in Artificial Intelligence and Data Science")
        st.write("Reva University")
        st.write("- Currently pursuing my 6th semester")
        st.write("- Graduation Year: 2025")
        st.write("- Average CGPA of all 6 semesters: 9.08")
        st.subheader("12th STATE Board")
        st.write("Poorna Prajna College")
        st.write("Passed out year: 2021")
        st.write("Percentage: 93.33")
        st.subheader("10th CBSE Board")
        st.write("Narayana School")
        st.write("Passed out year: 2019")
        st.write("Percentage: 79.90")

    elif page == "Skills":
        st_lottie(lottie_skills, height=300, key="skills")
        st.header("Skills")
        st.subheader("Programming Languages")
        st.write("Python, Java, Data Structures and Algorithms (DSA) in Java, SQL (Structured Query Language)")
        st.subheader("Frameworks/Libraries")
        st.write("Numpy, Pandas, Data Visualization (PowerBI), Machine Learning (ML), Natural Language Processing (NLP), ML Ops (Machine Learning Operations), NNDL (Neural Networks and Deep Learning), Streamlit, General Artificial Intelligence (Gen AI)")
        st.subheader("Database Management Systems (DBMS)")
        st.write("SQL, NoSQL (MongoDB)")

    elif page == "Projects":
        st_lottie(lottie_projects, height=300, key="projects")
        st.header("Projects")
        st.subheader("NLPantry - Recipe Generator Application")
        st.write("Developed a web application using Streamlit and Gemini Pro API to generate recipes based on user input. Implemented image processing and NLP techniques to enhance functionality and accuracy.")
        st.subheader("Webpage on Equity Research Tool")
        st.write("Developed an end-to-end LLM project utilizing LangChain, OpenAI API, and Streamlit, creating a sophisticated news research tool for equity research analysts. Enhanced skills in NLP, API integration, and industry-focused project development, adding substantial value to the data science and NLP engineering portfolio.")
        st.subheader("Empowering Early Disease Assessment with Deep Learning in Retinopathy Detection")
        st.write("Led a team of four in developing an innovative deep learning solution for early disease assessment in retinopathy detection. Collaborated closely with a guide to implement cutting-edge techniques, leveraging deep learning algorithms to improve diagnostic accuracy and facilitate timely intervention.")
        st.subheader("Brew Bliss Coffee Shop Webpage")
        st.write("Developed a responsive and visually appealing webpage for a fictional coffee shop called Brew Bliss. The webpage includes a navigation bar, hero section, about section, menu gallery, and contact form.")

    elif page == "Publishment":
        st.header("Publishment")
        st.write("Paper Title: Retina Vigil: Deep Learning-Enabled Retinopathy Detection for Early Disease Assessment")
        st.write("Spearheaded a team of four members under guidance to publish the paper titled 'Retina Vigil: Deep Learning-Enabled Retinopathy Detection for Early Disease Assessment' at IEEE MysuruCon-2023, the esteemed 3rd Edition of Mysore Subsection Flagship International Conference. Contributed to groundbreaking research in leveraging deep learning for early disease assessment in retinopathy detection, showcasing expertise in collaborative research and academic publication.")   
    
    elif page == "Contact":
        st_lottie(lottie_contact, height=300, key="contact")
        st.header("Contact")
        st.write("- Email: pravallikarajesh773@example.com")
        st.write("- Phone: 9513896465")
        st.write("- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/pravallika-rajesh-a02a5628a)")

if __name__ == "__main__":
    main()

