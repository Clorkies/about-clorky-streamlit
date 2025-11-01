from pathlib import Path

import streamlit as st
from PIL import Image

curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
main_css = curr_dir / "styles" / "main.css"
resume_file = curr_dir / "assets" / "Resume.pdf"
profile_pic = curr_dir / "assets" / "Modequillo_Formal_Cropped.png"
landscape_pic = curr_dir / "assets" / "Modequillo_Formal-Pic_Landscape.png"
grad_pic = curr_dir / "assets" / "Grad_pic.jpg"
hackathon_pic = curr_dir / "assets" / "Hackathon_pic.jpg"
pic_23 = curr_dir / "assets" / "img_23.jpg"
pic_20 = curr_dir / "assets" / "img_20.jpg"

#--- GENERAL SETTINGS ---
PAGE_TITLE = "About Clorky"
PAGE_ICON = "📋"

NAME = "Clark Modequillo"
FULL_NAME = "Clark Vincent A. Modequillo"
JOB_TITLE = "Graphic Designer / BS Computer Science Student"

EMAIL = "clarkvincent.modequillo@cit.edu"
PHONE = "+63 999 111 5655"

PROFILE_SUMMARY = (
    "<p>Creative and detail-oriented learner with experience in graphic design, "
    "layout artistry, and creative direction, currently pursuing a BS in Computer Science. "
    "Proven ability to manage end-to-end creative processes, mentor junior staff, and "
    "deliver high-quality publication materials for both academic and freelance clients.</p>"
)

AUTOBIOGRAPHY = (
    "<h3>Early Life</h3>"
    "<p>I was born and raised in Cogon Pardo, Cebu City, where I developed an early interest in both art and technology. "
    "From a young age, I was fascinated by computers and graphic design, spending hours exploring creative software, such as MS Paint and Gimp "
    "and learning how technology could enhance artistic expression.</p>"
    
    "<h3>Education Journey</h3>"
    "<p>My academic journey began at Pardo Elementary School, I then graduated and went to Talisay City Science High School, where I excelled in both scientific and creative subjects. "
    "This dual interest led me to pursue TVL ICT at University of San Jose-Recoletos, where I honed my technical skills "
    "while continuing to develop my design abilities.</p>"
    
    "<p>Currently, I'm pursuing a BS in Computer Science at Cebu Institute of Technology-University, where I'm combining "
    "my passions for technology and creativity.</p>"
    
    "<h3>Professional Development</h3>"
    "<p>My professional journey in design began with freelance work, creating custom graphics for various clients. "
    "This experience helped me develop a portfolio that eventually led to positions with The Josenian Premier, "
    "where I progressed from an Associate Creative Director to Creative Director.</p>"
    
    "<p>These roles allowed me to oversee creative processes, mentor junior staff, and develop consistent design systems "
    "that enhanced brand recognition and visual storytelling.</p>"
    
    "<h3>Personal Philosophy</h3>"
    "<p>I believe in the power of combining technical precision with creative vision. My dual background in computer science "
    "and graphic design gives me a unique perspective on problem-solving and creative expression.</p>"
    
    "<p>I'm passionate about creating designs that not only look appealing but also communicate effectively and serve a clear purpose. "
    "This philosophy guides my approach to both academic and professional projects.</p>"
    
    "<h3>Future Goals</h3>"
    "<p>Looking forward, I aim to leverage my computer science education to explore innovative ways technology can enhance "
    "design processes and outcomes. I'm particularly interested in areas where programming and creative design intersect, "
    "such as interactive media, web design, and digital art tools.</p>"
    
    "<p>I hope to continue growing both technically and creatively, eventually bringing these skills together in ways that "
    "push boundaries and create meaningful experiences.</p>"
)

SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/clorkies",
    "Instagram": "https://www.instagram.com/clorkies",
    "LinkedIn": "https://www.linkedin.com/in/clark-modequillo-35a8b3206/",
    "GitHub": "https://github.com/Clorkies"
}

