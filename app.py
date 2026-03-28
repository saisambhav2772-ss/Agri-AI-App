import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import hashlib

# -------------------------------
# HASH FUNCTION
# -------------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# -------------------------------
# USER DATABASE (HASHED PASSWORDS)
# -------------------------------
users = {
    "admin": hash_password("1234"),
    "sambhav": hash_password("pass"),
}

# -------------------------------
# SESSION STATE
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = None
def login():

    st.markdown(
        """
        <h1 style='text-align:center;'>🔐 Smart Crop System</h1>
        <h4 style='text-align:center;'>Login to Continue</h4>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        if st.button("🚀 Login", use_container_width=True):

            if username in users and users[username] == hash_password(password):
                st.session_state.logged_in = True
                st.session_state.username = username

                st.success(f"✅ Welcome {username}")
                st.rerun()

            else:
                st.error("❌ Invalid username or password")
def logout():
    st.sidebar.write(f"👤 Logged in as: {st.session_state.username}")

    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()
if not st.session_state.logged_in:
    login()
    st.stop()
logout()
# -------------------------------
# YOUR MAIN APP STARTS HERE
# -------------------------------
                            
    

language_labels = {
    "English": "English",
    "Hindi": "Hindi (हिंदी)",
    "Odia": "Odia (ଓଡ଼ିଆ)",
    "Bengali": "Bengali (বাংলা)",
    "Tamil": "Tamil (தமிழ்)",
    "Telugu": "Telugu (తెలుగు)",
    "Kannada": "Kannada (ಕನ್ನಡ)",
    "Punjabi": "Punjabi (ਪੰਜਾਬੀ)",
    "Gujarati": "Gujarati (ગુજરાતી)",
    "Assamese": "Assamese (অসমীয়া)",
}


# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Crop Recommendation", layout="wide")

# -------------------------------
# TRANSLATIONS
# -------------------------------
translations = {
    "English": {
        "title": "Smart Crop Recommendation System",
        "subtitle": "AI-powered crop & yield prediction",
        "language": "Language",
        "select_region": "Select Region",
        "recommendation": "Recommendation",
        "rec_surplus": "You can export or store excess production.",
        "rec_deficit": "Increase production or import from other regions.",
        "predict": "Predict",
        "results": "Results",
        "yield": "Yield",
        "weather": "Weather Conditions",
        "demand": "Demand",
        "surplus": "SURPLUS",
        "deficit": "DEFICIT",
        "recommendation": "Recommendation",
        "no_data": "No demand data available",
        "analysis_chart": "Analysis Chart",
        "comparison_chart": "Yield vs Demand",
        "stage": "Stage",
        "start": "Start",
        "mid": "Mid",
        "end": "End",
        "quintal": "Quintal",
        "key_insights": "Key Insights",
        "major_crops": "Major Crops",
        "minor_crops": "Minor Crops",
        "soil": "Soil",
        "insight": "Insight",
        "insights_data": {
            "Punjab": "High irrigation makes Punjab ideal for wheat and rice production.",
            "Odisha": "High rainfall supports water-intensive crops like rice.",
            "Bihar": "Fertile plains support diverse crop cultivation.",
            "Maharashtra": "Black soil supports cotton and irrigation supports sugarcane.",
            "West Bengal": "Fertile delta soil and high rainfall support rice and tea.",
            "Karnataka": "Diverse climate supports coffee and maize.",
            "Tamil Nadu": "Irrigation and climate support both staple and plantation crops.",
            "Andhra Pradesh": "River deltas support major rice production.",
            "Uttar Pradesh": "Fertile land supports wheat and sugarcane.",
            "Rajasthan": "Dry climate limits crops but irrigation helps wheat.",
            "Assam": "High rainfall supports rice and tea.",
            "Gujarat": "Black soil supports cotton farming.",
        },
        "soil_input": "Enter Soil Details",
        "nitrogen": "Nitrogen",
        "phosphorus": "Phosphorus",
        "potassium": "Potassium",
        "ph": "pH",
        "fertilizer": "Fertilizer",
        "temperature": "Temperature",
        "humidity": "Humidity",
        "rainfall": "Rainfall",
        "yield_unit": "quintal/hectare",
        "ph_range": "pH (0-14)",
        "fertilizer_unit": "Fertilizer (kg/ha)",
    },
    "Hindi": {
        "title": "स्मार्ट फसल प्रणाली",
        "subtitle": "एआई आधारित फसल और उत्पादन पूर्वानुमान",
        "language": "भाषा",
        "select_region": "क्षेत्र चुनें",
        "recommendation": "सिफारिश",
        "rec_surplus": "आप अतिरिक्त उत्पादन को निर्यात या संग्रहित कर सकते हैं।",
        "rec_deficit": "उत्पादन बढ़ाएं या अन्य क्षेत्रों से आयात करें।",
        "predict": "पूर्वानुमान करें",
        "results": "परिणाम",
        "yield": "उत्पादन",
        "weather": "मौसम की स्थिति",
        "demand": "मांग",
        "surplus": "अधिशेष",
        "deficit": "कमी",
        "recommendation": "सिफारिश",
        "no_data": "कोई मांग डेटा उपलब्ध नहीं",
        "analysis_chart": "विश्लेषण चार्ट",
        "comparison_chart": "उत्पादन बनाम मांग",
        "stage": "चरण",
        "start": "शुरुआत",
        "mid": "मध्य",
        "end": "अंत",
        "quintal": "क्विंटल",
        "key_insights": "मुख्य जानकारी",
        "major_crops": "मुख्य फसलें",
        "minor_crops": "अन्य फसलें",
        "soil": "मिट्टी",
        "insight": "जानकारी",
        "insights_data": {
            "Punjab": "अधिक सिंचाई पंजाब को गेहूं और चावल के लिए उपयुक्त बनाती है",
            "Odisha": "अधिक वर्षा धान जैसी फसलों के लिए उपयुक्त है",
            "Bihar": "उपजाऊ भूमि विविध फसलों के लिए उपयुक्त है",
            "Maharashtra": "काली मिट्टी कपास और सिंचाई गन्ने के लिए उपयुक्त है",
            "West Bengal": "डेल्टा मिट्टी और वर्षा चावल व चाय के लिए उपयुक्त है",
            "Karnataka": "विविध जलवायु कॉफी और मक्का के लिए उपयुक्त है",
            "Tamil Nadu": "सिंचाई और जलवायु कई फसलों के लिए उपयुक्त है",
            "Andhra Pradesh": "नदी डेल्टा चावल उत्पादन के लिए उपयुक्त है",
            "Uttar Pradesh": "उपजाऊ भूमि गेहूं और गन्ने के लिए उपयुक्त है",
            "Rajasthan": "शुष्क जलवायु में सिंचाई से गेहूं उगाया जाता है",
            "Assam": "अधिक वर्षा चावल और चाय के लिए उपयुक्त है",
            "Gujarat": "काली मिट्टी कपास के लिए उपयुक्त है",
        },
        "soil_input": "मिट्टी का विवरण दर्ज करें",
        "nitrogen": "नाइट्रोजन",
        "phosphorus": "फॉस्फोरस",
        "potassium": "पोटैशियम",
        "ph": "पीएच",
        "fertilizer": "उर्वरक",
        "temperature": "तापमान",
        "humidity": "आर्द्रता",
        "rainfall": "वर्षा",
        "yield_unit": "क्विंटल/हेक्टेयर",
        "ph_range": "पीएच (0-14)",
        "fertilizer_unit": "उर्वरक (किग्रा/हेक्टेयर)",
    },
    "Odia": {
        "title": "ସ୍ମାର୍ଟ ଫସଲ ପ୍ରଣାଳୀ",
        "subtitle": "AI ଆଧାରିତ ଫସଲ ଓ ଉତ୍ପାଦନ ପୂର୍ବାନୁମାନ",
        "language": "ଭାଷା",
        "select_region": "ଅଞ୍ଚଳ ବାଛନ୍ତୁ",
        "recommendation": "ପରାମର୍ଶ",
        "rec_surplus": "ଅଧିକ ଉତ୍ପାଦନକୁ ରପ୍ତାନି କିମ୍ବା ସଞ୍ଚୟ କରନ୍ତୁ।",
        "rec_deficit": "ଉତ୍ପାଦନ ବଢ଼ାନ୍ତୁ କିମ୍ବା ଅନ୍ୟ ଅଞ୍ଚଳରୁ ଆଣନ୍ତୁ।",
        "predict": "ପୂର୍ବାନୁମାନ",
        "results": "ଫଳାଫଳ",
        "yield": "ଉତ୍ପାଦନ",
        "weather": "ଆବହାଅବସ୍ଥା",
        "demand": "ଚାହିଦା",
        "surplus": "ଅଧିକ",
        "deficit": "ଅଭାବ",
        "recommendation": "ପରାମର୍ଶ",
        "no_data": "କୌଣସି ତଥ୍ୟ ଉପଲବ୍ଧ ନାହିଁ",
        "analysis_chart": "ବିଶ୍ଳେଷଣ ଚାର୍ଟ",
        "comparison_chart": "ଉତ୍ପାଦନ ବନାମ ଚାହିଦା",
        "stage": "ପର୍ଯ୍ୟାୟ",
        "start": "ଆରମ୍ଭ",
        "mid": "ମଧ୍ୟ",
        "end": "ଶେଷ",
        "quintal": "କ୍ୱିଣ୍ଟାଲ",
        "key_insights": "ମୁଖ୍ୟ ସୂଚନା",
        "major_crops": "ମୁଖ୍ୟ ଫସଲ",
        "minor_crops": "ଅନ୍ୟ ଫସଲ",
        "soil": "ମାଟି",
        "insight": "ସୂଚନା",
        "insights_data": {
            "Punjab": "ଅଧିକ ସିଚାଇ ପଞ୍ଜାବକୁ ଗହମ ଓ ଧାନ ପାଇଁ ଉପଯୁକ୍ତ କରେ",
            "Odisha": "ଅଧିକ ବର୍ଷା ଧାନ ପାଇଁ ଉପଯୁକ୍ତ",
            "Bihar": "ଉର୍ବର ମାଟି ବିଭିନ୍ନ ଫସଲ ପାଇଁ ଉପଯୁକ୍ତ",
            "Maharashtra": "କଳା ମାଟି କପାସ ଓ ସିଚାଇ ଖଣ୍ଡସାର ପାଇଁ ଉପଯୁକ୍ତ",
            "West Bengal": "ଡେଲ୍ଟା ମାଟି ଧାନ ଓ ଚା ପାଇଁ ଉପଯୁକ୍ତ",
            "Karnataka": "ବିଭିନ୍ନ ଜଳବାୟୁ କଫି ଓ ମକା ପାଇଁ ଉପଯୁକ୍ତ",
            "Tamil Nadu": "ସିଚାଇ ଓ ଜଳବାୟୁ ବିଭିନ୍ନ ଫସଲ ପାଇଁ ଉପଯୁକ୍ତ",
            "Andhra Pradesh": "ନଦୀ ଡେଲ୍ଟା ଧାନ ପାଇଁ ଉପଯୁକ୍ତ",
            "Uttar Pradesh": "ଉର୍ବର ମାଟି ଗହମ ଓ ଖଣ୍ଡସାର ପାଇଁ ଉପଯୁକ୍ତ",
            "Rajasthan": "ଶୁଷ୍କ ଜଳବାୟୁରେ ସିଚାଇ ଗହମ ପାଇଁ ସହାୟକ",
            "Assam": "ଅଧିକ ବର୍ଷା ଧାନ ଓ ଚା ପାଇଁ ଉପଯୁକ୍ତ",
            "Gujarat": "କଳା ମାଟି କପାସ ପାଇଁ ଉପଯୁକ୍ତ",
        },
        "soil_input": "ମାଟି ବିବରଣୀ ଦିଅନ୍ତୁ",
        "nitrogen": "ନାଇଟ୍ରୋଜେନ",
        "phosphorus": "ଫସ୍ଫୋରସ",
        "potassium": "ପୋଟାସିୟମ",
        "ph": "ପିଏଚ୍",
        "fertilizer": "ସାର",
        "temperature": "ତାପମାତ୍ରା",
        "humidity": "ଆର୍ଦ୍ରତା",
        "rainfall": "ବର୍ଷା",
        "yield_unit": "କ୍ୱିଣ୍ଟାଲ/ହେକ୍ଟର",
        "ph_range": "ପିଏଚ୍ (0-14)",
        "fertilizer_unit": "ସାର (କିଗ୍ରା/ହେକ୍ଟର)",
    },
    "Bengali": {
        "title": "স্মার্ট ফসল সুপারিশ ব্যবস্থা",
        "subtitle": "এআই ভিত্তিক ফসল ও উৎপাদন পূর্বাভাস",
        "language": "ভাষা",
        "select_region": "অঞ্চল নির্বাচন করুন",
        "recommendation": "পরামর্শ",
        "rec_surplus": "অতিরিক্ত উৎপাদন সংরক্ষণ বা রপ্তানি করতে পারেন।",
        "rec_deficit": "উৎপাদন বাড়ান বা অন্য অঞ্চল থেকে আমদানি করুন।",
        "predict": "পূর্বাভাস করুন",
        "results": "ফলাফল",
        "yield": "উৎপাদন",
        "weather": "আবহাওয়া",
        "demand": "চাহিদা",
        "surplus": "অতিরিক্ত",
        "deficit": "ঘাটতি",
        "recommendation": "পরামর্শ",
        "no_data": "কোনও ডেটা উপলব্ধ নেই",
        "analysis_chart": "বিশ্লেষণ চার্ট",
        "comparison_chart": "উৎপাদন বনাম চাহিদা",
        "stage": "পর্যায়",
        "start": "শুরু",
        "mid": "মধ্য",
        "end": "শেষ",
        "quintal": "কুইন্টাল",
        "key_insights": "মূল তথ্য",
        "major_crops": "প্রধান ফসল",
        "minor_crops": "গৌণ ফসল",
        "soil": "মাটি",
        "insight": "তথ্য",
        "insights_data": {
            "Punjab": "উচ্চ সেচ গম ও ধানের জন্য উপযুক্ত",
            "Odisha": "উচ্চ বৃষ্টি ধানের জন্য উপযুক্ত",
            "Bihar": "উর্বর জমি বিভিন্ন ফসলের জন্য উপযুক্ত",
            "Maharashtra": "কালো মাটি তুলা ও আখের জন্য উপযুক্ত",
            "West Bengal": "ডেল্টা মাটি ধান ও চায়ের জন্য উপযুক্ত",
            "Karnataka": "বিভিন্ন আবহাওয়া কফি ও ভুট্টার জন্য উপযুক্ত",
            "Tamil Nadu": "সেচ ও জলবায়ু বিভিন্ন ফসলের জন্য উপযুক্ত",
            "Andhra Pradesh": "নদীর ডেল্টা ধানের জন্য উপযুক্ত",
            "Uttar Pradesh": "উর্বর জমি গম ও আখের জন্য উপযুক্ত",
            "Rajasthan": "শুষ্ক আবহাওয়ায় সেচে গম হয়",
            "Assam": "উচ্চ বৃষ্টি ধান ও চায়ের জন্য উপযুক্ত",
            "Gujarat": "কালো মাটি তুলার জন্য উপযুক্ত",
        },
        "soil_input": "মাটির বিবরণ দিন",
        "nitrogen": "নাইট্রোজেন",
        "phosphorus": "ফসফরাস",
        "potassium": "পটাশিয়াম",
        "ph": "পিএইচ",
        "fertilizer": "সার",
        "temperature": "তাপমাত্রা",
        "humidity": "আর্দ্রতা",
        "rainfall": "বৃষ্টি",
        "yield_unit": "কুইন্টাল/হেক্টর",
        "ph_range": "পিএইচ (0-14)",
        "fertilizer_unit": "সার (কেজি/হেক্টর)",
    },
    "Tamil": {
        "title": "ஸ்மார்ட் பயிர் பரிந்துரை அமைப்பு",
        "subtitle": "AI அடிப்படையிலான பயிர் மற்றும் விளைச்சல் கணிப்பு",
        "language": "மொழி",
        "select_region": "பகுதி தேர்வு செய்யவும்",
        "recommendation": "பரிந்துரை",
        "rec_surplus": "அதிக உற்பத்தியை சேமிக்க அல்லது ஏற்றுமதி செய்யலாம்.",
        "rec_deficit": "உற்பத்தியை அதிகரிக்க அல்லது பிற பகுதிகளில் இருந்து பெறுங்கள்.",
        "predict": "கணிக்க",
        "results": "முடிவுகள்",
        "yield": "விளைச்சல்",
        "weather": "வானிலை",
        "demand": "தேவை",
        "surplus": "அதிகம்",
        "deficit": "குறைவு",
        "recommendation": "பரிந்துரை",
        "no_data": "தரவு இல்லை",
        "analysis_chart": "பகுப்பாய்வு வரைபடம்",
        "comparison_chart": "விளைச்சல் vs தேவை",
        "stage": "அடுக்கு",
        "start": "தொடக்கம்",
        "mid": "நடு",
        "end": "முடிவு",
        "quintal": "குவிண்டல்",
        "key_insights": "முக்கிய தகவல்கள்",
        "major_crops": "முக்கிய பயிர்கள்",
        "minor_crops": "சிறிய பயிர்கள்",
        "soil": "மண்",
        "insight": "தகவல்",
        "insights_data": {
            "Punjab": "அதிக பாசனம் கோதுமை மற்றும் அரிசிக்கு ஏற்றது",
            "Odisha": "அதிக மழை அரிசிக்கு ஏற்றது",
            "Bihar": "செயற்கை வளமான நிலம் பல பயிர்களுக்கு ஏற்றது",
            "Maharashtra": "கரிமண் பருத்தி மற்றும் கரும்புக்கு ஏற்றது",
            "West Bengal": "டெல்டா மண் அரிசி மற்றும் தேயிலை வளர்க்க ஏற்றது",
            "Karnataka": "பல்வேறு காலநிலை காபி மற்றும் மக்காச்சோளத்திற்கு ஏற்றது",
            "Tamil Nadu": "பாசனம் மற்றும் காலநிலை பல பயிர்களுக்கு ஏற்றது",
            "Andhra Pradesh": "நதி டெல்டா அரிசிக்கு ஏற்றது",
            "Uttar Pradesh": "வளமான நிலம் கோதுமை மற்றும் கரும்புக்கு ஏற்றது",
            "Rajasthan": "வறண்ட காலநிலையில் பாசனம் கோதுமைக்கு உதவும்",
            "Assam": "அதிக மழை அரிசி மற்றும் தேயிலை வளர்க்க ஏற்றது",
            "Gujarat": "கரிமண் பருத்திக்கு ஏற்றது",
        },
        "soil_input": "மண் விவரங்களை உள்ளிடவும்",
        "nitrogen": "நைட்ரஜன்",
        "phosphorus": "பாஸ்பரஸ்",
        "potassium": "பொட்டாசியம்",
        "ph": "பிஎச்",
        "fertilizer": "உரம்",
        "temperature": "வெப்பநிலை",
        "humidity": "ஈரப்பதம்",
        "rainfall": "மழை",
        "yield_unit": "குவிண்டல்/ஹெக்டேர்",
        "ph_range": "பிஎச் (0-14)",
        "fertilizer_unit": "உரம் (கிலோ/ஹெக்டேர்)",
    },
    "Telugu": {
        "title": "స్మార్ట్ పంట సిఫార్సు వ్యవస్థ",
        "subtitle": "AI ఆధారిత పంట మరియు దిగుబడి అంచనా",
        "language": "భాష",
        "select_region": "ప్రాంతాన్ని ఎంచుకోండి",
        "recommendation": "సిఫార్సు",
        "rec_surplus": "అధిక ఉత్పత్తిని నిల్వ చేయండి లేదా ఎగుమతి చేయండి.",
        "rec_deficit": "ఉత్పత్తిని పెంచండి లేదా ఇతర ప్రాంతాల నుండి దిగుమతి చేయండి.",
        "predict": "అంచనా వేయండి",
        "results": "ఫలితాలు",
        "yield": "దిగుబడి",
        "weather": "వాతావరణ పరిస్థితులు",
        "demand": "డిమాండ్",
        "surplus": "మిగులు",
        "deficit": "లోటు",
        "recommendation": "సిఫార్సు",
        "no_data": "డేటా అందుబాటులో లేదు",
        "analysis_chart": "విశ్లేషణ చార్ట్",
        "comparison_chart": "దిగుబడి vs డిమాండ్",
        "stage": "దశ",
        "start": "ప్రారంభం",
        "mid": "మధ్య",
        "end": "ముగింపు",
        "quintal": "క్వింటాల్",
        "key_insights": "ప్రధాన సమాచారం",
        "major_crops": "ప్రధాన పంటలు",
        "minor_crops": "చిన్న పంటలు",
        "soil": "మట్టి",
        "insight": "సమాచారం",
        "insights_data": {
            "Punjab": "అధిక సాగునీరు గోధుమ మరియు బియ్యానికి అనుకూలం",
            "Odisha": "అధిక వర్షపాతం బియ్యానికి అనుకూలం",
            "Bihar": "సారవంతమైన భూమి అనేక పంటలకు అనుకూలం",
            "Maharashtra": "నల్ల మట్టి పత్తి మరియు చెరకు పంటలకు అనుకూలం",
            "West Bengal": "డెల్టా మట్టి బియ్యం మరియు టీకి అనుకూలం",
            "Karnataka": "వైవిధ్యమైన వాతావరణం కాఫీ మరియు మక్కకు అనుకూలం",
            "Tamil Nadu": "సాగునీరు మరియు వాతావరణం పంటలకు అనుకూలం",
            "Andhra Pradesh": "నది డెల్టా బియ్యానికి అనుకూలం",
            "Uttar Pradesh": "సారవంతమైన భూమి గోధుమ మరియు చెరకు పంటలకు అనుకూలం",
            "Rajasthan": "ఎండ వాతావరణంలో సాగునీరు గోధుమకు సహాయపడుతుంది",
            "Assam": "అధిక వర్షపాతం బియ్యం మరియు టీకి అనుకూలం",
            "Gujarat": "నల్ల మట్టి పత్తికి అనుకూలం",
        },
        "soil_input": "మట్టి వివరాలు నమోదు చేయండి",
        "nitrogen": "నైట్రోజన్",
        "phosphorus": "ఫాస్ఫరస్",
        "potassium": "పోటాషియం",
        "ph": "పీహెచ్",
        "fertilizer": "ఎరువు",
        "temperature": "ఉష్ణోగ్రత",
        "humidity": "ఆర్ద్రత",
        "rainfall": "వర్షపాతం",
        "yield_unit": "క్వింటాల్/హెక్టారు",
        "ph_range": "పీహెచ్ (0-14)",
        "fertilizer_unit": "ఎరువు (కిలో/హెక్టారు)",
    },
    "Kannada": {
        "title": "ಸ್ಮಾರ್ಟ್ ಬೆಳೆ ಶಿಫಾರಸು ವ್ಯವಸ್ಥೆ",
        "subtitle": "AI ಆಧಾರಿತ ಬೆಳೆ ಮತ್ತು ಉತ್ಪಾದನೆ ಮುನ್ಸೂಚನೆ",
        "language": "ಭಾಷೆ",
        "select_region": "ಪ್ರದೇಶ ಆಯ್ಕೆಮಾಡಿ",
        "recommendation": "ಶಿಫಾರಸು",
        "rec_surplus": "ಹೆಚ್ಚುವರಿ ಉತ್ಪಾದನೆಯನ್ನು ಸಂಗ್ರಹಿಸಿ ಅಥವಾ ರಫ್ತು ಮಾಡಿ.",
        "rec_deficit": "ಉತ್ಪಾದನೆಯನ್ನು ಹೆಚ್ಚಿಸಿ ಅಥವಾ ಇತರ ಪ್ರದೇಶಗಳಿಂದ ಆಮದು ಮಾಡಿ.",
        "predict": "ಅಂದಾಜು ಮಾಡಿ",
        "results": "ಫಲಿತಾಂಶಗಳು",
        "yield": "ಉತ್ಪಾದನೆ",
        "weather": "ಹವಾಮಾನ ಪರಿಸ್ಥಿತಿ",
        "demand": "ಬೇಡಿಕೆ",
        "surplus": "ಅಧಿಕ",
        "deficit": "ಕಮ್ಮಿ",
        "recommendation": "ಶಿಫಾರಸು",
        "no_data": "ಡೇಟಾ ಲಭ್ಯವಿಲ್ಲ",
        "analysis_chart": "ವಿಶ್ಲೇಷಣ ಚಾರ್ಟ್",
        "comparison_chart": "ಉತ್ಪಾದನೆ vs ಬೇಡಿಕೆ",
        "stage": "ಹಂತ",
        "start": "ಆರಂಭ",
        "mid": "ಮಧ್ಯ",
        "end": "ಅಂತ್ಯ",
        "quintal": "ಕ್ವಿಂಟಲ್",
        "key_insights": "ಮುಖ್ಯ ಮಾಹಿತಿ",
        "major_crops": "ಮುಖ್ಯ ಬೆಳೆಗಳು",
        "minor_crops": "ಇತರೆ ಬೆಳೆಗಳು",
        "soil": "ಮಣ್ಣು",
        "insight": "ಮಾಹಿತಿ",
        "insights_data": {
            "Punjab": "ಅಧಿಕ ನೀರಾವರಿ ಗೋಧಿ ಮತ್ತು ಅಕ್ಕಿಗೆ ಸೂಕ್ತ",
            "Odisha": "ಅಧಿಕ ಮಳೆ ಅಕ್ಕಿಗೆ ಸೂಕ್ತ",
            "Bihar": "ಸಾರವಂತ ಭೂಮಿ ವಿವಿಧ ಬೆಳೆಗಳಿಗೆ ಸೂಕ್ತ",
            "Maharashtra": "ಕರಿ ಮಣ್ಣು ಹತ್ತಿ ಮತ್ತು ಕಬ್ಬಿಗೆ ಸೂಕ್ತ",
            "West Bengal": "ಡೆಲ್ಟಾ ಮಣ್ಣು ಅಕ್ಕಿ ಮತ್ತು ಚಹಾಕ್ಕೆ ಸೂಕ್ತ",
            "Karnataka": "ವೈವಿಧ್ಯಮಯ ಹವಾಮಾನ ಕಾಫಿ ಮತ್ತು ಮಕ್ಕೆಗೆ ಸೂಕ್ತ",
            "Tamil Nadu": "ನೀರಾವರಿ ಮತ್ತು ಹವಾಮಾನ ವಿವಿಧ ಬೆಳೆಗಳಿಗೆ ಸೂಕ್ತ",
            "Andhra Pradesh": "ನದಿ ಡೆಲ್ಟಾ ಅಕ್ಕಿಗೆ ಸೂಕ್ತ",
            "Uttar Pradesh": "ಸಾರವಂತ ಭೂಮಿ ಗೋಧಿ ಮತ್ತು ಕಬ್ಬಿಗೆ ಸೂಕ್ತ",
            "Rajasthan": "ಒಣ ಹವಾಮಾನದಲ್ಲಿ ನೀರಾವರಿ ಗೋಧಿಗೆ ಸಹಾಯಕ",
            "Assam": "ಅಧಿಕ ಮಳೆ ಅಕ್ಕಿ ಮತ್ತು ಚಹಾಕ್ಕೆ ಸೂಕ್ತ",
            "Gujarat": "ಕರಿ ಮಣ್ಣು ಹತ್ತಿಗೆ ಸೂಕ್ತ",
        },
        "soil_input": "ಮಣ್ಣಿನ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ",
        "nitrogen": "ನೈಟ್ರೋಜನ್",
        "phosphorus": "ಫಾಸ್ಫರಸ್",
        "potassium": "ಪೊಟ್ಯಾಸಿಯಂ",
        "ph": "ಪಿಹೆಚ್",
        "fertilizer": "ರಸಗೊಬ್ಬರ",
        "temperature": "ತಾಪಮಾನ",
        "humidity": "ಆದ್ರತೆ",
        "rainfall": "ಮಳೆ",
        "yield_unit": "ಕ್ವಿಂಟಲ್/ಹೆಕ್ಟೇರ್",
        "ph_range": "ಪಿಹೆಚ್ (0-14)",
        "fertilizer_unit": "ರಸಗೊಬ್ಬರ (ಕೆಜಿ/ಹೆಕ್ಟೇರ್)",
    },
    "Punjabi": {
        "title": "ਸਮਾਰਟ ਫਸਲ ਸਿਫਾਰਸ਼ ਪ੍ਰਣਾਲੀ",
        "subtitle": "AI ਆਧਾਰਿਤ ਫਸਲ ਅਤੇ ਉਤਪਾਦਨ ਅਨੁਮਾਨ",
        "language": "ਭਾਸ਼ਾ",
        "select_region": "ਖੇਤਰ ਚੁਣੋ",
        "recommendation": "ਸਿਫਾਰਸ਼",
        "rec_surplus": "ਵਾਧੂ ਉਤਪਾਦਨ ਨੂੰ ਸੰਭਾਲੋ ਜਾਂ ਨਿਰਯਾਤ ਕਰੋ।",
        "rec_deficit": "ਉਤਪਾਦਨ ਵਧਾਓ ਜਾਂ ਹੋਰ ਖੇਤਰਾਂ ਤੋਂ ਆਯਾਤ ਕਰੋ।",
        "predict": "ਅਨੁਮਾਨ ਲਗਾਓ",
        "results": "ਨਤੀਜੇ",
        "yield": "ਉਤਪਾਦਨ",
        "weather": "ਮੌਸਮ ਦੀ ਸਥਿਤੀ",
        "demand": "ਮੰਗ",
        "surplus": "ਵਾਧੂ",
        "deficit": "ਘਾਟ",
        "recommendation": "ਸਿਫਾਰਸ਼",
        "no_data": "ਡਾਟਾ ਉਪਲਬਧ ਨਹੀਂ",
        "analysis_chart": "ਵਿਸ਼ਲੇਸ਼ਣ ਚਾਰਟ",
        "comparison_chart": "ਉਤਪਾਦਨ ਵਿਰੁੱਧ ਮੰਗ",
        "stage": "ਚਰਨ",
        "start": "ਸ਼ੁਰੂ",
        "mid": "ਵਿਚਕਾਰ",
        "end": "ਅੰਤ",
        "quintal": "ਕੁਇੰਟਲ",
        "key_insights": "ਮੁੱਖ ਜਾਣਕਾਰੀ",
        "major_crops": "ਮੁੱਖ ਫਸਲਾਂ",
        "minor_crops": "ਹੋਰ ਫਸਲਾਂ",
        "soil": "ਮਿੱਟੀ",
        "insight": "ਜਾਣਕਾਰੀ",
        "insights_data": {
            "Punjab": "ਵੱਧ ਸਿੰਚਾਈ ਗੰਹੂ ਅਤੇ ਚੌਲ ਲਈ ਉਚਿਤ ਹੈ",
            "Odisha": "ਵੱਧ ਮੀਂਹ ਚੌਲ ਲਈ ਉਚਿਤ ਹੈ",
            "Bihar": "ਉਰਵਰ ਜ਼ਮੀਨ ਕਈ ਫਸਲਾਂ ਲਈ ਉਚਿਤ ਹੈ",
            "Maharashtra": "ਕਾਲੀ ਮਿੱਟੀ ਕਪਾਹ ਅਤੇ ਗੰਨੇ ਲਈ ਉਚਿਤ ਹੈ",
            "West Bengal": "ਡੈਲਟਾ ਮਿੱਟੀ ਚੌਲ ਅਤੇ ਚਾਹ ਲਈ ਉਚਿਤ ਹੈ",
            "Karnataka": "ਵੱਖ-ਵੱਖ ਮੌਸਮ ਕੌਫੀ ਅਤੇ ਮੱਕੀ ਲਈ ਉਚਿਤ ਹੈ",
            "Tamil Nadu": "ਸਿੰਚਾਈ ਅਤੇ ਮੌਸਮ ਕਈ ਫਸਲਾਂ ਲਈ ਉਚਿਤ ਹੈ",
            "Andhra Pradesh": "ਨਦੀ ਡੈਲਟਾ ਚੌਲ ਲਈ ਉਚਿਤ ਹੈ",
            "Uttar Pradesh": "ਉਰਵਰ ਜ਼ਮੀਨ ਗੰਹੂ ਅਤੇ ਗੰਨੇ ਲਈ ਉਚਿਤ ਹੈ",
            "Rajasthan": "ਸੁੱਕੇ ਮੌਸਮ ਵਿੱਚ ਸਿੰਚਾਈ ਗੰਹੂ ਲਈ ਸਹਾਇਕ ਹੈ",
            "Assam": "ਵੱਧ ਮੀਂਹ ਚੌਲ ਅਤੇ ਚਾਹ ਲਈ ਉਚਿਤ ਹੈ",
            "Gujarat": "ਕਾਲੀ ਮਿੱਟੀ ਕਪਾਹ ਲਈ ਉਚਿਤ ਹੈ",
        },
        "soil_input": "ਮਿੱਟੀ ਦੇ ਵੇਰਵੇ ਦਰਜ ਕਰੋ",
        "nitrogen": "ਨਾਈਟਰੋਜਨ",
        "phosphorus": "ਫਾਸਫੋਰਸ",
        "potassium": "ਪੋਟਾਸੀਅਮ",
        "ph": "ਪੀਐਚ",
        "fertilizer": "ਖਾਦ",
        "temperature": "ਤਾਪਮਾਨ",
        "humidity": "ਨਮੀ",
        "rainfall": "ਮੀਂਹ",
        "yield_unit": "ਕੁਇੰਟਲ/ਹੈਕਟੇਅਰ",
        "ph_range": "ਪੀਐਚ (0-14)",
        "fertilizer_unit": "ਖਾਦ (ਕਿਲੋ/ਹੈਕਟੇਅਰ)",
    },
    "Gujarati": {
        "title": "સ્માર્ટ પાક ભલામણ સિસ્ટમ",
        "subtitle": "AI આધારિત પાક અને ઉત્પાદન આગાહી",
        "language": "ભાષા",
        "select_region": "પ્રદેશ પસંદ કરો",
        "recommendation": "ભલામણ",
        "rec_surplus": "વધારાનું ઉત્પાદન સંગ્રહિત કરો અથવા નિકાસ કરો.",
        "rec_deficit": "ઉત્પાદન વધારો અથવા અન્ય પ્રદેશોથી આયાત કરો.",
        "predict": "આગાહી કરો",
        "results": "પરિણામ",
        "yield": "ઉત્પાદન",
        "weather": "હવામાન સ્થિતિ",
        "demand": "માગ",
        "surplus": "વધારું",
        "deficit": "કમી",
        "recommendation": "ભલામણ",
        "no_data": "ડેટા ઉપલબ્ધ નથી",
        "analysis_chart": "વિશ્લેષણ ચાર્ટ",
        "comparison_chart": "ઉત્પાદન સામે માંગ",
        "stage": "ચરણ",
        "start": "શરૂઆત",
        "mid": "મધ્ય",
        "end": "અંત",
        "quintal": "ક્વિન્ટલ",
        "key_insights": "મુખ્ય માહિતી",
        "major_crops": "મુખ્ય પાક",
        "minor_crops": "અન્ય પાક",
        "soil": "માટી",
        "insight": "માહિતી",
        "insights_data": {
            "Punjab": "વધુ સિંચાઈ ઘઉં અને ચોખા માટે યોગ્ય છે",
            "Odisha": "વધુ વરસાદ ચોખા માટે યોગ્ય છે",
            "Bihar": "ઉપજાઉ જમીન વિવિધ પાક માટે યોગ્ય છે",
            "Maharashtra": "કાળી માટી કપાસ અને શેરડી માટે યોગ્ય છે",
            "West Bengal": "ડેલ્ટા માટી ચોખા અને ચા માટે યોગ્ય છે",
            "Karnataka": "વિવિધ હવામાન કૉફી અને મકાઈ માટે યોગ્ય છે",
            "Tamil Nadu": "સિંચાઈ અને હવામાન પાક માટે યોગ્ય છે",
            "Andhra Pradesh": "નદી ડેલ્ટા ચોખા માટે યોગ્ય છે",
            "Uttar Pradesh": "ઉપજાઉ જમીન ઘઉં અને શેરડી માટે યોગ્ય છે",
            "Rajasthan": "શુષ્ક હવામાનમાં સિંચાઈ ઘઉં માટે મદદરૂપ છે",
            "Assam": "વધુ વરસાદ ચોખા અને ચા માટે યોગ્ય છે",
            "Gujarat": "કાળી માટી કપાસ માટે યોગ્ય છે",
        },
        "soil_input": "માટીની માહિતી દાખલ કરો",
        "nitrogen": "નાઈટ્રોજન",
        "phosphorus": "ફોસ્ફરસ",
        "potassium": "પોટાશિયમ",
        "ph": "પીએચ",
        "fertilizer": "ખાતર",
        "temperature": "તાપમાન",
        "humidity": "ભેજ",
        "rainfall": "વરસાદ",
        "yield_unit": "ક્વિન્ટલ/હેક્ટર",
        "ph_range": "પીએચ (0-14)",
        "fertilizer_unit": "ખાતર (કિગ્રા/હેક્ટર)",
    },
    "Assamese": {
        "title": "স্মাৰ্ট শস্য পৰামৰ্শ প্ৰণালী",
        "subtitle": "AI আধাৰিত শস্য আৰু উৎপাদন পূৰ্বানুমান",
        "language": "ভাষা",
        "recommendation": "পৰামৰ্শ",
        "rec_surplus": "অধিক উৎপাদন সংৰক্ষণ বা ৰপ্তানি কৰিব পাৰে।",
        "rec_deficit": "উৎপাদন বৃদ্ধি কৰক বা আন অঞ্চলৰ পৰা আমদানি কৰক।",
        "select_region": "অঞ্চল বাছক",
        "predict": "পূৰ্বানুমান কৰক",
        "results": "ফলাফল",
        "yield": "উৎপাদন",
        "weather": "বতৰ অৱস্থা",
        "demand": "চাহিদা",
        "surplus": "অধিক",
        "deficit": "অভাৱ",
        "recommendation": "পৰামৰ্শ",
        "no_data": "ডাটা উপলব্ধ নহয়",
        "analysis_chart": "বিশ্লেষণ চাৰ্ট",
        "comparison_chart": "উৎপাদন বনাম চাহিদা",
        "stage": "পর্যায়",
        "start": "আৰম্ভ",
        "mid": "মধ্য",
        "end": "শেষ",
        "quintal": "কুইন্টাল",
        "key_insights": "মুখ্য তথ্য",
        "major_crops": "মুখ্য শস্য",
        "minor_crops": "অন্যান্য শস্য",
        "soil": "মাটি",
        "insight": "তথ্য",
        "insights_data": {
            "Punjab": "বেছি সিঞ্চাই গম আৰু ধানৰ বাবে উপযোগী",
            "Odisha": "বেছি বৰষুণ ধানৰ বাবে উপযোগী",
            "Bihar": "উৰ্বৰ মাটি বিভিন্ন শস্যৰ বাবে উপযোগী",
            "Maharashtra": "ক’লা মাটি কপাহ আৰু আখৰ বাবে উপযোগী",
            "West Bengal": "ডেল্টা মাটি ধান আৰু চাহৰ বাবে উপযোগী",
            "Karnataka": "বিভিন্ন জলবায়ু কফি আৰু মকাইৰ বাবে উপযোগী",
            "Tamil Nadu": "সিঞ্চাই আৰু জলবায়ু বিভিন্ন শস্যৰ বাবে উপযোগী",
            "Andhra Pradesh": "নদী ডেল্টা ধানৰ বাবে উপযোগী",
            "Uttar Pradesh": "উৰ্বৰ মাটি গম আৰু আখৰ বাবে উপযোগী",
            "Rajasthan": "শুকান জলবায়ুত সিঞ্চাই গমৰ বাবে সহায়ক",
            "Assam": "বেছি বৰষুণ ধান আৰু চাহৰ বাবে উপযোগী",
            "Gujarat": "ক’লা মাটি কপাহৰ বাবে উপযোগী",
        },
        "soil_input": "মাটিৰ বিৱৰণ দিয়ক",
        "nitrogen": "নাইট্ৰোজেন",
        "phosphorus": "ফছফৰাছ",
        "potassium": "পটাছিয়াম",
        "ph": "পিএইচ",
        "fertilizer": "সাৰ",
        "temperature": "তাপমাত্রা",
        "humidity": "আৰ্দ্ৰতা",
        "rainfall": "বৰষুণ",
        "yield_unit": "কুইন্টাল/হেক্টৰ",
        "ph_range": "পিএইচ (0-14)",
        "fertilizer_unit": "সাৰ (কেজি/হেক্টৰ)",
    },
}

# -------------------------------
# CSS (FINAL FIXED)
# -------------------------------
st.markdown(
    """
<style>

/* REMOVE DEFAULT STREAMLIT GAP */
.block-container {
    padding-top: 1rem !important;
}

div[data-testid="stVerticalBlock"] > div {
    gap: 0.5rem !important;
}

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #e6f0ff, #e6ffe6, #fff0f5);
    font-family: 'Segoe UI', sans-serif;
}

