import streamlit as st
import sqlite3
import os
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="my webapp", layout="wide")
##deploy hide
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {
    padding-top: 0rem !important;
    margin-top: -20px;   /*  pulls everything upward */
    padding-left: 20px !important;
    padding-right: 20px !important;
}

.stVerticalBlock{background-color:#ffffff!important;}

</style>
""", unsafe_allow_html=True)

# ================= DATABASE =================
conn = sqlite3.connect("portal.db", check_same_thread=False)
cursor = conn.cursor()

#cursor.execute("DELETE FROM ui_components WHERE name='navbar' AND type='css'")
#conn.commit()

#cursor.execute("DELETE FROM ui_components WHERE name='navbar' AND type='html'")
#conn.commit()



cursor.execute("""
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image BLOB
)
""")
conn.commit()
cursor.execute("""
CREATE TABLE IF NOT EXISTS navbar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    option1 TEXT,
    option2 TEXT
)
""")
conn.commit()
# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS ui_components (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    content TEXT
)
""")
conn.commit()


# INSERT MENU DATA (ONLY ONCE)
cursor.execute("SELECT COUNT(*) FROM navbar")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("INSERT INTO navbar (name, option1, option2) VALUES (?, ?, ?)", 
                   ("Home", "Overview", "Updates"))
    cursor.execute("INSERT INTO navbar (name, option1, option2) VALUES (?, ?, ?)", 
                   ("About Us", "Our Story", "Team"))
    cursor.execute("INSERT INTO navbar (name, option1, option2) VALUES (?, ?, ?)", 
                   ("Career", "Jobs", "Internships"))
    cursor.execute("INSERT INTO navbar (name, option1, option2) VALUES (?, ?, ?)", 
                   ("Resources", "Case Studies", "Downloads"))
    cursor.execute("INSERT INTO navbar (name, option1, option2) VALUES (?, ?, ?)", 
                   ("Blog", "Latest Posts", "News"))
    conn.commit()

######### NEW TABLE FOR HTML###############
# ================= NAVBAR HTML =================

cursor.execute("SELECT COUNT(*) FROM ui_components WHERE name='navbar' AND type='html'")
count = cursor.fetchone()[0]

if count == 0:
    #  FIRST TIME INSERT
    cursor.execute("""
    INSERT INTO ui_components (name, type, content)
    VALUES (?, ?, ?)
    """, ("navbar", "html", """

<!--  NEW DROPDOWN HTML -->
<div class="navbar">

    <div class="navbar-left">
        <img class="logo" src="data:image/webp;base64,__LOGO__">
    </div>

    <div class="navbar-center">

        <div class="menu-item">
            <span>Home</span>
            <span class="arrow" onclick="toggleDropdown('home')"></span>
            <div id="home" class="dropdown-content">
                <a href="#">Overview</a>
                <a href="#">Updates</a>
            </div>
        </div>

        <div class="menu-item">
            <span>About Us</span>
            <span class="arrow" onclick="toggleDropdown('about')"></span>
            <div id="about" class="dropdown-content">
                <a href="#">Our Story</a>
                <a href="#">Team</a>
            </div>
        </div>

        <div class="menu-item">
            <span>Career</span>
            <span class="arrow" onclick="toggleDropdown('career')"></span>
            <div id="career" class="dropdown-content">
                <a href="#">Jobs</a>
                <a href="#">Internships</a>
            </div>
        </div>

        <div class="menu-item">
            <span>Resources</span>
            <span class="arrow" onclick="toggleDropdown('resources')"></span>
            <div id="resources" class="dropdown-content">
                <a href="#">Case Studies</a>
                <a href="#">Downloads</a>
            </div>
        </div>

        <div class="menu-item">
            <span>Blog</span>
            <span class="arrow" onclick="toggleDropdown('blog')"></span>
            <div id="blog" class="dropdown-content">
                <a href="#">Latest Posts</a>
                <a href="#">News</a>
            </div>
        </div>

    </div>

 <div class="navbar-right">
    <span class="search-icon">🔍︎</span>
    <a class="login-btn" href="#">Login</a>
    <a class="contact-btn" href="#">Get in Touch</a>
</div>   

</div>

"""))
    conn.commit()

# ================= INSERT NAVBAR CSS =================
cursor.execute("SELECT COUNT(*) FROM ui_components WHERE name='navbar' AND type='css'")
count = cursor.fetchone()[0]

