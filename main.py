import streamlit as st
import sqlite3
import base64
import streamlit.components.v1 as components


# ================= PAGE CONFIG =================
st.set_page_config(page_title=" ", page_icon=" ", layout="wide")

st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
""", unsafe_allow_html=True)

# ================= DB CONNECTION =================
conn = sqlite3.connect("portal.db", check_same_thread=False)
cursor = conn.cursor()

def get_images():
    cursor.execute("SELECT image FROM images ORDER BY id ASC")
    return cursor.fetchall()

def to_base64(img):
    return base64.b64encode(img).decode()

images = get_images()



logo = None

if images and len(images) > 0:
    logo = to_base64(images[0][0])





main_img = ""
iso1 = iso2 = iso3 = ""

if len(images) >= 5:
    main_img = to_base64(images[1][0])
    iso1 = to_base64(images[2][0])
    iso2 = to_base64(images[3][0])
    iso3 = to_base64(images[4][0])

# ================= FUNCTIONS (DEFINE FIRST) =================
# ================= FUNCTIONS (DEFINE FIRST) =================
st.markdown("""

<style>

#MainMenu, header, footer {
    visibility: hidden;
}

.block-container {
    padding: 0rem !important;
    max-width: 100% !important;
}

/* NAVBAR (SLIGHTLY WIDER) */
.navbar {
    position: fixed;   /*  always stays on top */
    top: 0;
    left: 0;
    width: 100%;       /*  full width (logo to right edge) */
    z-index: 9999;

    display: flex;
    align-items: flex-start;
    justify-content: center;

    padding: 35px 45px;

    background: white;   /* IMPORTANT (so content doesn’t show through) */
}


.block-container {
    padding-top: 25px !important;  /*  adjust based on navbar height */
}




/* NAV LINKS */
.navbar a {
    text-decoration: none;
    color: black;

    font-size: 17px;
    font-weight: 400;

    white-space: nowrap;
    margin: 0 6px; 
}

/* HOVER */
.navbar a:hover {
    text-decoration: none;
}

i.bi {
    display: inline-block;
}



/* CENTER MENU */
.nav-menu {
    display: flex;
    align-items: center;
    gap: 15px;
}

/* RIGHT SIDE AREA */
.nav-right {
    position: absolute;   /*  pulls it out of center flow */
    right: 30px;          /* same as navbar padding */
    
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: -10px;
}

/* LOGIN TEXT */
.login-text {
    font-size: 17px;
    font-weight: 600;
    cursor: pointer;
    color: black;
    margin-right: 5px;
}

.login-text:hover {
    color: #0b2a5b;
}

/* YELLOW BUTTON */
.cta-btn {
    background:  #FF9F00;  /* yellow */
    color: black;
    border: none;

    padding: 10px 28px;
    border-radius: 8px;

    font-size: 15px;
    font-weight: 600;

    cursor: pointer;
}

/* BUTTON HOVER */
.cta-btn:hover {
    background: #f5c400;
}

/* SEARCH ICON */
.bi-search {
    font-size: 18px;
    cursor: pointer;
    color: black;
}

.menu-link::after {
    content: " ˅";
    font-size: 13px;
    margin-left: 4px;
}

.menu-link {
    text-decoration: none;
    color: black;

    font-size: 17px;
    font-weight: 400;

    white-space: nowrap;
    margin: 0 6px;
    cursor: pointer;
}

/* hover */
.menu-link:hover {
    color: #0b2a5b;
}

</style>

<div class="navbar">
    <span class="menu-link">About</span>
    <span class="menu-link">Our Expertise</span>
    <span class="menu-link">Portfolio</span>
    <span class="menu-link">Events</span>
    <span class="menu-link">Resources</span>
    <span class="menu-link">Career</span>
    <span class="menu-link">Blog</span>
    
<div class="nav-right">
    <span class="search-icon">
        <i class="bi bi-search"></i>
    </span>
    <span class="login-text">Login</span>
    <button class="cta-btn">Get in Touch</button>
</div>


</div>
""", unsafe_allow_html=True) 





# ================= LOGO (PUT BEFORE TEXT) =================
if logo is not None:
    st.markdown(f"""
