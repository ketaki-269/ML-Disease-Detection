import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="HealthWise", layout="wide")

# Function to encode images in Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load and encode images
logo_path = "pictures/logo.jpg"
injection_image_path = "pictures/injection.jpg"
influenza_image_path = "pictures/influenza.jpg"
kidney_stones_path = "pictures/kidneystone.jpg"
migraine_path="pictures/migraine.jpg"  # Add this new image path
arthritis_path="pictures/arthritis.jpg"  # Add this new image path
parkinson_path="pictures/parkinson.jpg"  # Add this new image path
tuberculosis_path="pictures/tuberculosis.jpg"  # Add this new image path
varicoseveins_path="pictures/varicoseveins.jpg"  # Add this new image path
hypertension_path="pictures/hypertension.jpg"  # Add this new image path
heartdisease_path="pictures/heartd.jpg"  # Add this new image path
diabetes_path="pictures/diabetes.jpg"  # Add this new image path





encoded_logo = get_base64_image(logo_path)
encoded_injection = get_base64_image(injection_image_path)
encoded_influenza = get_base64_image(influenza_image_path)
encoded_kidney_stones = get_base64_image(kidney_stones_path)  
encoded_migraine=get_base64_image(migraine_path) 
encoded_arthritis=get_base64_image(arthritis_path) # Encode the new image
encoded_parkinson=get_base64_image(parkinson_path) # Encode the new image
encoded_tuberculosis=get_base64_image(tuberculosis_path) # Encode the new image
encoded_varicoseveins=get_base64_image(varicoseveins_path) # Encode the new image
encoded_hypertension=get_base64_image(hypertension_path) # Encode the new image
encoded_heartdisease=get_base64_image(heartdisease_path) # Encode the new image
encoded_diabetes=get_base64_image(diabetes_path) # Encode the new image
encoded_heartdisease=get_base64_image(heartdisease_path) # Encode the new image




# --- Navigation Bar ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: white;
        padding: 15px 30px;
        border-bottom: 2px solid #ddd;
        font-family: 'Poppins', sans-serif;
    }}
    .navbar .left-section {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}
    .navbar .app-name {{
        font-size: 24px;
        font-weight: 600;
        color: #333;
        cursor: pointer;
        padding: 8px 15px;
        border-radius: 5px;
        transition: background-color 0.3s ease, color 0.3s ease;
    }}
    .navbar .app-name:hover {{
        background-color: #007bff;
        color: white;
    }}
    .navbar .nav-links {{
        display: flex;
        align-items: center;
        gap: 25px;
    }}
    .navbar .nav-links a {{
        text-decoration: none;
        color: #333;
        font-size: 18px;
        font-weight: 500;
        transition: color 0.3s ease;
    }}
    .navbar .nav-links a:hover {{
        color: #007bff;
    }}
    .navbar img {{
        height: 50px;
        width: 50px;
        border-radius: 50%;
    }}
    .search-bar {{
        padding: 8px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 15px;
        width: 250px;
        outline: none;
    }}
    .upper-heading {{
        text-align: left;
        font-size: 28px;
        font-weight: 600;
        color: #333;
        margin: 30px 0 10px 30px;
        font-family: 'Poppins', sans-serif;
        font-style: italic;
    }}
    .image-container {{
        text-align: center;
        margin-top: 10px;
    }}
    .image-container img {{
        width: 80%;
        max-width: 800px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }}
</style>

<div class="navbar">
    <div class="left-section">
        <img src="data:image/jpeg;base64,{encoded_logo}" alt="Logo">
        <div class="app-name" onclick="location.reload()">HealthWise</div>
    </div>
    <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
        <input type="text" class="search-bar" placeholder="Search...">
    </div>
</div>

<h2 class="upper-heading"><i>Disease Precautions</i></h2>

<div class="image-container">
    <img src="data:image/jpeg;base64,{encoded_injection}" alt="Injection Image">
</div>
""", unsafe_allow_html=True)

# --- Subheading ----
st.markdown("""
<style>
    .subheading-section {
        padding: 60px;
        text-align: center;
        background-color: white;
        font-family: 'Poppins', sans-serif;
    }
    .subheading-heading {
        font-size: 40px;
        font-weight: bold;
        font-style: italic;
        color: #000000;
        margin-bottom: 20px;
    }