if count == 0:     
    cursor.execute("""
    INSERT INTO ui_components (name, type, content)
    VALUES (?, ?, ?)
    """, ("navbar", "css", """
<style>
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #f8f8f8;   /* back to light */
    padding: 10px 25px;
    font-family: sans-serif;
    color: black;          /*  text back to black */
}

.navbar-left {
    flex: 1;
}

.navbar-center {
    flex: 2;
    display: flex;
    justify-content: center;
    gap: 25px;
    align-items: center;
}

.navbar-right {
    flex: 1;
    display: flex;
    justify-content: flex-end;
    gap: 10px;
}

.logo {
    height: 65px;
}

/* MENU */
    .menu-item {
    position: relative;
    cursor: pointer;
    padding: 5px 0;
}
.menu-item:hover .dropdown-content {
    display: block;
}



/* DROPDOWN */
.dropdown-content {
    display: none;
    position: absolute;
    top: 100%;   /*  CHANGE from 35px */
    left: 0;
    background: white;
    color: black;
    min-width: 150px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    border-radius: 5px;
    z-index: 9999;
}



.dropdown-content a {
    display: block;
    padding: 10px;
    text-decoration: none;
    color: black;
}

.dropdown-content a:hover {
    background: #f2f2f2;
}

/*  ARROW FIX */
.arrow {
    display: inline-block;
    margin-left: 6px;
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid black;   /*  FIX */
    cursor: pointer;
}


/* BUTTONS - MODERN */
.login-btn,
.contact-btn {
    display: inline-block;
    padding: 10px 22px;
    font-size: 15px;
    font-weight: 600;
    border-radius: 8px;
    text-decoration: none !important;
    border: none;
    transition: all 0.3s ease;
}

.search-icon {
    font-size: 20px;   /*  bigger */
    cursor: pointer;
    margin-right: 6px;
}



/* LOGIN BUTTON */
.login-btn {
    background: white;
    color: #002366;
    border: 1px solid #002366;
}

.login-btn:hover {
    background: #002366;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    text-decoration: none !important;
}

/* CONTACT BUTTON */
.contact-btn {
    background: linear-gradient(135deg, #ff8c00, #ff5e00);
    color: white;
}

.contact-btn:hover {
    background: linear-gradient(135deg, #ff5e00, #ff8c00);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    text-decoration: none !important;
}

/*  FORCE REMOVE UNDERLINE */
a {
    text-decoration: none !important;
}
</style>




"""))
    conn.commit()


# ================= INSERT NAVBAR JS =================
cursor.execute("SELECT COUNT(*) FROM ui_components WHERE name='navbar' AND type='js'")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("""
    INSERT INTO ui_components (name, type, content)
    VALUES (?, ?, ?)
    """, ("navbar", "js", """
<script>
function toggleDropdown(id) {

    var all = document.getElementsByClassName("dropdown-content");

    for (var i = 0; i < all.length; i++) {
        if (all[i].id !== id) {
            all[i].style.display = "none";
        }
    }

    var dropdown = document.getElementById(id);

    if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
    } else {
        dropdown.style.display = "block";
    }
}
</script>
"""))
    conn.commit()


def get_component(name, type_):
    cursor.execute(
        "SELECT content FROM ui_components WHERE name=? AND type=?",
        (name, type_)
    )
    result = cursor.fetchone()
    return result[0] if result else ""




# ================= INSERT IMAGES (ONLY ONCE) =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def insert_image(path):
    full_path = os.path.join(BASE_DIR, path)   #  FIXED PATH

    if os.path.exists(full_path):
        st.success(f" Found: {full_path}")
        with open(full_path, "rb") as f:
            cursor.execute("INSERT INTO images (image) VALUES (?)", (f.read(),))
    else:
        st.error(f"❌ Image not found: {full_path}")



# Insert only if empty
cursor.execute("SELECT COUNT(*) FROM images")
count = cursor.fetchone()[0]

##deploy hide

if count == 0:
    insert_image("images/header-logo.webp")
    insert_image("images/discover-section-img.webp")
    insert_image("images/ISO1.webp")
    insert_image("images/ISO2.webp")
    insert_image("images/ISO-9001-2015.webp")
    conn.commit()
cursor.execute("SELECT COUNT(*) FROM images")
count = cursor.fetchone()[0]

cursor.execute("SELECT id, length(image) FROM images")
rows = cursor.fetchall()




# ================= GET IMAGES =================
def get_images():
    cursor.execute("SELECT image FROM images ORDER BY id ASC")
    return cursor.fetchall()

# ================= NAVBAR =================
# ================= NAVBAR =================
# ================= NAVBAR =================
images = get_images()

logo_base64 = ""

html_part = get_component("navbar", "html")
css_part = get_component("navbar", "css")
js_part = get_component("navbar", "js")

full_code = css_part + html_part + js_part

if len(images) > 0:
    logo_base64 = base64.b64encode(images[0][0]).decode()
    full_code = full_code.replace("__LOGO__", logo_base64)

components.html(full_code, height=140)




######  PAGE CONTENT
st.markdown("""
<div style="
    margin-top:-32px;
    padding-left:25px;   /* MATCH NAVBAR */
    width:100%;
    font-size:52px;
    font-family: Georgia, serif;
    font-weight:700;
    color:#002366;
    line-height:1.3;
">
    Constructing Certinity with BIM Technology
</div>
""", unsafe_allow_html=True)







video_url = "https://res.cloudinary.com/dnodncslz/video/upload/v1774435343/pinnacle-infotech-latest_h3qbk3.mp4"

