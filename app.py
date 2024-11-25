import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
#from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander

#test

# Set page title
st.set_page_config(page_title="Madhan Kumar N", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2024 Madhan Kumar N';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_utown = Image.open("images/about1.gif")
img_lh = Image.open("images/20230720_121643.jpg")
img_ifg = Image.open("images/aboutme.jpg")
#Assets for competitions
img_lite = Image.open("images/a.jpg")
img_lifehack2 = Image.open("images/c.jpg")
img_lifehack = Image.open("images/d.jpg")
img_he4d = Image.open("images/e.jpg")
img_ecc = Image.open("images/k.jpg")
img_shopee = Image.open("images/m.jpg")
img_sbcc = Image.open("images/sbcc.png")
img_runes = Image.open("images/runes.png")
# Assets for education
img_sji = Image.open("images/kkd.jpeg")
img_nus = Image.open("images/clg.jpg")
img_poc = Image.open("images/Karpagam.jpg")
img_gmss = Image.open("images/sslc.png")
img_sjij = Image.open("images/kkd.jpeg")
img_dsa = Image.open("images/pg.jpg")
# Assets for experiences

img_lit = Image.open("images/ad-media-logo.png")
img_scor = Image.open("images/teamads-logo.png")
img_iasg = Image.open("images/cropped-calibrelogo-4.jpg")
img_sshsph = Image.open("images/sshsph.jpg")
img_yll = Image.open("images/yll.jpg")
img_saf = Image.open("images/saf.jpg")
img_bitmetrix = Image.open("images/cropped-calibrelogo-4.jpg")
img_groundup = Image.open("images/ad-media-logo.png")
img_hedgedrip = Image.open("images/hedgedrip.jpg")
# Assets for projects
image_names_projects = ["ayu","bhavya","car", "dc", 
                         "diabetes", "eashwar", "gireesh", "gold", 
                         "ibt","map","loan", "pv", "sentiment", "sofware", "spactrs","student","heart","opencart","presta","mage"
                         ]
images_projects = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_projects]
# Assets for volunteering
image_names_vol = ["fullstack", "PHP", "JAVA", "csclogo", 
                         "nussulogo", "sklogo", "calibre infotech", "Team ads", 
                         "panads", "NUMPY", "machine", "datascience","power"]
