import streamlit as st
import sqlite3
import os
import streamlit.components.v1 as components
import base64
# ---------------- STATE (ADD BELOW IMPORTS) ----------------


st.set_page_config(page_title="my webapp", layout="wide")

st.markdown("""
<style>

/* ================= GLOBAL LAYOUT FIX ================= */
html, body {
    overflow-x: hidden;
}

/* remove Streamlit padding (VERY IMPORTANT) */
.block-container {
    padding-top: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
    margin-top: -20px;
}

/* ================= DEPLOY HIDE (YOUR SECTION) ================= */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* background fix */
.stVerticalBlock {
    background-color: #ffffff !important;
}


/* ================= REMOVE EXTRA VERTICAL GAP ================= */
div[data-testid="stVerticalBlock"] {
    gap: 0.5rem !important;
}

/* remove spacing between markdown blocks */
div[data-testid="stMarkdownContainer"] {
    margin-top: 0px !important;
    margin-bottom: 0px !important;
}

/* tighten headings */
h1, h2, h3, h4 {
    margin-top: 0.2rem !important;
    margin-bottom: 0.2rem !important;
}

/* remove extra space from components */
iframe {
    margin: 0 !important;
}




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
""", height=530)




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
    max-width:1200px;
    margin:60px auto;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:30px;
    padding:0 20px;
'>





    <!-- LEFT TEXT -->
    <div style="width:50%;">

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
    <div style='width:50%; position:relative;'>

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
components.html("""
<style>
@keyframes scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}
</style>

<div style="
    position:relative;
    width:100vw;
    left:50%;
    transform:translateX(-50%);
    background:#e0e0e0;
    margin:60px 0;
    box-shadow:0 8px 20px rgba(0,0,0,0.1);
    padding:40px 0;
    overflow:hidden;
">

<!-- TEXT -->
<div style="
    position:absolute;
    top:50%;
    transform:translateY(-50%);
    left:30px;
    font-size:24px;
    font-weight:700;
    color:#002366;
    font-family: Georgia, serif;
    z-index:5;
">
    Industry Associations
</div>

<!-- INVISIBLE LINES -->
<div style="
    margin-left:320px;
    margin-right:120px;
    overflow:hidden;
">

<!-- TRACK WRAPPER -->
<div style="display:flex; width:max-content;">

    <!-- TRACK 1 -->
    <div style="
        display:flex;
        gap:60px;
        animation: scroll 20s linear infinite;
    ">

        <!-- SET 1 -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

        <!-- SET 2 -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

        <!-- SET 3 -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

        <!-- SET 4 -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

    </div>

    <!-- TRACK 2 (CLONE) -->
    <div style="
        display:flex;
        gap:60px;
        animation: scroll 20s linear infinite;
    ">

        <!-- SAME 4 SETS AGAIN -->

        <!-- SET 1 -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

        <!-- SET 2 -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

        <!-- SET 3 -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

        <!-- SET 4 -->
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774440686/ahk_u5d2h6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441251/npca_vypoo6.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441161/buildingsmart_d7yder.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774441027/building_mqyiow.webp" style="height:75px;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1774528765/stpi_fbnfw1.webp" style="height:75px;">

    </div>

</div>
</div>
</div>
""", height=300)
















































































































































































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
    align-items:stretch;
    gap:40px;
    margin:40px auto;
    width:100%;
    max-width:1200px;
    flex-wrap:wrap;
    padding:0 20px;
    box-sizing:border-box;
'>

    <!-- LEFT TEXT -->
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

        <a href="javascript:void(0)" class="custom-btn">
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

        <img src="{bim_image_url}" style="
            width:100%;
            max-width:320px;
            aspect-ratio: 1 / 1;
            object-fit:cover;
            border-radius:12px;
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

    <a href="javascript:void(0)" class="custom-btn">
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
    aspect-ratio: 1 / 1;
    object-fit:cover;
    border-radius:12px;
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

        <a href="javascript:void(0)" class="custom-btn">
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
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: #002366;
    color: white;
    padding: 12px 22px;
    border-radius: 50px;
    text-decoration: none;
    margin-top: 25px;
    font-size: 16px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: background 0.2s ease;
}}