components.html(f"""
<div style="
    width:100%;
    padding-left:25px;   /*  MATCH NAVBAR */
    padding-right:25px;  /*  MATCH RIGHT SIDE */
    margin-top:20px;
">

    <video autoplay muted loop playsinline 
        style="
            width:100%;
            height:auto;
            border-radius:12px;
        ">
        <source src="{video_url}" type="video/mp4">
    </video>

</div>
""", height=520)




# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
def to_base64(img):
    return base64.b64encode(img).decode()

images = get_images()

main_img = iso1 = iso2 = iso3 = ""

if len(images) >= 5:
    main_img = to_base64(images[1][0])
    iso1 = to_base64(images[2][0])
    iso2 = to_base64(images[3][0])
    iso3 = to_base64(images[4][0])






html = f"""
<div style='
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:30px;
    margin-top:60px;
    width:100%;
'>

    <!-- LEFT TEXT -->
    <div style="width:50%; margin-left:30px;">

        <h2 style='color:#002366; font-size:34px; font-weight:700;'>
            Discover Pinnacle
        </h2>

        <p style="font-size:22px; line-height:1.8; margin-bottom:20px;color:#2a4d8f;">
Pinnacle is your gateway to innovative solutions and transformative experiences. We specialize in delivering excellence across technology, design, and strategy.
</p>

<p style='font-size:16px; line-height:1.7;'>
Our 30+ years of expertise drive excellence in the Design, Preconstruction, Construction Management, Digital Twin, and Facilities Management.
</p>


       


<a href="#" style="
    display:inline-flex;
    align-items:center;
    gap:12px;
    background:#002366;
    color:white;
    padding:12px 24px;
    border-radius:50px;
    text-decoration:none;
    margin-top:25px;
    font-size:16px;
    font-weight:600;
">

    Know More

    <span style="
        display:flex;
        align-items:center;
        justify-content:center;
        width:30px;
        height:30px;
        background:white;
        border-radius:50%;
        color:#002366;   /*  BLUE arrow */
        font-size:16px;
        font-weight:bold;
    ">
        →
    </span>

</a>


    </div>

    <!-- RIGHT IMAGE -->
    <div style='width:55%; position:relative;'>

        <img src='data:image/webp;base64,{main_img}'
             style='width:100%; height:420px; object-fit:cover; border-radius:12px;' />

        <div style='
            position:absolute;
            bottom:70px;
            left:40px;
            background:white;
            padding:15px 25px;
            border-radius:10px;
            display:flex;
            gap:20px;
            box-shadow:0 6px 15px rgba(0,0,0,0.2);
        '>

            <img src='data:image/webp;base64,{iso1}' style='height:60px;'>
            <img src='data:image/webp;base64,{iso2}' style='height:60px;'>
            <img src='data:image/webp;base64,{iso3}' style='height:60px;'>

        </div>

    </div>

</div>
"""

components.html(html, height=520)



# ================= MOVING IMAGE BAR =================


#  MOVING IMAGE BAR (PUT HERE)
components.html("""
<div style="
    width:100%;
    background:#e0e0e0;
    border-radius:12px;
    margin:60px 0;
    position:relative;
    box-shadow:0 8px 20px rgba(0,0,0,0.1);
    padding:40px 25px 40px 25px;   /*  SAME LEFT PADDING */
">

    <!--  TITLE -->
    <div style="
        position:absolute;
        top:20px;
        left:25px;   /* SAME AS PADDING */
        font-size:24px;
        font-weight:700;
        color:#002366;
        font-family: Georgia, serif;
    ">
        Industry Associations
    </div>

    <!--  LOGO ALIGNMENT -->
    <div style="
        width:100%;
        height:110px;
        display:flex;
        align-items:center;
        overflow:hidden;
    ">

        <!-- MOVING LOGOS -->
        <div style="
            display:flex;
            align-items:center;
            gap:80px;
            animation: scroll 15s linear infinite;
        ">

            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

            <!-- repeat -->
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

        </div>

    </div>

</div>

<style>
@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
</style>
""", height=260)

st.markdown("""
<div style="
    width:100%;
    text-align:center;
    margin-top:60px;
    font-size:34px;
    font-family: Georgia, serif;
    font-weight:700;
    color:#002366;
">
    What We Do
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    width:100%;
    text-align:center;
    margin-top:10px;
    font-size:20px;
    font-family:sans-serif;
    color:#4a6fa5;   /*  light dark blue */
">
    Adhering to international construction codes and standards, our range of services includes the following.
""",unsafe_allow_html=True)


# ================= BIM SERVICES (NEW SECTION) =================

bim_image_url = "https://res.cloudinary.com/dnodncslz/image/upload/v1774604187/bim_services_pinnacle_infotech_2_zrp9oc.webp"  # 🔥 replace with your image
# ================= BIM SERVICES (3 COLUMN LAYOUT) =================