images_vol = [Image.open(f"images/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_vol]
# Assets for blog
img_qb = Image.open("images/qb.jpg")
img_mayans = Image.open("images/mayans.jpg")
img_outlier = Image.open("images/outlier.png")
img_dac = Image.open("images/dac.png")
img_raffles = Image.open("images/raffles.jpg")
img_covid = Image.open("images/covid.jpg")
img_gender = Image.open("images/gender.jpg")
img_hci = Image.open("images/hci.jpg")
img_wordcloud = Image.open("images/wordcloud.jpg")
img_taste = Image.open("images/taste.jpg")
img_measles = Image.open("images/measles.jpeg")
img_dac1 = Image.open("images/dac1.png")
img_dac2 = Image.open("images/dac2.png")
# Assets for gallery

#img_lottie_animation = Image.open("images/lottie_animation.gif")
# Assets for contact
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_linkedin = Image.open("images/linkedin.png")
img_github = Image.open("images/github.png")
img_email = Image.open("images/email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "youtube": "https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png",
                "linkedin": "https://img.icons8.com/ios-filled/100/ff8c00/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
                "wordpress": "https://img.icons8.com/ios-filled/100/ff8c00/wordpress--v1.png",
                "email": "https://img.icons8.com/ios-filled/100/ff8c00/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

#def txt3(a, b):
  #col1, col2 = st.columns([1,2])
  #with col1:
    #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  #with col2:
    # Split the text at the comma and wrap each part in backticks separately
    #b_parts = b.split(',')
    #b_formatted = '`' + ''.join(b_parts) + '`'
    #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')   


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_lh, width=175)
        with r:
            st.empty()
    choose = option_menu(
                        "Madhan Kumar N", 
                        ["About Me","Experience", "Technical Skills", "Education", "Projects", "Competitions", "Certificate", "Blog", "Gallery", "Resume","Contact"],
                         icons=['person fill','clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'star fill', 'pencil square', 'image', 'paperclip','envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    youtube_url = "https://www.youtube.com/@madhankumar.n3381"
    linkedin_url = "https://www.linkedin.com/in/madhan0102"
    github_url = "https://github.com/Madhan0102"
    wordpress_url = "https://madhan1991.wordpress.com/"
    email_url = "connectmadhan01@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, Youtube=youtube_url, LinkedIn=linkedin_url, GitHub=github_url, Wordpress=wordpress_url, Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Madhan Kumar N")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Data Scientist | AI Developer | Machine Learning Enthusiast")
            st.write("👋🏻 Hi, I'm Madhan! have over 4 years of experience in web development, with a focus on PHP development, website management, SEO, and Google My Business (GMB). My career highlights include:")
            st.write("💼 Ad Media (July 2019 – Present): PHP Developer, Website Developer, SEO & GMB Specialist.")
            st.write("🏋🏻 Team Ads (Aug 2017 – March 2018): PHP Developer")
            st.write("👨🏼‍💻 Calibre Infotech (Feb 2016 – May 2017): PHP Developer & Website Developer")
            st.write("🔭 I’m currently working on AI Development and Machine Learning projects.")
            st.write("🌱 I'm learning more about Deep Learning and Data Engineering to expand my skill set.")
            st.write("👯 I’m open to collaborating on AI, Machine Learning, Data Science, and Full-stack development projects.")
            st.write("👨🏼‍💻 Currently, I am enhancing my skills in Data Science and Artificial Intelligence through training at QTree Technologies, preparing to leverage data-driven approaches for solving real-world problems.")
            st.write("💭 Ideal Career Prospects: Data Analyst, Data Scientist, Data Engineer, Business Intelligence Analyst, Product Manager")
            st.write("📫 How to reach me: [connectmadhan01@gmail.com]")
            st.write("👨‍💻 All of my projects are available at https://github.com/Madhan0102")
            st.write("📄 [Resume (1 page)](https://docs.google.com/document/d/0B0W0TfmuQjv7LUNEQV9MRENVVENiWmZZeVpKakt4VjNYMXpj/edit?resourcekey=0-ePV7xs6o32NsvMLrhdz3zw)")
            st.empty()
        with right_column:
            st.image(img_utown)
# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")

    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_groundup)
        with text_column:
            st.subheader("Technical Role (PHP Developer) [AD MEDIA](https://admediacbe.in/)")
            st.subheader("Ad Media – Coimbatore, India")
            st.write(" Jul 2019 - Jul 2022  ")
            st.markdown("""
            -  Developed and maintained over 20 dynamic websites for clients, focusing on SEO optimization and responsiveness.
            - My responsibilities span a wide range, from developing dynamic websites using PHP to optimizing web content for search engines to improve rankings and drive traffic
            - I also manage Google My Business (GMB) profiles, enhancing local business visibility.
            - This diverse experience has strengthened my technical skills and digital marketing expertise, allowing me to contribute to the company's online presence and growth effectively
            
            `PHP` `MYSQL` `HTML` `CSS` `JAVA SCRIPT` `SEO` `GMB` `WORDPRESS` `ECOMMECNCE` 
            """)
    
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_scor)
        with text_column:
            st.subheader("PHP Developer & E-commerce Website Developer, [TEAM ADS](https://teamads.com/)")
            st.write("*Team Ads — August 2017 - March 2018* | [*Testimonial*](https://drive.google.com/file/d/17-VLkbPDOR6LzkJx7oW7sMkx21hEJmbW/view?usp=drive_link)")
            st.markdown("""
            - At Team Ads, from August 2017 to March 2018, I worked as a PHP developer and e-commerce website developer. My role involved designing and developing dynamic, user-friendly websites with PHP, enhancing site functionality, and ensuring smooth integration with databases
            - I also collaborated with clients to meet their specific business needs, focusing on delivering responsive and optimized e-commerce platforms.
            - Debugged and resolved issues to ensure seamless user experience across different browsers and devices.
                        
            `PHP, HTML, CSS, JavaScript` `MySQL, Database Integration` `E-commerce Platforms (e.g., Magento, opencart,prestashop.)` `Responsive Design & Web Optimization`, `Client Collaboration & Requirement Analysis`.
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_bitmetrix)
        with text_column:
            st.subheader("PHP Developer and Website Developer, [Calibre Infotech](https://calibreinfotech.in/)")
            st.write("*Calibre Infotech — August 2017 - March 2018* | [*Testimonial*](https://drive.google.com/file/d/17-VLkbPDOR6LzkJx7oW7sMkx21hEJmbW/view?usp=drive_link)")
            st.markdown("""
            - I worked as a PHP Developer and Website Developer at Calibre Infotech from February 2016 to May 2017
            - My responsibilities included designing and developing dynamic websites using PHP, ensuring smooth functionality, integrating databases, and collaborating with clients to create responsive, user-friendly websites tailored to their needs.

            `PHP` `MYSQL` `HTML` `CSS` `JAVA SCRIPT`
            """)

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages","`C`, `Python`, `SQL`, `Java`, `C++`, `PHP`")
    txt3("Academic Interests","`Data Visualization`, `Data science`, `Recommendation Systems`, `Natural Language Processing`")
    txt3("Data Visualization", "`ggplot2`, `matplotlib`, `seaborn`, `Plotly`, `Librosa`, `Folium`, `Gephi`, `GIS`, `Tableau`, `Power BI`, `Google Data Studio`, `Domo`, `Google Analytics`")
    txt3("Database Systems", "`MySQL`, `PostgreSQL`, `SQLite`, `NoSQL`, `Google BigQuery`, `Cloud Firestore`, `InfluxDB`, `ScyllaDB`")
    txt3("Cloud Platforms", "`Google Cloud Platform`, `Amazon Web Services`, `Heroku`, `Streamlit Cloud`, `Render`, `Hugging Face`, `Minio`")
    txt3("Natural Language Processing", "`NLTK`, `Word2Vec`, `TF-IDF`, `TextStat`")
    txt3("Version Control", "`Git`, `Docker`, `Azure`")
    txt3("Design and Front-end Development", "`Canva`, `Figma`, `HTML`, `CSS`, `Streamlit`, `Wordpress`, `Java Script`")
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `Association Rules Mining`, `Random Forest`, `Decison Trees`, `Principal Components Analysis`, `Text Classification`, `Sentiment Analysis`, `Matrix Factorisation`, `Collaborative Filtering`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`, `JAX`")
    txt3("Task Management Tools", "`Asana`, `Notion`, `ClickUp`, `Slack`, `Jira`, `Confluence`, `Miro`, `Mural`")
    txt3("Miscellaneous", "`Google Firebase`, `Microsoft Office`, `Retool`, `Google Ads`")

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    selected_options = ["Summary", "Modules"
                        ]
    selected = st.selectbox("Which section would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Summary":
        st.subheader("Summary")
        st.write("*Summary of education from primary school till university*")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_nus)
            with text_column:
                st.subheader("Master of Computer Applications (MCA) - [Karpagam College of Engineering,Coimbatore](https://kce.ac.in/) (2012-2015)")
                st.write("I hold a Master of Computer Applications (MCA) degree, which I completed in 2015 from Karpagam College of Engineering, Coimbatore, with an impressive 84.4% score. This program enhanced my skills in software development, database management, and system analysis, equipping me with a strong foundation in computer science concepts and practical applications. The rigorous curriculum, combined with hands-on projects, enabled me to master various programming languages, algorithms, and software engineering techniques. This qualification has significantly contributed to my professional growth and technical expertise in the IT industry.")
                
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_poc)
            with text_column:
                st.subheader("Bachelor of Science -(BSc) in Computer Science , [Karpagam University, Coimbatore](https://kahedu.edu.in/) (2009-2012)")
                st.write("I completed my Bachelor of Science (BSc) in Computer Science from Karpagam University, Coimbatore, in 2012, securing a commendable 74.5%. This academic journey provided me with a strong foundation in programming, algorithms, data structures, and system design. I gained practical experience through various projects and coursework, which helped me develop problem-solving skills and critical thinking. The program equipped me with essential knowledge of computer systems, software development, and emerging technologies, preparing me for real-world challenges in the IT industry and laying the groundwork for further studies in the field")
               
    
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_sji)
            with text_column:
                st.subheader("Higher Secondary Certificate (HSC)- [Government Higher Secondary School, Kinathukadavu](https://schools.org.in/) (2009)")
                st.write("Coursework: Tamil, English, Mathematics, Additional Mathematics, Physics, Chemistry,botany, zoology.")
                st.write("The user completed their Higher Secondary Certificate (HSC) at Government Higher Secondary School, Kinathukadavu, in 2009, achieving a percentage of 63%.")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_gmss)
            with text_column:
                st.subheader("Secondary School Leaving Certificate (SSLC) - [Government High School, Muthugoundanur)](https://schools.org.in/) (2007)")
                st.write("Coursework: English, Mathematics, Science, Tamil, Geography, Economics")
                st.write("")
    elif selected == "Modules":
        st.subheader("Modules")
        
        with st.container():
            left, mid, right = st.columns((0.1,1,0.1))
            with left:
                st.empty()
            with mid:
                st.write("**Graduation Requirements**")
                st.image(img_dsa)
            with right:
                st.empty()
    #elif selected == "Module Reviews":
        #st.subheader("Module Reviews")
        #st.write("*Reviews for selected modules taken in university*")

elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Car Price Prediction App")
            st.write("*The goal of this project is to predict the price of a car using a machine learning algorithm.*")
            st.markdown("""
            - The Car Price Prediction project is a practical example of how machine learning can be applied to real-world business problems. By using historical car data, the project can offer valuable insights for car buyers and sellers, making the process of pricing cars more efficient and accurate.
            -  Used algorithms like Linear Regression, Random Forest, and XGBoost for model training. The project also includes an interactive Streamlit web application for users to input car details and get real-time price predictions. This project demonstrates expertise in data analysis, machine learning model deployment, and user-friendly web application design.
            """)
            st.write("Machine Learning · Data Analytics · Data Science · Data Visualization")
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            mention(label="Github Repo", icon="github", url="https://github.com/Madhan0102/carprice_predictions")
            mention(label="Streamlit App", icon="streamlit", url="https://carpricepredictions-xkiumszqywxhrznnwd6nrt.streamlit.app/",)          
        with image_column:
            st.image(images_projects[2])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Software developer salary prediction")
            st.write("*Developed a machine learning model to predict the salaries of software developers based on multiple factors such as years of experience, skills, education level, location, and company size*")
            st.markdown("""
            - Gathered and cleaned a dataset of salary information from multiple sources, ensuring data quality by handling missing values, outliers, and normalizing categorical data.
            - Created and selected relevant features, including technical skills, job titles, years of experience, and geographic location to improve prediction accuracy.
            - Built predictive models using various machine learning algorithms, including Linear Regression, Decision Trees, and Random Forest. Evaluated model performance using metrics like RMSE, MAE, and R² scores to ensure accuracy

             Python, Pandas, NumPy, Scikit-learn, Matplotlib, streamlit, Jupyter Notebook.

            -Outcome: Achieved a prediction accuracy of 85%, with the model successfully providing salary estimates based on a developer's background and market trends.
            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            mention(label="Streamlit App", icon="streamlit", url="https://salary-prediction-khfbsdsbitz8qvrb2kftvq.streamlit.app/",)
            mention(label="Github Repo", icon="github", url="https://github.com/Madhan0102/salary-prediction",)
        with image_column:
            st.image(images_projects[13])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Amazon Echo Review Sentiment Analysis")
            st.write("*The Amazon Echo Review Sentiment Analysis project aims to analyze customer reviews to determine their sentiment (positive, negative, or neutral). By utilizing natural language processing (NLP) techniques and machine learning models, this project helps identify customer opinions, enhancing user experience and aiding in product improvement strategies.*")
            st.markdown("""
            -  Implemented machine learning algorithms (e.g., Naive Bayes, Random Forest) and Natural Language Processing (NLP) techniques to classify reviews as positive, negative, or neutral.
            - Assessed model performance using metrics like accuracy, precision, recall, and F1-score, ensuring reliable sentiment classification.
            - Created visual representations of the analysis results using libraries such as Matplotlib and Seaborn to present insights clearly and effectively.
            - Generated detailed reports summarizing findings and actionable insights, assisting stakeholders in understanding customer sentiments towards Amazon Echo products.

            - Python, Pandas, NLTK, Scikit-learn, Matplotlib, Seaborn


            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            mention(label="Github Repo", icon="github", url="https://github.com/Madhan0102/sentiment_analysis",)
            mention(label="Streamlit App", icon="streamlit", url="https://sentimentanalysis-8nm7cxks2ppkjcapp2emzpq.streamlit.app/",)
        with image_column:
            st.image(images_projects[12])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Gold Price Prediction")
            st.write("*Gold Price Prediction using Machine Learning*")
            st.markdown("""
            - Developed a predictive model to forecast gold prices utilizing machine learning algorithms, analyzing historical data and market trends.
            - Collected and preprocessed data from multiple sources, ensuring accuracy and relevance for modeling.
            - Employed various algorithms, including linear regression, decision trees, and neural networks, to evaluate their performance in predicting gold price fluctuations.
            - Implemented feature engineering techniques to enhance model accuracy and reliability.
            - Evaluated model performance using metrics such as RMSE and R-squared, optimizing for the best predictive outcomes.
            - Visualized results through informative charts and graphs, enabling stakeholders to comprehend trends and insights effectively.
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/sp1541-nlp)")
            mention(label="Streamlit App", icon="streamlit", url="https://goldpricepredictions-99ykhqejr5srm4kejknv7i.streamlit.app/",)
            mention(label="Github Repo", icon="github", url="https://github.com/Madhan0102/gold_price_predictions",)
        with image_column:
            st.image(images_projects[7])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Loan Approval Prediction Project")
            st.write("*Developed a machine learning model to predict loan approval status based on various applicant features. The project involved data preprocessing, exploratory data analysis, and model training using algorithms such as logistic regression and decision trees. Key tasks included:*")
            #st.write("Methods performed on [Kaggle dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings):")
            st.markdown("""
            -  Analyzed applicant data, including demographics, income, credit history, and loan characteristics, to identify patterns and insights.
            -  Created and selected relevant features to enhance model accuracy.
            - Implemented and tested various algorithms to determine the most effective model for predicting loan approval
            - Designed a user-friendly Streamlit application to input applicant data and display predictions.
            - Achieved a prediction accuracy of [insert accuracy percentage] and provided actionable insights for improving the loan approval process.
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/st4248-termpaper) | [Term Paper](https://github.com/harrychangjr/st4248-termpaper/blob/main/ST4248%20Term%20Paper%20(A0201825N)%20v5.pdf)")
            mention(label="Github Repo", icon="github", url="https://github.com/Madhan0102/Loan_predictions",)
            mention(label="Streamlit App", icon="streamlit", url="https://loanpredictions-am89dzggkybvrrin4cvq8r.streamlit.app/",)
        with image_column:
            st.image(images_projects[10])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Diabetes Prediction")
            st.write("*Developed a web application for predicting diabetes using machine learning algorithms and Streamlit. The application allows users to input relevant health parameters and receive predictions based on trained models:*")
            st.markdown("""
            - Technologies Used : Python, Streamlit, scikit-learn, pandas, NumPy, Matplotlib
            - User-friendly interface for data input and output visualization.
            - Utilized machine learning models for accurate diabetes prediction.
            - Implemented data preprocessing techniques for model training. 
            - Visualized predictions and model performance metrics using charts and graphs.
            - Successfully demonstrated the potential of machine learning in healthcare applications, facilitating early diagnosis and preventive measures.
            """)
            #st.write("[Final Report](https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing) | [Pitch Deck](https://www.canva.com/design/DAFeSnJeqgM/uXpz0kw8e7If4T1PG2tpaQ/view?utm_content=DAFeSnJeqgM&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Product Demo](https://www.youtube.com/watch?v=XMlt-kfdC7g)")
            mention(label="Github Repo", icon="github", url="https://github.com/Madhan0102/diabetics_predictions",)
            mention(label="Streamlit App", icon="streamlit", url="https://diabeticspredictions-iqzv6arqxsxcvrckrdjuwm.streamlit.app/",)
        with image_column:
            st.image(images_projects[4])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Heart Attack Predictions Project")
            st.write("*Developed a machine learning model to predict the likelihood of heart attacks based on various health parameters, aiming to assist healthcare professionals in early diagnosis and preventive care.*")
            st.markdown("""
            - Utilized Python and relevant libraries (e.g., scikit-learn, pandas, NumPy) for data preprocessing, feature selection, and model training.
            - Employed various classification algorithms (e.g., logistic regression, decision trees, random forests) to determine the best predictive model.
            - Conducted hyperparameter tuning and cross-validation to optimize model performance.
            - Outcome: Achieved a high accuracy rate in predictions, enabling better risk assessment for heart attack patients. The model can be integrated into healthcare systems for real-time predictions, enhancing decision-making in patient care.
            """)
            #st.write("[Github Repo](https://github.com/harrychangjr/biopics) | [RPubs](https://rpubs.com/harrychangjr/biopics)")
            mention(label="Github Repo", icon="github", url="https://github.com/Madhan0102/Heart_Attack_Analysis_Prediction",)
        with image_column:
            st.image(images_projects[16])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("DC Law Firms Project")
            st.write("*Developed and maintained a comprehensive legal services website for DC Law Firms, aimed at providing a user-friendly platform to showcase various legal services, case studies, and expertise in multiple practice areas. The project involved creating a dynamic and responsive website that facilitated seamless client interaction, appointment bookings, and legal consultations.*")
            st.markdown("""
            - Designed and implemented the front-end interface using HTML, CSS, JavaScript, ensuring an intuitive and visually appealing user experience.
            -Integrated contact forms and appointment scheduling systems, automating client queries and consultation requests
            - Applied SEO techniques to improve the site’s visibility on search engines and attract potential clients.
            - Collaborated closely with the legal team to ensure content accuracy and compliance with legal standards.
            - Front-end: HTML, CSS, JavaScript
            - Back-end: PHP, MySQL
            - Tools: Adobe Photoshop, WordPress (if applicable)
            -SEO: Google Analytics, Keyword Optimization

            """)
        mention(label="Final Report", icon="📄", url="https://www.dclawfirms.in/",)
        with image_column:
            st.image(images_projects[3])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Gireesh Heat Exchangers Project")
            st.write("*WordPress Developer & SEO Specialist – Gireesh Heat Exchangers Project*")
            st.markdown("""
            - Designed and developed a dynamic website for the "Gireesh Heat Exchangers" project using WordPress, ensuring a responsive and user-friendly interface.
            - Customized themes and integrated plugins to enhance the functionality of the website, aligning with the specific needs of the heat exchanger industry.
            - Focused on SEO optimization to improve the website's visibility on search engines, conducting keyword research, optimizing content, and implementing on-page SEO strategies
            - Utilized SEO tools to monitor performance, ensuring the website ranks for relevant industry keywords and drives organic traffic
            - Tools: Adobe Photoshop, WordPress (if applicable)
            - SEO: Google Analytics, Keyword Optimization
            """)
        mention(label="Final Report", icon="📄", url="https://www.gireeshheatexchangers.com/",)
        with image_column:
            st.image(images_projects[6])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("BT Institute Private Limited")
            st.write("*ERP admin panel to maintain student details*")
            st.markdown("""
            - Validating files uploading and clean the user inputs from forms before storing it into database to prevent sql injection
            - Delivered responsive, mobile-friendly web applications to ensure accessibility on multiple devices.
            - Front-end: HTML, CSS, JavaScript
            - Back-end: PHP, MySQL
            """)
        mention(label="Final Report", icon="📄", url="https://www.ibtindia.com/",)
        with image_column:
            st.image(images_projects[8])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("PV Engineers & Developers project")
            st.write("*For the PV Engineers & Developers project, as an SEO Developer, you optimized their website for search engines by conducting keyword research, improving on-page SEO elements like meta tags, titles, and descriptions, and enhancing site performance*")
            st.markdown("""
            - SEO Developer 
            - Conducted keyword research, implemented on-page and off-page SEO strategies.
            - Analyzed website performance using SEO tools like Google Analytics and Search Console.
            - Collaborated with the content and development teams to ensure SEO best practices across web platforms
            """)
        mention(label="Final Report", icon="📄", url="https://www.pvengineersdevelopers.in/",)
        with image_column:
            st.image(images_projects[11])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Spectra Plast Project")
            st.write("*www.spectraplast.in focused on PHP development and SEO development*")
            st.markdown("""
            - PHP Development: Designed, developed, and maintained dynamic, user-friendly website features using PHP, ensuring smooth integration with databases and delivering optimized web pages for improved user experience.
            - SEO Optimization: Conducted comprehensive SEO audits, identifying opportunities for on-page and off-page SEO improvements. Optimized meta tags, headers, keywords, and website content to increase organic traffic and search engine rankings.
            - Performance Optimization: Enhanced website speed and performance by optimizing code, implementing caching strategies, and conducting regular website maintenance.
            - Collaborative Development: Worked closely with design and content teams to align the website with business goals, improving user engagement and driving conversions.
            """)
        mention(label="Final Report", icon="📄", url="https://www.spectraplast.in/",)
        with image_column:
            st.image(images_projects[14])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Bhavya Packers And Movers")
            st.write("*WordPress and SEO Developer*")
            st.markdown("""
            - Developed and maintained WordPress websites, enhancing user experience and functionality.
            - mplemented SEO strategies, improving organic search rankings and site visibility.
            - Collaborated with cross-functional teams to optimize content and increase web traffic.
            """)
        mention(label="Final Report", icon="📄", url="https://www.bhavyapackersandmovers.in/",)
        with image_column:
            st.image(images_projects[1])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("A K Ayurvedic Clinic Project")
            st.write("*Developed an SEO strategy for A K Ayurvedic Clinic, optimizing website content, enhancing local search visibility, and improving user engagement to attract more patients and increase online appointments*")
            st.markdown("""
            - SEO Development for A K Ayurvedic Clinic
            - The objective of this project is to enhance the online visibility and search engine ranking of A K Ayurvedic Clinic through comprehensive SEO strategies. By optimizing the clinic’s website and online presence, we aim to attract more local customers seeking Ayurvedic treatments, thereby increasing foot traffic and appointment bookings
            -  On-Page Optimization: Optimize website content, including meta titles, descriptions, headings, and images, to improve search engine friendliness and user experience.
            """)
        mention(label="Final Report", icon="📄", url="https://www.akayurvediclinic.com/",)
        with image_column:
            st.image(images_projects[0])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Eshwar College of Engineering")
            st.write("*SEO development work at Eshwar College of Engineering:*")
            st.markdown("""
            - developed and implemented SEO strategies to enhance website visibility and traffic.
            - Conducted keyword research, on-page optimization, and content strategy planning.
            - Analyzed website performance using analytics tools to drive continuous improvement.
            """)
            mention(label="Final Report", icon="📄", url="https://sece.ac.in/",)
        with image_column:
            st.image(images_projects[5])

    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Ecommerce Modules")
            st.write("*E-commerce Platform Development (OpenCart, PrestaShop, Magento) | Developer*")
            st.subheader("Open Cart")
            st.markdown("""
            - Website Customization: Integrated and customized theme and developed extensions to add extra features to the site such as refer a friend, news ticker in header, customized cart pages and shipping functionalities.
                                     Customize your opencart , remove checkout procedure , pricing , remove add to cart and add form for product 

            - Conducted keyword research, on-page optimization, and content strategy planning.
            - Analyzed website performance using analytics tools to drive continuous improvement.
            """)
            with image_column:
               st.image(images_projects[17])
            st.subheader("PrestaShop")
            st.write("*Modules And Description*")
            st.markdown("""
            - Contact Us:  Contact us form with captcha to prevent spam and displayed those details in admin panel with edit option
            - Chain Products:  Configure chain products and redirect through chain products in front end, once the main product is added to cart. Chain may have hidden products and customer cant able to buy or view without adding the main product in cart.
            - Product words:   Product name customization - Character count, price for each word, disallowed characters can be configured by admin. Based on every character product price varies dynamically.
            - Book Price   :   Dynamically calculate product price by using custom attributes such as number of pages, book cover, size, etc defined by admin
            - Custom Category : Configure slider option for category page and option to manage category page layout design (1 product/row or 3 products/row)
            - Customer Testimonials: Display customer testimonials at a separate page and in side bar of each page. Admin can manage (edit,delete,enable,disable) the testimonial before displayed in page.
            """)
            with image_column:
               st.image(images_projects[18])
            st.subheader("Magento")
            st.write("*Modules And Description*")
            st.markdown("""
            -  Website Customization: Integrated and customized theme and developed extensions to add extra features to the site such as refer a friend, news ticker in header, customized cart pages and shipping functionalities
            """)
            with image_column:
               st.image(images_projects[19])
            
elif choose == "Competitions":
    # Create section for Competitions
    #st.write("---")
    st.header("Competitions")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lite)
            #st.empty()
        with text_column:
            st.subheader("Rural Sports Competition (Pongal)")
            st.write("Participant in the Cricket Match")
            st.markdown("""
                    - Secured [First/Second/Third] Place
                    - Issued by the Tamil Nadu Government
            """)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_lifehack2)
            #st.empty()
        with text_column:
            st.subheader("One Day Workshop on .Net Framework")
            st.write(" certificate is for Prof/Dr/Mr/Ms N. MADHAN KUMAR, ITI MCA, of KARPAGAM COLLEGE OF ENGINEERING, COIMBATORE. It certifies their participation in a One Day Workshop on .Net Framework held on 14th March 2015. The workshop was organized by the Department of Master of Computer Applications")
            st.write("Built  and integrated PassionPassport with ChatGPT - a Streamlit-based web application that recommends travel locations based on one’s hobbies.")
            
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_ecc)
        with text_column:
            st.subheader("Annual Sports Meet 2008-2009")
            st.write("Government Higher Secondary School, Kinathukadavu")
       
            
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(img_shopee)
        with text_column:
            st.subheader("epublic Day & Bharathiar Day Zonal Sports & Tournaments (2006-2007)")
            st.write("Pollachi Educational District Secondary, Matric, and Higher Secondary Schools Athletic Association")
            st.write("Represented Government Higher Secondary School, Muthugoundanur in the Senior Category for Pollachi West Zone.")
        
    
elif choose =="Certificate":
    st.header("Certificate")
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Power BI Essentials Course ")
            st.write("*September 23rd to November 18, 2024 *")
            st.markdown("""
               Successfully completed the Power BI Essentials Course from Variablz Academy, Cuddalore, on November 18, 2024. The program enhanced my proficiency in creating data-driven dashboards, data modeling, and interactive visualizations. The certification, signed by the Chief Executive Officer, reflects my commitment to continuous learning and advancing my data analysis skills..
             - "Power BI: Certified by Variablz Academy (November 2024)."

            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[12])
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Artificial Intelligence & Data Science")
            st.write("*September 23rd to September 25th, 2024*")
            st.markdown("""
               Successfully completed a 3-Day Intensive Workshop in Artificial Intelligence & Data Science, conducted by NoviTech R&D Private Limited from September 23rd to September 25th, 2024.
             - "Acquired knowledge in key Artificial Intelligence and Data Science techniques, including data preprocessing, machine learning algorithms, and practical applications using tools like Python, TensorFlow, and scikit-learn during a 3-Day Intensive Workshop conducted by NoviTech R&D Private Limited."

            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[11])
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Stepwise Construction of a Machine Learning Models")
            st.write("*October 13th, 2024*")
            st.markdown("""
              
              - Gained proficiency in building and training machine learning models using Python and TensorFlow
              - successfully implemented a classification model with 92% accuracy on the MNIST dataset.
              - Mention the issuing organization: "NoviTech R&D Private Limited".
              - Understanding machine learning concepts
            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[10])
        with st.container():
          text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Python Pandas Basics Course")
            st.write("*July 2024 to October 20, 2024*")
            st.markdown("""
            - I have completed the 'Pandas Basic Course' from Simplilearn during the period of July 2024 to October 20, 2024.
            - It highlights his initiative and commitment to career advancement
            - he Python Pandas Basics Course covers the fundamental concepts and applications of the Pandas library, a powerful data manipulation tool in Python.

            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[8])    

    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Introduction to NumPy")
            st.write("*July 2024 to October 14, 2024*")
            st.markdown("""
            - Completed a comprehensive course on NumPy, focusing on array manipulation, mathematical operations, and data analysis techniques using Python
            - Data Analysis: Leveraging NumPy for efficient data analysis and manipulation.
            - Understanding how NumPy improves performance for numerical computations compared to traditional Python lists.
            - Basic linear algebra operations, including dot products and matrix multiplication.
            
            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[9])
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader(" Full-Stack Development")
            st.write("*NoviTech R&D Pvt. Ltd. – June 2024 to July 2024*")
            st.markdown("""
            - Successfully completed a one-month internship focused on full-stack development, building scalable web applications using Django and Flask.
            - Developed and maintained databases, ensuring smooth integration between front-end and back-end functionalities.
            - Collaborated with cross-functional teams to implement user-centric features.
            - Building fully functional web applications like e-commerce websites, blogs, social media platforms, or portfolio sites.
            - Implementing user registration, authentication, and CRUD (Create, Read, Update, Delete) functionality.
            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[0])
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("PHP Programming Certificate")
            st.write("*October 2015 to January 2016*")
            st.markdown("""
            - The PHP Programming Certificate, issued by Texasas Techno Park, recognizes the successful completion of a training program from October 2015 to January 2016
            - During this course, the user gained expertise in PHP programming, learning to develop dynamic websites, handle databases, and build server-side applications. The training covered PHP fundamentals, database integration, and web development best practices, enhancing the user's skills in creating robust, interactive web applications.
            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[1])
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Core Java Training Program")
            st.write("*September 17, 2015 – October 30, 2015*")
            st.markdown("""
              Institution: Mazenet, Coimbatore, Tamil Nadu, India
            - Description: Completed a training program in Core Java, focusing on fundamental concepts, object-oriented programming, and practical applications.

            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[2])
       
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("PHP Developer, E-commerce Website Developer")
            st.write("*Team Ads August 2017 - March 2018*")
            st.markdown("""
            - Responsibilities: Designing and developing e-commerce websites with PHP, focusing on user experience and functionality.
        
            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[7])
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("PHP Developer & Website Developer")
            st.write("*Calibre Infotech February 2016 - May 2017*")
            st.markdown("""
            - Developed and maintained dynamic websites using PHP
            - Collaborated with clients to gather requirements and deliver tailored web solutions.
            - Enhanced website functionality and user experience through effective coding practices.
            - Integrated databases to ensure smooth operation and data management on websites.
            - Worked on optimizing website performance and implementing SEO best practices.
            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[6])
    
elif choose == "Blog":
    st.header("Blog")
    selected_options = ["Overview",
    #"“It’s not pink, it’s salmon” – Why I returned to my previous start-up for FREE",  
                        "Does gender inequality still have a place in Singapore's society today?", 
                        "Reflections on Organising an 850-participant Data Analytics Competition (Extracted Using Google Sites REST API)",
                        "Reflections on Organising an 850-participant Data Analytics Competition (Formatted Version)",
                        "Worsened health disparities based on ethnicity and gender due to COVID-19",
                        "Obstacles in promoting healthy eating habits",
                        "Role of healthcare data analytics in managing COVID-19",
                        "Evaluating 'Chinese Privilege' in Singapore: Special Assisted Plan Schools",
                        "Analysing usefulness of word clouds in mental health studies",
                        "Investigating the relationship between culture and sweet-sour taste interactions",
                        "Timing vaccination campaign to reduce measles infections"
                        ]
    selected = st.selectbox("Which section or write-up would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Overview":
        st.subheader("Overview")
        st.markdown("""
        I must admit - I hated reading books as a kid, and in turn, I disliked writing essays or expressing my thoughts as well. However, throughout my time in university, I have gradually picked up the essence of writing, to the extent of making use of it as a destressor from my technical modules.

        Although my writing skills were novice at best when I was a freshman, I eventually got better at it (in my opinion), even to the extent of writing content articles as a regular hobby! It is indeed an asset to pick up as many skills as possible when still young, as you never know when you may need to utilise a particular skill whenever necessary.

        In this section, you will be able to read some of my finest write-ups from my university experiences, based on topics varying from science to politics. For those looking forward to a good read, enjoy!
        """)
   
    elif selected == "Does gender inequality still have a place in Singapore's society today?":
        st.subheader("Does gender inequality still have a place in Singapore's society today?")
        st.write("April 2, 2022 | [Term Paper]()")
        st.markdown("""
        On April 24, 2021, a new resolution was passed for women in the Singapore
        Recreation Club (SRC) to be entitled with the same rights and privileges as male
        members. With this new resolution, women now have voting rights, and can be elected
        to the club’s management committee. On top of this, they may assume the membership
        of either their spouse or their male next-of-kin. This news was announced after several
        failed attempts to amend the club’s constitution over the course of its 137 year history
        since its founding.

        This made me wonder: as one of Singapore’s most well-established clubs, what
        took it so long to amend this constitution and allow for female members to have equal
        rights? Furthermore, to what extent was gender inequality prevalent over the course of
        Singapore’s history? Therefore, this term paper intends to explore the history of gender
        inequality in Singapore, and whether it still has a place in our society today.
        For starters, we first need to understand the history of SRC. Originating as a
        crickets’ club for Eurasian players in 1883, the club gradually expanded to allow for more
        sports including football and hockey to be played, with various matches held against
        fellow clubs such as the Penang and Malacca Recreation Clubs. However, SRC
        membership was initially restricted to Eurasian males, with memberships only being made
        open to non-Europeans from 1955 onwards. Furthermore, European females were only
        formally allowed as guests in 1927, before subscription memberships were open to
        women of all races by 1956 as well, about one year after memberships were open to non-
        Eurasian men. With drinking as a main social activity and occasional tea parties as SRC’s
        non-sport social activities, it was no surprise that the club had only catered to men, which
        reinforced the stereotype against women as stay-at-home caregivers who did not enjoy
        such activities, especially before World War II.

        From a more macro perspective, the above-mentioned restriction of women’s
        enjoyment of such activities was also representative of the attitude towards women in
        colonial Singapore. With Singapore under British rule, women were “subjected to sociocultural
        and religious pressures to conform to the roles of wife and mother and to lead a
        more secluded life”. This had contrasted with men, whose gender was viewed to be more
        dominant based on the traditions of different cultures in Singapore. In addition, men were
        allowed to have multiple female partners, solidifying the perspective that women were
        inferior to men at that point of time.

        From the 1950s however, there was an increase in female leaders emerging in
        Singapore’s politics, leading the charge to pursue gender equality in the country. For
        instance, the establishment of the Women’s Charter by the Singapore government in
        1961 had aimed to provide equal rights to both genders. Clauses in the Charter include
        the compulsory registration of all marriages as well as providing women with the rights to
        their own housing, marriage and children if applicable. This was a big improvement from
        the Chinese Protectorate that was established during the colonial era, which mainly
        targeted at tackling the illegal prostitution of women. This showed that the local
        government did try to push for women to be treated as equals to men, instead of merely
        taking care of their basic human needs.

        In terms of job opportunities, more Singaporean women are seeking full-time
        employment by either pursuing higher education or entering the workforce, especially
        over the recent years. This breaks the traditional norm of women as stay-at-home
        caregivers, as more women aim to live independently as well. This is evident in the rise
        of the female labour force participation rate from 60.8% in 2018 to 61.2% in 2020.
        Furthermore, the increase in Professionals, Managers, Executives and Technicians from
        50% in 2010 to 59% in 2020 amongst female employees shows that women, just like
        men, are capable of upskilling themselves and contributing meaningfully to the Singapore
        economy when given the opportunity. While a pay gap still exists between employed
        males and females in Singapore, the inclusion of more women especially in higher
        positions within the local workforce has helped to decrease this gender pay gap, paving
        the way towards gender equality based on the employment aspect.

        To answer the question that I posed earlier: I believe that gender inequality should
        not have a place in Singapore’s society today. While there is still more that can be done
        to ensure equal opportunities for both men and women in the long run, we have to
        recognise that the local government today is indeed trying to advocate for women’s rights
        in Singapore. Its efforts in setting up the Women’s Charter and encouraging more women
        to take up higher positions in the workforce, for example, have likewise spurred similar
        initiatives amongst external organisations. This includes the founding of organisations
        such as AWARE for women to seek assistance against physical and emotional abuse, as
        well as the recent news of allowing women to take up management committee positions
        as well as have voting rights in SRC.

        As mentioned by Law and Home Affairs Minister Shanmugam in February 2021,
        perhaps one way to promote gender equality more in Singapore is for employees of both
        genders to be entitled to equal parental leave, as observed in certain European countries.
        This would grant men the opportunity to experience the caregiver role as normally
        experienced by their spouses. In fact, encouraging such role reversals between both
        genders would allow mutual understanding of each other’s roles, strengthening internal
        familial ties in the process.

        Alternatively, gender equality can be introduced in one’s education at a young age,
        such that this would be well ingrained in our future generations, gradually discouraging
        the idea of gender discrimination over time. Hopefully, these current initiatives and
        suggestions would allow women to realise their full potential and ensure that they are not
        seen as inferior compared to men. Furthermore, by having more diverse perspectives
        from both genders, this would allow for improved and balanced decisions to be made, in
        order to boost productivity in the workforce.

        References:

        1. Low, Y. (2021, April 24). After 137 years, Singapore Recreation Club votes to grant
        female members same rights and privileges as males. TODAY. Retrieved
        February 22, 2022, from https://www.todayonline.com/singapore/singaporerecreation-
        club-passes-resolution-allow-female-members-enjoy-same-rights-and

        2. Infopedia, National Library Board. (n.d.). Singapore Recreation Club. Retrieved
        February 23, 2022, from
        https://eresources.nlb.gov.sg/infopedia/articles/SIP_1041_2010-05-07.html

        3. Koh, T. (2019, February 18). Women's Quest for Justice and equality - A short
        history. The Straits Times. Retrieved February 24, 2022, from
        https://www.straitstimes.com/opinion/by-invitation-womens-quest-for-justice-andequality-
        a-short-history

        4. Ministry of Manpower, Singapore. (2021, October 12). Article: A gender-inclusive
        workforce. Retrieved February 24, 2022, from https://stats.mom.gov.sg/Pages/agender-
        inclusive-workforce.aspx

        5. Yuen-C, T. (2021, June 3). Men wanted: All need to play a part in pushing for
        gender equality, says Shanmugam. The Straits Times. Retrieved April 2, 2022,
        from https://www.straitstimes.com/singapore/politics/men-wanted-all-need-toplay-
        a-part-in-pushing-for-gender-equality-says-shanmugam
        """)
    
    elif selected == "Reflections on Organising an 850-participant Data Analytics Competition (Formatted Version)":
        st.subheader("Reflections on Organising an 850-participant Data Analytics Competition (Formatted Version)")
        st.write("February 18, 2022 | [Article](https://sites.google.com/view/nussds/articles/reflections-about-dac?authuser=0&pli=1)")
        st.write("*The content of this article was manually copied and pasted from the original site, along with manually embeedded media and captions for formatting purposes*")
        st.markdown("""
        **Overview**

        *What is DAC2022?*

        Serving as the annual flagship event of NUS SDS, this year’s Data Analytics Competition attracted over 850 participants across 230 teams from our 6 local universities. Originating as a Data Science Competition a few years ago, our organising team opted for a new format this year, choosing to focus on exploratory data analysis instead to make it more beginner-friendly. This year’s competition was a great success, which ultimately led to over 100 submissions and 5 top teams over the course of a week’s efforts. This year’s competition featured a geospatial dataset graciously sponsored by Grab and participants got to work with real-life transport data across countries in the region. This allowed them to practice their technical skills that they have learnt in class, giving them a glimpse of working as data analysts over a span of four days.

        To view the submissions made by our top 5 teams, you may check them out [here](https://drive.google.com/drive/u/0/folders/18O4XvIVAyTqtcXWM-v27vt8nDEpc5uIL)!

        **Background**

        With the success of last year’s Data Science Competition hosted by the previous organising team, we wanted to ensure that this year’s competition was similarly successful to reach a wider audience base. When we initially started planning the competition back in August 2021, we wanted to find a reputable sponsor for the event. Thanks to the Career Advisors at NUS Centre for Future-Ready Graduates (CFG), we were given the chance to pitch to Grab the idea of collaborating for our annual datathon event. Given the impromptu opportunity, we swiftly customised a pitch deck for Grab to explain the benefits of working with us for DAC 2022 such as raising awareness of Grab’s job/internship opportunities for students in NUS. It is not often that we get the opportunity to put our personal presentation skills to good use and convince an external party to host an event that would be beneficial for both parties.
        """)
        with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.image(img_dac1, caption = "A screenshot of our Opening Ceremony, featuring the introduction video of the dataset by Grab", width=600, )
            with col3:
                st.empty()
        st.markdown("""
        **Learnings**

        1. A smooth sea has never made a skilled sailor

        Organising such a large-scale datathon isn’t easy and will never be. There isn’t much information online as to what you need to have and what key points that you will need to take note of. Fortunately, NUS SDS does have previous experience hosting these kinds of events that we could tap into while we were planning for DAC 2022. Previous batches’ proper documentation of past planning mistakes and general competition guidelines helped us to gain a bigger picture of the event that we wanted to host and visualise the roles that we needed to fill.

        When we had first received the dataset from Grab, our organising team was stumped at extracting insights from it as no one on the team had prior experience with geospatial data. Our Workshop Team members, who were supporting the organising team, kindly volunteered to do more research on handling geospatial datasets. Their eagerness and confidence in dealing with the dataset allowed the organising team to confidently move forward with planning the rest of the competition.

        One major issue that we had faced midway through the planning of the competition was that we had underestimated the amount of work the organising team had to do to get the event up and running. There were indeed many administrative matters to resolve, which included the collation of Non-Disclosure Agreement forms as well as confirming the schedules of our judges to ensure their participation in our event. Handling all these processes in the right manner was indeed crucial to ensure the smooth operations of this event.

        On top of this, our initial plan was to host DAC 2022 on the 2nd week of January, when NUS students just started the semester in hopes of getting more teams to sign up. Yet, by the middle of December 2021, the organising team had not much to work with yet, with merely a skeletal structure of the event flow.

        After assessing the situation that we were in, where much of the event was not planned yet and the Grab personnel were currently on leave for the holidays, we decided to postpone the event to the start of February, right after the Chinese New Year celebrations to give ourselves more time to plan for the event. The main thought process behind this decision was that a delayed event will always be better than a rushed barely planned event.

        2. Communication is key (by Axel)

        It is one thing to have a vision for the competition and another to execute it. For myself, I tend to keep my ideas to myself and prefer to execute simple tasks by myself to not inconvenience others. However, in the scenario that I was in, having to juggle internship and planning of DAC, communicating my ideas to the team for them to execute was becoming increasingly important. After all, hosting DAC is a team effort and not an individual effort.

        Delegating tasks to the Events Team allowed for planning to occur even when I was occupied by my internship’s tasks. Delegating tasks to my team members also had a positive effect, as I was more able to focus on the big picture of the event and realise which areas of planning that we had neglected. Giving freedom to team members to resolve their own tasks at their own prerogative gave them a greater sense of ownership and an incentive to seek out innovative solutions.

        One thing that I’m really proud of in this competition came out of our member’s initiatives. One of them suggested using Discord as a central hub for disseminating information about the competition and providing a common platform for groups to discuss their projects. Discord has lots of useful bots and functions for running hackathons, such as user-defined roles and room assignment for teams. With Discord, we were also able to allow for Q&A questions to be publicly viewed and referenced by other teams. Using Discord did immensely help to streamline competition communication and I would wholeheartedly recommend other competition organisers to use it as well.

        Continuously communicating about what had not been done and what could be improved also helped us to assess the current situation that we were in. This really helped to smooth out the planning process and ensure that we covered any blind spots that we had failed to consider at first.

        Fortunately, our efforts paid off in the end, as there was an increase in the number of signups overall. This was particularly impressive, considering that we hosted our competition at a much later period compared to last year and were in fact expecting a decrease in participation rates. In fact, one of our main considerations of planning this event was to reinvigorate student life given the current COVID-19 situation. We were indeed glad to see that the large number of signups was a testament of this.

        Of course, this would not have been possible without the help of our Publicity Team members, who reached out to nearly 40 other student clubs to help us increase our outreach for the event. Other NUS departments such as CFG, Faculty of Science and School of Computing also helped us to publicise our event, which was much appreciated. Indeed, we’ve learnt that it’s vital for us to maintain good relations with other like-minded student organisations to ensure the success of organising such events.

        3. Failure is the key to success (by Harry)

        Similar to Axel, I gave my Marketing Team members the liberty to identify potential sponsors that could support our event. Doing this would allow them to learn more about the data/tech industry in general before we would proceed to shortlist our prospective partners and/or sponsors. Our team had managed to identify many different companies from various industries, but had faced rejections in the process. Worst still, many companies did not respond to our sponsorship emails, which felt demoralising at times.

        With multiple waves of attempts however, we managed to secure enough sponsors to support our event. Furthermore, we even exceeded our own sponsorship target in the end, leading to an overall increase in the prize pool compared to last year’s competition. The addition of having sponsored t-shirts from an external company was also a nice touch, given that this would entice participants to send in a valid submission to us for the competition.

        In summary, pursuing sponsorships was indeed an eye-opening experience for our team. This has taught us to be resilient when facing hardships or dejections, which would only make us mentally stronger over time. Without experiencing prior failures, achieving small successes like these would not be as enjoyable as one would expect. 
        """)
        with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.image(img_dac2, caption = "Jet New, President of NUS SDS, making his Closing Speech to thank all parties involved in DAC2022 during our Closing Ceremony", width=600, )
            with col3:
                st.empty()
        st.markdown("""
        4. Playing to each other's strengths

        Managing DAC 2022 was more than just handling a dataset, as there were a lot of tasks that we needed to complete to make it seem enticing for participants to join. The success of this event would not have been possible without the help and guidance from our fellow members in NUSSDS who excelled at their different roles:

        - Our President Jet and Vice-President of Events Ananya, for helping to look through our draft event proposals and giving constructive criticism of certain aspects of the event to make it better.

        - Our Events Team members Fang Ling, Shreya, Yi Fu and Madeline, for working together with Grab to plan out the timeline and problem statement for the competition. The team’s efforts were indeed vital in ensuring that everything operated smoothly without major hiccups throughout the competition week.

        - Our Marketing Team members: Gordon and Chenxiao for securing sponsors for DAC 2022; as well as Hannah and Aengus, for helping to manage a “Team Finder” feature of the event. This Team Finder matches people to form a team and was a rather important feature that we wanted to have. As most lessons are still taught virtually, we wanted to use DAC 2022 as a chance to connect data enthusiasts together to work on a meaningful project and from this experience hopefully build new friendships. Keeping to the theme of making the competition beginner-friendly, we wanted to make it as inclusive as possible to individuals who might not know many people interested in the field of data analytics. Hence, the Team Finder was important as it helps participants to make new friends and network with fellow data enthusiasts.

        - Stephen and Rui En, along with their Workshops Team members Keith, Javier and Wei Liang, for helping us to better understand the dataset and were integral in helping us to word the problem statement for the competition. Having them around to work on understanding the dataset really helped to lighten the load on the Events Team. During the actual competition, they assisted to get participants started on the provided dataset by hosting an introductory workshop.

        - Ethan and his Publicity Team members Briana, Tze Lynn and Yi Xuan, for helping to design cool slides and social media posts to make DAC 2022 look appealing! Their efforts in contributing appealing visuals and increasing social media outreach were also a major contributing factor to the success of this event.
        """)
        with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.image(img_dac, caption = "A screenshot from our Closing Ceremony, featuring our organising team, judges and participants", width=600, )
            with col3:
                st.empty()
        st.markdown("""
        **Conclusion**

        All in all, while organising DAC 2022 was a pretty stressful experience, we felt that this has helped us to achieve some form of personal growth and develop our leadership skills. We would both agree that this was indeed one of our toughest experiences in university so far. 

        **Acknowledgements**

        To commemorate the success of this event, we would also like to thank the following for their support:

        - Our main sponsor, Grab and its Data Science Team (consisting of Victor, Kenrex and Keru), for providing us with the dataset, prizes and expertise as judges;

        - Our other sponsors, AI Singapore and Quest Ventures, for providing us with prizes for our participants;

        - The NUS Department of Statistics and Data Science, for partially sponsoring the cash prizes for this event;

        - Gregory He and Emily Tan, our Career Advisors from NUS CFG who assisted us with onboarding Grab to support our event;

        - Jackie Tan, Head of Tribe Academy, for supporting our flagship event for the second consecutive year through his advanced technical workshop that was vital to the competition;

        - Prof Carol Hargreaves, Director of NUS Data Analytics Consulting Centre, for accepting our invitation as one of our judges;

        - And last but not least, the undergraduate population amongst our local universities for either participating actively in our competition or helping to spread the word about our event through various social media platforms.

        We hope that all parties involved have enjoyed their experience throughout the competition and had fun in the process. Our society looks forward to organising this flagship event again next year, so that more students will be inspired by the applications of data science and analytics in the real world.

        If this post has inspired you and you are keen to take on the challenge of hosting the next iteration of our flagship datathon event, do look out for our next recruitment cycle over the summer holidays.

        To find out more about Data Analytics Competition 2022, do check out the recordings of the following online events and workshops from the competition below:
        """)
        st.subheader("Opening and Closing Ceremonies")
        with st.container():
            col1, col2 = st.columns((2,2))
            with col1:
                st.video("https://www.youtube.com/watch?v=j0yvVP5XvTk")
            with col2:
                st.video("https://www.youtube.com/watch?v=goSAydRaOjY")
        st.subheader("Beginner and Advanced Workshops")
        with st.container():
            col1, col2 = st.columns((2,2))
            with col1:
                st.video("https://www.youtube.com/watch?v=6n3uQFZdN9g")
            with col2:
                st.video("https://www.youtube.com/watch?v=UlUU_WW3H_0")
        st.markdown("""
        *Axel Lau is the Events Director of the NUS Statistics and Data Science Society (AY21/22)*

        *Harry Chang is the Marketing Director of the NUS Statistics and Data Science Society (AY21/22)*       
        """)

    
    
    elif selected == "Obstacles in promoting healthy eating habits":
        st.subheader("Obstacles in promoting healthy eating habits")
        st.write("November 12, 2021 | [Essays]()")
        st.markdown("""
        An obstacle that may undermine national efforts aimed at reducing childhood obesity in high-income countries would be the lack of support by parents to cultivate healthy eating habits amongst children. As children are deemed rationally unprepared to make their own decisions at a young age, the actions of their parents are imperative in influencing their children’s behaviours. This is especially the case when children view their parents as their role models who they would like to develop similar traits with when they grow up in the future. In a 2019 Singaporean study, parents conveyed various difficulties in trying to promote healthy eating habits to their children. Parents preoccupied with work and other commitments do not have adequate time to prepare healthy food for their children. They would often opt to eat outside or order takeaways instead of consuming home-cooked meals, which increases the likelihood of fast food consumption instead. Furthermore, they cited the dietary preferences for less healthy food by either their spouse or their own parents that would compromise their own efforts in promoting healthy eating to their children (Chong, 2021). These observations are also similar in other high-income countries in the European Union (EU), including Germany and Italy. In a 2018 online survey targeted at 187 policy-makers and stakeholders from 12 EU member states, 67.6% of the respondents agreed that the lack of parental support contributed to the prevention of childhood obesity, ranking it amongst the top three reasons from a possible nine listed in the survey (Abu-Omar et al., 2018).
    
        Another obstacle that may hinder national efforts to reduce childhood obesity in high-income countries would be the difficulty in enforcing regulations against unhealthy food marketing. As most food companies aim to generate profits by maximising revenue and minimising costs, they may not necessarily be obliged to promote healthier foods, especially when the latter may not be as popular amongst citizens compared to fast foods and sugary beverages. In fact, eating healthily is considered a more costly option due to the higher cost required to farm fresh fruits and vegetables, even in high-income countries such as the USA (Sotirovska & Philip, 2018). Moreover, promoting healthier foods is considered high-risk, especially when competing firms choose to continue marketing their less healthy yet popular products instead. To illustrate, PepsiGo had unsuccessfully attempted to market healthier products in the past, resulting in a fall in revenue and market share. It had to recenter its focus to its main products (e.g Cheetos, Doritos and Pepsi) to gradually regain its position in the food industry (Fleming-Milici & Harris, 2020). Even with increasing regulations against unhealthy food marketing in different countries, the wide usage of social media platforms especially amongst today’s children is a loophole constantly exploited by food companies to maximise their outreach and promote the sale of their products. As such, the difficulty in regulating unhealthy food marketing deters national efforts to reduce childhood obesity, particularly due to firms’ common aim to maximise profits by any means necessary, even at the possible expense of their consumers’ long-term health.
    
        In my personal opinion, the lack of parental support to promote healthy eating habits is a more difficult obstacle to overcome compared to the difficulty in regulating unhealthy food marketing when it comes to reducing childhood obesity in high-income countries. Given the fast pace of living in metropolitan areas, it is understandable that citizens living in such conditions may not necessarily afford the luxury of time to prepare healthy meals diligently for their children, especially when they are working. In addition, parents would struggle to constantly find the motivation to impose a healthy diet on their children or themselves all the time. A sudden slip-up in maintaining such efforts may lead to a rebound towards unhealthy food consumption once again, which is especially detrimental for parents as their children would likely be influenced to follow suit. On the other hand, tackling unhealthy food marketing may be an easier problem to overcome. As online media is often referred to as a double-edged sword, it can either be used by firms to positively promote healthy eating habits or encourage unhealthy food consumption instead. Therefore, it would ultimately be up to the individual’s self-control to decide which form of influence to follow when it comes to making eating decisions.

        References:

        1. Abu-Omar, K., Messing, S., Sarkadi-Nagy, E., Kovács, V. A., Kaposvari, C., Brukało, K., ... & World Health Organization. (2018). Barriers, facilitators and capacities for childhood obesity prevention in 12 European Union member states: results of a policy-maker survey. Public health panorama, 4(03), 360-367. https://apps.who.int/iris/bitstream/handle/10665/324940/php-4-3-360-367-eng.pdf 
        2. Chong, M. (2021). Commentary: Why do some children choose unhealthy food when they get older? CNA. https://www.channelnewsasia.com/commentary/children-fast-food-healthy-eating-parents-research-1883946 
        3. Sotirovska, D., & Philip, E. (2018). Why eating healthy is so expensive in America. Vox. https://www.vox.com/videos/2018/3/22/17152460/healthy-eating-expensive 
        4. Fleming-Milici, F. & Harris, J. (2020). Food marketing to children in the United States: Can industry voluntarily do the right thing for children's health?. Physiology & Behavior. 227. 113139. https://doi.org/10.1016/j.physbeh.2020.113139   
        """)

    elif selected == "Role of healthcare data analytics in managing COVID-19":
        st.subheader("Role of healthcare data analytics in managing COVID-19")
        st.write("November 12, 2021 | [Essays]()")   
        st.markdown("""
        Contact tracing was one method which demonstrated the usage of healthcare data analytics to help tackle the pandemic. The idea behind contact tracing revolves around the usage of mobile applications for users to transmit their localisation data as unchangeable time-stamped records into a common database. This database will then be used as an investigation system by governments to trace persons who either had contact with newly infected patients or had frequented high-risk areas. Collecting such data also ensures that users suspected of contracting COVID-19 are not contravening self-isolation protocols, as their locations are constantly monitored to deter them from doing so (Benreguia et al., 2020). Moreover, Asian countries such as Taiwan and South Korea have resorted to tracking their citizens’ movements without the latter’s consent to maximise the effectiveness of contact tracing efforts (Nageshwaran et al., 2021). In particular, the TraceTogether mobile application, developed in Singapore, has greatly assisted the country in identifying suspected and confirmed COVID-19 cases. Using this application involves the exchange of Bluetooth signals between phones within range of each other to discover nearby users. With the increasing number of confirmed cases in Singapore, the usage of TraceTogether application was eventually made compulsory for users to check-in when visiting high traffic areas such as shopping centres and workplaces using the in-built SafeEntry system within the application for them to monitor their whereabouts. The local authorities commended TraceTogether for helping to “reduce the average time taken to contact trace from four days to less than 1.5 days” (Low, 2021), indicating its usefulness in Singapore’s battle against COVID-19.
        
        Data analytics also contributed to healthcare decision-making by helping countries to “evaluate the effectiveness of COVID-19 control measures'' (Alsunaidi et al., 2021). To illustrate, a study on China published in March 2020 concluded that restricting and relaxing quarantine measures at different timings greatly impacts the trend in the number of daily cases in the subsequent stages of the outbreak (Chen et al., 2020). Using the data of daily confirmed cases reported in Hubei, the researchers ran a simulation using the C-SEIR mathematical model (Zhang et al., 2005) to predict different peak periods of the pandemic in the region. The simulation revealed that adjusting the lockdown start date earlier or later by two days could have decreased or increased the number of confirmed cases by almost twice the actual amount respectively. Furthermore, the study showed that the relaxation of such restrictive measures should occur in a more controlled manner to minimise the number of infections and avoid experiencing subsequent large waves of infections. In correspondence to the study’s results, China has adopted a “zero tolerance policy” as its main public health approach, as its main priority remains in preserving the good health of its citizens and minimising deaths (Ning et al., 2020). Strict lockdowns are enforced whenever clusters occur in certain regions, which includes the restriction of inter-city movements such as workplace closures and transport bans. The daily cases in China remain negligible compared to other countries such as Britain and USA, both which have adopted the endemic approach of living with the virus instead (Feng, 2021). While China’s approach is effective in minimising daily infections, this may come at a high economic cost, especially when the country relies on the international market to boost its economy, which is hindered by travel restrictions. 
        
        While both above-mentioned applications of healthcare data analytics have their respective merits, contact tracing is a more successful contribution in comparison to the control of the COVID-19 restrictive measures. With reference to the Socio-Ecological Model, the main focus of contract tracing is at the individual level. Individuals would be more conscious to only leave their houses whenever necessary, or at the very least monitor their whereabouts to minimise the risk of infection during the pandemic. On the other hand, the control of restrictive measures focuses at the policy level, since the decision making by governments on such measures affects its citizens’ livelihoods, which may not be agreeable by all members of the local community especially when the country’s economy would be affected in the long run. As such, contact tracing would be deemed more successful in its contribution against COVID-19, especially when the individual belief of exercising social responsibility has the potential to relieve the burden borne by governments to tackle the virus. After all, the prevention of more cases is indeed better than cure.

        References:
        1. Alsunaidi, S. J., Almuhaideb, A. M., Ibrahim, N. M., Shaikh, F. S., Alqudaihi, K. S., Alhaidari, F. A., Khan, I. U., Aslam, N., & Alshahrani, M. S. (2021). Applications of Big Data Analytics to Control COVID-19 Pandemic. Sensors (Basel, Switzerland), 21(7), 2282. https://doi.org/10.3390/s21072282 
        2. Nageshwaran, G., Harris, R. C., & Guerche-Seblain, C. E. (2021). Review of the role of big data and digital technologies in controlling COVID-19 in Asia: Public health interest vs. privacy. DIGITAL HEALTH. https://doi.org/10.1177/20552076211002953 
        3. Benreguia, B., Moumen, H., & Merzoug, M.A. (2020). Tracking COVID-19 by Tracking Infectious Trajectories. IEEE Access, 8, 145242-145255. https://doi.org/10.1109/ACCESS.2020.3015002 
        4. Low, Z. (2021). Mandatory TraceTogether-only SafeEntry brought forward to May 17. CNA. https://www.channelnewsasia.com/singapore/covid19-tracetogether-safeentry-may-17-brought-forward-token-app-1358126 
        5. Chen, B., Shi, M., Ni, X., Ruan, L., Jiang, H., Yao, H., ... & Ge, T. (2020). Visual data analysis and simulation prediction for COVID-19. https://doi.org/10.18562/IJEE.055
        6. Zhang. J., Lou, J., Ma. Z., et al. (2005). A compartmental model for the analysis of SARS transmission patterns and outbreak control measures in China. Applied Mathematics and Computation, 162(2), 909-924.
        7. Feng, E. (2021). China Is Imposing Strict Lockdowns To Contain New COVID Outbreaks. But There’s A Cost. NPR. https://choice.npr.org/index.html?origin=https://www.npr.org/sections/goatsandsoda/2021/09/02/1033396323/china-is-imposing-strict-lockdowns-to-contain-new-covid-outbreaks-but-theres-a-c 
        8. Ning, Y., Ren, R., & Nkengurutse, G. (2020). China's model to combat the COVID-19 epidemic: a public health emergency governance approach. Global health research and policy, 5, 34. https://doi.org/10.1186/s41256-020-00161-4 
        """)
    elif selected == "Evaluating 'Chinese Privilege' in Singapore: Special Assisted Plan Schools":
        st.subheader("Evaluating 'Chinese Privilege' in Singapore - Special Assisted Plan Schools")
        st.write("April 29, 2021 | [Final Essay]()")
        st.markdown("""
        In 1979, the Special Assistance Plan (SAP) was established in order to preserve the heritage of top Chinese schools, nurture traditional Chinese values in students and promote bilingualism. Today, critics question the relevance of SAP schools, as they claim that these schools no longer fulfil their original goals. Instead, they cite these schools as an example of “Chinese privilege” in Singapore, which is defined as a scenario where “Chinese-Singaporeans, unlike minority Malays, Indians, or Eurasians, enjoy exclusive racial advantages that position them as Singapore’s cultural, economic, political, and social core”. In my opinion, SAP has reinforced “Chinese privilege” in Singapore as it has been perceived by Singaporeans to promote racial segregation and social inequality instead.

        For starters, the admission criteria required to enrol in these schools heavily favour the top Chinese students, which may encourage “Chinese elitism”, where they deem themselves to be superior compared to their non-Chinese peers due to their enrolment in SAP schools. SAP students are not only required to take Chinese as a subject in the Primary School Leaving Examinations (PSLE), but also at the secondary level. Furthermore, SAP schools are only open to the top 30% of students in each PSLE cohort. In fact, some SAP schools are more stringent with their admission requirements, including Hwa Chong Institution, which admits only the top 3% of PSLE graduates annually. While this is partly due to historical prestige, government policies were also introduced to boost the elite status of the SAP schools. When educational streaming was first introduced in Singapore, only the nine SAP schools at the time were banded as “Special”, which formally branded them as the cream of the crop amongst all Singapore schools. Subsequently, the Integrated Programme (IP) was later introduced, allowing top secondary school students to skip the GCE ‘O’ Level examination and proceed to take a national pre-university examination after six years of secondary education. As SAP schools were among the first to pilot the programme, about 35% of the IP schools also benefit from SAP today. Enrolling in such prestigious institutions would indeed be a “Chinese privilege”, particularly due to the compulsory prerequisite of studying Mandarin, which would disadvantage the students from minority races who are mostly unable to do so. 

        In addition, the lack of daily interaction with people of other races may discourage multiracialism amongst SAP students, which arises from the inadequate ethnic sensitivities of other racial groups. While SAP schools are open to all eligible students regardless of race, they are required to be highly proficient in Mandarin as it is the only mother tongue offered. This, along with the strong Chinese tradition of SAP schools, have greatly discouraged students of minority races from enrolling. As such, the minimal inter-ethnic interaction experienced by SAP students results in them having “less ethnically diverse social networks than their non-SAP peers.” To support this, a 2012 Straits Times survey conducted amongst the top 5 schools (of which 2 are in SAP) revealed that 82% of SAP students reported a lack of close friends from other races, compared to 12% for the non-SAP schools. In a RICE Media interview, a Malay SAP alumnus elaborated that certain SAP students lack cultural knowledge of other races, citing quotes such as “I can’t differentiate between Malay and Indian” and being asked “if water was halal”. This shows that minorities who enrol in SAP schools would find it nearly impossible to avoid racist jokes and insensitive comments from their Chinese peers in SAP schools, suggesting the latter’s inability to interact meaningfully with other races. In fact, students from minority races would find it challenging to represent their own races and cultures to face the predominantly Chinese cohort of SAP students. This would ultimately lead to an increased racial segregation between the Chinese and the minority races, as xenophobic sentiments may arise especially from the former, believing that their status as the majority race is indeed a social privilege in Singapore. Despite the government’s attempts to alleviate this through Racial Harmony Day celebrations and weekly conversational Malay lessons, this may be insufficient to encourage inter-racial understanding between students of different races. A possible suggestion to rectify this would be to abolish the SAP system. By eliminating the prerequisite of studying Mandarin in these Chinese schools, this would allow the minority races to be better represented in each school. Also, this provides more opportunities for daily interactions between the different races to better promote multiracialism in all schools.

        Furthermore, students in SAP schools are provided an “unequal access to educational resources” compared to their peers in other public schools, which reinforces the idea of “Chinese privilege” in Singapore. As a reward for performing well under Singapore’s meritocratic system, students in SAP schools experience multiple advantages over their counterparts in other schools. For instance, SAP schools enjoyed additional funding in the form of annual grants and interest-free loans, including a per capita government funding for SAP school students that was up to over 50% higher than other secondary school students during the programme’s initial years. In 2019, then Education Minister Ong Ye Kung updated that each SAP student receives an additional S\$300 “to develop their proficiency and interest in Chinese language-related studies.” SAP schools often receive donations from alumni working in top organisations and firms to repay their alma mater for contributing to their educational success. These schools also have a lower student-teacher ratio, as attributed in their additional funding used to improve both the quality and quantity of their teaching staff. In particular, selected SAP schools offer the Bicultural Studies Programme (BSP), which provides its top students with unrivalled opportunities to visit China and learn more about Chinese culture and values through daily interactions with the mainland Chinese. As BSP is not offered to non-SAP schools, this signifies the increased government funding that is invested in nurturing the SAP elites. Again, these privileges are only offered to students that take Chinese as an examinable subject, which mostly excludes the minority races. As such, the advantages that are offered to SAP schools reinforces the idea that “Chinese privilege” exists, given that the SAP students are mostly Chinese. To alleviate this, a “donation cap” can be imposed by the government on SAP schools to prevent them from receiving excessive financial support for additional facilities and exclusive programmes. Under this framework, donations should be declared and checked annually by the government. SAP schools which exceed this “donation cap” would then incur a decrease in additional funding per student, down from S\$300 to S\$150 for example.

        Moreover, SAP “perpetuates social inequality by instilling cultural capital in its students that enables them to thrive in a world where China is an emerging economy of opportunities”. To justify the relevance of SAP, Ong Ye Kung explained in 2019 that the rapid development of China, as Singapore’s largest trading partner, raises the importance of helping students to amass Chinese cultural capital. Doing so could reap economic benefits when doing business with China, especially when one possesses Chinese cultural knowledge that is essential in facilitating access and building strong professional ties with China’s market, which serves as a key motivation behind SAP. As mentioned earlier, the introduction of BSP to selected SAP schools exemplifies this belief, as top students are offered the opportunity to visit China and learn the Chinese culture, language and values directly from daily interactions with the mainland Chinese. Pierre Bourdieu’s concept of capital suggests that by having a deeper understanding of Chinese culture and values, SAP students could be well-versed with the “knowledge, skills and abilities to pursue further opportunities professionally and maintain or advance their social positions,” provided that they seize the opportunities to make these connections. These include either working or studying in China, as well as building professional ties with Chinese firms and individuals. By restricting such opportunities to a handful of students from a particular racial group, this widens the inequality gap between the SAP and non-SAP students since the latter do not have access to such overseas immersion programmes. To resolve this, the government can consider expanding BSP to Malay and Tamil-speaking students, especially in the form of overseas immersion programmes for non-SAP public schools.

        Given that Singapore boasts a population that is nearly 75% Chinese, the SAP is a prime example of how “Chinese privilege” is deemed prevalent in the country today. The government should explore solutions to minimise the unfair advantages enjoyed by the SAP schools. As previously mentioned, it can reduce the additional funding to resolve the unfair allocation of resources that favours the SAP schools. Alternatively, SAP can be expanded by creating similar programmes that cater to Malay and Tamil-speaking students and offered to all schools in Singapore to close the inequality gap between the Chinese and the minority races. Better still, SAP should be abolished to ensure a more equal representation of all races in every school and encourage multiracialism amongst students through inter-racial interactions. These suggestions would align with the Ministry of Education’s vision that “every school is a good school”.

        References:

        1.	Gien, Si Yun (2019). Time To Rethink? SAP Schools and Chineseness: The Millennial Experience. ScholarBank@NUS Repository. Retrieved from https://scholarbank.nus.edu.sg/handle/10635/157979  
        2.	Saharudin, Hydar (2016). Confronting ‘Chinese privilege’ in Singapore. New Mandala. Retrieved from https://www.newmandala.org/brief-history-chinese-privilege-singapore/  
        3.	Zhuo, Tee (2017). The Special Assistance Plan: Singapore’s own bumiputera policy. Equality & Democracy (Yale-NUS College). Retrieved from https://equalitydemocracy.commons.yale-nus.edu.sg/2017/12/07/the-special-assistance-plan-singapores-own-bumiputera-policy/  
        4.	Koh Jhai Leng, Shammah (2018). A Fruitful Graft: Examining the Localisation of 'White Privilege' as 'Chinese Privilege' in Singapore. ScholarBank@NUS Repository. Retrieved from https://scholarbank.nus.edu.sg/handle/10635/144416  
        5.	Ong, Ye Kung (2019). Funding to Special Assistance Plan Schools and non-Special Assistance Plan schools. Parliament Sitting No. 96, Volume 94. Singapore: Parliament of Singapore: No. 13. Retrieved from https://sprs.parl.gov.sg/search/sprs3topic?reportid=written-answer-4643  
        6.	Yong, Charissa., & Zaccheus, Melody (2012). Top schools’ students tend to have friends like themselves: Poll. The Straits Times, Retrieved from https://www.asiaone.com/News/Latest%2BNews/Edvantage/Story/A1Story20121117-384060.html  
        7.	Pang, Ethel (2019). As Long As SAP Schools Exist, ‘Chinese Elitism’ in Singapore Will Exist. RICE Media. Retrieved from https://www.ricemedia.co/current-affairs-opinion-sap-schools-chinese-elitism-singapore/ 
        8.	Ngu Li Xuan, Geraldine (2020). Sapping Resources? The Ineffectiveness and Inequalities of SAP School Education. ScholarBank@NUS Repository. Retrieved from https://scholarbank.nus.edu.sg/handle/10635/170314  
        9.	Bourdieu, Pierre (1986). “The Forms of Capital.” Pp. 241-258 in Handbook of Theory and Research for the Sociology of Education, edited by J. G. Richarson. New York: Greenwood Press

        """)
    elif selected == "Analysing usefulness of word clouds in mental health studies":
        st.subheader("Analysing usefulness of word clouds in mental health studies")
        st.markdown("""
        For this assignment, I will be analysing word clouds from a research article published in
        2019, which aimed to understand and measure psychological stress levels based on social
        media posts.

        In today’s digital age, people are increasingly using social media platforms to inform others
        of their mental states, garner social support, as well as to record their daily activities.
        Despite previous studies which investigate the underlying factors behind stresses in our
        daily lives, many researchers believe that there is still a gap in the scientific understanding of
        how psychological stress is expressed on social media. In particular, they believe that mental
        health conditions, such as depression and anxiety, can be predicted from the social media
        language of its users.

        In 2019, a study was implemented to explore how to differentiate high-stress users from
        low-stress users by performing natural language processing methods on text in social media
        posts.

        To facilitate data collection, the study’s researchers deployed a survey on Qualtrics, which
        consisted of several demographic questions (age, gender, race, education, income) and the
        Perceived Stress Scale questionnaire. Each item in the scale is scored from 0 to 4, with an
        absolute maximum summing to 40. The stress scores for each survey participant range from
        6 to 39, with a mean value of 30.

        Interestingly, the researchers chose to obtain their data from Facebook and Twitter, as they
        are amongst the most widely used social media platforms worldwide. Survey participants
        were invited to share access to their Facebook and/or Twitter posts. Among the
        participants, 601 users completed the survey and had active accounts with more than 900
        words on Facebook and Twitter. Their social media posts were then downloaded by using
        the Facebook Graph and Twitter APIs. All participants who completed the survey were
        based in the United States.

        The posts were then processed using the HappierFunTokenizer available with the DLATK
        package in Python. The language of each user and county is then represented as a set of
        features. In the dictionary-based method, social media language is transformed into
        numerical features representing percentage proportions of lexical categories in an existing
        dictionary. In the data-driven method, the language is morphed into numerical features
        which represent the proportions of word clusters that are statistically similar according to
        their frequency distributions.

        Afterwards, 1-,2-, and 3-grams were extracted from all posts to analyse significant
        associations between words & phrases and stress. As seen above, the word clouds are
        visualizations of the Pearson correlations of words and phrases with stress scores obtained
        from the survey. The word clouds were generated by uploading the dataset containing the
        processed Facebook posts onto Wordle.net, a free online word cloud creator that no longer
        exists today. The red word cloud represents words commonly used by users with high stress
        levels while the blue word cloud represents words from Facebook posts of low-stress users.
        The size of each word indicates the correlation strength while the colour intensity indicates
        frequency (darker being more frequent).

        Based on the researchers’ analysis, the language of high stress users is made prevalent
        either by expressions of perceived lack of control, expressions of a need state or a lack of
        resources, along with a negative-angry sentiment. Also, high stress language seems to be
        comorbid with mental health conditions. Indeed, it is intriguing to see how these words
        reflect the adverse effects that stress can have on health. On the other hand, the language
        of low stress users has prominent positive affect, which include discussions of meals as well
        as feelings of social inclusion.

        Most of the time, the size of each word in a word cloud corresponds to the relative
        frequency of that particular word in a corpus. In the case of this visualization, however, the
        Pearson correlation coefficient between words & phrases and stress score is used as the
        metric that affects word size in a word cloud. On the other hand, the colour intensity of
        each word is used to measure frequency instead. In short, the researchers have attempted
        to address the common limitation of size misinterpretation by adding another metric when
        generating each word cloud.

        Although word clouds are simple to visualize and interpret, there are certain limitations that
        come with them. For instance, word clouds do not categorise words that have similar or the
        exact same meaning. In the context of my chosen visualisation, pairs of words such as
        “depressed” and “depression”, as well as “I” and “me”, are almost equal in size when
        compared in their own pairs. Having such synonyms as duplicated could omit out other
        unique words from appearing in the word cloud, which could affect the researchers’ analysis
        of identifying the words with the highest Pearson correlation values within the processed
        dataset.

        Another limitation of the visualisations discussed is that only Facebook data was used,
        despite also gaining access to the users’ Twitter updates during the data collection phase.
        To improve the results of the analysis, separate sets of word clouds can be generated using
        posts from other popular social media platforms, such as Twitter, Instagram, LinkedIn and
        Reddit. These different sets of word clouds, representing each social media platform, can
        then be compared against each other for further analysis to evaluate if the words with the
        highest Pearson correlation values are consistent across all sets. This is especially important
        since the social media language used in each platform may vary.

        To reiterate, word clouds are simple to use and were popularized in the early 2000s, when
        the photo sharing site Flickr first introduced their usage to display commonly used tags on
        its website. Being one of the most widely used forms of information visualization today,
        critics believe that word clouds can often be misinterpreted by the general public, primarily
        due to the issue of word size and the lack of context. However, the word clouds discussed
        above are generally appropriate in my opinion, as it has been made clear that the clouds
        were generated for academic research purposes to supplement the findings of a mental
        health study.

        References:

        1. Guntuku, Sharath Chandra, Anneke Buffone, Kokil Jaidka, Johannes C. Eichstaedt,
        and Lyle H. Ungar. "Understanding and measuring psychological stress using social
        media." In Proceedings of the International AAAI Conference on Web and Social
        Media, vol. 13, pp. 214-225. 2019.
        2. Viégas, F. B., & Wattenberg, M. “Timelines tag clouds and the case for vernacular
        visualization.” Interactions, 15(4), 49-52. 2008.
        """)
    elif selected == "Investigating the relationship between culture and sweet-sour taste interactions":
        st.subheader("Investigating the relationship between culture and sweet-sour taste interactions")
        st.write("October 31, 2020 | [Article])")
        st.write("*Are we correct to stereotype taste perceptions and preferences based on different cultures?*")
        st.markdown("""
        Imagine that you are drinking a glass of margarita. After that first sip, you find that your drink is too sour. You then lick some of the salt from the rim of the glass before taking a second sip. You find that now, the margarita tastes less sour! This is a perfect example of a taste interaction between different taste qualities. 
        
        When two or more taste qualities interact, they affect the perception of one another. The taste qualities involved can either enhance or suppress one another, which is dependent on their concentrations.
        
        Previous studies have shown that cultural differences do affect taste sensitivities and taste interactions amongst different individuals. For instance, a US study discovered that taste sensitivities across all five taste qualities are lower amongst individuals of African-American and Hispanic origin compared to Caucasians. Another study also revealed that Taiwanese students tend to have higher sweetness sensitivity compared to their American counterparts.
        
        Thus, a new study has sought to validate the above-mentioned findings. Conducted by a group of Danish and Chinese researchers earlier this year, this cross-cultural study suggested that culture does affect taste interactions to a certain degree. In particular, Danish consumers experienced a smaller extent of sourness suppression by the sweetness of sucrose as compared to their Chinese counterparts.
        
        To the researchers’ surprise, they discovered that the vice versa does not prove to be true. As they could not establish a relationship between culture and the extent of sourness suppressing sweetness, this suggests that the differences in taste perception may need to be further classified at the individual level. 
        
        So, in the first place, how does the suppression between sweetness and sourness occur?
        
        Sucrose, widely known as table sugar, undergoes hydrolysis to be further decomposed to glucose and fructose. This process can be quickened by introducing acids such as citric acid, commonly present in fruit juices. As such, hydrolysis reduces the formation of sugar crystals, explaining how sourness can suppress sweetness.
        
        Let us now try to break down this process from another perspective. Citric acid, for instance, has an estimated pH of 2.2, which exemplifies its relatively high acidity to its sourness. On the other hand, sucrose is known to be slightly alkaline – and a bit bitter, given its higher pH value of 8. However, when citric acid is introduced to sucrose, the resultant solution will have a pH range between 4 to 7. Simply put, we can also make use of the same reaction to explain how sweetness suppresses sourness.
        
        To further appreciate the findings of the study, we should also understand how taste sensitivities relate to taste preferences. 
        
        In a separate study conducted by Canadian researchers in 2019, there is evidence of a relationship between certain taste sensitivities of consumers and their taste preferences. In particular, sweetness and saltiness were revealed to be less preferred by consumers who recorded higher sensitivities in these two taste qualities.
        
        As such, the study sought to investigate how these taste interactions vary between both cultures. The Danish and Chinese test subjects evaluated six liquid mixtures: namely water, sucrose, tartaric acid, citric acid, a mixture of sucrose with tartaric acid and sucrose mixed with citric acid. Both citric and tartaric acids were used as samples to exhibit the taste of sourness, while sucrose was used to exhibit sweetness.
        
        Participants were tasked to taste one sample at a time, with a 30 second break in between after rinsing their mouth with water. For each sample, the taste sensitivity was evaluated on a 9-point scale, with 1 being ‘not at all’ and 9 rated as ‘extremely’ sweet or sour, depending on the sample.
        
        For samples containing a mixture of sweetness and sourness, they were evaluated with an additional ‘Just About Right’ (JAR) scale to measure the appropriate concentrations of sucrose and acids based on each individual. Together with the taste sensitivities, the JAR ratings for each sample were recorded using a questionnaire. Data collected from this questionnaire was later used for further analysis.
        
        On average, the Danish consumers consistently recorded higher sweetness sensitivities than their Chinese counterparts. This further explains how the researchers concluded that sucrose had managed to suppress tartaric acid to a greater extent in Chinese consumers compared to the Danish consumers.
        
        The researchers added that based on their research on similar studies, a Caucasian population generally tends to have a lower taste sensitivity for sweetness, sourness, saltiness and bitterness than an Asian population. Since an inverse relationship between taste sensitivity and taste preference has been established from the Canadian study, comparing the taste sensitivities of these Chinese and Danish consumers may therefore not be entirely representative of the ‘East vs. West’ comparison.
        
        In addition, the researchers could not conclude if culture had a role in sweetness suppression by sourness. This is because the results had varied between each individual, regardless of whether they were Chinese or Danish.
        
        Upon obtaining the necessary readings, the test subjects were later divided into three different clusters based on their relative sensitivities to sourness. For instance, consumers with similarly low sourness sensitivity were grouped together under the same category. This may be due to the high suppression of sourness by sweetness.
        
        This same method of classification based on sweetness was also performed on these customers. Likewise, each cluster comprised of both Chinese and Danish consumers. While there were certain trends that may imply a relationship between culture and taste interactions, the researchers could not affirm this conclusion upon further analysis.
        
        Overall, beverage manufacturers stand to benefit most from the results of the study. In order to boost their sales revenue, they would need to re-evaluate their product segmentation strategies to diversify their target consumer range. Instead of focusing on culture, these companies may wish to explore other variables such as age and gender instead.
        
        With this stereotype debunked, do we now expect people of different cultures to appreciate unique drinks such as sugarcane juice with lemon the same way? Only time and experience will tell. 
        
        References:
        1. Bertino, M., Beauchamp, G. K., & Jen, K. L. C. (1983). Rated taste perception in two cultural groups. Chemical senses, 8(1), 3-15. Also available from https://academic.oup.com/chemse/article-abstract/8/1/3/271785 
        2. Chamoun, E., Liu, A. A., Duizer, L. M., Darlington, G., Duncan, A. M., Haines, J., & Ma, D. W. (2019). Taste sensitivity and taste preference measures are correlated in healthy young adults. Chemical senses, 44(2), 129-134. Also available from https://pubmed.ncbi.nlm.nih.gov/30590512/ 
        3. Hydrolysis. (n.d). In Wikipedia. Retrieved from https://en.wikipedia.org/wiki/Hydrolysis 
        4. Junge, J.Y.; Bertelsen, A.S.; Mielby, L.A.; Zeng, Y.; Sun, Y.-X.; Byrne, D.V.; Kidmose, U. Taste Interactions between Sweetness of Sucrose and Sourness of Citric and Tartaric Acid among Chinese and Danish Consumers. Foods 2020, 9, 1425. Also available from https://www.mdpi.com/2304-8158/9/10/1425 
        5. Williams, J. A., Bartoshuk, L. M., Fillingim, R. B., & Dotson, C. D. (2016). Exploring ethnic differences in taste perception. Chemical senses, 41(5), 449-456. Also available from https://academic.oup.com/chemse/article/41/5/449/2366044 
        """)
    elif selected == "Timing vaccination campaign to reduce measles infections":
        st.subheader("Timing vaccination campaign to reduce measles infections")
        st.write("September 30, 2020 | [Article]()")
        st.write("*Despite having a vaccine that is readily accessible, measles cases and deaths are still surging worldwide, especially in recent years. Why is this so and are there any long-term solutions to resolve this?*")
        st.markdown("""
        According to an update from the World Health Organisation (WHO), nearly 10 million cases of measles were reported in the year 2018. During that year, more than 140,000 people worldwide have died from the disease. In addition, reported measles cases have surged internationally in devastating outbreaks across different regions.

        Besides the mild symptoms of fever, runny nose and body rashes, this highly contagious disease may also lead to long term effects on the immune systems of those affected. For instance, as many as 1 in 20 children with measles will contract pneumonia, which is the leading cause of death amongst young children. In addition, about 1 in every 1000 who contract measles will develop encephalitis - or brain infection - which can result in the child being deaf or developing intellectual disability. This raises the importance of vaccinating children so that they will not have to live with such complications in the long run.

        Despite the long existence of an effective and cost-efficient vaccine, the outbreak of measles remains a pressing global health issue particularly for developing countries. These nations have often been identified to lack access to vaccinations and high-quality health infrastructure.
        
        As such, a study on the measles outbreak in Pakistan has predicted that optimising the timing of a vaccination campaign plays an important role in reducing the total infections of measles.

        The study, led by senior researcher Niket Thakkar from the Institute for Disease Modelling (based in the USA), was conducted in response to the sudden increase in measles cases within the span of a year. From 2016 to 2017, the number of cases in Pakistan have more than doubled, as confirmed by local laboratories.

        Prior to the study, measles vaccination coverage in toddlers aged under 2 was estimated to be 61% nationwide, as cited from Pakistan’s Demographic and Health Survey (DHS) in 2012 – 2013. With Pakistan being identified as one of the top countries with the most unvaccinated infants, the need to improve this rate was therefore essential, as suggested by Thakkar and his team of researchers.

        The researchers came up with a mathematical model which uses linear regression to predict the severity of future outbreaks. Using case data from Pakistan that contains the number of new measles cases per month, they predicted the number of cases of subsequent months within the next three years. This data was also categorised by province level to compare the severity of the measles outbreak between different regions in Pakistan. 

        To understand how linear regression works, let us think of this example. If you spent \$10 on a Monday, \$20 on a Tuesday, \$30 on a Wednesday, how much would you win on Thursday? If your answer is $40, you’ve just performed linear regression - this method thus makes use of available information to constantly make predictions.

        This model assisted researchers in understanding when and where the vaccine should be distributed within the country. Their results show that holding a vaccination campaign in November has the greatest impact, with an estimated 440,000 more infections that could be prevented in comparison to a January campaign. These results were later used by the Pakistani government in vaccination planning, which led to the implementation of the campaign in November 2018.

        According to the study, less cases were confirmed from May to October as compared to the rest of the year. This suggests a low transmission season during this period, reiterating why the campaign is best implemented in November, when cases start to surge again. As a result of this implementation, the estimated measles vaccination coverage in infants aged under 2 had improved to 73% nationwide. This statistic was reported in 2017 – 2018’s iteration of Pakistan’s DHS, which was published in January 2019.

        On the other hand, if the campaign was delayed from November 2018 to May 2019, can you guess the number of additional infections that would have occurred? There would have been more than 600,000 additional infections from 2018 to 2021 - this significant number is sandwiched between the population sizes of Sialkot and Sukkur, the 13th and 14th most densely populated cities in Pakistan respectively (out of 99 cities in total). As such, this further justifies the researchers’ preference for the campaign to be conducted in November.

        Beyond immediate outbreak response, countries should continue investing in high quality immunisation programmes, as well as disease surveillance. This would help to ensure that these outbreaks are detected quickly and stopped as soon as possible.

        It is indeed a tragedy to witness a sudden increase in cases and deaths from a disease that is easily preventable, especially in recent times. Therefore, it is crucial to ensure that even the poorest countries have access to these high-quality vaccination programmes. This would help prevent the unnecessary loss of lives to easily treatable diseases, including measles.
        
        References:

        1. Thakkar, N., Gilani, S. S. A., Hasan, Q., & McCarthy, K. A. (2019). Decreasing measles burden by optimizing campaign timing. Proceedings of the National Academy of Sciences, 201818433. Also available from https://www.pnas.org/content/pnas/116/22/11069.full.pdf 
        2. Patel, M. K., Dumolard, L., Nedelec, Y., Sodha, S. V., Steulet, C., Gacic-Dobo, M., ... & Goodson, J. L. (2019). Progress toward regional measles elimination—worldwide, 2000–2018. Morbidity and Mortality Weekly Report, 68(48), 1105. Also available from https://www.cdc.gov/mmwr/volumes/68/wr/pdfs/mm6848a1-H.pdf 
        3. National Institute of Population Studies (NIPS) [Pakistan] and ICF. 2019. Pakistan Demographic and Health Survey 2017-18. Islamabad, Pakistan, and Rockville, Maryland, USA: NIPS and ICF. Also available from https://dhsprogram.com/pubs/pdf/FR354/FR354.pdf 
        4. Pakistan Bureau of Statistics. Block Wise Provisional Summary Results of 6th Population & Housing Census-2017 [As on January 03, 2018]. Also available from http://www.pbs.gov.pk/content/block-wise-provisional-summary-results-6th-population-housing-census-2017-january-03-2018 
        5. Centers for Disease Control and Prevention. Epidemiology and Prevention of Vaccine-Preventable Diseases. Chapter 10, Measles. 8th Edition, 2004. https://www.cdc.gov/vaccines/pubs/pinkbook/meas.html 
        """)

#elif choose == "Site Analytics":
    #st.header("Site Analytics")
    #with st.container():
      #with streamlit_analytics.track():
            #st.text_input("Enter something below if you'd like!", key="name_input", 
                      #help="Just type something!", 
                      #value="Type something here!", 
                      #max_chars=100, 
                      #type="default",
                      #)
            #st.markdown("""
            #<style>
                #/* Add custom CSS styles for the text input */
                ##name_input input[type=text] {
                    #background-color: #f2f2f2;
                    #border: none;
                    #padding: 8px;
                    #font-size: 16px;
                    #width: 100%;
                #}
            #</style>
            #""", unsafe_allow_html=True)
            #st.button("Click me!")
            #st.write("...and now add `?analytics=on` to the URL to see the analytics dashboard 👀")

elif choose == "Resume":   
    resume_url = "https://docs.google.com/document/d/0B0W0TfmuQjv7LUNEQV9MRENVVENiWmZZeVpKakt4VjNYMXpj/edit?resourcekey=0-ePV7xs6o32NsvMLrhdz3zw"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (1 page)**"), unsafe_allow_html=True)
    show_pdf("madhan.pdf")
    with open("madhan.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume (1 page)",
            data=file,
            file_name="madhan.pdf",
            mime="application/pdf"
        )
elif choose == "Contact":
# Create section for Contact
    #st.write("---")
    st.header("Contact")
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid, image_column = st.columns((1,0.2,0.5))
        with text_column:
            st.write("Let's connect! You may either reach out to me at connectmadhan01@gmail.com or use the form below!")
            #with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                #st.write('Please help us improve!')
                #Name=st.text_input(label='Your Name',
                                    #max_chars=100, type="default") #Collect user feedback
                #Email=st.text_input(label='Your Email', 
                                    #max_chars=100,type="default") #Collect user feedback
                #Message=st.text_input(label='Your Message',
                                        #max_chars=500, type="default") #Collect user feedback
                #submitted = st.form_submit_button('Submit')
                #if submitted:
                    #st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
            def create_database_and_table():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS contacts
                            (name TEXT, email TEXT, message TEXT)''')
                conn.commit()
                conn.close()
            create_database_and_table()

            st.subheader("Contact Form")
            if "name" not in st.session_state:
                st.session_state["name"] = ""
            if "email" not in st.session_state:
                st.session_state["email"] = ""
            if "message" not in st.session_state:
                st.session_state["message"] = ""
            st.session_state["name"] = st.text_input("Name", st.session_state["name"])
            st.session_state["email"] = st.text_input("Email", st.session_state["email"])
            st.session_state["message"] = st.text_area("Message", st.session_state["message"])


            column1, column2= st.columns([1,5])
            if column1.button("Submit"):
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                        (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
                conn.commit()
                conn.close()
                st.success("Your message has been sent!")
                # Clear the input fields
                st.session_state["name"] = ""
                st.session_state["email"] = ""
                st.session_state["message"] = ""
            def fetch_all_contacts():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("SELECT * FROM contacts")
                rows = c.fetchall()
                conn.close()
                return rows
            
            if "show_contacts" not in st.session_state:
                st.session_state["show_contacts"] = False
            if column2.button("View Submitted Forms"):
                st.session_state["show_contacts"] = not st.session_state["show_contacts"]
            
            if st.session_state["show_contacts"]:
                all_contacts = fetch_all_contacts()
                if len(all_contacts) > 0:
                    table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
                    table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
                    markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
                    st.markdown(markdown_table)
                else:
                    st.write("No contacts found.")


            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/madhan0102/"
            github_url = "https://github.com/Madhan0102"
            email_url = "mailto:connectmadhan01@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
            #st.write("© 2024 Madhan Kumar N")
            #st.write("[LinkedIn](https://www.linkedin.com/in/madhan0102/) | [Github](https://github.com/Madhan0102) | [Linktree]()")
        with mid:
            st.empty()
        with image_column:
            st.image(img_ifg)
st.markdown("*Copyright © 2024 Madhan Kumar N*")