</style>
<div class="subheading-section">
    <div class="subheading-heading">Common Diseases and Precautions</div>
</div>
""", unsafe_allow_html=True)

# --- CSS Styles ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    body {
        font-family: 'Poppins', sans-serif;
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: white;
        padding: 15px 30px;
        border-bottom: 2px solid #ddd;
    }

    .navbar .app-name {
        font-size: 24px;
        font-weight: 600;
        color: #333;
        cursor: pointer;
    }

    .subheading-section {
        text-align: center;
        font-family: 'Poppins', sans-serif;
    }

    .subheading-heading {
        font-size: 30px;
        font-weight: bold;
        font-style: italic;
        margin-bottom: 20px;
    }

    .card-container {
        display: flex;
        align-items: center;
        gap: 20px;
        cursor: pointer;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        background-color: white;
        transition: all 0.3s ease-in-out;
        max-width: 500px;
        margin-bottom: 20px;
    }

    .card-container:hover {
        box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.3);
    }

    .card-container img {
        width: 80px;
        height: 80px;
        border-radius: 10px;
    }

    .disease-title {
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }

    .expanded-card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        background-color: white;
        width: 100%;
        max-width: 600px;
        margin-bottom: 20px;
    }

    .expanded-card ul {
        text-align: left;
        padding-left: 20px;
    }

    .expanded-card li {
        font-size: 16px;
        margin: 5px 0;
    }
    
    .feature-card {
        display: flex;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        background-color: white;
        width: 100%;
        max-width: 600px;
        margin-bottom: 20px;
        gap: 20px;
    }
    
    .feature-card-content {
        flex: 1;
    }
    
    .feature-card img {
        width: 150px;
        height: 150px;
        border-radius: 10px;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for both cards
if "expanded_influenza" not in st.session_state:
    st.session_state.expanded_influenza = False
if "expanded_kidney" not in st.session_state:
    st.session_state.expanded_kidney = False
if "expanded_migraine" not in st.session_state:
    st.session_state.expanded_migraine = False
if "expanded_arthritis" not in st.session_state:
    st.session_state.expanded_arthritis = False
if "expanded_parkinson" not in st.session_state:
    st.session_state.expanded_parkinson = False
if "expanded_tuberculosis" not in st.session_state:
    st.session_state.expanded_tuberculosis = False
if "expanded_varicoseveins" not in st.session_state:
    st.session_state.expanded_varicoseveins = False
if "expanded_hypertension" not in st.session_state:
    st.session_state.expanded_hypertension = False
if "expanded_heartdisease" not in st.session_state:
    st.session_state.expanded_heartdisease = False
if "expanded_diabetes" not in st.session_state:
    st.session_state.expanded_diabetes = False

# Function to toggle card states
def toggle_influenza():
    st.session_state.expanded_influenza = not st.session_state.expanded_influenza

def toggle_kidney():
    st.session_state.expanded_kidney = not st.session_state.expanded_kidney

def toggle_migraine():
        st.session_state.expanded_migraine = not st.session_state.expanded_migraine

def toggle_arthritis():
        st.session_state.expanded_arthritis = not st.session_state.expanded_arthritis

def toggle_parkinson():
        st.session_state.expanded_parkinson = not st.session_state.expanded_parkinson

def toggle_tuberculosis():
        st.session_state.expanded_tuberculosis = not st.session_state.expanded_tuberculosis

def toggle_varicoseveins():
        st.session_state.expanded_varicoseveins = not st.session_state.expanded_varicoseveins

def  toggle_hypertension():
        st.session_state.expanded_hypertension = not st.session_state.expanded_hypertension

def toggle_heart_disease():
        st.session_state.expanded_heartdisease = not st.session_state.expanded_heartdisease

def toggle_diabetes():
        st.session_state.expanded_diabetes = not st.session_state.expanded_diabetes

# --- Display Logo ---


# --- Display Cards ---

# Influenza Card
if st.button("🤧 Aacho, Know More ", key="influenza_card"):
    toggle_influenza()

if not st.session_state.expanded_influenza:
    # Collapsed View
    st.markdown(
        f"""
        <div class="card-container">
            <img src="data:image/jpeg;base64,{encoded_influenza}" alt="Influenza">
            <span class="disease-title">Influenza</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Expanded View
    st.markdown(
        f"""
        <div class="expanded-card">
            <img src="data:image/jpeg;base64,{encoded_influenza}" alt="Influenza" style="width: 100%; border-radius: 10px;">
            <h2>Influenza</h2>
            <ul>
                <li>💉 <strong>Get Vaccinated</strong> – Annual flu shots help prevent infection.</li>
                <li>🧼 <strong>Practice Good Hygiene</strong> – Wash hands frequently with soap for at least 20 seconds.</li>
                <li>🤧 <strong>Cover Coughs & Sneezes</strong> – Use a tissue or your elbow to prevent spreading germs.</li>
                <li>🚫 <strong>Avoid Touching Face</strong> – Especially eyes, nose, and mouth to reduce infection risk.</li>
                <li>🏠 <strong>Stay Home if Sick</strong> – Prevent spreading the virus to others.</li>
                <li>🏥 <strong>Seek Medical Attention if Needed</strong> – Especially if symptoms worsen.</li>
                <li>💨 <strong>Ensure Good Ventilation</strong> – Open windows or use air purifiers to reduce airborne particles.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# Kidney Stones Card
if st.button("Click Me", key="kidney_card"):
    toggle_kidney()

if not st.session_state.expanded_kidney:
    # Collapsed View
    st.markdown(
        f"""
        <div class="card-container">
            <img src="data:image/jpeg;base64,{encoded_kidney_stones}" alt="Kidney Stones">
            <span class="disease-title">Kidney Stones</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Expanded View
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-card-content">
                <h3>Kidney Stones</h3>
                <ul>
                    <li>💧 <strong>Stay Hydrated</strong> – Drink plenty of water to help flush out minerals.</li>
                    <li>🥗 <strong>Maintain a Balanced Diet</strong> – Reduce sodium and eat calcium-rich foods.</li>
                    <li>🚫 <strong>Limit Oxalate-Rich Foods</strong> – Avoid spinach, nuts, and chocolate if prone to stones.</li>
                    <li>⚖ <strong>Monitor Protein Intake</strong> – Too much animal protein can increase risk.</li>
                    <li>☕ <strong>Limit Caffeine & Sugary Drinks</strong> – These can lead to dehydration.</li>
                    <li>🏃 <strong>Stay Active</strong> – Regular exercise helps kidney function.</li>
                    <li>🔍 <strong>Know the Symptoms</strong> – Severe pain, blood in urine, and nausea may indicate stones.</li>
                    <li>🏥 <strong>Seek Medical Advice</strong> – If experiencing severe pain or recurring stones.</li>
                    <li>💊 <strong>Follow Prescribed Treatments</strong> – Medications or lifestyle changes may be needed.</li>
                </ul>
            </div>
            <img src="data:image/jpeg;base64,{encoded_kidney_stones}" alt="Kidney Stones">
        </div>
        """,
        unsafe_allow_html=True
    )
# Migraine Card
if st.button("Click Me", key="migraine_card"):
    toggle_migraine()

if not st.session_state.expanded_migraine:
    # Collapsed View
    st.markdown(
        f"""
        <div class="card-container">
            <img src="data:image/jpeg;base64,{encoded_migraine}" alt="Migraine">
            <span class="disease-title">Migraine</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Expanded View
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-card-content">
                <h3>Migraine</h3>
                <ul>
                    <li>💊 <strong>Manage Triggers</strong> – Identify and avoid food, stress, or environmental triggers.</li>
                    <li>💦 <strong>Stay Hydrated</strong> – Dehydration can contribute to migraines, so drink enough water.</li>
                    <li>😴 <strong>Maintain a Regular Sleep Schedule</strong> – Ensure consistent sleep patterns to prevent attacks.</li>
                    <li>🧘 <strong>Practice Stress Management</strong> – Meditation, deep breathing, and yoga can help reduce stress-related migraines.</li>
                    <li>🥗 <strong>Eat a Balanced Diet</strong> – Avoid skipping meals and reduce intake of processed foods.</li>
                    <li>🚫 <strong>Limit Caffeine & Alcohol</strong> – Excessive consumption can trigger migraines.</li>
                    <li>💡 <strong>Avoid Bright Lights & Loud Noises</strong> – Sensory overload can worsen migraine symptoms.</li>
                    <li>🏃 <strong>Engage in Moderate Exercise</strong> – Regular physical activity can help reduce migraine frequency.</li>
                    <li>🩺 <strong>Seek Medical Advice</strong> – Consult a doctor for proper diagnosis and medication if migraines persist.</li>
                </ul>
            </div>
            <img src="data:image/jpeg;base64,{encoded_migraine}" alt="Migraine">
        </div>
        """,
        unsafe_allow_html=True
    )
# Hypertension Card
if st.button("Click Me", key="hypertension_card"):
    toggle_hypertension()

if not st.session_state.expanded_hypertension:
    # Collapsed View
    st.markdown(
        f"""
        <div class="card-container">
            <img src="data:image/jpeg;base64,{encoded_hypertension}" alt="Hypertension">
            <span class="disease-title">Hypertension</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Expanded View
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-card-content">
                <h3>Hypertension</h3>
                <ul>
                    <li>🥗 <strong>Eat a Healthy Diet</strong> – Focus on fruits, vegetables, whole grains, and low-sodium foods.</li>
                    <li>🏃‍♂ <strong>Stay Physically Active</strong> – Regular exercise like walking or cycling helps lower blood pressure.</li>
                    <li>⚖ <strong>Maintain a Healthy Weight</strong> – Excess weight increases strain on the heart.</li>
                    <li>🚫 <strong>Limit Salt Intake</strong> – Reduce processed and fast food consumption.</li>
                    <li>🥤 <strong>Reduce Caffeine & Alcohol</strong> – Excessive consumption can elevate blood pressure.</li>
                    <li>😌 <strong>Manage Stress</strong> – Practice meditation, deep breathing, or yoga to keep blood pressure in check.</li>
                    <li>💧 <strong>Stay Hydrated</strong> – Drinking enough water supports overall heart health.</li>
                    <li>🩺 <strong>Monitor Blood Pressure Regularly</strong> – Keep track of your readings to detect any changes early.</li>
                    <li>💊 <strong>Follow Medical Advice</strong> – Take prescribed medications and consult a doctor if needed.</li>
                </ul>
            </div>
            <img src="data:image/jpeg;base64,{encoded_hypertension}" alt="Hypertension">
        </div>
        """,
        unsafe_allow_html=True
    )

# Initialize session state variables if they don't exist
if 'expanded_heart_disease' not in st.session_state:
    st.session_state.expanded_heart_disease = False

def toggle_heart_disease():
    st.session_state.expanded_heart_disease = not st.session_state.expanded_heart_disease

# Heart Disease Card
if st.button("Click Me", key="heart_disease_card"):
    toggle_heart_disease()

if not st.session_state.expanded_heart_disease:
    # Collapsed View
    st.markdown(
        f"""
        <div class="card-container">
            <img src="data:image/jpeg;base64,{encoded_heartdisease}" alt="Heart Disease">
            <span class="disease-title">Heart Disease</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Expanded View
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-card-content">
                <h3>Heart Disease</h3>
                <ul>
                    <li>🥗 <strong>Eat a Heart-Healthy Diet</strong> – Include fruits, vegetables, whole grains, and healthy fats.</li>
                    <li>🏃‍♂ <strong>Stay Physically Active</strong> – Regular exercise strengthens the heart and improves circulation.</li>
                    <li>⚖ <strong>Maintain a Healthy Weight</strong> – Reducing excess weight lowers heart disease risk.</li>
                    <li>🚭 <strong>Avoid Smoking & Tobacco</strong> – Smoking damages blood vessels and increases heart disease risk.</li>
                    <li>🥤 <strong>Limit Alcohol & Caffeine</strong> – Excessive intake can raise blood pressure and strain the heart.</li>
                    <li>😌 <strong>Manage Stress</strong> – Practice meditation, yoga, or deep breathing to reduce stress levels.</li>
                    <li>🩺 <strong>Monitor Blood Pressure & Cholesterol</strong> – Regular check-ups help detect early signs of heart disease.</li>
                    <li>💊 <strong>Take Medications as Prescribed</strong> – Follow your doctor's advice for managing conditions like hypertension or diabetes.</li>
                    <li>💧 <strong>Stay Hydrated</strong> – Drinking enough water supports cardiovascular health.</li>
                </ul>
            </div>
            <img src="data:image/jpeg;base64,{encoded_heartdisease}" alt="Heart Disease">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state for diabetes card
if 'expanded_diabetes' not in st.session_state:
    st.session_state.expanded_diabetes = False

def toggle_diabetes():
    st.session_state.expanded_diabetes = not st.session_state.expanded_diabetes

# Diabetes Card
if st.button("Click Me", key="diabetes_card"):
    toggle_diabetes()

if not st.session_state.expanded_diabetes:
    # Collapsed View
    st.markdown(
        f"""
        <div class="card-container">
            <img src="data:image/jpeg;base64,{encoded_diabetes}" alt="Diabetes">
            <span class="disease-title">Diabetes</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Expanded View
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-card-content">
                <h3>Diabetes</h3>
                <ul>
                    <li>🥗 <strong>Eat a Balanced Diet</strong> – Focus on whole grains, lean proteins, and fiber-rich foods while limiting sugar and processed foods.</li>
                    <li>🏃‍♂ <strong>Stay Physically Active</strong> – Regular exercise helps regulate blood sugar levels and improve overall health.</li>
                    <li>⚖ <strong>Maintain a Healthy Weight</strong> – Keeping a healthy weight reduces the risk of diabetes complications.</li>
                    <li>💉 <strong>Monitor Blood Sugar Levels</strong> – Regularly check your blood glucose levels as advised by your doctor.</li>
                    <li>💊 <strong>Take Medications as Prescribed</strong> – Follow medical advice for insulin or other diabetes medications.</li>
                    <li>🚫 <strong>Limit Sugar & Refined Carbs</strong> – Reduce intake of sweets, sodas, and processed foods to prevent blood sugar spikes.</li>
                    <li>🩺 <strong>Regular Health Checkups</strong> – Monitor for complications like nerve damage, kidney disease, or eye problems.</li>
                    <li>💧 <strong>Stay Hydrated</strong> – Drinking enough water helps regulate blood sugar and prevent dehydration.</li>
                    <li>😌 <strong>Manage Stress</strong> – Practice yoga, meditation, or deep breathing to maintain stable blood sugar levels.</li>
                </ul>
            </div>
            <img src="data:image/jpeg;base64,{encoded_diabetes}" alt="Diabetes">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state for arthritis card
if 'expanded_arthritis' not in st.session_state:
    st.session_state.expanded_arthritis = False

def toggle_arthritis():
    st.session_state.expanded_arthritis = not st.session_state.expanded_arthritis

# Arthritis Card
if st.button("Click Me", key="arthritis_card"):
    toggle_arthritis()

if not st.session_state.expanded_arthritis:
    # Collapsed View
    st.markdown(
        f"""
        <div class="card-container">
            <img src="data:image/jpeg;base64,{encoded_arthritis}" alt="Arthritis">
            <span class="disease-title">Arthritis</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Expanded View
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-card-content">
                <h3>Arthritis</h3>
                <ul>
                    <li>🏃‍♂ <strong>Stay Active</strong> – Regular low-impact exercise like walking or swimming helps maintain joint function.</li>
                    <li>🥗 <strong>Eat a Healthy Diet</strong> – Anti-inflammatory foods like fish, nuts, and leafy greens can help reduce symptoms.</li>
                    <li>⚖ <strong>Maintain a Healthy Weight</strong> – Excess weight puts extra stress on joints, especially knees and hips.</li>
                    <li>🧘 <strong>Practice Joint Protection</strong> – Use proper posture and assistive devices to reduce strain on joints.</li>
                    <li>🛌 <strong>Get Enough Rest</strong> – Proper sleep is crucial for reducing pain and inflammation.</li>
                    <li>🩺 <strong>Consult a Doctor</strong> – Seek medical advice for pain management and treatment options.</li>
                    <li>💊 <strong>Take Medications as Prescribed</strong> – Follow your doctor's recommendations for pain relief and inflammation control.</li>
                    <li>🧊 <strong>Use Hot & Cold Therapy</strong> – Warm compresses ease stiffness, while cold packs reduce swelling.</li>
                    <li>🧘‍♀ <strong>Try Stress-Relief Techniques</strong> – Yoga, meditation, and deep breathing can help manage arthritis symptoms.</li>
                </ul>
            </div>
            <img src="data:image/jpeg;base64,{encoded_arthritis}" alt="Arthritis">
        </div>
        """,
        unsafe_allow_html=True
    )