# ================= BIM SERVICES (3 COLUMN - BUTTON LEFT) =================
components.html(f"""
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">

<style>
.custom-btn {{
    display:inline-flex;
    align-items:center;
    gap:12px;
    background:#002366;
    color:white;
    padding:12px 26px;
    border-radius:50px;
    text-decoration:none;
    margin-top:25px;
    font-size:16px;
    font-weight:600;
    transition:0.3s;
}}
.custom-btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}}
</style>

<div style='
    display:flex;
    justify-content:center;
    align-items:center;
    gap:40px;
    margin:40px auto;
    width:100%;
    max-width:1200px;
    flex-wrap:wrap;
    padding:0 20px;
    box-sizing:border-box;
'>



    <!-- LEFT TEXT + BUTTON -->
    <div style='
    flex:1;
    min-width:280px;
    padding:10px 20px;
    box-sizing:border-box;
'>



        <div style='
            color:#4a6fa5;
            font-size:26px;
            font-weight:700;
            font-family: Georgia, serif;
            margin-bottom:15px;
        '>
            BIM Services
        </div>

        <p style='
            font-size:15px;
            line-height:1.6;
            color:#333;
            margin-bottom:20px;
        '>
        We provide intelligent BIM solutions that improve coordination,
        reduce risks, and enhance overall project efficiency.
        </p>

        <!-- CAPSULE BUTTON -->
        <a href="#" class="custom-btn">
            Know More
            <span style="
                display:flex;
                align-items:center;
                justify-content:center;
                width:30px;
                height:30px;
                background:white;
                border-radius:50%;
                color:#002366;
                font-size:16px;
                font-weight:bold;
            ">→</span>
        </a>

    </div>

    <!-- CENTER IMAGE -->
   
<!-- CENTER IMAGE -->
<!-- CENTER IMAGE -->
<div style="
    flex:1;
    min-width:280px;
    padding:10px 20px;
    box-sizing:border-box;
    display:flex;
    justify-content:center;
    align-items:center;
">

    <img src="{bim_image_url}" style="
        width:100%;
        max-width:320px;
        height:320px;
        object-fit:cover;
        border-radius:12px;
        display:block;
        margin:auto;
    "/>

</div>



    <!-- RIGHT SIDE WITH ICONS -->
    <div style="
    flex:1;
    min-width:280px;
    padding:10px 20px;
    box-sizing:border-box;
">



        <div style='font-size:17px; color:#333; font-weight:500;'>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-diagram-3-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Coordination & Collaboration
            </div>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-exclamation-triangle-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Risk Reduction
            </div>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-clock-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Time Efficiency
            </div>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-cpu-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Smart Modeling
            </div>

            <div style="display:flex; align-items:center;">
                <i class="bi bi-bar-chart-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Better Project Outcomes
            </div>

        </div>

    </div>

</div>

""", height=420)


# ================= ENGINEERING DESIGN SECTION =================

# ================= ENGINEERING DESIGN SECTION =================
# ================= ENGINEERING DESIGN (3 COLUMN) =================

eng_image_url = "https://res.cloudinary.com/dnodncslz/image/upload/v1774604330/engineering_design_pinnacle_infotech_lbnhpf.webp"

components.html(f"""
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">

<style>
.custom-btn {{
    display:inline-flex;
    align-items:center;
    gap:12px;
    background:#002366;
    color:white;
    padding:12px 26px;
    border-radius:50px;
    text-decoration:none;
    margin-top:25px;
    font-size:16px;
    font-weight:600;
    transition:0.3s;
}}
.custom-btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}}
</style>

<div style='
    display:flex;
    justify-content:center;
    align-items:stretch;
    gap:40px;
    margin:40px auto;
    width:100%;
    max-width:1200px;
    flex-wrap:wrap;
    padding:0 20px;
    box-sizing:border-box;
'>




    <!-- LEFT TEXT + BUTTON -->
<div style='
    flex:1;
    min-width:280px;
    padding:10px 20px;
    box-sizing:border-box;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:flex-start;
'>

    <div style='
        color:#4a6fa5;
        font-size:26px;
        font-weight:700;
        font-family: Georgia, serif;
        margin-bottom:15px;
    '>
        Engineering Design
    </div>

    <p style='
        font-size:15px;
        line-height:1.6;
        color:#333;
        margin-bottom:20px;
    '>
    We deliver innovative engineering design solutions with precision,
    ensuring efficiency and sustainability across all projects.
    </p>

    <a href="#" class="custom-btn">
        Know More
        <span style="
            display:flex;
            align-items:center;
            justify-content:center;
            width:30px;
            height:30px;
            background:white;
            border-radius:50%;
            color:#002366;
            font-size:16px;
            font-weight:bold;
        ">→</span>
    </a>

</div>    

<!-- CENTER IMAGE -->
<div style="
    flex:1;
    min-width:280px;
    padding:10px 20px;
    box-sizing:border-box;
    display:flex;
    justify-content:center;
    align-items:center;
">

    <img src="{eng_image_url}" style="
        width:100%;
        max-width:320px;
        height:320px;
        object-fit:cover;
        border-radius:12px;
        display:block;
        margin:auto;
    "/>

</div>




    <!-- RIGHT SIDE WITH ICONS -->
<div style="
    flex:1;
    min-width:280px;
    padding:10px 20px;
    box-sizing:border-box;
    display:flex;
    flex-direction:column;
    justify-content:center;
">






    <div style='font-size:16.5px; color:#333;'>

        <div style="display:flex; align-items:center; margin-bottom:12px;">
            <i class="bi bi-rulers" style="color:#002366; margin-right:10px; font-size:19px;"></i>
            Precision Engineering
        </div>

        <div style="display:flex; align-items:center; margin-bottom:12px;">
            <i class="bi bi-lightbulb-fill" style="color:#002366; margin-right:10px; font-size:19px;"></i>
            Innovative Solutions
        </div>

        <div style="display:flex; align-items:center; margin-bottom:12px;">
            <i class="bi bi-speedometer2" style="color:#002366; margin-right:10px; font-size:19px;"></i>
            High Performance
        </div>

        <div style="display:flex; align-items:center; margin-bottom:12px;">
            <i class="bi bi-globe" style="color:#002366; margin-right:10px; font-size:19px;"></i>
            Sustainable Design
        </div>

        <div style="display:flex; align-items:center;">
            <i class="bi bi-gear-fill" style="color:#002366; margin-right:10px; font-size:19px;"></i>
            Advanced Tools
        </div>

    </div>

</div>   



""", height=420)
   





 # ================= DIGITAL CONSTRUCTION SECTION =================