/* TITLE */
h1 {
    color: #1f4e79;
    text-align: center;
    font-weight: 700;
}

/* CARD STYLE */
.section {
    background: white;
    padding: 16px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.06);
    margin: 0px !important;
}

/* REMOVE SELECT BOX GAP */
.stSelectbox {
    margin-bottom: 0px !important;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #4CAF50, #2196F3);
    color: white;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
    font-weight: bold;
    border: none;
}

/* METRICS */
[data-testid="stMetric"] {
    background: #ffffff;
    padding: 10px;
    border-radius: 10px;
}
@media (max-width: 768px) {
    .block-container {
        padding: 1rem !important;
    }
}

</style>
""",
    unsafe_allow_html=True,
)

# -------------------------------
# LOAD MODELS
# -------------------------------
model_crop = pickle.load(open("model/crop_model.pkl", "rb"))
model_yield = pickle.load(open("model/yield_model.pkl", "rb"))

# -------------------------------
# LOAD DATA
# -------------------------------
demand_data = pd.read_csv("data/demand_data.csv")

# -------------------------------
# WEATHER DATA
# -------------------------------
weather_data = {
    "Odisha": {"temperature": 30, "humidity": 75, "rainfall": 150},
    "Punjab": {"temperature": 25, "humidity": 60, "rainfall": 80},
    "Bihar": {"temperature": 28, "humidity": 70, "rainfall": 110},
    "Maharashtra": {"temperature": 32, "humidity": 65, "rainfall": 90},
    "West Bengal": {"temperature": 29, "humidity": 80, "rainfall": 140},
    "Karnataka": {"temperature": 27, "humidity": 68, "rainfall": 100},
    "Tamil Nadu": {"temperature": 31, "humidity": 70, "rainfall": 95},
    "Andhra Pradesh": {"temperature": 30, "humidity": 72, "rainfall": 105},
    "Uttar Pradesh": {"temperature": 26, "humidity": 65, "rainfall": 85},
    "Rajasthan": {"temperature": 35, "humidity": 40, "rainfall": 60},
    "Assam": {"temperature": 28, "humidity": 85, "rainfall": 200},
    "Gujarat": {"temperature": 33, "humidity": 55, "rainfall": 70},
}

# -------------------------------
# CROP TRANSLATIONS
# -------------------------------
crop_translations = {
    "Rice": {
        "Hindi": "चावल",
        "Odia": "ଧାନ",
        "Bengali": "ধান",
        "Tamil": "அரிசி",
        "Telugu": "బియ్యం",
        "Kannada": "ಅಕ್ಕಿ",
        "Assamese": "ধান",
        "Gujarati": "ચોખા",
        "Punjabi": "ਚੌਲ",
        "Marathi": "तांदूळ",
    },
    "Wheat": {
        "Hindi": "गेहूं",
        "Odia": "ଗହମ",
        "Bengali": "গম",
        "Tamil": "கோதுமை",
        "Telugu": "గోధుమ",
        "Kannada": "ಗೋಧಿ",
        "Assamese": "গম",
        "Gujarati": "ઘઉં",
        "Punjabi": "ਗੰਹੂ",
        "Marathi": "गहू",
    },
    "Maize": {
        "Hindi": "मक्का",
        "Odia": "ମକା",
        "Bengali": "ভুট্টা",
        "Tamil": "மக்காச்சோளம்",
        "Telugu": "మొక్కజొన్న",
        "Kannada": "ಮಕ್ಕಿ",
        "Assamese": "ভুট্টা",
        "Gujarati": "મકાઈ",
        "Punjabi": "ਮੱਕੀ",
        "Marathi": "मका",
    },
    "Sugarcane": {
        "Hindi": "गन्ना",
        "Odia": "ଖଣ୍ଡସାର",
        "Bengali": "আখ",
        "Tamil": "கரும்பு",
        "Telugu": "చెరకు",
        "Kannada": "ಕಬ್ಬು",
        "Assamese": "আখ",
        "Gujarati": "ઉખ",
        "Punjabi": "ਗੰਨਾ",
        "Marathi": "ऊस",
    },
    "Cotton": {
        "Hindi": "कपास",
        "Odia": "କପାସ",
        "Bengali": "তুলা",
        "Tamil": "பருத்தி",
        "Telugu": "పత్తి",
        "Kannada": "ಹತ್ತಿ",
        "Assamese": "কপাহ",
        "Gujarati": "કપાસ",
        "Punjabi": "ਕਪਾਹ",
        "Marathi": "कापूस",
    },
    "Tea": {
        "Hindi": "चाय",
        "Odia": "ଚା",
        "Bengali": "চা",
        "Tamil": "தேநீர்",
        "Telugu": "టీ",
        "Kannada": "ಚಹಾ",
        "Assamese": "চাহ",
        "Gujarati": "ચા",
        "Punjabi": "ਚਾਹ",
        "Marathi": "चहा",
    },
    "Coffee": {
        "Hindi": "कॉफी",
        "Odia": "କଫି",
        "Bengali": "কফি",
        "Tamil": "காபி",
        "Telugu": "కాఫీ",
        "Kannada": "ಕಾಫಿ",
        "Assamese": "কফি",
        "Gujarati": "કોફી",
        "Punjabi": "ਕੌਫੀ",
        "Marathi": "कॉफी",
    },
}


def translate_crop(crop, lang):
    if lang == "English":
        return crop
    return crop_translations.get(crop, {}).get(lang, crop)


soil_translation = {
    "Alluvial Soil": {
        "English": "Alluvial Soil",
        "Hindi": "जलोढ़ मिट्टी",
        "Odia": "ଆଲୁଭିଆଲ୍ ମାଟି",
        "Bengali": "পলিমাটি",
        "Tamil": "அலுவியல் மண்",
        "Telugu": "అల్యూవియల్ మట్టి",
        "Kannada": "ಅಲುವಿಯಲ್ ಮಣ್ಣು",
        "Punjabi": "ਗਾਰ ਮਿੱਟੀ",
        "Gujarati": "અલ્યુવિયલ માટી",
        "Assamese": "পলিমাটি",
    },
    "Laterite Soil": {
        "English": "Laterite Soil",
        "Hindi": "लेटेराइट मिट्टी",
        "Odia": "ଲେଟେରାଇଟ୍ ମାଟି",
        "Bengali": "ল্যাটেরাইট মাটি",
        "Tamil": "லேட்டரைட் மண்",
        "Telugu": "లేటరైట్ మట్టి",
        "Kannada": "ಲೇಟರೈಟ್ ಮಣ್ಣು",
        "Punjabi": "ਲੇਟੇਰਾਈਟ ਮਿੱਟੀ",
        "Gujarati": "લેટરાઈટ માટી",
        "Assamese": "লেটাৰাইট মাটি",
    },
    "Black Soil": {
        "English": "Black Soil",
        "Hindi": "काली मिट्टी",
        "Odia": "କଳା ମାଟି",
        "Bengali": "কালো মাটি",
        "Tamil": "கரிமண்",
        "Telugu": "నల్ల మట్టి",
        "Kannada": "ಕರಿ ಮಣ್ಣು",
        "Punjabi": "ਕਾਲੀ ਮਿੱਟੀ",
        "Gujarati": "કાળી માટી",
        "Assamese": "ক'লা মাটি",
    },
    "Red Soil": {
        "English": "Red Soil",
        "Hindi": "लाल मिट्टी",
        "Odia": "ଲାଲ ମାଟି",
        "Bengali": "লাল মাটি",
        "Tamil": "சிவப்பு மண்",
        "Telugu": "ఎర్ర మట్టి",
        "Kannada": "ಕೆಂಪು ಮಣ್ಣು",
        "Punjabi": "ਲਾਲ ਮਿੱਟੀ",
        "Gujarati": "લાલ માટી",
        "Assamese": "ৰঙা মাটি",
    },
    "Desert Soil": {
        "English": "Desert Soil",
        "Hindi": "रेगिस्तानी मिट्टी",
        "Odia": "ମରୁଭୂମି ମାଟି",
        "Bengali": "মরুভূমির মাটি",
        "Tamil": "பாலைவன மண்",
        "Telugu": "ఎడారి మట్టి",
        "Kannada": "ಮರಳು ಮಣ್ಣು",
        "Punjabi": "ਰੇਗਿਸਤਾਨੀ ਮਿੱਟੀ",
        "Gujarati": "મરુસ્થલી માટી",
        "Assamese": "মৰু মাটি",
    },
}

# -------------------------------
# STATE INFO
# -------------------------------
state_info = {
    "Punjab": {
        "major": ["Wheat", "Rice"],
        "minor": ["Maize", "Cotton"],
        "soil": "Alluvial Soil",
        "insight": "High irrigation makes Punjab ideal for wheat and rice production.",
    },
    "Odisha": {
        "major": ["Rice"],
        "minor": ["Tea", "Cotton"],
        "soil": "Laterite Soil",
        "insight": "High rainfall supports water-intensive crops like rice.",
    },
    "Bihar": {
        "major": ["Sugarcane", "Wheat"],
        "minor": ["Tea", "Coffee"],
        "soil": "Alluvial Soil",
        "insight": "Fertile plains support diverse crop cultivation.",
    },
    "Maharashtra": {
        "major": ["Cotton", "Sugarcane", "Rice", "Wheat"],
        "minor": ["Tea", "Maize", "Coffee"],
        "soil": "Black Soil + Alluvial Soil",
        "insight": "Black soil supports cotton, while irrigation drives sugarcane production.",
    },
    "West Bengal": {
        "major": ["Rice", "Tea", "Sugarcane"],
        "minor": ["Coffee", "Cotton", "Maize"],
        "soil": "Alluvial Soil",
        "insight": "Fertile delta soil and high rainfall make it ideal for rice and tea cultivation.",
    },
    "Karnataka": {
        "major": ["Rice", "Coffee", "Maize"],
        "minor": ["Wheat", "Tea"],
        "soil": "Red Soil + Laterite Soil",
        "insight": "Diverse climate supports both plantation crops (coffee) and cereals like maize.",
    },
    "Tamil Nadu": {
        "major": ["Rice", "Cotton", "Sugarcane", "Tea", "Coffee"],
        "minor": ["Wheat"],
        "soil": "Red Soil + Alluvial Soil + Laterite Soil",
        "insight": "Irrigation (Cauvery) and hill climate enable both staple and plantation crops.",
    },
    "Andhra Pradesh": {
        "major": ["Rice", "Cotton"],
        "minor": ["Wheat", "Coffee", "Tea"],
        "soil": "Alluvial Soil + Red Soil",
        "insight": "River deltas and irrigation canals make Andhra a major rice-producing state.",
    },
    "Uttar Pradesh": {
        "major": ["Wheat", "Rice", "Sugarcane"],
        "minor": ["Cotton", "Tea"],
        "soil": "Alluvial Soil",
        "insight": "Fertile plains and irrigation make it a leading producer of wheat and sugarcane.",
    },
    "Rajasthan": {
        "major": ["Wheat"],
        "minor": ["Rice", "Sugarcane"],
        "soil": "Desert Soil",
        "insight": "Arid climate limits crops; irrigation enables wheat cultivation.",
    },
    "Assam": {
        "major": ["Rice", "Tea", "Sugarcane"],
        "minor": ["Wheat", "Coffee", "Cotton"],
        "soil": "Alluvial Soil",
        "insight": "High rainfall and humidity strongly favor rice and world-class tea production.",
    },
    "Gujarat": {
        "major": ["Cotton", "Wheat", "Maize"],
        "minor": ["Rice"],
        "soil": "Black Soil + Alluvial Soil",
        "insight": "Black soil and irrigation support cotton dominance and cash crop farming.",
    },
}
region_translation = {
    "Punjab": {
        "Hindi": "पंजाब",
        "Odia": "ପଞ୍ଜାବ",
        "Bengali": "পাঞ্জাব",
        "Tamil": "பஞ்சாப்",
        "Telugu": "పంజాబ్",
        "Kannada": "ಪಂಜಾಬ್",
        "Punjabi": "ਪੰਜਾਬ",
        "Gujarati": "પંજાબ",
        "Assamese": "পঞ্জাব",
    },
    "Odisha": {
        "Hindi": "ओडिशा",
        "Odia": "ଓଡ଼ିଶା",
        "Bengali": "ওডিশা",
        "Tamil": "ஒடிஷா",
        "Telugu": "ఒడిశా",
        "Kannada": "ಒಡಿಶಾ",
        "Punjabi": "ਓਡੀਸ਼ਾ",
        "Gujarati": "ઓડિશા",
        "Assamese": "ওডিশা",
    },
    "Bihar": {
        "Hindi": "बिहार",
        "Odia": "ବିହାର",
        "Bengali": "বিহার",
        "Tamil": "பீகார்",
        "Telugu": "బీహార్",
        "Kannada": "ಬಿಹಾರ",
        "Punjabi": "ਬਿਹਾਰ",
        "Gujarati": "બિહાર",
        "Assamese": "বিহাৰ",
    },
    "Maharashtra": {
        "Hindi": "महाराष्ट्र",
        "Odia": "ମହାରାଷ୍ଟ୍ର",
        "Bengali": "মহারাষ্ট্র",
        "Tamil": "மகாராஷ்டிரா",
        "Telugu": "మహారాష్ట్ర",
        "Kannada": "ಮಹಾರಾಷ್ಟ್ರ",
        "Punjabi": "ਮਹਾਰਾਸ਼ਟਰ",
        "Gujarati": "મહારાષ્ટ્ર",
        "Assamese": "মহাৰাষ্ট্ৰ",
    },
    "West Bengal": {
        "Hindi": "पश्चिम बंगाल",
        "Odia": "ପଶ୍ଚିମ ବଙ୍ଗ",
        "Bengali": "পশ্চিমবঙ্গ",
        "Tamil": "மேற்கு வங்காளம்",
        "Telugu": "పశ్చిమ బెంగాల్",
        "Kannada": "ಪಶ್ಚಿಮ ಬಂಗಾಳ",
        "Punjabi": "ਪੱਛਮੀ ਬੰਗਾਲ",
        "Gujarati": "પશ્ચિમ બંગાળ",
        "Assamese": "পশ্চিমবংগ",
    },
    "Karnataka": {
        "Hindi": "कर्नाटक",
        "Odia": "କର୍ଣ୍ଣାଟକ",
        "Bengali": "কর্নাটক",
        "Tamil": "கர்நாடகா",
        "Telugu": "కర్ణాటక",
        "Kannada": "ಕರ್ನಾಟಕ",
        "Punjabi": "ਕਰਨਾਟਕ",
        "Gujarati": "કર્ણાટક",
        "Assamese": "কৰ্ণাটক",
    },
    "Tamil Nadu": {
        "Hindi": "तमिलनाडु",
        "Odia": "ତାମିଲନାଡୁ",
        "Bengali": "তামিলনাড়ু",
        "Tamil": "தமிழ்நாடு",
        "Telugu": "తమిళనాడు",
        "Kannada": "ತಮಿಳುನಾಡು",
        "Punjabi": "ਤਮਿਲਨਾਡੁ",
        "Gujarati": "તમિલનાડુ",
        "Assamese": "তামিলনাডু",
    },
    "Andhra Pradesh": {
        "Hindi": "आंध्र प्रदेश",
        "Odia": "ଆନ୍ଧ୍ର ପ୍ରଦେଶ",
        "Bengali": "আন্ধ্র প্রদেশ",
        "Tamil": "ஆந்திரப் பிரதேசம்",
        "Telugu": "ఆంధ్రప్రదేశ్",
        "Kannada": "ಆಂಧ್ರ ಪ್ರದೇಶ",
        "Punjabi": "ਆੰਧਰਾ ਪ੍ਰਦੇਸ਼",
        "Gujarati": "આંધ્ર પ્રદેશ",
        "Assamese": "আন্ধ্ৰ প্ৰদেশ",
    },
    "Uttar Pradesh": {
        "Hindi": "उत्तर प्रदेश",
        "Odia": "ଉତ୍ତର ପ୍ରଦେଶ",
        "Bengali": "উত্তর প্রদেশ",
        "Tamil": "உத்தரப் பிரதேசம்",
        "Telugu": "ఉత్తరప్రదేశ్",
        "Kannada": "ಉತ್ತರ ಪ್ರದೇಶ",
        "Punjabi": "ਉੱਤਰ ਪ੍ਰਦੇਸ਼",
        "Gujarati": "ઉત્તર પ્રદેશ",
        "Assamese": "উত্তৰ প্ৰদেশ",
    },
    "Rajasthan": {
        "Hindi": "राजस्थान",
        "Odia": "ରାଜସ୍ଥାନ",
        "Bengali": "রাজস্থান",
        "Tamil": "ராஜஸ்தான்",
        "Telugu": "రాజస్థాన్",
        "Kannada": "ರಾಜಸ್ಥಾನ",
        "Punjabi": "ਰਾਜਸਥਾਨ",
        "Gujarati": "રાજસ્થાન",
        "Assamese": "ৰাজস্থান",
    },
    "Assam": {
        "Hindi": "असम",
        "Odia": "ଆସାମ",
        "Bengali": "অসম",
        "Tamil": "அசாம்",
        "Telugu": "అస్సాం",
        "Kannada": "ಅಸ್ಸಾಂ",
        "Punjabi": "ਅਸਾਮ",
        "Gujarati": "આસામ",
        "Assamese": "অসম",
    },
    "Gujarat": {
        "Hindi": "गुजरात",
        "Odia": "ଗୁଜରାଟ",
        "Bengali": "গুজরাট",
        "Tamil": "குஜராத்",
        "Telugu": "గుజరాత్",
        "Kannada": "ಗುಜರಾತ್",
        "Punjabi": "ਗੁਜਰਾਤ",
        "Gujarati": "ગુજરાત",
        "Assamese": "গুজৰাট",
    },
}


def translate_region(region, lang):
    if lang == "English":
        return region
    return f"{region} ({region_translation.get(region, {}).get(lang, region)})"


selected_lang_label = st.selectbox("🌐 Select Language", list(language_labels.values()))
if selected_lang_label is None:
    st.info("👆 Please select a language to continue")
    st.stop()

# reverse mapping
language = list(language_labels.keys())[
    list(language_labels.values()).index(selected_lang_label)
]

t = translations[language]

# -------------------------------
# TITLE
# -------------------------------
st.markdown(
    f"""