.custom-btn:hover {{
    background: #001a4d;
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

        <a href="javascript:void(0)" class="custom-btn">
    Know More
    <span style="
        display: flex;
        align-items: center;
        justify-content: center;
        width: 30px;
        height: 30px;
        background: white;
        border-radius: 50%;
        color: #002366;
        font-size: 16px;
        font-weight: bold;
    ">
        →
    </span>
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


""", height=1300)


st.markdown("""
<div style="height:20px;"></div>
""", unsafe_allow_html=True)


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
    Our Projects
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="
    width:100%;
    text-align:center;
    margin-top:10px;
    font-size:20px;
    font-family:sans-serif;
    color:#4a6fa5;
">
    Explore world-class projects that testify to our global industry expertise and commitment to crafting excellence.
</div>
""", unsafe_allow_html=True)




####### PROJECT IMGES ####
components.html("""
<style>
.wrapper {
    width:100%;
    margin:0;
    display:flex;
    overflow-x:auto;

    gap:16px;              /* slight gap*/
    padding:60px 16px;

    box-sizing:border-box;
    cursor:grab;
    scroll-snap-type: none;
}

.wrapper::-webkit-scrollbar {
    display:none;
}


.card {
    flex: 0 0 32%;
    scroll-snap-align: start;   /*  THIS CONTROLS HOW MANY IMAGES FIT */
}

.card img {
    width: 100%;
    height: 20vw;        /* scales with screen */
    max-height: 240px;   /* limit */
    min-height: 200px;   /* keep minimum */
    object-fit: cover;
    border-radius: 16px;
    pointer-events: none;
}


/* zig-zag */
.up { transform:translateY(-16px); }
.down { transform:translateY(16px); }

.wrapper:active {
    cursor:grabbing;
}
</style>



<div class="wrapper" id="dragArea">

    <div class="card up"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776171393/3d_bim_riyadh_metro_stations.jpg_bytbcb.webp"></div>
    <div class="card down"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776171445/new_orleans_international_airport-02.jpg_fy7hz4.webp"></div>
    <div class="card up"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776171484/legacy-cool-spring.jpg_jg0uab.webp"></div>
    <div class="card down"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776171521/lusail_stadium_afl_architects1.jpg_o2xuko.webp"></div>
    <div class="card up"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776171585/new-childrens-hospital.jpg_fj14hq.webp"></div>
    <div class="card down"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776171643/601-n-central_mghdva.jpg"></div>
    <div class="card up"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776171712/facebook-datacenter3_vrhftd.webp"></div>

</div>

<script>
const slider = document.getElementById("dragArea");

//  Duplicate content (keeps same alignment automatically)
slider.innerHTML += slider.innerHTML;

let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener("mousedown", (e) => {
    isDown = true;
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
    slider.style.cursor = "grabbing";
});

slider.addEventListener("mouseleave", () => {
    isDown = false;
    slider.style.cursor = "grab";
});

slider.addEventListener("mouseup", () => {
    isDown = false;
    slider.style.cursor = "grab";
});

slider.addEventListener("mousemove", (e) => {
    if(!isDown) return;
    e.preventDefault();

    const x = e.pageX - slider.offsetLeft;
    const walk = (x - startX) * 1.5;  // smoother
    slider.scrollLeft = scrollLeft - walk;
});

//  Infinite loop without affecting alignment
slider.addEventListener("scroll", () => {
    const maxScroll = slider.scrollWidth / 2;

    if (slider.scrollLeft >= maxScroll) {
        slider.scrollLeft -= maxScroll;
    }
    if (slider.scrollLeft <= 0) {
        slider.scrollLeft += maxScroll;
    }
});
</script>


""", height=340)

##### BOTTON####

st.markdown('''
<div class="middle-btn">
    <button class="know-more-btn">
        <span>View All Projects</span>
        <span class="arrow-circle">→</span>
    </button>
</div>

<style>
.middle-btn {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

.know-more-btn {
    display: flex;
    align-items: center;
    gap: 12px;

    padding: 10px 14px 10px 24px;
    border-radius: 999px;
    border: none;

    background: #0A2A66;   /* rich dark blue */
    color: #fff;

    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
}

/* white circle */
.arrow-circle {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: #fff;
    color: #0A2A66;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 14px;
    font-weight: bold;
}

/* hover */
.know-more-btn:hover {
    background: #081F4D;   /* darker on hover */
    transform: translateY(-2px);
}

.know-more-btn:hover .arrow-circle {
    transform: translateX(4px);
    transition: 0.3s;
}
</style>
''', unsafe_allow_html=True)




##### PEOPLE  #######
components.html("""
<style>

.wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 180px;   /* increased spacing */
    width: 100%;
    flex-wrap: nowrap;
    padding: 40px 0;  /* gives breathing space */
}

/* TEXT BOX */
.text-box {
    max-width:750px;
    min-height:240px;
    position: relative;
    overflow: visible;
    padding-left: 15px;   /*  creates gap from icon */
    padding-top: 5px;    /*  adds vertical breathing space */
}

/* TEXT */
#text {
    display:block;
    transform: translateX(0px);
    opacity: 1;
    transition: transform 0.45s ease, opacity 0.45s ease;
    will-change: transform, opacity;
    font-size: 18px;   /*  bigger text */
    line-height: 1.6;
}

/* DECK */
.deck {
    width:340px;    /*  increased */
    height:400px;   /*  increased */
    position:relative;
    flex-shrink: 0;
    overflow: hidden;
}

/* STACKED CARDS */
.card {
    position:absolute;
    width:260px;   /* increased */
    height:340px;  /*  increased */
}

.card1 { transform: translate(0px,0px) rotate(-2deg); z-index:5; }
.card2 { transform: translate(8px,3px) rotate(1deg); z-index:4; }
.card3 { transform: translate(16px,6px) rotate(3deg); z-index:3; }
.card4 { transform: translate(24px,9px) rotate(-1deg); z-index:2; }
.card5 { transform: translate(32px,12px) rotate(2deg); z-index:1; }

.card img{
    width:100%;
    height:100%;
    object-fit:cover;
    border-radius:14px;
    box-shadow:0 12px 30px rgba(0,0,0,0.30);
}

/* BUTTONS */
.controls {
    margin-top:18px;
}

.btn {
    border:none;
    background:#0A2A66;
    color:white;
    padding:8px 14px;
    margin-right:10px;
    border-radius:8px;
    cursor:pointer;
    font-size:14px;
}

.quote-icon {
    width: 55px;
    height: 80px;
    position: absolute;
    top: -3px;   /*  slightly higher */
    left: -50px;  /*  slightly left but fully visible */
    opacity: 1;
}





</style>









<div class="wrapper">

    <div class="text-box">
    <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776763634/top-double-invited-comma_yptu3r.svg" class="quote-icon">
        <h3>What people are Saying</h3>

        <p id="text"></p>

        <div class="controls">
            <button class="btn" onclick="prev()">&lt;</button>
            <button class="btn" onclick="next()">&gt;</button>
        </div>
    </div>

    <div class="deck" id="deck"></div>

</div>

<script>

const data = [

{
text:`Jessica Resta
Our Pinnacle team has been very helpful.
They deliver high quality work.
Always meet deadlines.
Communication is excellent.`,
html: `
<div class="card card1"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323491/Jessica-Resta_axwvxz.webp"></div>
<div class="card card2"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323505/Leonidas-Tzevelekas_y97z40.webp"></div>
<div class="card card3"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323520/Keith-Rodriguez_kjr8gn.webp"></div>
<div class="card card4"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323532/Garnette-Rouse_mnlcxq.webp"></div>
<div class="card card5"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323545/stewart_bohrer_xmhl1t.webp"></div>
`
},

{
text:`Leonidas Tzevelekas
The team understands requirements deeply.
Communication is smooth and fast.
Execution is very professional.
Work quality is strong.`,
html: `
<div class="card card1"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323505/Leonidas-Tzevelekas_y97z40.webp"></div>
<div class="card card2"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323520/Keith-Rodriguez_kjr8gn.webp"></div>
<div class="card card3"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323532/Garnette-Rouse_mnlcxq.webp"></div>
<div class="card card4"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323545/stewart_bohrer_xmhl1t.webp"></div>
<div class="card card5"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323491/Jessica-Resta_axwvxz.webp"></div>
`
},

{
text:`Keith Rodriguez
They always meet deadlines.
Quality is consistent.
Highly reliable team.
Strong technical understanding.`,
html: `
<div class="card card1"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323520/Keith-Rodriguez_kjr8gn.webp"></div>
<div class="card card2"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323532/Garnette-Rouse_mnlcxq.webp"></div>
<div class="card card3"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323545/stewart_bohrer_xmhl1t.webp"></div>
<div class="card card4"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323491/Jessica-Resta_axwvxz.webp"></div>
<div class="card card5"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323505/Leonidas-Tzevelekas_y97z40.webp"></div>
`
},

{
text:`Garnette Rouse
Excellent coordination across teams.
Very professional workflow.
Strong communication system.
Smooth project handling.`,
html: `
<div class="card card1"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323532/Garnette-Rouse_mnlcxq.webp"></div>
<div class="card card2"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323545/stewart_bohrer_xmhl1t.webp"></div>
<div class="card card3"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323491/Jessica-Resta_axwvxz.webp"></div>
<div class="card card4"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323505/Leonidas-Tzevelekas_y97z40.webp"></div>
<div class="card card5"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323520/Keith-Rodriguez_kjr8gn.webp"></div>
`
},

{
text:`Stewart Bohrer
Very dependable and consistent delivery.
Strong attention to detail.
Great collaboration experience.
Highly professional approach.`,
html: `
<div class="card card1"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323545/stewart_bohrer_xmhl1t.webp"></div>
<div class="card card2"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323491/Jessica-Resta_axwvxz.webp"></div>
<div class="card card3"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323505/Leonidas-Tzevelekas_y97z40.webp"></div>
<div class="card card4"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323520/Keith-Rodriguez_kjr8gn.webp"></div>
<div class="card card5"><img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776323532/Garnette-Rouse_mnlcxq.webp"></div>
`
}

];

let index = 0;

function animateTextChange(newIndex){

    const textEl = document.getElementById("text");
    const deckEl = document.getElementById("deck");

    textEl.style.transform = "translateX(-120px)";
    textEl.style.opacity = "0";

    setTimeout(() => {

        index = newIndex;

        textEl.innerText = data[index].text;
        deckEl.innerHTML = data[index].html;

        textEl.style.transition = "none";
        textEl.style.transform = "translateX(120px)";
        textEl.style.opacity = "0";

        void textEl.offsetWidth;

        setTimeout(() => {
            textEl.style.transition = "transform 0.45s ease, opacity 0.45s ease";
            textEl.style.transform = "translateX(0px)";
            textEl.style.opacity = "1";
        }, 20);

    }, 200);
}

function next(){
    animateTextChange((index + 1) % data.length);
}

function prev(){
    animateTextChange((index - 1 + data.length) % data.length);
}

animateTextChange(0);

</script>
""", height=550)

##### Say Hello ########

st.markdown(
"""
<style>
.cta-box {
    width: 100%;
    background: #0A2A66;
    padding: 80px 20px;
    border-radius: 24px;
    text-align: center;
    font-family: sans-serif;
    color: white;
}
.cta-title {
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 12px;
}
.cta-subtitle {
    font-size: 16px;
    font-weight: 400;
    opacity: 0.85;
    line-height: 1.5;
}
</style>

<div class="cta-box">
    <div class="cta-title">Say Hello</div>
    <div class="cta-subtitle">
        We’d love to hear from you and help you build something amazing
    </div>
</div>
""",
unsafe_allow_html=True
)

#### more about##


st.markdown("""
<h3 style="
    color:#0A2A66;
    font-family:sans-serif;
    font-size:18px;
    font-weight:600;
    margin:5px 0 5px 0;
    text-align:center;
">
More About Pinnacle
</h3>
""", unsafe_allow_html=True)



#### 3 Bar #####
#### OUR PRODUCTS #### 

components.html(""" 
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<style>
.tab-btn {
    background-color: #3a66ab;
    color: white;
    height: 70px;
    min-width: 340px;
    padding: 0 50px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 600;
    border: none;
    transition: 0.3s ease;
}

.tab-btn:hover { background-color: #2f5a9a; }
.active-tab {
    background-color: #0b2a5b !important;
    box-shadow: 0 6px 18px rgba(11, 42, 91, 0.35);
}

.no-padding {
    padding-left: 0 !important;
    padding-right: 0 !important;
}

.grey-card {
    background: #e5e7eb;
    border-radius: 14px;
    padding: 16px;
    flex: 1;
    min-height: 160px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: 0.3s ease;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}

.grey-card:hover {
    background: #dbe1e8;
    transform: translateY(-3px);
}

.grey-card .title {
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 6px;
}

.grey-card .desc {
    font-size: 13px;
    color: #555;
}
</style>

<div class="container mt-4">

    <!-- TABS -->
    <div class="d-flex justify-content-center gap-3 flex-wrap text-center">
        <button class="tab-btn active-tab" onclick="showTab('products', this)">Our Products</button>
        <button class="tab-btn" onclick="showTab('solutions', this)">Our Specialized Solutions</button>
        <button class="tab-btn" onclick="showTab('software', this)">Software We Use</button>
    </div>

    <!-- CONTENT -->
    <div class="row mt-4 gx-3 justify-content-center">

        <!-- LEFT SIDE (TEXT + CARDS) -->
        <div class="col-auto no-padding">

            <!-- PRODUCTS -->
            <div id="products" class="tab-section d-none" style="width:620px;">
                <div class="p-3 bg-light rounded text-left">
                    The workforce at Pinnacle is proficient in software platforms spanning the entire construction lifecycle. They include software for design, 3D modeling/rendering, BIM modeling/fabrication, CAD drafting, and Common Data Environment. Using these software tools, we implement advanced workflows that streamline interdisciplinary coordination, facilitate proactive clash resolution, and help clients achieve the best-in-class outputs.
                </div>

                <div style="display:flex; gap:12px; margin-top:14px;">
                    <div class="grey-card"><div class="title">Product 1</div><div class="desc">Desc</div></div>
                    <div class="grey-card"><div class="title">Product 2</div><div class="desc">Desc</div></div>
                    <div class="grey-card"><div class="title">Product 3</div><div class="desc">Desc</div></div>
                </div>
            </div>

            <!-- SOLUTIONS -->
            <div id="solutions" class="tab-section d-none" style="width:620px;">
                <div class="p-3 bg-light rounded text-left">
                    Beyond our core services, Pinnacle is a proud Autodesk Learning and Reselling partner and also delivers exclusive CAD support to HP. Being an Authorized Training Centre (ATC), our sessions comply with Autodesk’s training benchmarks. As a valued partner of HP, Pinnacle’s expertise in accurately converting 2D CAD files or 3D models into 2D DXF files powers HP SitePrint’s core operations.



                </div>

                <div style="display:flex; gap:12px; margin-top:14px;">
                    <div class="grey-card"><div class="title">Solution 1</div><div class="desc">Desc</div></div>
                    <div class="grey-card"><div class="title">Solution 2</div><div class="desc">Desc</div></div>
                    <div class="grey-card"><div class="title">Solution 3</div><div class="desc">Desc</div></div>
                </div>
            </div>

            <!-- SOFTWARE -->
            <div id="software" class="tab-section d-none" style="width:620px;">
                <div class="p-3 bg-light rounded text-left">
                    The workforce at Pinnacle is proficient in software platforms spanning the entire construction lifecycle. They include software for design, 3D modeling/rendering, BIM modeling/fabrication, CAD drafting, and Common Data Environment. Using these software tools, we implement advanced workflows that streamline interdisciplinary coordination, facilitate proactive clash resolution, and help clients achieve the best-in-class outputs.





                </div>

                <div style="display:flex; gap:12px; margin-top:14px;">
                    <div class="grey-card"><div class="title">Software 1</div><div class="desc">Desc</div></div>
                    <div class="grey-card"><div class="title">Software 2</div><div class="desc">Desc</div></div>
                    <div class="grey-card"><div class="title">Software 3</div><div class="desc">Desc</div></div>
                </div>
            </div>

        </div>

        <!-- RIGHT IMAGE -->
        <div class="col-auto no-padding">

<div id="products-img" class="tab-img d-none ms-3 h-100" style="width:420px;">
    <div style="height:100%; display:flex;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776344032/our_products_2_g6lnrn.webp"
             style="width:100%; height:100%; object-fit:cover; border-radius:10px;">
    </div>
</div>

<div id="solutions-img" class="tab-img d-none ms-3 h-100" style="width:420px;">
    <div style="height:100%; display:flex;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776411327/our_specilized_solutions_hv8egs.webp"
             style="width:100%; height:100%; object-fit:cover; border-radius:10px;">
    </div>
</div>


<div id="software-img" class="tab-img d-none ms-3 h-100" style="width:420px;">
    <div style="height:100%; display:flex;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776411367/software_we_use_2_rjrfyh.webp"
             style="width:100%; height:100%; object-fit:cover; border-radius:10px;">
    </div>
</div>

            




        </div>

    </div>
</div>

<script>
function showTab(tabId, btn) {

    document.querySelectorAll('.tab-section').forEach(e => e.classList.add("d-none"));
    document.querySelectorAll('.tab-img').forEach(e => e.classList.add("d-none"));

    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove("active-tab"));
    btn.classList.add("active-tab");

    document.getElementById(tabId).classList.remove("d-none");
    document.getElementById(tabId + "-img").classList.remove("d-none");
}

/*  AUTO-LOAD DEFAULT TAB */
window.onload = function () {
    const defaultBtn = document.querySelector('.tab-btn');
    showTab('products', defaultBtn);
};
</script>







""", height=530)


#### bar#### 
components.html("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<div style="
    width: 100%;
    background: linear-gradient(135deg, #4a77c2, #1f3f7a);
    padding: 50px 20px;
    margin-top: 40px;
    border-radius: 18px;
    position: relative;
">

    <!-- LEFT CENTER LABEL -->
    <div style="
        position: absolute;
        left: 40px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 22px;
        font-weight: 700;
        color: white;
        letter-spacing: 1px;
        white-space: nowrap;
    ">
        Our CSR
    </div>

    <div class="container">
        <div class="row justify-content-center g-3">

            <!-- CARD 1 -->
            <div class="col-md-5">
                <div class="d-flex align-items-center bg-white rounded-4 shadow-sm p-3"
                     style="height: 130px;">

                    <div class="me-3">
                        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776418591/swabhimaan-logo_l1u6ef.webp" style="
                            width: 85px;
                            height: 85px;
                            object-fit: contain;
                            background: #f1f1f1;
                            padding: 6px;
                            border-radius: 10px;
                        ">
                    </div>

                    <div>
                        <div style="
                            font-size: 13px;
                            font-weight: 600;
                            color: #333;
                        ">
                            Through swaviman we support the education and well being of overlooked community.
                        </div>
                    </div>

                </div>
            </div>

            <!-- CARD 2 -->
            <div class="col-md-5">
                <div class="d-flex align-items-center bg-white rounded-4 shadow-sm p-3"
                     style="height: 130px;">

                    <div class="me-3">
                        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776418654/ankuran-logo_xeut4l.webp" style="
                            width: 85px;
                            height: 85px;
                            object-fit: contain;
                            background: #f1f1f1;
                            padding: 6px;
                            border-radius: 10px;
                        ">
                    </div>

                    <div>
                        <div style="
                            font-size: 13px;
                            font-weight: 600;
                            color: #333;
                        ">
                            Nurturing the young minds to become innovators through experiential science learning.
                        </div>
                    </div>

                </div>
            </div>

        </div>
    </div>

</div>
""", height=280)

##### GLOBAL PRESENCE####

components.html("""
<div style="
    width: 100%;
    text-align: center;
    margin-top: 30px;
    font-family: sans-serif;
    color: #1f3f7a;
    font-size: 28px;
    font-weight: 700;
    letter-spacing: 1px;
">
    Global Presence
</div>
""", height=80)

### GRAY BAR####

components.html("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<div style="
    width: 100%;
    background: #e5e7eb;
    padding: 60px 20px;
    margin-top: 40px;
">

    <div class="container">
        <div class="row align-items-center">

            <!-- LEFT SIDE (STYLISH BLOCKS) -->
            <div class="col-md-6" style="font-family: 'Segoe UI', sans-serif;">

                <!-- BLOCK 1 -->
                <div style="margin-bottom: 32px;">
                    <div style="
                        display: flex;
                        align-items: center;
                        gap: 10px;
                        margin-bottom: 6px;
                    ">
                        <div style="
                            width: 6px;
                            height: 22px;
                            background: #1f3f7a;
                            border-radius: 3px;
                        "></div>

                        <div style="
                            font-size: 22px;
                            font-weight: 800;
                            color: #1f3f7a;
                            letter-spacing: 0.5px;
                        ">
                            Pinnacle Infotech
                        </div>
                    </div>

                    <div style="font-size: 13px; color: #444; font-weight: 500;">
                        3250 Bloor Street West, East Tower, Unit 600, Toronto, Ontario, M8X2X9

Mr. Subhojit Sarkar

ssarkar@pinnacleinfotech.com

+1 437 782 0030, +1 680 210 9909











                    </div>
                </div>

                <!-- BLOCK 2 -->
                <div style="margin-bottom: 32px;">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                        <div style="width: 6px; height: 22px; background: #1f3f7a; border-radius: 3px;"></div>
                        <div style="font-size: 22px; font-weight: 800; color: #1f3f7a; letter-spacing: 0.5px;">
                            Pinnacle Infotech
                        </div>
                    </div>

                    <div style="font-size: 13px; color: #444; font-weight: 500;">
                        6065 Roswell Rd NE #625, Atlanta, GA 30328

Mr. Samrat Mallick

samratm@pinnacleinfotech.com

+1 832 818 1253













                    </div>
                </div>

                <!-- BLOCK 3 -->
                <div style="margin-bottom: 32px;">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                        <div style="width: 6px; height: 22px; background: #1f3f7a; border-radius: 3px;"></div>
                        <div style="font-size: 22px; font-weight: 800; color: #1f3f7a; letter-spacing: 0.5px;">
                            Pinnacle Infotech
                        </div>
                    </div>

                    <div style="font-size: 13px; color: #444; font-weight: 500;">
                         6065 Roswell Rd NE #625, Atlanta, GA 30328

Mr. Samrat Mallick

samratm@pinnacleinfotech.com

+1 832 818 1253








                    </div>
                </div>

                <!-- BLOCK 4 -->
                <div style="margin-bottom: 32px;">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                        <div style="width: 6px; height: 22px; background: #1f3f7a; border-radius: 3px;"></div>
                        <div style="font-size: 22px; font-weight: 800; color: #1f3f7a; letter-spacing: 0.5px;">
                            Pinnacle Infotech
                        </div>
                    </div>

                    <div style="font-size: 13px; color: #444; font-weight: 500;">
                        25 N 14th Street, Suite # 670, San Jose, CA – 95112

Mr. Nikhil Varandani

nvarandani@pinnacleinfotech.com

+1 (832) 874-2798








                    </div>
                </div>

                <!-- BLOCK 5 -->
                <div>
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                        <div style="width: 6px; height: 22px; background: #1f3f7a; border-radius: 3px;"></div>
                        <div style="font-size: 22px; font-weight: 800; color: #1f3f7a; letter-spacing: 0.5px;">
                            Pinnacle Infotech
                        </div>
                    </div>

                    <div style="font-size: 13px; color: #444; font-weight: 500;">
                        50 Sugar Creek Center Blvd, Suite #350, Sugar Land, TX 77478

                        Mr. B. Todd

                        btodi@pinnacleinfotech.com

                        +1 713 780 2135, +1 437 782 0030, +1 713 780 8784




                    </div>
                </div>

            </div>

            <!-- RIGHT SIDE (BIG IMAGE) -->
            <div class="col-md-6 d-flex align-items-center justify-content-center"
                 style="overflow: visible;">

                <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776670560/download_1_o23tg1.png" style="
                    width: 100%;
                    max-width: 500px;
                    height: auto;
                    border-radius: 14px;
                    object-fit: contain;
                    display: block;
                ">

            </div>

        </div>
    </div>

</div>
""", height=630)

#### IMAGE#### 

components.html("""
<div style="
    width: 100%;
    margin-top: 40px;
    border-radius: 18px;
    overflow: hidden;
    position: relative;
">

    <!-- BACKGROUND IMAGE -->
    <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776424759/home-career-bgimg_kz52zt.webp" style="
        width: 100%;
        height: 630px;
        object-fit: cover;
        display: block;
    ">

    <!-- BIG CENTER BLUE TAB -->
    <div style="
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #3a66ab;
    padding: 60px 90px;
    border-radius: 18px;
    min-width: 450px;
    min-height: 140px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
">

    <!-- TEXT -->
    <div style="
        color: white;
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 12px;
        font-family: sans-serif;
        letter-spacing: 0.5px;
    ">
        Grow At Pinnacle
    </div>

    <!-- BUTTON -->
    <div style="
        background: white;
        color: #3a66ab;
        padding: 18px 40px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 18px;
        cursor: pointer;
        white-space: nowrap;
    ">
        View all opportunities
    </div>

</div>




</div>
""", height=690)

### latest update ###


components.html("""
<div style="text-align: center; margin: 20px 0;">

    <h2 style="
        color: #0b2a5b;
        font-family: sans-serif;
        font-weight: 600;
        margin-bottom: 8px;
    ">
        Latest Updates
    </h2>

    <p style="
        color: #3f5f8a;   /* light dark blue */
        font-family: sans-serif;
        font-size: 16px;
        margin-top: 0;
    ">
        Your go-to hub for sharp industry insights, key event updates, and more.
    </p>

</div>
""", height=150)

### events ### 

components.html("""
<div style="display:flex; justify-content:center; width:100%;">

<div style="width:100%; max-width:1100px;">

<div style="display:flex; align-items:flex-start; padding:10px 20px; font-family:sans-serif; gap:30px;">

<!-- LEFT SIDE -->
<div style="width:40%; display:flex; flex-direction:column;">

<h3 style="color:#0b2a5b; margin-bottom:15px;">
    Blogs & Articles
</h3>

<div>

<div onclick="changeImages('live')" style="padding:12px 0; cursor:pointer;"
onmouseover="this.style.color='#0b2a5b'" onmouseout="this.style.color='#3f5f8a'">
    Live Events
</div>
<div style="width:140px; border-top:1px solid #d0d9e6;"></div>

<div onclick="changeImages('insights')" style="padding:12px 0; cursor:pointer;"
onmouseover="this.style.color='#0b2a5b'" onmouseout="this.style.color='#3f5f8a'">
    Industry Insights
</div>
<div style="width:140px; border-top:1px solid #d0d9e6;"></div>

<div onclick="changeImages('updates')" style="padding:12px 0; cursor:pointer;"
onmouseover="this.style.color='#0b2a5b'" onmouseout="this.style.color='#3f5f8a'">
    Product Updates
</div>
<div style="width:140px; border-top:1px solid #d0d9e6;"></div>

<div onclick="changeImages('case')" style="padding:12px 0; cursor:pointer;"
onmouseover="this.style.color='#0b2a5b'" onmouseout="this.style.color='#3f5f8a'">
    Case Studies
</div>
<div style="width:140px; border-top:1px solid #d0d9e6;"></div>

<div onclick="changeImages('tutorials')" style="padding:12px 0; cursor:pointer;"
onmouseover="this.style.color='#0b2a5b'" onmouseout="this.style.color='#3f5f8a'">
    Tutorials
</div>

</div>

</div>

<!-- RIGHT SIDE IMAGES -->
<div id="imageContainer" style="display:flex; flex-direction:column; gap:14px; margin-top:5px;">

<div style="display:flex; gap:14px;">
    <img id="img1" style="width:280px;height:320px;border-radius:14px;object-fit:cover;">
    <img id="img2" style="width:280px;height:180px;border-radius:14px;object-fit:cover;">
    <img id="img3" style="width:280px;height:320px;border-radius:14px;object-fit:cover;">
</div>

<div style="display:flex; gap:14px;">
    <img id="img4" style="width:280px;height:180px;border-radius:14px;object-fit:cover;">
    <img id="img5" style="width:280px;height:320px;border-radius:14px;object-fit:cover;   transform: translateY(-130px);">
    <img id="img6" style="width:280px;height:180px;border-radius:14px;object-fit:cover;">
</div>

</div>

</div>
</div>
</div>

<script>

// IMAGE SETS
const imageSets = {

live: [
"https://res.cloudinary.com/dnodncslz/image/upload/v1776429100/BIM-Clash-Detection-A-Detailed-Guide_crxhje.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776429076/Construction-Asset-Management-A-Complete-Guide_aeeewh.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776429203/GIS-BIM-Integration-Application-and-Benefits_bmifck.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776429342/Landscape-Architecture_Definitions-Significance_1_wfviab.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776429391/IoT-in-Construction_n6pjew.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776429460/Revit-Vs-AutoCAD-History-Basic-Differences-Plugins_cgfhsp.webp"
],

insights: [
"https://res.cloudinary.com/dnodncslz/image/upload/v1776769564/business-value-bim-mechanical-hvac-construction_cbn6xa.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776769595/business-value-bim-water-projects_eyra7b.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776769625/no-img_noixhe.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776769664/latest_news_pinnacle_on_autodesk_madurai_campus_vzlyoe.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776769703/no-img_xi4gnp.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776769703/no-img_xi4gnp.webp"
],

updates: [
"https://res.cloudinary.com/dnodncslz/image/upload/v1776770103/pinnacle-bim-series-pop-up.png_vu0ydd.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776770265/Pinnacle-Infotech-at-New-York-Build-Expo-2024-2048x1583_xdq3og.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776770056/Pinnacle-at-AU-2024_y0ekie.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776770095/pinnacle-global-customer-event-cover-image_dbkpwf.png",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776770220/Big-5-Saudi_2025-1_lmn8eh.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776770146/Japan-Build-Tokyo_uh8x4b.webp"
],

case: [
"https://res.cloudinary.com/dnodncslz/image/upload/v1776767493/bimal_patwari_cnbs_tv18_interview_2024_gyiyq1.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776767482/bimal_patwari_journey_continues_2021_big_cjb2kb.webp",
"https://res.cloudinary.com/dnodncslz/image/upload/v1776770095/pinnacle-global-customer-event-cover-image_dbkpwf.png"
],

tutorials: [
"https://res.cloudinary.com/dnodncslz/image/upload/v1776770757/stats-img-01_a9ufd4.webp"
]

};


// CHANGE FUNCTION
function changeImages(type){

    const imgs = imageSets[type];

    for(let i=1;i<=6;i++){
        const el = document.getElementById("img"+i);

        if(imgs[i-1]){
            el.src = imgs[i-1];
            el.style.display = "block";
        } else {
            el.style.display = "none";
        }
    }
}

// DEFAULT LOAD
changeImages('live');

</script>
""", height=680)






























#### BlUE CONTENT BOX ### 

components.html("""
<div style="
    width: 100%;
    margin-top: 50px;
">

    <!-- BLUE BAR -->
    <div style="
        width: 100%;
        background: #0b2a5b;
        border-radius: 30px;
        min-height: 1000px;
        padding: 60px;
        box-sizing: border-box;
        font-family: sans-serif;
    ">

        <!-- TOP ROW -->
        <div style="
            display: flex;
            align-items: flex-start;
        ">

            <!-- LEFT BLOCK (LOGO + PARAGRAPH WIDTH CONTROL) -->
            <div style="
                width: 420px;   /* SAME as paragraph width */
            ">

                <!-- LOGO -->
                <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776670638/logo-white_oz7xl7.svg"
                    style="margin-bottom: 20px;">

                <!-- PARAGRAPH -->
                <p style="
                    color: rgba(255,255,255,0.7);
                    font-size: 15px;
                    line-height: 1.6;
                ">
                    This is a placeholder paragraph. You can describe your product,
                    services, or highlights here in a subtle and clean way.
                </p>

<!-- SECOND LOGO -->
<img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776681616/iso-19650_1_oe5tbv.webp"
    style="
        margin-top: 20px;
        width: 140px;
        height: auto;
        object-fit: contain;
    ">


            </div>

          <!-- ADD THIS ON TOP (only once in your page) -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">


<!-- RIGHT SIDE -->
<div style="
    display: flex;
    gap: 40px;
flex-wrap: nowrap;   /*  prevents going below */
align-items: flex-start;


    margin-left: 60px;
    color: white;
    font-size: 16px;
">

    <!-- CONTACT COLUMN -->
<div>
    <div style="font-weight: 510;  font-size: 15px; margin-bottom: 15px;">
        Contact
    </div>

    <!-- PHONE -->
   <div style="
    display: flex;
    align-items: center;
    gap: 10px;
    color: rgba(255,255,255,0.75);
    margin-bottom: 14px;
">
    <i class="bi bi-telephone-fill" style="color:#7fa6d9;"></i>
    <span style="font-size: 13px;">
        +91 98765 43210
    </span>
</div>



    <!-- EMAIL -->
<div style="
    display: flex;
    align-items: center;
    gap: 10px;
    color: rgba(255,255,255,0.75);
    margin-bottom: 18px;
">
    <i class="bi bi-envelope-fill" style="color:#7fa6d9; font-size:13px;"></i>
    <span style="font-size: 13px;">
        example@email.com
    </span>
</div>










    <!-- SOCIAL CONNECT -->
    <div style="
        font-weight: 510;
        color: white;
        margin-bottom: 12px;
    ">
        Social Connect
    </div>

    <!-- ICONS (row but below heading) -->
    <div style="
        display: flex;
        gap: 14px;
    ">
        <i class="bi bi-facebook" style="color:#7fa6d9; font-size:18px;"></i>
        <i class="bi bi-twitter-x" style="color:#7fa6d9; font-size:18px;"></i>
        <i class="bi bi-linkedin" style="color:#7fa6d9; font-size:18px;"></i>
        <i class="bi bi-youtube" style="color:#7fa6d9; font-size:18px;"></i>
    </div>
</div>

<!-- JOIN NEWSLETTER COLUMN -->
<div>
    <div style="
        font-weight: 510;
        color: white;
        margin-bottom: 15px;
         font-size: 15px;
    ">
        Join Our Newsletter
    </div>

    <!-- PARAGRAPH -->
    <p style="
        color: rgba(255,255,255,0.7);
        font-size: 14px;
        line-height: 1.6;
        max-width: 260px;
        margin-bottom: 15px;
    ">
        Get the latest updates about trending BIM news and informative articles on your inbox by subscribing.
    </p>

    <div style="
    position: relative;
    width: 260px;
    margin-top: 5px;
">

    <!-- INPUT -->
    <input type="text" placeholder="Enter your email"
        style="
            width: 100%;
            height: 50px;
            border-radius: 10px;
            border: none;
            padding: 0 50px 0 12px;  /* space for button */
            outline: none;
            box-sizing: border-box;
        ">

    <!-- YELLOW BUTTON -->
    <div style="
        position: absolute;
        right: 4px;
        top: 4px;
        bottom: 4px;          /* stretches vertically */
        width: 36px;
        background: #f4b400;
        border-radius: 10px;  /* ALL corners rounded */
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    ">


        <!-- BLUE ARROW -->
        <span style="
            color: #0b2a5b;
            font-size: 16px;
            font-weight: bold;
        ">
            →
        </span>

    </div>

</div>
</div> 

<!-- POPULAR POST -->
<div style="
    min-width: 200px;
">

    <!-- HEADING -->
    <div style="
        font-weight: 510;
        color: white;
        margin-bottom: 15px;
        font-size: 15px;
    ">
        Popular Post
    </div>

    <!-- POSTS LIST -->
    <div style="
        display: flex;
        flex-direction: column;
        gap: 14px;
    ">

        <!-- ITEM 1 -->
        <div style="display:flex; gap:10px; align-items:center;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776681020/Lidar-Vs-Laser_What-is-the-difference_lbxrzt.webp"
                style="width:60px; height:60px; border-radius:8px; object-fit:cover;">
            <div style="color: rgba(255,255,255,0.8); font-size:13px;">
                BIM Clash Detection Guide
            </div>
        </div>

        <!-- ITEM 2 -->
        <div style="display:flex; gap:10px; align-items:center;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776680987/IoT-in-Construction_1_jgbehm.webp"
                style="width:60px; height:60px; border-radius:8px; object-fit:cover;">
            <div style="color: rgba(255,255,255,0.8); font-size:13px;">
                Construction Asset Management
            </div>
        </div>

        <!-- ITEM 3 -->
        <div style="display:flex; gap:10px; align-items:center;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776680769/Whats-the-Difference-Between-VRV-and-VRF_zmjs2x.webp"
                style="width:60px; height:60px; border-radius:8px; object-fit:cover;">
            <div style="color: rgba(255,255,255,0.8); font-size:13px;">
                GIS & BIM Integration Benefits
            </div>
        </div>

        <!-- ITEM 4 -->
        <div style="display:flex; gap:10px; align-items:center;">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776680825/Bar-Bending-Schedule-in-Construction_uhfsek.webp"
                style="width:60px; height:60px; border-radius:8px; object-fit:cover;">
            <div style="color: rgba(255,255,255,0.8); font-size:13px;">
                Smart Infrastructure Trends
            </div>
        </div>

    </div>

</div>


    </div>

</div>

<!-- FULL WIDTH GREEN DIVIDER -->
<div style="
    width: 100%;
    height: 1px;
    background: #2ecc71;
    opacity: 0.7;
    margin-top: 40px;
"></div>


<!-- BOTTOM NAV ROW -->
<div style="
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 30px;
    color: white;
    font-weight: bold;
    font-family: sans-serif;
    flex-wrap: wrap;
    gap: 20px;
">

    <!-- ABOUT COLUMN -->
<div style="min-width: 180px;">

    <div style="font-weight: 510; color: white; margin-bottom: 12px;">
        About
    </div>

    <div style="
        color: rgba(255,255,255,0.65);
        font-size: 14px;
        font-weight: 400; 
        line-height: 1.8;
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">
        <div style="cursor:pointer;">About Pinnacle</div>
        <div style="cursor:pointer;">Pinnacle Advantage</div>
        <div style="cursor:pointer;">Our Team</div>
        <div style="cursor:pointer;">Partnerships</div>
        <div style="cursor:pointer;">Awards and Milestones</div>
    </div>

</div>

<div style="min-width: 180px;">

    <div style="font-weight: 510; color: white; margin-bottom: 12px;">
        Consulting Services
    </div>

    <div style="
        color: rgba(255,255,255,0.65);
        font-weight: 400; 
        font-size: 14px;
        line-height: 1.8;
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">
        <div style="cursor:pointer;">Strategy Consulting</div>
        <div style="cursor:pointer;">Digital Transformation</div>
        <div style="cursor:pointer;">BIM Consulting</div>
        <div style="cursor:pointer;">Project Advisory</div>
        <div style="cursor:pointer;">Sustainability Consulting</div>
        <div style="cursor:pointer;">Risk Management</div>
    </div>

</div>

<div style="min-width: 180px;">

    <div style="font-weight: 510; color: white; margin-bottom: 12px;">
        Verticals
    </div>

    <div style="
        color: rgba(255,255,255,0.65);
        font-weight: 400; 
        font-size: 14px;
        line-height: 1.8;
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">
        <div style="cursor:pointer;">Architecture</div>
        <div style="cursor:pointer;">Construction</div>
        <div style="cursor:pointer;">Infrastructure</div>
        <div style="cursor:pointer;">Real Estate</div>
        <div style="cursor:pointer;">Industrial</div>
        <div style="cursor:pointer;">stadium</div>
    </div>

</div>

<div style="min-width: 180px;">

    <div style="font-weight: 510; color: white; margin-bottom: 12px;">
        Resources
    </div>

    <div style="
        color: rgba(255,255,255,0.65);
        font-weight: 400; 
        font-size: 14px;
        line-height: 1.8;
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">
        <div style="cursor:pointer;">Blogs</div>
        <div style="cursor:pointer;">Case Studies</div>
        <div style="cursor:pointer;">Whitepapers</div>
        <div style="cursor:pointer;">Guides</div>
        <div style="cursor:pointer;">publications</div>
    </div>

</div>


<div style="min-width: 180px;">

    <div style="font-weight: 510; color: white; margin-bottom: 12px;">
        Markets
    </div>

    <div style="
        color: rgba(255,255,255,0.65);
        font-size: 14px;
        font-weight: 400; 
        line-height: 1.8;
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">
        <div style="cursor:pointer;">India</div>
        <div style="cursor:pointer;">Middle East</div>
        <div style="cursor:pointer;">Europe</div>
        <div style="cursor:pointer;">USA</div>
        <div style="cursor:pointer;">Japan</div>
        <div style="cursor:pointer;">Australia</div>
    </div>

</div>

<div style="min-width: 180px;">

    <div style="font-weight: 510; color: white; margin-bottom: 12px;">
        BIM Services
    </div>

    <div style="
        color: rgba(255,255,255,0.65);
        font-size: 14px;
        line-height: 1.8;
        font-weight: 400; 
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">
        <div style="cursor:pointer;">3D BIM Modeling</div>
        <div style="cursor:pointer;">Clash Detection</div>
        <div style="cursor:pointer;">Scan to BIM</div>
        <div style="cursor:pointer;">BIM Coordination</div>
    </div>

</div>

<!-- OUR PRODUCTS FOOTER SECTION -->
<div style="margin-top: 60px;">

    <!-- MAIN HEADING -->
    <div style="
        font-weight: 510;
        color: white;
        font-size: 16px;
        margin-bottom: 14px;
    ">
        Our Products
    </div>

    <!-- SUB ITEMS (VERTICAL) -->
    <div style="
        color: rgba(255,255,255,0.65);
        font-size: 14px;
        font-weight: 400; 
        line-height: 2;
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">

        <div style="cursor:pointer;">BIM Modeling Tools</div>
        <div style="cursor:pointer;">Clash Detection Suite</div>
        <div style="cursor:pointer;">CAD Automation Tools</div>
       

    </div>

</div>

<!-- PORTFOLIO FOOTER SECTION -->
<div style="margin-top: 40px;">

    <div style="
        font-weight: 510;
        color: white;
        font-size: 16px;
        margin-bottom: 14px;
    ">
        Portfolio
    </div>

    <div style="
        color: rgba(255,255,255,0.65);
        font-size: 14px;
        font-weight: 400; 
        line-height: 2;
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">

        <div style="cursor:pointer;">Residential Projects</div>
        <div style="cursor:pointer;">Commercial Buildings</div>
        <div style="cursor:pointer;">Infrastructure Works</div>
      
    </div>

</div>


<!-- CAREERS FOOTER SECTION -->
<div style="margin-top: 40px;">

    <div style="
        font-weight: 510;
        color: white;
        font-size: 16px;
        margin-bottom: 14px;
    ">
        Careers
    </div>

    <div style="
        color: rgba(255,255,255,0.65);
        font-weight: 400; 
        font-size: 14px;
        line-height: 2;
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">

        <div style="cursor:pointer;">Current Openings</div>
        <div style="cursor:pointer;">Internships</div>
        <div style="cursor:pointer;">Life at Pinnacle</div>
        <div style="cursor:pointer;">Employee Benefits</div>
        

    </div>

</div>

<!-- CLIENTS FOOTER SECTION -->
<div style="margin-top: 40px;">

    <div style="
        font-weight: 510;
        color: white;
        font-size: 16px;
        margin-bottom: 14px;
    ">
        Clients
    </div>

    <div style="
        color: rgba(255,255,255,0.65);
        font-size: 14px;
        font-weight: 400; 
        line-height: 2;
        display: flex;
        flex-direction: column;
        gap: 6px;
    ">

        <div style="cursor:pointer;">Government Projects</div>
        <div style="cursor:pointer;">Private Developers</div>
        <div style="cursor:pointer;">Real Estate Firms</div>
        <div style="cursor:pointer;">Infrastructure Clients</div>
        <div style="cursor:pointer;">Global Partners</div>

    </div>

</div>


<!-- GREEN DIVIDER LINE (MOVED UP) -->
<div style="
    width: 100%;
    height: 1px;
    background: #2ecc71;
    opacity: 0.7;
    margin-top: 0px;   /* reduced from 50px */
"></div>

<!-- COPYRIGHT WRAPPER -->
<div style="
    margin-top: 15px;
    color: rgba(255,255,255,0.65);
    font-size: 13px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
    align-items: flex-start;
">

    <!-- LEFT SIDE -->
    <div>
        © 2026 pinnacleinfotech.com. All rights reserved.
    </div>

    <!-- RIGHT SIDE (DIGITAL PARTNER) -->
    <div style="
        display: flex;
        gap: 8px;
        align-items: center;
    ">
        <span>Digital Partner</span>
        <span style="color: white; font-weight: bold;">
            Indus Net Technologies
        </span>
    </div>

</div>



<!-- RIGHT SIDE LINKS (SEPARATE ROW) -->
<div style="
    margin-top: 12px;
    display: flex;
    justify-content: flex-end;
    gap: 18px;
    color: rgba(255,255,255,0.65);
    font-size: 13px;
    flex-wrap: wrap;
">

    <div style="cursor:pointer; font-weight: 400 !important;">Privacy Policy</div>
    <div style="cursor:pointer; font-weight: 400 !important;">Terms & Conditions</div>
    <div style="cursor:pointer; font-weight: 400 !important;">Cookies Policy</div>
    <div style="cursor:pointer; font-weight: 400 !important;">Sitemap</div>

</div>




















    </div>

</div>


""", height=1200)