digital_image_url = "https://res.cloudinary.com/dnodncslz/image/upload/v1774604275/digital_construction_pinnacle_infotech_mxz5kc.webp"

# ================= DIGITAL CONSTRUCTION (3 COLUMN) =================

# ================= DIGITAL CONSTRUCTION SECTION =================



components.html(f"""
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">

<style>
.custom-btn {{
    display:flex;
    align-items:center;
    gap:12px;
    background:#002366;
    color:white;
    padding:12px 22px;
    border-radius:50px;
    text-decoration:none;
    margin-top:25px;
    font-size:16px;
    font-weight:600;
    transition:0.3s;
    width:fit-content;
}}

.custom-btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(0,0,0,0.18);
}}
</style>

<div style='
    display:flex;
    justify-content:center;
    align-items:stretch;
    gap:40px;
    margin:40px auto;
    width:100%;
    max-width:1200px;
    flex-wrap:wrap;
    padding:0 20px;
    box-sizing:border-box;
'>

    <!-- LEFT TEXT + BUTTON -->
    <div style='
        flex:1;
        min-width:280px;
        padding:10px 20px;
        box-sizing:border-box;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:flex-start;
    '>

        <div style='
            color:#4a6fa5;
            font-size:26px;
            font-weight:700;
            font-family: Georgia, serif;
            margin-bottom:15px;
        '>
            Digital Construction
        </div>

        <p style='
            font-size:15px;
            line-height:1.6;
            color:#333;
            margin-bottom:20px;
        '>
        Our digital construction approach enhances visualization, planning,
        and execution through advanced technologies and smart workflows.
        </p>

        <a href="#" class="custom-btn">
            Know More
            <span style="
                display:flex;
                align-items:center;
                justify-content:center;
                width:30px;
                height:30px;
                background:white;
                border-radius:50%;
                color:#002366;
                font-size:16px;
                font-weight:bold;
            ">→</span>
        </a>

    </div>

    <!-- CENTER IMAGE -->
    <div style="
        flex:1;
        min-width:280px;
        padding:10px 20px;
        box-sizing:border-box;
        display:flex;
        justify-content:center;
        align-items:center;
    ">

        <img src="{digital_image_url}" style="
            width:100%;
            max-width:320px;
            height:320px;
            object-fit:cover;
            border-radius:12px;
            display:block;
            margin:auto;
        "/>

    </div>

    <!-- RIGHT SIDE -->
    <div style="
        flex:1;
        min-width:280px;
        padding:10px 20px;
        box-sizing:border-box;
        display:flex;
        flex-direction:column;
        justify-content:center;
    ">

        <div style='font-size:17px; color:#333; font-weight:500;'>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-box-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                3D Modelling
            </div>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-building" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Architectural
            </div>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-megaphone-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Marketing / BID Presentation
            </div>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-map-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                GIS
            </div>

            <div style="display:flex; align-items:center;">
                <i class="bi bi-file-earmark-text-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Documentation
            </div>

        </div>

    </div>

</div>

""", height=420)
















###### DIGITAL TWIN
digital_twin_image_url =" https://res.cloudinary.com/dnodncslz/image/upload/v1775560726/bim-vdc_consulting_pinnacle_infotech_xovez5.webp"
###### DIGITAL TWIN