<div style="
    position: fixed;       /* key change */
    top: 10px;             /* 👈 control vertical alignment */
    left: 25px;            /* 👈 align with navbar padding */
    z-index: 10000;
    display: flex;
    align-items: center;
">
    <img src="data:image/png;base64,{logo}" style="
        height: 60px;
        width: auto;
        object-fit: contain;
    ">
</div>
""", unsafe_allow_html=True)




#### text 
st.markdown("""
<div style="
    font-family: 'Playfair Display', serif;
    color: #002366;
    font-size: 56px;
    font-weight: 700;
    white-space: nowrap;
    padding: 20px 20px 20px 20px; 
    text-align: left;
">
    Constructing Certainty with BIM Technology
</div>
""", unsafe_allow_html=True)
# ================= VIDEO =================



video_url = "https://res.cloudinary.com/dnodncslz/video/upload/v1774435343/pinnacle-infotech-latest_h3qbk3.mp4"



components.html(f"""
<div style="
    width:100%;
    padding-left:20px;
    padding-right:10px;   /* reduced right side space */
    box-sizing:border-box;
    margin-top: -10px; 
">

    <video autoplay muted loop playsinline
        style="
            width:100%;
            height:520px;
            object-fit:cover;
            border-radius:30px;
            display:block;
        ">
        <source src="{video_url}" type="video/mp4">
    </video>

</div>
""", height=540)

# ================= IMAGE SECTION =================
# ================= IMAGE SECTION =================
html = f"""
<div style='max-width:1200px;margin:60px auto;display:flex;gap:30px;'>

<div style="width:50%;">
<h2 style='color:#002366;'>Discover Pinnacle</h2>

<p style="
    color:#4A6FA5;
    font-size:22px;
    font-weight:500;
    line-height:1.6;
    margin-top:10px;
">
Pinnacle Infotech leads the global AECO sector with Building Information Modeling (BIM), Engineering Design, and Digital Construction Solutions.
</p>

<p style="
    color:#000;
    font-size:15px;
    font-weight:400;
    line-height:1.7;
    margin-top:15px;
">
Our 30+ years of expertise drive excellence in the Design, Preconstruction, Construction Management, Digital Twin, and Facilities Management of your project.
</p>

<!-- ✅ BUTTON ADDED HERE -->
<a class="custom-btn" onclick="return false;" style="
    display:inline-flex;
    align-items:center;
    gap:10px;
    margin-top:18px;
    padding:10px 18px;
    background:#002366;
    color:white;
    border-radius:30px;
    text-decoration:none;
    font-size:14px;
    font-weight:500;
    width:max-content;
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
        color:#002366;
        font-size:16px;
        font-weight:bold;
    ">→</span>
</a>

</div>

<div style='width:50%; position:relative;'>
<img src='data:image/webp;base64,{main_img}' style='width:100%;height:420px;object-fit:cover; border-radius:20px;' />

<div style='position:absolute;bottom:70px;left:40px;background:white;padding:15px;border-radius:10px;display:flex;gap:20px;'>
<img src='data:image/webp;base64,{iso1}' style='height:60px;'>
<img src='data:image/webp;base64,{iso2}' style='height:60px;'>
<img src='data:image/webp;base64,{iso3}' style='height:60px;'>
</div>