<h1 style='text-align:center;'>
🌾 {t['title']}
</h1>
""",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div style='text-align:center;'>
<h3>{t.get('subtitle', 'AI-powered crop & yield prediction')}</h3>
</div>
""",
    unsafe_allow_html=True,
)


# -------------------------------
# REGION SELECT (MULTILINGUAL)
# -------------------------------
region_options = ["Select"] + list(weather_data.keys())

region_display = [
    "Select" if r == "Select" else translate_region(r, language) for r in region_options
]

selected_region_display = st.selectbox(f"📍 {t['select_region']}", region_display)

# reverse mapping
region = region_options[region_display.index(selected_region_display)]

if not region or region == "Select":
    st.stop()

# ✅ ADD THIS
if region and region != "Select":

    # -------------------------------
    # KEY INSIGHTS
    # -------------------------------
    info = state_info.get(region)

    if info:
        st.markdown(
            f"""
        <div class="section">
        <h4>📊 {t.get('key_insights','Key Insights')}</h4>
        <ul>
        <li>🌾 {t.get('major_crops','Major Crops')}: {", ".join([translate_crop(c, language) for c in info['major']])}</li>
        <li>🌱 {t.get('minor_crops','Minor Crops')}: {", ".join([translate_crop(c, language) for c in info['minor']])}</li>
       <li>🌍 {t.get('soil','Soil')}: {
           " + ".join([
                soil_translation.get(s.strip(), {}).get(language, s.strip())
                for s in info['soil'].split("+")
           ])
         }</li>
        <li>💡 {t.get('insight','Insight')}: {t.get("insights_data", {}).get(region, info['insight'])}</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # -------------------------------
    # INPUTS
    # -------------------------------
    st.markdown(f"### 🌱 {t.get('soil_input','Enter Soil Details')}")

    col1, col2 = st.columns(2)

    with col1:
        N = st.number_input(t.get("nitrogen", "Nitrogen") + " (kg/ha)", 0, 200, 0)
        P = st.number_input(t.get("phosphorus", "Phosphorus") + " (kg/ha)", 0, 200, 0)

    with col2:
        K = st.number_input(t.get("potassium", "Potassium") + " (kg/ha)", 0, 200, 0)
        ph = st.number_input(t.get("ph_range", "pH (0-14)"), 0.0, 14.0, 0.0)
        fertilizer = st.number_input(
            t.get("fertilizer_unit", "Fertilizer (kg/ha)"), 0, 200, 0
        )

        # -------------------------------
    # BUTTON (FIXED PROPERLY)
    # -------------------------------
    if st.button(f"🚀 {t['predict']}"):

        with st.spinner("⏳ Processing..."):

            # -------------------------------
            # INPUT VALIDATION
            # -------------------------------
            if N == 0 and P == 0 and K == 0:
                st.warning("⚠ Please enter valid soil nutrients (N, P, K)")
                st.stop()

            if ph <= 0 or ph > 14:
                st.error("⚠ Invalid pH value (0–14)")
                st.stop()

            if fertilizer <= 0:
                st.warning("⚠ Please enter fertilizer value")
                st.stop()

            # -------------------------------
            # WEATHER DATA
            # -------------------------------
            weather = weather_data[region]
            temperature = weather["temperature"]
            humidity = weather["humidity"]
            rainfall = weather["rainfall"]

            # -------------------------------
            # FEATURES
            # -------------------------------
            crop_features = pd.DataFrame(
                [[N, P, K, temperature, humidity, ph, rainfall]],
                columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
            )

            yield_features = pd.DataFrame(
                [[rainfall, temperature, fertilizer]],
                columns=["rainfall", "temperature", "fertilizer"],
            )

            # -------------------------------
            # SAFE PREDICTION
            # -------------------------------
            try:
                predicted_crop = model_crop.predict(crop_features)[0]
                predicted_yield = model_yield.predict(yield_features)[0]

            except Exception as e:
                st.error("⚠ Prediction error. Please check inputs.")
                st.stop()

            # -------------------------------
            # DEMAND MATCH
            # -------------------------------
            match = demand_data[
                (demand_data["region"] == region)
                & (demand_data["crop"] == predicted_crop)
            ]

            # -------------------------------
            # RESULTS
            # -------------------------------
            st.markdown(f"## 📊 {t['results']}")

            translated_crop = translate_crop(predicted_crop, language)
            st.write(f"🌾 {translated_crop}")

            st.write(
                f"📊 {t.get('yield','Yield')}: {round(predicted_yield, 2)} {t.get('yield_unit','quintal/hectare')}"
            )

            # -------------------------------
            # WEATHER DISPLAY
            # -------------------------------
            st.markdown(f"### 🌦 {t['weather']}")
            c1, c2, c3 = st.columns(3)

            c1.metric(f"🌡 {t.get('temperature','Temperature')}", f"{temperature} °C")
            c2.metric(f"💧 {t.get('humidity','Humidity')}", f"{humidity} %")
            c3.metric(f"🌧 {t.get('rainfall','Rainfall')}", f"{rainfall} mm")

            # -------------------------------
            # DEMAND + ANALYSIS
            # -------------------------------
            if not match.empty:

                demand = match["demand"].values[0]

                st.write(
                    f"📦 {t.get('demand','Demand')}: {demand} {t.get('quintal','Quintal')}"
                )

                diff = round(predicted_yield - demand, 2)

                if diff > 0:
                    st.success(f"{t.get('surplus')} {diff}")
                    st.info(
                        f"💡 {t.get('recommendation','Recommendation')}: {t.get('rec_surplus')}"
                    )
                else:
                    st.error(f"{t.get('deficit')} {abs(diff)}")
                    st.info(
                        f"💡 {t.get('recommendation','Recommendation')}: {t.get('rec_deficit')}"
                    )

                st.markdown(f"### 📊 {t.get('analysis_chart','Analysis')}")

                # -------------------------------
                # GRAPHS
                # -------------------------------
                col1, col2 = st.columns(2)

                # AREA CHART
                with col1:
                    st.subheader(t.get("analysis_chart", "Analysis"))

                    chart_df = pd.DataFrame(
                        {
                            t.get("stage", "Stage"): [
                                t.get("start", "Start"),
                                t.get("mid", "Mid"),
                                t.get("end", "End"),
                            ],
                            t.get("yield", "Yield"): [
                                predicted_yield * 0.7,
                                predicted_yield * 0.9,
                                predicted_yield,
                            ],
                            t.get("demand", "Demand"): [
                                demand * 0.7,
                                demand * 0.9,
                                demand,
                            ],
                        }
                    ).set_index(t.get("stage", "Stage"))

                    st.area_chart(chart_df)

                # LINE GRAPH
                with col2:
                    st.subheader(t.get("comparison_chart", "Comparison"))

                    fig, ax = plt.subplots()

                    x = [0, 1]
                    y = [predicted_yield, demand]

                    ax.plot(x, y, marker="o")

                    ax.set_xticks([0, 1])
                    ax.set_xticklabels(
                        [t.get("yield", "Yield"), t.get("demand", "Demand")]
                    )

                    ax.set_ylabel(t.get("quintal", "Quintal"))
                    ax.set_title(t.get("comparison_chart", "Comparison"))

                    st.pyplot(fig)

            else:
                st.warning(f"⚠ {t.get('no_data','No demand data available')}")