components.html(f"""
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">

<style>
.custom-btn {{
    display:flex;
    align-items:center;
    gap:12px;
    background:#002366;
    color:white;
    padding:12px 22px;
    border-radius:50px;
    text-decoration:none;
    margin-top:25px;
    font-size:16px;
    font-weight:600;
    transition:0.3s;
    width:fit-content;
}}

.custom-btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(0,0,0,0.18);
}}
</style>

<div style='
    display:flex;
    justify-content:center;
    align-items:stretch;
    gap:40px;
    margin:40px auto;
    width:100%;
    max-width:1200px;
    flex-wrap:wrap;
    padding:0 20px;
    box-sizing:border-box;
'>

    <!-- LEFT TEXT + BUTTON -->
    <div style='
        flex:1;
        min-width:280px;
        padding:10px 20px;
        box-sizing:border-box;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:flex-start;
    '>

        <div style='
            color:#4a6fa5;
            font-size:26px;
            font-weight:700;
            font-family: Georgia, serif;
            margin-bottom:15px;
        '>
            Digital Twin
        </div>

        <p style='
            font-size:15px;
            line-height:1.6;
            color:#333;
            margin-bottom:20px;
        '>
        Our Digital Twin solutions create real-time virtual replicas of
        physical assets, enabling better monitoring, analysis, and
        decision-making throughout the project lifecycle.
        </p>

        <a href="#" class="custom-btn">
            Know More
            <span style="
                display:flex;
                align-items:center;
                justify-content:center;
                width:30px;
                height:30px;
                background:white;
                border-radius:50%;
                color:#002366;
                font-size:16px;
                font-weight:bold;
            ">→</span>
        </a>

    </div>

    <!-- CENTER IMAGE -->
    <div style="
        flex:1;
        min-width:280px;
        padding:10px 20px;
        box-sizing:border-box;
        display:flex;
        justify-content:center;
        align-items:center;
    ">

        <img src="{digital_twin_image_url}" style="
            width:100%;
            max-width:320px;
            height:320px;
            object-fit:cover;
            border-radius:12px;
            display:block;
            margin:auto;
        "/>

    </div>

    <!-- RIGHT SIDE ICONS -->
    <div style="
        flex:1;
        min-width:280px;
        padding:10px 20px;
        box-sizing:border-box;
        display:flex;
        flex-direction:column;
        justify-content:center;
    ">

        <div style='font-size:17px; color:#333; font-weight:500;'>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-cpu-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Real-Time Monitoring
            </div>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-diagram-3-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Data Integration
            </div>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-graph-up-arrow" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Performance Analysis
            </div>

            <div style="display:flex; align-items:center; margin-bottom:14px;">
                <i class="bi bi-tools" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Predictive Maintenance
            </div>

            <div style="display:flex; align-items:center;">
                <i class="bi bi-eye-fill" style="color:#002366; margin-right:12px; font-size:21px;"></i>
                Enhanced Visualization
            </div>

        </div>

    </div>

</div>

""", height=420)










































































































