</div>
</div>
"""

components.html(html, height=560)

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
       animation: scroll 40s linear infinite;
       will-change: transform;
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
       animation: scroll 40s linear infinite;
       will-change: transform;
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

        <a class="custom-btn" onclick="return false;">
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

    <a class="custom-btn" onclick="return false;">
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

        <a class="custom-btn" onclick="return false;">
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

        
<a class="custom-btn" onclick="return false;">
    <span>Know More</span>

    <span style="
        display: flex;
        align-items: center;
        justify-content: center;
        width: 28px;
        height: 28px;
        background: white;
        border-radius: 50%;
        color: #002366;
        font-size: 14px;
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

  <a class="custom-btn" onclick="return false;">
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
    justify-content: space-between;

    max-width: 1400px;
    margin: 0 auto;

    gap: 120px;
    padding: 60px 40px;

    box-sizing: border-box;
    overflow: visible;
    transform: translateX(60px);
}

/* TEXT BOX */
.text-box {
    max-width: 900px;
    flex: 1;
    position: relative;
    transform: translateY(-110px);
}

/* HEADING */
.text-box h3 {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 16px;

    color: #0A2A66;                  /* deep blue */
    font-family: 'Inter', 'Segoe UI', sans-serif;   
    transform: translateY(-60px);    
}





/* TEXT */
#text {
    display: block;
    width: 100%;
    font-size: 20px;
    line-height: 1.9;
    margin-top: -40px;
    display: inline-block;
    transform: skewY(-2deg);
}

/* DECK */
.deck {
    width: 420px;
    height: 520px;
    flex-shrink: 0;
    position: relative;
    margin-top: -40px; 
}

/* CARDS */
.card {
    position: absolute;
    width: 320px;
    height: 460px;
}

.card1 { transform: translate(0px,0px) rotate(-2deg); z-index:5; }
.card2 { transform: translate(8px,3px) rotate(1deg); z-index:4; }
.card3 { transform: translate(16px,6px) rotate(3deg); z-index:3; }
.card4 { transform: translate(24px,9px) rotate(-1deg); z-index:2; }
.card5 { transform: translate(32px,12px) rotate(2deg); z-index:1; }

.card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 14px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.30);
}



.controls {
    position: absolute;
    bottom: -180px;
    left: 0;
}




.btn {
    border: none;
    background: #0A2A66;
    color: white;
    padding: 8px 14px;
    margin-right: 10px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
}

/* QUOTE ICON */
.quote-icon {
    width: 90px;
    height: 120px;
    position: absolute;
    top: -65px;
    left: -90px;
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
My company was delighted with Pinnacle's performance on this project. Their project team was very helpful, got us everything we needed on time, and maintained a schedule. I will be utilizing their BIM Services again in the future.`,
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
The Pinnacle team can thoroughly review and analyze the drawing set and quickly respond with succinct questions needed to complete the task. Their responsiveness is assuring, and the quality and completeness of work are consistent with what our firm expects of all its employees.`,
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
This was a very large project with 5 jobs at the same time. The schedule was aggressive, with lots of DRBs and RFIs to incorporate. Pinnacle did a great job being organized and hit our deadlines almost 100% of the time.`,
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
The Pinnacle team can thoroughly review and analyze the drawing set and quickly respond with succinct questions needed to complete the task. Their responsiveness is assuring, and the quality and completeness of work are consistent with what our firm expects of all its employees.`,
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
Our Pinnacle team has been very helpful and very dedicated to our projects. The team is very good about asking questions and learning the process while meeting deadlines they are very professional.`,
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

components.html("""
<style>

.cta-box {
    width: 100%;
    background: #0A2A66;
    padding: 80px 40px;
    border-radius: 24px;
    text-align: center;
    font-family: sans-serif;
    color: white;
    position: relative;
    box-sizing: border-box;
    overflow: hidden;
    position: relative;
    z-index: 1;
}

/* TEXT */
.cta-title {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 12px;
}

.cta-subtitle {
    font-size: 16px;
    opacity: 0.85;
    margin-bottom: 30px;
}

/* BUTTON DEFAULT */
.cta-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;

    background: white;
    color: #0A2A66;
    padding: 10px 20px;
    border-radius: 999px;
    font-weight: 600;

    position: absolute;
    left: 50%;
    top: calc(100% - 90px);

    transform: translateX(-50%);  /*  FIXED (not full translate) */

    white-space: nowrap;
    will-change: left, top;       /*  smoother movement */
}





/* ARROW CIRCLE */
.cta-arrow-circle {
    width: 26px;
    height: 26px;
    background: #0A2A66;
    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-left: 8px;
}



.edge-mask {
    position: absolute;
    inset: 0;
    border-radius: 24px;
    pointer-events: none;
    box-shadow: inset 0 0 0 2px transparent;
    z-index: 2;
}




</style>

<div class="cta-box" id="ctaBox">
    
    <div class="cta-title">Say Hello</div>
    
    <div class="cta-subtitle">
        We’d love to hear from you and help you build something amazing
    </div>

    <div class="cta-btn" id="ctaBtn">
        <span>Reach Out Today</span>

        <div class="cta-arrow-circle">
            <span style="color:white; font-size:14px;">→</span>
        </div>
    </div>