SKILLS = {
    "Design Software": [
        "Adobe Photoshop",
        "Adobe Illustrator",
        "Adobe InDesign",
        "Figma",
        "Canva",
        "Adobe After Effects"
    ],
    "Professional Skills": [
        "Collaboration",
        "Typography",
        "Teamwork",
        "Creative Direction",
        "Layout Design",
        "Branding Consistency"
    ],
    "Technical Skills": [
        "C/C++", 
        "Java", 
        "Python", 
        "HTML", 
        "CSS", 
        "JavaScript", 
        "Version Control",
        "Data Structures and Algorithms"
    ],
    "Certifications": [
        "CodeChum C Certification",
        "CodeChum Java Certification",
        "Canva Certification",
        "TechMahindra Internship Completion Certificate"
    ]
}

EDUCATION = [
    {
        "degree": "BS Computer Science",
        "institution": "Cebu Institute of Technology-University",
        "years": "2023-2027",
        "details": "Current student."
    },
    {
        "degree": "Senior High School - TVL ICT",
        "institution": "University of San Jose-Recoletos",
        "years": "2021-2023",
        "details": ""
    },
    {
        "degree": "High School Diploma",
        "institution": "Talisay City Science High School",
        "years": "2017-2021",
        "details": ""
    },
]

EXPERIENCE = [
    {
        "position": "Creative Director",
        "company": "The Josenian Premier (Official School Publication)",
        "years": "2022-2023",
        "description": [
            "Oversaw the entire creative process for school publication materials (magazines, newsletters, layouts, videos).",
            "Developed and implemented consistent color schemes and layout styles to ensure brand alignment.",
            "Directed and mentored creative teams, monitoring progress and ensuring adherence to deadlines and standards.",
            "Evaluated and approved final designs before publication."
        ]
    },
    {
        "position": "Associate Creative Director",
        "company": "The Josenian Premier",
        "years": "2021-2022",
        "description": [
            "Corrected layout errors and ensured consistent design quality and branding adherence across publications.",
            "Created layouts for school magazines, newsletters, and promotional materials.",
            "Contributed to the creative direction and aesthetic vision through brainstorming sessions.",
            "Supported junior designers with guidance on layout techniques."
        ]
    },
    {
        "position": "Freelance Graphic Designer",
        "company": "Clark Visuals",
        "years": "2020-2022",
        "description": [
            "Designed custom shirt graphics, YouTube thumbnails, and corporate/esports logos for various clients.",
            "Developed publication material (pubmat) layouts."
        ]
    },
    {
        "position": "Social Media Manager - Layout Artist",
        "company": "Basilica Minore Del Santo Niño 2023 Media Volunteer",
        "years": "2022-2023",
        "description": [
            "Managed postings and updates during Sinulog 2023 in collaboration with other managers.",
            "Designed post templates and curated photos to enhance visual storytelling and branding consistency."
        ]
    },
]