#### our####
components.html("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">

<style>
.vertical-section {
    position: relative;
    padding: 25px 0;
    margin-bottom: 20px;
    height: 120px;        /* fixed height */
    overflow: hidden;
    border-radius: 12px;
    transition: background 0.5s ease;
    overflow: visible; 
}

/* blue bar appears with pseudo-element */



.vertical-section::before {
    content: "";
    position: absolute;

    left: -30px;
    right: -30px;

    top: 50%;
    height: 80%;  /* smaller initially */

    transform: translateY(-50%) scaleY(0.8);  /*  center-based */
    transform-origin: center;

    background: linear-gradient(90deg, #2c3e66, #5a7fcf);

    opacity: 0;
    transition: all 0.4s ease;

    border-radius: 20px;
    z-index: 1;
}

.vertical-section:hover::before {
    opacity: 1;
    transform: translateY(-50%) scaleY(1.5);  /*  expands BOTH up & down */
    box-shadow: 0 20px 50px rgba(44, 62, 102, 0.35);
}


   /*  keeps it clean inside */
.vertical-section {
    overflow: visible;   /* MUST */
}
.vertical-content, .title {
    position: relative;
    z-index: 5;
}



.vertical-content {
    overflow: visible;
}




/* hide content initially */
.vertical-content {
    display: flex;
    align-items: center;
    gap: 40px;

    position: absolute;
    right: 100px; 
    top: 50%;
    transform: translateY(-50%) translateX(0);

    opacity: 0;
    visibility: hidden;

    transition: all 0.4s ease;
}
.title span:last-child {
    letter-spacing: 0.5px;
    opacity: 0.85;
}




/* show content on hover */
.vertical-section:hover .vertical-content {
    opacity: 1;
    visibility: visible;
    transform: translateY(-50%) translateX(0);
}

.vertical-content img {
    position: relative;
    z-index: 6;   /*  topmost */
}



/* hover trigger */
.vertical-section:hover .vertical-content img {
    opacity: 1;
    transform: translateX(0);
    animation: imgSwingOnce 0.8s ease-out;
}

/* ONE-TIME LEFT-RIGHT SWING */
@keyframes imgSwingOnce {
    0%   { transform: translateX(0px) rotate(0deg); }
    25%  { transform: translateX(0px) rotate(-4deg); }
    60%  { transform: translateX(0px) rotate(3deg); }
    100% { transform: translateX(0px) rotate(0deg); }
}

/* Airport icon + text becomes white on hover */
.vertical-section:hover .title {
    color: white !important;
}

/* icon specifically */
.vertical-section:hover .title i {
    color: white !important;
}



/* divider line */

.vertical-section::after {
    content: "";
    position: absolute;
    left: 40px;
    right: 40px;
    bottom: 0;
    height: 0.5px;
    background: rgba(0,0,0,0.15);
    z-index: 0;
    transition: opacity 0.3s ease;
}



/* make icon white on hover */
.vertical-section:hover .title i {
    color: white !important;
    transition: color 0.3s ease;
}
/* make icon white on hover */
.vertical-section:hover .title i {
    color: white !important;
    transition: color 0.3s ease;
}

.vertical-row {
    display: flex;
    align-items: center;
    gap: 60px;
    padding-left: 80px;   /* increase a bit for balance */
}

.vertical-section:hover .title span:last-child {
    color: white !important;
    transition: color 0.3s ease;
}
.sub-text {
    font-size: 18px;
    font-weight: 400;
    color: #4a6fa5;
    line-height: 1.5;
    opacity: 0;
    visibility: hidden;
    transform: translateY(6px);

    height: 0;
    overflow: hidden;

    transition: all 0.3s ease;
}

/* show only on hover */
.vertical-section:hover .sub-text {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);

    height: auto;
    color: white !important;
}
.vertical-section {
    display: flex;
    align-items: center;
}

.vertical-section:hover::after {
    opacity: 0;   /*  hides line smoothly */
}

.vertical-content img {
    height: 240px;   /* set once → applies everywhere */
}

.custom-btn {
    display: inline-flex;
    align-items: center;
    gap: 12px;

    padding: 12px 26px;
    background: #002366;
    color: white;
    text-decoration: none;

    border-radius: 50px;
    font-size: 16px;
    font-weight: 600;

    transition: all 0.3s ease;
}

/* SIMPLE HOVER */
.custom-btn:hover {
    background: #1a3d8f;   /* slightly lighter blue */
    transform: translateY(-3px);   /* slight lift */
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}

/* ARROW MOVE */
.custom-btn span {
    transition: transform 0.3s ease;
}

.custom-btn:hover span {
    transform: translateX(4px);
}

.expand-icon {
    position: absolute;
    right: 60px;
    top: 50%;
    transform: translateY(-50%) translateX(-10px);

    width: 56px;   /* ⬅ bigger circle */
    height: 56px;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #e6e6e6;
    color: #002366;

    font-size: 26px;   /* ⬅ bigger arrow */

    font-weight: bold;

    z-index: 10;

    transition: all 0.3s ease;
}


/* HOVER STATE */
.vertical-section:hover .expand-icon {
    background: rgba(255, 255, 255, 0.2); 
    
    color: #ffffff;
    transform: translateY(-50%) translateX(-10px);
}

.vertical-content img {
    height: 240px;
    position: relative;
    left: -140px;   /* control all images here */
}



















</style>

<div style="
    width:100%;
    background:#f5f5f5;
    padding:40px 0 120px 0;
    margin-top:40px;
">

    <div style="
        max-width:1200px;
        margin:0 auto;
        padding:0 40px;
    ">








    <!-- TOP CENTER HEADING -->
    <div style="text-align:center; max-width:1000px; margin:0 auto 60px auto;">

        <h2 style="
            color:#002366;
            font-size:32px;
            font-weight:800;
            font-family: Georgia, serif;
            margin-bottom:10px;
        ">
            Our Verticals
        </h2>

        <p style="
            color:#4a6fa5;
            font-size:22px;
            font-weight:500;
        ">
            Pinnacle’s 360° BIM solutions cater to complete lifecycles of large-scale infrastructure projects across continents
        </p>

    </div>
<div class="airport-section" style="
    position:relative;

    min-height:220px;
    padding-bottom:20px 0;
">
<div class="vertical-section">

    <div class="vertical-row">

        <!-- ICON + TITLE -->
    <div class="title" style="
    display:flex;
    flex-direction:row;
    align-items:flex-start;
    gap:12px;
    font-size:24px;
    font-weight:700;
    color:#4a6fa5;
">

    <!-- ICON -->
    <i class="bi bi-airplane-fill" style="
        font-size:28px;
        transform:rotate(20deg);
        margin-top:4px;
    "></i>

    <!-- TEXT BLOCK -->
    <div style="display:flex; flex-direction:column; line-height:1.2;">

        <span style="font-size:24px; font-weight:700;">
            Airport
        </span>

<span style="margin-top:6px; display:inline-block;" class="sub-text">
    Clash DetectionIdentify and resolve <br> conflicts between systems efficiently.

</span>


    </div>
  
</div>

        <!-- TEXT + IMAGE -->
        <div class="vertical-content">

            <div style="
                width:300px;
                font-size:16px;
                line-height:1.6;
            ">
                
            </div>

            <img 
                src="https://res.cloudinary.com/dnodncslz/image/upload/v1775639362/OIP_hlipg2.jpg"
                style="
                    width:360px;
                    height:240px;
                    object-fit:cover;
                    border-radius:12px;
                    position: relative;
               
                    z-index: 6;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.25);

                ">

        
        </div>

    </div>
    <div class="expand-icon">›</div>