<div class="edge-mask"></div>
</div>

<script>
const box = document.getElementById("ctaBox");
const btn = document.getElementById("ctaBtn");

box.addEventListener("mousemove", (e) => {

    const rect = box.getBoundingClientRect();
    const btnRect = btn.getBoundingClientRect();

    let x = e.clientX - rect.left;
    let y = e.clientY - rect.top;

    const halfW = btnRect.width / 2;
    const halfH = btnRect.height / 2;

    const padding = 10;

    x = Math.max(halfW + padding, Math.min(x, rect.width - halfW - padding));
    y = Math.max(halfH + padding, Math.min(y, rect.height - halfH - padding));

    btn.style.left = x + "px";
    btn.style.top = y + "px";

    /*  CRITICAL FIX */
    btn.style.transform = "translate(-50%, -50%)";
});

/* reset */
box.addEventListener("mouseleave", () => {
    btn.style.left = "50%";
    btn.style.top = "calc(100% - 90px)";
    btn.style.transform = "translateX(-50%)";
});
</script>





""", height=400)




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
    padding: 14px;
    flex: 1;
    gap: 6px;
    min-height: 230px;   /* increased height */
    display: flex;
    flex-direction: column;
    justify-content: flex-start; /* IMPORTANT */
    transition: 0.3s ease;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}


.grey-card img {
    width: 130px;        /* control size */
    height: 130px;       /* same height */
    object-fit: contain;
}




.logo-box {
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 4px;
}




.grey-card .desc {
    font-size: 13px;
    color: #555;
    line-height: 1.5;
    margin-top: -8px;   /*  move text upward */
    margin-bottom: 4px;
}




.card-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #0b2a5b;
    color: white;
    padding: 5px 12px;   /*  compact */
    border-radius: 30px;
    font-size: 12px;
    font-weight: 500;
    text-decoration: none;
    width: fit-content;
    transition: 0.25s ease;
    margin-top: 4px;   /*  slightly upward */
}

.card-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}
.card-btn .circle {
    width: 20px;
    height: 20px;
    background: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.card-btn .circle span {
    color: #0b2a5b;
    font-size: 11px;
    font-weight: bold;
}

.tab-btn {
    position: relative;  /* IMPORTANT */
}

/* ▼ Arrow */
.tab-btn::after {
    content: "";
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: -12px;

    width: 0;
    height: 0;
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-top: 10px solid #0b2a5b; /* same as active tab */

    opacity: 0;
    transition: 0.3s ease;
}

/* Show only for active tab */
.active-tab::after {
    opacity: 1;
}



</style>

<div class="container mt-4">

    <!-- TABS -->
    <div style="width:1100px; margin:0 auto;">
    <div class="d-flex justify-content-between">
        <button class="tab-btn active-tab" onclick="showTab('products', this)">Our Products</button>
        <button class="tab-btn" onclick="showTab('solutions', this)">Our Specialized Solutions</button>
        <button class="tab-btn" onclick="showTab('software', this)">Software We Use</button>
    </div>
</div>

    <!-- CONTENT -->
   <div class="row mt-4 gx-2 align-items-stretch" style="width:1100px; margin:0 auto;">

        <!-- LEFT SIDE (TEXT + CARDS) -->
        <div class="col-auto no-padding">

            <!-- PRODUCTS -->
            <div id="products" class="tab-section " style="width:620px;">
                <div class="p-3 bg-light rounded text-left">
                    The workforce at Pinnacle is proficient in software platforms spanning the entire construction lifecycle. They include software for design, 3D modeling/rendering, BIM modeling/fabrication, CAD drafting, and Common Data Environment. Using these software tools, we implement advanced workflows that streamline interdisciplinary coordination, facilitate proactive clash resolution, and help clients achieve the best-in-class outputs.
                </div>

                <div style="display:flex; gap:12px; margin-top:14px;">

<div class="grey-card">

    <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776839659/vdc-logo_bth6y1.webp">

    <div class="desc">
        Integrate PiVDC, an innovation of Pinnacle. into your daily workflow to automate repetitive tasks.


    </div>

<a class="card-btn" onclick="return false;">
    <span>Know More</span>

    <span class="circle">
        <span>→</span>
    </span>
</a>
    

</div>

<div class="grey-card">

    <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776840965/innomaint-logo_3_tia3bq.webp">

    <div class="desc">
        

A product of Pinnacle, InnoMaint integrates with Digital Twins for top-tier tech driven 


    </div>

<a class="card-btn" onclick="return false;">
    <span>Know More</span>

    <span class="circle">
        <span>→</span>
    </span>
</a>


</div>

<div class="grey-card">

    <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776841013/cd-logo_1_xkfxsy.webp">

    <div class="desc">
        

Need a customized plugin? Share your requirements and kickstart the development process.




    </div>

   <a class="card-btn" onclick="return false;">
    <span>Know More</span>

    <span class="circle">
        <span>→</span>
    </span>
</a>


</div>



                </div>
            </div>

            <!-- SOLUTIONS -->
<!-- SOLUTIONS -->
<div id="solutions" class="tab-section d-none" style="width:620px;">

    <div class="p-3 bg-light rounded text-left">
        Beyond our core services, Pinnacle is a proud Autodesk Learning and Reselling partner and also delivers exclusive CAD support to HP. Being an Authorized Training Centre (ATC), our sessions comply with Autodesk’s training benchmarks. As a valued partner of HP, Pinnacle’s expertise in accurately converting 2D CAD files or 3D models into 2D DXF files powers HP SitePrint’s core operations.
    </div>

    <div style="display:flex; gap:12px; margin-top:14px;">

        <div class="grey-card">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776849531/atc-logo_odfqvi.webp">
            <div class="desc">Get industry-grade training from certified instructors on the latest Autodesk software products.</div>

            <a class="card-btn" onclick="return false;">
                <span>Know More</span>
                <span class="circle"><span>→</span></span>
            </a>
        </div>

        <div class="grey-card">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776849531/atc-logo_odfqvi.webp">
            <div class="desc">Pinnacle is an authorized partner of Autodesk, offering genuine software license and top-tier support.</div>

            <a class="card-btn" onclick="return false;">
                <span>Know More</span>
                <span class="circle"><span>→</span></span>
            </a>
        </div>

        <div class="grey-card">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776849613/hp-site-print-service_ur2rst.webp">
            <div class="desc">Exclusive CAD support services in partnership with HP for precise and error-free construction site layouts.</div>

            <a class="card-btn" onclick="return false;">
                <span>Know More</span>
                <span class="circle"><span>→</span></span>
            </a>
        </div>

    </div>

</div>





            <!-- SOFTWARE -->
            
<!-- SOFTWARE -->
<div id="software" class="tab-section d-none" style="width:620px;">

    <!-- PARAGRAPH (same style as others) -->
    <div class="p-3 bg-light rounded text-left">
        The workforce at Pinnacle is proficient in software platforms spanning the entire construction lifecycle. They include software for design, 3D modeling/rendering, BIM modeling/fabrication, CAD drafting, and Common Data Environment.
    </div>

    <!-- CARDS -->
    <div style="display:flex; gap:12px; margin-top:14px;">

        <div class="grey-card">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776849531/atc-logo_odfqvi.webp">

            <div class="desc">
                Pinnacle uses top-tier Autodesk solutions to drive excellence and agility in project execution.
            </div>

            <a class="card-btn" onclick="return false;">
                <span>Know More</span>
                <span class="circle"><span>→</span></span>
            </a>
        </div>

        <div class="grey-card">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776851269/bentley-logo_zn61i4.webp">

            <div class="desc">
                
        Using a range of Bentley offerings for design, 3D modeling, CAD drafting, and more.




            </div>

            <a class="card-btn" onclick="return false;">
                <span>Know More</span>
                <span class="circle"><span>→</span></span>
            </a>
        </div>

        <div class="grey-card">
            <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776851319/tekla-logo_uv6fde.webp">

            <div class="desc">
                Leveraging Tekla for well-coordinated, accurate, and fabrication-ready BIM models.
            </div>

            <a class="card-btn" onclick="return false;">
                <span>Know More</span>
                <span class="circle"><span>→</span></span>
            </a>
        </div>

    </div>

</div>
</div>

<!-- RIGHT SIDE IMAGE -->
<!-- IMAGE BELOW CONTENT -->

<!-- RIGHT SIDE IMAGE -->
<div class="col-auto no-padding "style="margin-left:60px ;margin-top:5px;">

    <div id="products-img" class="tab-img " style="width:420px; height:100%;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776344032/our_products_2_g6lnrn.webp"
             style="width:100%; height:100%; object-fit:cover; border-radius:12px;">
    </div>

    <div id="solutions-img" class="tab-img d-none" style="width:420px; height:100%;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776411327/our_specilized_solutions_hv8egs.webp"
             style="width:100%; height:100%; object-fit:cover; border-radius:12px;">
    </div>

    <div id="software-img" class="tab-img d-none" style="width:420px; height:100%;">
        <img src="https://res.cloudinary.com/dnodncslz/image/upload/v1776411367/software_we_use_2_rjrfyh.webp"
             style="width:100%; height:100%; object-fit:cover; border-radius:12px;">
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


window.onload = function () {
    const defaultBtn = document.querySelector('.tab-btn');
    showTab('products', defaultBtn);
};




</script>

""", height=680)