PROJECTS = [
    {
        "title": "THE JOSENIAN PREMIER MAGAZINE - VOLUME 7, ISSUE 1 (Creative Director)",
        "description": "Led the creative direction for the university's official magazine, supervising layout design, graphics, and overall visual aesthetics. Managed a team of designers to deliver a cohesive publication."
    },
    {
        "title": "THE JOSENIAN PREMIER MAGAZINE - VOLUME 6, ISSUE 2 (Associate Creative Director)",
        "description": "Assisted in creative direction and handled quality control for the magazine's previous issue, ensuring design consistency and visual appeal throughout the publication."
    },
    {
        "title": "THE JOSENIAN PREMIER NEWSLETTER - ACADEMIC YEAR 2022-2023 (Associate Creative Director)",
        "description": "Oversaw the layout and design of regular newsletters, creating templates and ensuring information was presented in a clear and visually engaging format."
    },
    {
        "title": "USJ-R SHS TVL DAYS - BYAHE TA ΒΑΙ (Lead Layout Artist)",
        "description": "Designed comprehensive layout materials for the school's special event, creating cohesive visual identity across various promotional materials."
    },
    {
        "title": "USJ-R SHS DAYS 2023 (Layout Artist)",
        "description": "Created promotional materials and event graphics for the high school's annual celebration, focusing on engaging visuals that resonated with students."
    },
]

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# Load CSS and Assets
with open(main_css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_image = Image.open(profile_pic)
landscape_image = Image.open(landscape_pic)
grad_image = Image.open(grad_pic)
hackathon_image = Image.open(hackathon_pic)
social_icons = {
    "Facebook": "📘",
    "Instagram": "📸",
    "LinkedIn": "🔗",
    "GitHub": "💻",
}


# --- HERO SECTION ---
st.markdown(f"""
<h1 style="text-align: center; font-size: 10rem; color: white; 
           margin-top: -2rem; margin-bottom: 20px; border-bottom: none;">
    {PAGE_TITLE}
</h1>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown('<div class="bio-image-column">', unsafe_allow_html=True)
    st.image(profile_image, use_container_width=True)
    st.image(grad_image, use_container_width=True)
    st.image(hackathon_image, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
 
with col2:
    st.markdown('<div class="bio-content-column">', unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-header">My Journey</div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="biography-content">
        {AUTOBIOGRAPHY}
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# Portfolio section
st.markdown("<h1 class='centered-header'>Portfolio</h1>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    st.image(landscape_image, width=463)
    
with col2:
    st.write("📫", EMAIL)
    st.write("📞", PHONE)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        icon = social_icons.get(platform, "🌐") 
        cols[index].markdown(
            f"""
            <div class="social-icon-container">
                <a href="{link}" target="_blank" class="social-icon">
                    <div class="icon-box">{icon}</div>
                    <span>{platform}</span>
                </a>
            </div>
            """, 
            unsafe_allow_html=True
        )

st.write("# Profile Summary")

st.markdown(f"""
<div class="profile-summary">
    {PROFILE_SUMMARY}
</div>
""", unsafe_allow_html=True)

# --- SKILLS ---
st.write("# Skills")
tabs = st.tabs(list(SKILLS.keys()))
for i, (category, skills_list) in enumerate(SKILLS.items()):
    with tabs[i]:
        num_cols = min(3, len(skills_list))
        if num_cols == 0:
            continue
            
        skills_per_col = -(-len(skills_list) // num_cols)  # Ceiling division
        cols = st.columns(num_cols)
        
        for col_idx in range(num_cols):
            with cols[col_idx]:
                start_idx = col_idx * skills_per_col
                end_idx = min(start_idx + skills_per_col, len(skills_list))
                for skill in skills_list[start_idx:end_idx]:
                    st.markdown(f"- **{skill}**")

st.write("# Education")
for edu in EDUCATION:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader(edu['degree'])
        st.write(f"**{edu['institution']}**")
        if edu['details']:
            st.write(edu['details'])
    with col2:
        st.write(f"**{edu['years']}**")
    st.divider()

# --- EXPERIENCE ---
st.write("# Experience")
for exp in EXPERIENCE:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader(exp['position'])
        st.write(f"**{exp['company']}**")
    with col2:
        st.write(f"**{exp['years']}**")
    
    with st.container():
        for item in exp['description']:
            st.markdown(f"- {item}")
    st.divider()

st.write("# Projects")

st.markdown("<h2 class='centered-subheader'>Portfolio Highlights</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)  
with col1:
    st.image(pic_20, use_container_width=True) 
with col2:
    st.image(pic_23, use_container_width=True) 

for i, project in enumerate(PROJECTS):
    with st.expander(f"Project {i+1}: {project['title']}"):
        st.markdown(f"### {project['title']}")
        st.markdown("---")
        
        st.markdown(project['description'])
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write("**Type:** Design Project")
        with col2:
            if 'details' in project:
                st.write(project['details'])

# --- FOOTER ---
st.divider()
st.write("### Thank You For Visiting!")
footer_cols = st.columns([1, 1, 1])
with footer_cols[0]:
    st.write("📞 Contact")
    st.write(f"[{PHONE}](tel:{PHONE.replace(' ', '')})")
    st.write(f"[{EMAIL}](mailto:{EMAIL})")
with footer_cols[1]:
    st.write("🔗 Connect")
    for platform, link in SOCIAL_MEDIA.items():
        icon = social_icons.get(platform, "🌐")
        st.markdown(f"<a href='{link}' target='_blank' class='footer-social-link'>{icon} {platform}</a>", unsafe_allow_html=True)
with footer_cols[2]:
    st.write("📄 Resources")
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(f"© {NAME} | {JOB_TITLE}")