</div>
   
    <!-- DATA CENTre -->
    <!-- DATA CENTRE (SAME AS AIRPORT) -->
<div class="vertical-section">

    <div class="vertical-row">

        <!-- ICON + TITLE -->
        <div class="title" style="
            display:flex;
            flex-direction:row;
            align-items:flex-start;
            gap:12px;
            font-size:24px;
            font-weight:700;
            color:#4a6fa5;
        ">

            <!-- ICON -->
            <i class="bi bi-database-fill" style="
                font-size:28px;
                margin-top:4px;
            "></i>

            <!-- TEXT BLOCK -->
            <div style="display:flex; flex-direction:column; line-height:1.2;">

                <span style="font-size:24px; font-weight:700;">
                    Data Centre
                </span>

                <span style="margin-top:6px; display:inline-block;" class="sub-text">
                    Smart Infrastructure Monitoring  
                    Real-time <br> tracking and optimization of data systems.
                </span>

            </div>

        </div>

        <!-- TEXT + IMAGE -->
        <div class="vertical-content">

            <div style="
                width:300px;
                font-size:16px;
                line-height:1.6;
            ">
            </div>

            <img 
                src="https://res.cloudinary.com/dnodncslz/image/upload/v1775813326/OIP_1_kauxwo.jpg"
                style="
                    width:360px;
                    height:240px;
                    object-fit:cover;
                    border-radius:12px;
                ">
        </div>

    </div>
    <div class="expand-icon">›</div>
</div>

<!-- SEMICONDUCTOR -->

<div class="vertical-section">
    <div class="vertical-row">

        <div class="title" style="display:flex; gap:12px; font-size:24px; font-weight:700; color:#4a6fa5;">
            <i class="bi bi-cpu-fill" style="font-size:28px; margin-top:4px;"></i>

            <div style="display:flex; flex-direction:column;">
                <span>Semiconductor</span>

                <span class="sub-text" style="margin-top:6px;">
                    Chip Design & Fabrication  
                    Precision <br>modeling  for advanced semiconductor facilities.
                </span>
            </div>
        </div>

        <div class="vertical-content">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1775816240/OIP_2_aedd85.jpg" style="width:360px; height:240px; object-fit:cover; border-radius:12px;">
        </div>

    </div>
    <div class="expand-icon">›</div>
</div>

<div class="vertical-section">
    <div class="vertical-row">

        <div class="title" style="display:flex; gap:12px; font-size:24px; font-weight:700; color:#4a6fa5;">
            <i class="bi bi-record-circle" style="font-size:28px; margin-top:4px;"></i>

            <div style="display:flex; flex-direction:column;">
                <span>Stadium</span>

                <span class="sub-text" style="margin-top:6px;">
                    Crowd Flow Optimization  
                    Efficient <br> planning for large-scale venues.
                </span>
            </div>
        </div>

        <div class="vertical-content">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1775816261/OIP_3_xizapr.jpg" style="width:360px; height:240px; object-fit:cover; border-radius:12px;">
        </div>

    </div>
    <div class="expand-icon">›</div>    
</div>

<div class="vertical-section">
    <div class="vertical-row">

        <div class="title" style="display:flex; gap:12px; font-size:24px; font-weight:700; color:#4a6fa5;">
            <i class="bi bi-building-gear" style="font-size:28px; margin-top:4px;"></i>

            <div style="display:flex; flex-direction:column;">
                <span>Industrial</span>

                <span class="sub-text" style="margin-top:6px;">
                    Process Optimization  
                    Streamlining <br> operations for industrial efficiency.
                </span>
            </div>
        </div>

        <div class="vertical-content">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1775816269/OIP_4_paiwph.jpg" style="width:360px; height:240px; object-fit:cover; border-radius:12px;">
        </div>

    </div>
    <div class="expand-icon">›</div>
</div>

<div style="text-align:center; margin-top:40px;">

    <a href="#" class="custom-btn">
        Explore All
        <span style="
            display:flex;
            align-items:center;
            justify-content:center;
            width:30px;
            height:30px;
            background:white;
            border-radius:50%;
            color:#002366;
            font-size:16px;
            font-weight:bold;
        ">→</span>
    </a>

</div>

</div>


""", height=2000)