#### bar#### 
components.html("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<div style="
    width: 100%;
   background: linear-gradient(135deg, #5f88cd, #3f66a6);
    padding: 50px 20px;
    margin-top: 40px;
    border-radius: 18px;
    position: relative;
">

    <!-- LEFT CENTER LABEL -->
    




    <div class="container">


 <!-- FLEX WRAPPER -->
    <div style="display:flex; align-items:center; gap:5px;">

        <!-- LEFT TEXT -->
        <div style="
            font-size:22px;
            font-weight:700;
            color:white;
            white-space:nowrap;
            min-width:120px;
        ">
            Our CSR
        </div>



<div style="flex:1;">








        <div class="row justify-content-start g-3">

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
    background: linear-gradient(135deg, #587dd0, #2f548f);
    padding: 60px 70px;
    border-radius: 18px;
    min-width: 380px;
    min-height: 180px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    text-align: center;
">

    <!-- SMALL TITLE -->
    <div style="
        color: white;
        font-size: 18px;
        font-weight: 500;
        letter-spacing: 1px;
        margin-bottom: 8px;
        opacity: 0.9;
    ">
        Build Your Career
    </div>

    <!-- MAIN TITLE -->
   <div style="
    color: white;
    font-size: 32px;
    font-weight: 700;
    font-family: 'Playfair Display', serif;
    letter-spacing: 0.5px;
    margin-bottom: 20px;
">
    Grow At Pinnacle
</div>
    <!-- DESCRIPTION -->
    <div style="
        color: white;
        font-size: 17px;
        line-height: 1.6;
        max-width: 320px;
        margin-bottom: 25px;
        opacity: 0.95;
    ">
        Join our team for meaningful career growth along with personal development programs.
    </div>

   <!-- BUTTON WITH ATTACHED ARROW -->
<div style="
    display: inline-flex;
    align-items: center;
    background: white;
    border-radius: 50px;
    padding: 6px;
">

    <!-- TEXT PART -->
    <div style="
        color: #355c9a;
        padding: 10px 18px;
        font-weight: 700;
        font-size: 15px;
        white-space: nowrap;
    ">
        View all opportunities
    </div>

    <!-- ARROW CIRCLE (INSIDE CAPSULE) -->
    <div style="
        width: 34px;
        height: 34px;
      background: #243f73;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 16px;
        font-weight: bold;
    ">
        →
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

<style>
.custom-btn {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    background: #002366;
    color: white;
    padding: 10px 20px;
    border-radius: 50px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    transition: 0.3s ease;
}

.custom-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(0,0,0,0.18);




</style>

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

<!-- KNOW MORE BUTTON -->
<div style="margin-top:20px;">

<a class="custom-btn" onclick="return false;">
    <span>Know More</span>

    <span style="
        display:flex;
        align-items:center;
        justify-content:center;
        width:28px;
        height:28px;
        background:white;
        border-radius:50%;
        color:#002366;
        font-size:14px;
        font-weight:bold;
    ">
        →
    </span>
</a>

</div>

</div>

</div>

<!-- RIGHT SIDE IMAGES -->
<div id="imageContainer" style="display:flex; flex-direction:column; gap:14px; margin-top:5px;">

<div id="row1" style="display:flex; gap:14px; justify-content:flex-start;">
    <img id="img1" style="width:280px;height:320px;border-radius:14px;object-fit:cover;">
    <img id="img2" style="width:280px;height:180px;border-radius:14px;object-fit:cover;">
    <img id="img3" style="width:280px;height:320px;border-radius:14px;object-fit:cover;">
</div>

<div style="display:flex; gap:14px;">
    <img id="img4" style="width:280px;height:180px;border-radius:14px;object-fit:cover;">
    <img id="img5" style="width:280px;height:320px;border-radius:14px;object-fit:cover; transform: translateY(-130px);">
    <img id="img6" style="width:280px;height:180px;border-radius:14px;object-fit:cover;">
</div>

</div>

</div>
</div>
</div>

<script>

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

function changeImages(type){

    const imgs = imageSets[type];
    const row1 = document.getElementById("row1");

    // reset layout
    row1.style.display = "flex";
    row1.style.justifyContent = "flex-start";

    // reset all images
    for(let i=1;i<=6;i++){
        const el = document.getElementById("img"+i);
        el.src = "";
        el.style.display = "none";
        el.style.visibility = "visible";
    }

    // =========================
    // TUTORIALS ONLY
    // =========================
    if(type === "tutorials"){

    // show ONLY first image (LEFT box)
    const el = document.getElementById("img1");
    el.src = imageSets.tutorials[0];
    el.style.display = "block";
    el.style.visibility = "visible";

    // hide others BUT keep space (so layout doesn't break)
    for(let i=2;i<=6;i++){
        const e = document.getElementById("img"+i);
        e.src = "";
        e.style.visibility = "hidden";  //  IMPORTANT (not display none)
        e.style.display = "block";      // keep structure
    }

    return;
}
    // =========================
    // ALL OTHER SECTIONS
    // =========================
    let count = 0;

    for(let i=1;i<=6;i++){
        const el = document.getElementById("img"+i);

        if(imgs[i-1]){
            el.src = imgs[i-1];
            el.style.display = "block";
            count++;
        }
    }

    // hide remaining empty slots (important for case studies)
    for(let i=count+1;i<=6;i++){
        const el = document.getElementById("img"+i);
        el.style.display = "none";
    }
}

changeImages('live');

</script>

""", height=630)


st.markdown("""
<style>
.block-container {
    padding-bottom: 0rem !important;
}
</style>
""", unsafe_allow_html=True)






#### BlUE CONTENT BOX ### 
#### BlUE CONTENT BOX ### 

components.html("""
<div style="
    width: 100%;
    margin-top: 20px;
">

    <!-- BLUE BAR -->
    
<div style="
    width: 100%;
    background: #0b2a5b;
    border-radius: 30px;
    min-height: 1000px;
    box-sizing: border-box;
    font-family: sans-serif;

    display: flex;
    justify-content: center;
    padding: 60px 20px;
">



<div style="
    width: 100%;
    max-width: 1200px;
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
    flex-wrap: wrap;   /* FIX: was nowrap */
    align-items: flex-start;
    margin-left: 40px; /* reduced from 60px */
    color: white;
    font-size: 16px;
    width: 100%;
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
            padding: 0 50px 0 12px;  
            outline: none;
            box-sizing: border-box;
        ">

    <!-- YELLOW BUTTON -->
    <div style="
        position: absolute;
        right: 4px;
        top: 4px;
        bottom: 4px;          
        width: 36px;
        background: #f4b400;
        border-radius: 10px;  
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
    margin-bottom: 35px;
    margin-top:40px;
"></div>

<!-- FOOTER WRAPPER -->
<div>

<!-- TOP ROW -->
<!-- TOP ROW (WITH SUBHEADINGS LIKE SECOND ROW) -->
<div style="
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 40px;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 80px;
">

    <!-- ABOUT -->
    <div>
        <div style="font-weight:510; color:white; margin-bottom:12px;">About</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>Company Overview</div>
            <div>Our Story</div>
            <div>Leadership Team</div>
            <div>CSR</div>
            <div>Partnership</div>
            <div>Our Team</div>


        </div>
    </div>

    <!-- CONSULTING SERVICES -->
    <div>
        <div style="font-weight:510; color:white; margin-bottom:12px;">Consulting Services</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>BIM Consulting</div>
            <div>Digital Transformation</div>
            <div>Project Advisory</div>
            <div>ISO 19650</div>
            <div>BIM Execution Plan</div>
            <div>Automation</div>
            <div>Training</div>

        </div>
    </div>

    <!-- VERTICALS -->
    <div>
        <div style="font-weight:510; color:white; margin-bottom:12px;">Verticals</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>Residential</div>
            <div>Commercial</div>
            <div>Infrastructure</div>
            <div>Data Centre</div>
            <div>Industrial</div>
            <div>Stadium</div>
        </div>
    </div>

    <!-- RESOURCES -->
    <div>
        <div style="font-weight:510; color:white; margin-bottom:12px;">Resources</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>Blogs</div>
            <div>Case Studies</div>
            <div>Brochures</div>
            <div>Blog</div>
            <div>Events</div>
            <div>Publications</div>
            <div>Whitepapers</div>
        </div>
    </div>

    <!-- MARKETS -->
    <div>
        <div style="font-weight:510; color:white; margin-bottom:12px;">Markets</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>India</div>
            <div>Middle East</div>
            <div>Global Projects</div>
             <div>Germany</div>
              <div>Japan</div>
               <div>UAE</div>
        </div>
    </div>

    <!-- BIM SERVICES -->
    <div>
        <div style="font-weight:510; color:white; margin-bottom:12px;">BIM Services</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>3D Modeling</div>
            <div>Clash Detection</div>
            <div>Mechanical</div>
            <div>Coordination</div>
            <div>Plumbing</div>
        </div>
    </div>

</div>

<!-- SECOND ROW (FIXED PROPER GRID) -->
<div style="
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
    justify-content: space-between;
    width: 100%;
    margin-top: 100px;
">

    <div style="min-width:180px; flex:1;">
        <div style="font-weight:510; color:white; margin-bottom:14px;">Our Products</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>BIM Modeling Tools</div>
            <div>Clash Detection Suite</div>
            <div>CAD Automation Tools</div>
        </div>
    </div>

    <div style="min-width:180px; flex:1;">
        <div style="font-weight:510; color:white; margin-bottom:14px;">Portfolio</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>Residential Projects</div>
            <div>Commercial Buildings</div>
            <div>Infrastructure Works</div>
        </div>
    </div>

    <div style="min-width:180px; flex:1;">
        <div style="font-weight:510; color:white; margin-bottom:14px;">Careers</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>Current Openings</div>
            <div>Internships</div>
            <div>Life at Pinnacle</div>
            <div>Employee Benefits</div>
        </div>
    </div>

    <div style="min-width:180px; flex:1;">
        <div style="font-weight:510; color:white; margin-bottom:14px;">Clients</div>
        <div style="color:rgba(255,255,255,0.65); font-size:14px; line-height:2;">
            <div>Government Projects</div>
            <div>Private Developers</div>
            <div>Real Estate Firms</div>
            <div>Infrastructure Clients</div>
            <div>Global Partners</div>
        </div>
    </div>

</div>

</div>

<!-- GREEN DIVIDER -->
<div style="
    width: 100%;
    height: 1px;
    background: #2ecc71;
    opacity: 0.7;
    margin-top: 25px;
"></div>

<!-- COPYRIGHT -->
<div style="
    margin-top: 15px;
    color: rgba(255,255,255,0.65);
    font-size: 13px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
">

    <div>© 2026 pinnacleinfotech.com. All rights reserved.</div>

    <div style="display:flex; gap:8px;">
        <span>Digital Partner</span>
        <span style="color:white; font-weight:bold;">Indus Net Technologies</span>
    </div>

</div>

<!-- POLICY LINKS -->
<div style="
    margin-top: 12px;
    display: flex;
    justify-content: flex-end;
    gap: 18px;
    color: rgba(255,255,255,0.65);
    font-size: 13px;
    flex-wrap: wrap;
">

    <div>Privacy Policy</div>
    <div>Terms & Conditions</div>
    <div>Cookies Policy</div>
    <div>Sitemap</div>

</div>

""", height=1110)

