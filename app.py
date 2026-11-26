import streamlit as st
import pandas as pd
import requests
from PIL import Image
import pytesseract
import numpy as np
import io
from bs4 import BeautifulSoup

st.set_page_config(page_title="Agent V11 - Expert Complet", page_icon="🤖", layout="wide")
st.title("🤖 Agent V11 - Expert Complet")
st.write("الحملة + الفيديو + الكوبي + السكيلينغ - كلشي فبلاصة وحدة")

tab0, tab1, tab2, tab4, tab5 = st.tabs(["🟢 0. ابدا هنا - واش أول مرة؟", "📊 1. تحليل الحملة - SCALE or KILL", "🎬 2. تحليل الفيديو + Ad Copy", "🩺 4. محلل COD - CPL / CONF / DELIV", "🌐 5. محلل Landing Page - واش غادي يبيع؟"])

# ================= TAB 0 =================
with tab0:
    st.subheader("🟢 قبل ما تطلق أي حملة - جاوب هنا و نعطيك استراتيجية كاملة")
    st.write("هادا هو الـ Media Buyer ديالك. جاوب بالصح، و غادي نعطيك شنو تدير من Campaign حتى لـ Ads، و شحال غادي يجيك CPL، و امتى تطفي.")
    c1, c2 = st.columns(2)
    with c1:
        first_time = st.selectbox("1. واش أول مرة تحل Ad Account؟", ["إيه، أول مرة", "لا، عندي واحد قديم و خدام", "لا، عندي واحد و لكن تبانا / تقيد"], key="t0_first")
        produit0 = st.text_input("2. شنو المنتج؟", placeholder="مثال: كريم المفاصل", key="t0_prod")
        probleme0 = st.text_input("3. شنو المشكل اللي كيحل؟", placeholder="مثال: ألم الركبة ملي كتنوض الصباح", key="t0_prob")
        prix_vente0 = st.number_input("4. شحال ثمن البيع؟ (DH)", min_value=0.0, value=249.0, key="t0_prix")
        prix_cout0 = st.number_input("5. شحال طايح عليك؟ منتج + توصيل (DH)", min_value=0.0, value=90.0, key="t0_cout")
    with c2:
        budget0 = st.number_input("6. شحال Budget ديال التيست؟ (DH في النهار)", min_value=0.0, value=150.0, key="t0_bud")
        nb_videos0 = st.number_input("7. شحال عندك من فيديو؟", min_value=1, value=3, key="t0_vid")
        target0 = st.selectbox("8. شكون Target ديالك؟", ["نساء 35-65", "رجال 35-65", "نساء 18-35", "رجال 18-35", "الأمهات", "رجال + نساء 35-65", "ما عرفتش"], key="t0_target")
        page0 = st.selectbox("9. واش الصفحة واجدة ولا جديدة؟", ["جديدة - 0 متابع", "قديمة و فيها تفاعل", "قديمة و لكن ميتة"], key="t0_page")
        ville0 = st.selectbox("10. فين غادي تبيع؟", ["المغرب كامل", "كازا + الرباط + طنجة فقط", "مدينة وحدة"], key="t0_ville")
    if st.button("🤖 عطيني الاستراتيجية ديالي كاملة", type="primary", key="btn_t0"):
        marge0 = prix_vente0 - prix_cout0
        if prix_vente0 <= 180:
            cpl_min, cpl_max, cpl_bad = 10, 18, 30
        elif prix_vente0 <= 280:
            cpl_min, cpl_max, cpl_bad = 12, 22, 45
        else:
            cpl_min, cpl_max, cpl_bad = 18, 32, 55
        st.divider()
        st.subheader(f"📋 استراتيجية {produit0 if produit0 else 'المنتج ديالك'} - من Campaign حتى Ads")
        if first_time == "إيه، أول مرة":
            st.warning("⚠️ **أول مرة؟** ما تطلقش بـ Budget كبير. أول 3 أيام هي Warm-up. دير صفحة، دير 3 بوستات عاديين، و عاد أطلق بـ 150-200 DH/نهار.")
            st.write("**Checklist أول مرة:** 1) صفحة فيها تصويرة + غلاف + 3 بوستات 2) حساب إعلاني مربوط بالصفحة 3) طريقة خلاص خدامة 4) WhatsApp Business مربوط")
        elif first_time == "لا، عندي واحد و لكن تبانا / تقيد":
            st.error("🚨 **الحساب تبانا؟** ما تطلقش فيه نفس المنتج بنفس الفيديو. بدل الفيديو، بدل الصفحة، و سخن الحساب الجديد بـ 50 DH/نهار لمدة 2 أيام عاد أطلق الحملة الحقيقية.")
        else:
            st.success("✅ **حساب قديم و خدام:** مزيان، تقدر تطلق نيشان بـ Budget اللي قلتي.")
        if page0 == "جديدة - 0 متابع":
            st.write("**نصيحة الصفحة:** الصفحة الجديدة كتجيب CPL طالع شوية في الأول. زيد 3 بوستات ديال Reviews و فيديو ديال المنتج قبل ما تطلق.")
        st.write(f"**المارج ديالك:** {marge0:.0f} DH في البياسة. إلا بعتي بـ {prix_vente0:.0f} DH و CPL ديالك {cpl_min}-{cpl_max} DH، خاصك CONF + DELIV مزيانين باش تربح. سير لـ Tab 4 و حسبها.")
        if marge0 < 80:
            st.error(f"🚨 المارج قليل: {marge0:.0f} DH. بهاد الثمن صعيب تربح في COD. يا زيد الثمن لـ {prix_vente0+50:.0f} DH، يا دير Bundle 1+1، يا نقص ثمن الشراء.")
        elif marge0 < 120:
            st.warning(f"⚠️ المارج متوسط: {marge0:.0f} DH. خدم بـ Bundle باش تطلع AOV.")
        else:
            st.success(f"✅ المارج مزيان: {marge0:.0f} DH. تقدر تسكيلي.")
        total_test = budget0 * 3
        if total_test < 300:
            st.error(f"🚨 Budget قليل: {budget0:.0f} DH/نهار × 3 أيام = {total_test:.0f} DH. هادا غير باش تعرف واش الفيديو خدام ولا لا، ماشي باش تبيع.")
        else:
            st.success(f"✅ Budget التيست مزيان: {total_test:.0f} DH في 3 أيام. كافي باش تحكم.")
        st.divider()
        st.subheader("🏗️ STRUCTURE - كيفاش تبني الحملة في Ads Manager")
        st.write("**Campaign:** Sales - Leads / WhatsApp - CBO ولا ABO")
        st.write(f"**Ad Sets: 3** - كل Ad Set فيه فيديو واحد، Budget: {budget0/3:.0f} DH / Ad Set إلا كنتي ABO، ولا {budget0:.0f} DH كاملة إلا كنتي CBO")
        st.write(f"**Target:** {target0} | {ville0} | Broad - بلا اهتمامات ضيقة، خلي Facebook يقلب")
        st.write("**Placement:** Advantage+ - Facebook + Instagram + Reels")
        st.write("**Ad Set 1 - زاوية الألم:** 'كتعاني من ...؟'")
        st.write("**Ad Set 2 - زاوية الحياة اليومية:** 'ما بقيتيش كتقدر تمشى / تنعس / تخدم؟'")
        st.write("**Ad Set 3 - زاوية العرض:** 'توصيل فابور اليوم فقط + الدفع عند التوصيل'")
        st.write(f"**Ads:** {nb_videos0} فيديوهات. إلا عندك أقل من 3، دير نفس الفيديو بـ 3 Hooks مختلفين في أول 3 ثواني.")
        st.divider()
        st.subheader("🎯 CPL المتوقع + امتى نطفي و امتى نسكيلي؟")
        st.write(f"**إلا مشات مزيان:** CPL بين **{cpl_min} DH و {cpl_max} DH** - كمل و سكيلي +20% كل يومين.")
        st.write(f"**إلا مشات متوسطة:** CPL بين **{cpl_max+1} DH و {cpl_bad-5} DH** - خليه يكمل نهار آخر، بدل غير Hook.")
        st.write(f"**إلا مشات عيانة:** CPL فوق **{cpl_bad} DH** لمدة يومين = طفي.")
        st.write(f"- صرفتي 50 DH و 0 Lead = طفي الـ Ad Set، المشكل في Hook")
        st.write(f"- صرفتي 100 DH و CTR أقل من 1% = المشكل في الفيديو / CTA")
        st.write(f"- صرفتي {budget0:.0f} DH و جبتي Leads و 0 تأكيد = المشكل في Call Center / Offer، ماشي في الإعلان")
        st.write(f"- CPL > {cpl_bad} DH لمدة 2 أيام = طفي الحملة كاملة و بدا وحدة جديدة")
        st.write(f"- CPL < {cpl_max} DH + Lead Rate > 10% = سكيلي: {budget0:.0f} -> {budget0*1.2:.0f} -> {budget0*1.44:.0f} DH")
        st.divider()
        st.subheader("✍️ Copywriter - الكوبي واجد، كوبيه نيشان")
        st.code(f"""كتعاني من {probleme0 if probleme0 else 'المشكل ديالك'}؟ 😩
جربتي بزاف و والو؟
{produit0 if produit0 else 'المنتج'} كيعاونك ترجع تتحرك مرتاح، و أكثر من 500 واحد في المغرب جربوه.
✅ النتيجة كتبان في أيام قليلة
✅ التوصيل فابور اليوم فقط
✅ الدفع عند التوصيل - ما تخلص حتى يوصلك
👉 كليكي على الزر دابا و طلبي، العرض كيسالي اليوم!
الثمن: {prix_vente0:.0f} DH فقط""", language="text")
        st.write("**ممنوع في Meta:** 'كيحيد الألم نهائيا' / 'علاج سحري' / 'مضمون 100%'. دير 'كيعاون' / 'كيساعد' / 'كيخفف'.")
        st.write("**Hook للفيديو (أول 3 ثواني):** 'واش الركبة كتضرك ملي تنوض الصباح؟ شوف هادي...' + وري المشكل في الكاميرا.")

# ================= TAB 1 =================
with tab1:
    st.subheader("📁 Upload Facebook Export")
    uploaded = st.file_uploader("Upload CSV / Excel من Meta Ads", type=["csv", "xlsx", "xls"], key="exp")
    if uploaded is not None:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)
        if len(df) == 0 or "No data available" in str(df.values):
            st.error("🚨 الفايل خاوي! سير لـ Ads Manager و حيد الفلتر ديال التاريخ، دير Last 30 days ولا Lifetime، و عاود Export")
            st.stop()
        def find_col(possibles):
            for c in df.columns:
                for p in possibles:
                    if p.lower() in c.lower():
                        return c
            return None
        col_campaign = find_col(["campaign name"])
        col_spend = find_col(["amount spent"])
        col_impr = find_col(["impressions"])
        col_click_link = find_col(["link clicks"])
        col_click_all = find_col(["clicks (all)"])
        col_landing = find_col(["landing page views"])
        col_outbound = find_col(["outbound clicks"])
        col_leads = find_col(["leads"])
        col_purchases = find_col(["purchases"])
        col_purchase_value = find_col(["purchase value", "conversion value"])
        col_atc = find_col(["adds to cart", "add to cart"])
        col_checkout = find_col(["checkouts initiated", "initiated checkouts"])
        col_results = find_col(["results"])
        def get(row, col, default=0):
            try:
                if col is None: return default
                v = row[col]
                return float(str(v).replace(",", "").replace(" ", "")) if pd.notna(v) else default
            except: return default
        if col_campaign:
            selected = st.selectbox("Campaign Name", df[col_campaign].unique().tolist())
            row = df[df[col_campaign] == selected].iloc[0]
        else:
            row = df.iloc[0]
        spend = get(row, col_spend)
        impressions = get(row, col_impr)
        clicks_link = get(row, col_click_link)
        clicks_all = get(row, col_click_all)
        landing = get(row, col_landing)
        outbound = get(row, col_outbound)
        leads = get(row, col_leads) if col_leads else get(row, col_results)
        purchases = get(row, col_purchases)
        purchase_value = get(row, col_purchase_value)
        atc = get(row, col_atc)
        checkout = get(row, col_checkout)
        cpl = (spend/leads) if leads>0 else 999
        cpa = (spend/purchases) if purchases>0 else 0
        aov = (purchase_value/purchases) if purchases>0 else 0
        roas = (purchase_value/spend) if spend>0 else 0
        lead_rate = (leads/landing*100) if landing>0 else 0
        landing_rate = (landing/clicks_link*100) if clicks_link>0 else 0
        page_speed = (landing/outbound*100) if outbound>0 else landing_rate
        ctr_link = (clicks_link/impressions*100) if impressions>0 else 0
        cpc = (spend/clicks_link) if clicks_link>0 else 0
        cpm = (spend/impressions*1000) if impressions>0 else 0
        atc_rate = (atc/landing*100) if landing>0 else 0
        checkout_rate = (checkout/atc*100) if atc>0 else 0
        purchase_rate = (purchases/landing*100) if landing>0 else 0
        st.subheader("📊 الـ 39 ميتريك - الملخص")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("AOV", f"{aov:.0f} DH")
        m2.metric("CPA", f"{cpa:.0f} DH")
        m3.metric("ROAS", f"{roas:.2f}x")
        m4.metric("Page Speed", f"{page_speed:.0f}%")
        m1.metric("ATC Rate", f"{atc_rate:.1f}%")
        m2.metric("Checkout Rate", f"{checkout_rate:.1f}%")
        m3.metric("Purchase Rate", f"{purchase_rate:.1f}%")
        m4.metric("Lead Rate", f"{lead_rate:.1f}%")
        if purchases>0:
            if aov < cpa:
                st.error(f"🚨 كتخسر! AOV {aov:.0f} DH أصغر من CPA {cpa:.0f} DH - زيد Bundle ولا Free Shipping من 400 DH")
            elif aov < cpa*2:
                st.warning(f"⚠️ ربح قليل - AOV {aov:.0f} DH قريب لـ CPA {cpa:.0f} DH - زيد عرض 1+1")
            else:
                st.success(f"✅ AOV مزيان - {aov:.0f} DH أكبر من CPA {cpa:.0f} DH")
        if page_speed < 80 and page_speed>0:
            st.error(f"🚨 الصفحة ثقيلة - غير {page_speed:.0f}% وصلو للستور. خفف التصاور.")
        st.write("**الفيديو - من Ad بوحدو (ما كاينش فالـ Export)**")
        c1, c2 = st.columns(2)
        with c1:
            views_3s = st.number_input("3-Second Video Views", min_value=0, value=int(impressions*0.25) if impressions>0 else 0, key="v3")
            views_15s = st.number_input("15-Second Video Views", min_value=0, value=0, key="v15")
            thruplay = st.number_input("ThruPlay", min_value=0, value=0, key="th")
        with c2:
            v25 = st.number_input("Video Plays at 25%", min_value=0, value=0, key="25")
            v50 = st.number_input("Video Plays at 50%", min_value=0, value=0, key="50")
            v75 = st.number_input("Video Plays at 75%", min_value=0, value=0, key="75")
            v95 = st.number_input("Video Plays at 95%", min_value=0, value=0, key="95")
        load_time = st.number_input("Page Speed (seconds)", min_value=0.0, value=2.5, key="sp")
        bounce = st.number_input("Bounce Rate %", min_value=0.0, value=60.0, key="bo")
        days = st.number_input("Days running?", min_value=1, value=3, key="days")
        current_budget = st.number_input("Current Daily Budget (MAD)", min_value=0.0, value=200.0, key="bud")
        target_cpl = st.number_input("Target CPL - شحال بغيتي تخلص على Lead؟ (MAD)", min_value=0.0, value=20.0, key="tcpl")
        if st.button("🤖 Analyze - فين المشكل و شحال نسكيلي؟", type="primary", key="ana1"):
            hook = (views_3s / impressions * 100) if impressions > 0 else 0
            hold = (views_15s / views_3s * 100) if views_3s > 0 else 0
            r50 = (v50 / impressions * 100) if impressions > 0 else 0
            r75 = (v75 / impressions * 100) if impressions > 0 else 0
            st.divider()
            st.subheader("🏆 DECISION + شحال نسكيلي؟")
            if spend < 150:
                st.info(f"⏳ WAIT - صرفتي غير {spend:.0f} MAD. خليها حتى 300-400 MAD عاد حكم.")
            elif hook >= 25 and ctr_link >= 1 and cpl <= target_cpl and lead_rate >= 10:
                new_budget = current_budget * 1.2
                new_budget_2 = new_budget * 1.2
                st.success(f"🚀 SCALE! - سكيلي دابا!")
                st.write(f"**علاش؟** Hook {hook:.1f}% مزيان + CTR {ctr_link:.2f}% مزيان + CPL {cpl:.1f} MAD أقل من الهدف {target_cpl:.0f} + Lead Rate {lead_rate:.1f}% مزيان.")
                st.write(f"اليوم: {current_budget:.0f} MAD -> بعد 2 أيام: **{new_budget:.0f} MAD** (+20%)")
                st.write(f"من بعد 2 أيام أخرى: **{new_budget_2:.0f} MAD** (+20% عاود)")
                st.write(f"إلا CPL طلع فوق {target_cpl*1.5:.0f} MAD، حبس السكيلينغ و رجع لـ {current_budget:.0f} MAD.")
                st.write("**القاعدة الذهبية:** ما تزيدش كثر من 20% كل يومين، و ما تبدلش الفيديو ولا الجمهور ملي كتسكيلي.")
            elif hook < 20 and ctr_link < 0.8 and cpl > 40 and days >= 3:
                st.error(f"🛑 KILL IT! - حبسها! Hook {hook:.1f}% + CTR {ctr_link:.2f}% + CPL {cpl:.1f} MAD - كلشي طايح و دازو {days} أيام.")
            else:
                st.warning("🔧 FIX IT! - صايب المشكل اللي لتحت، ما تحبس ما تسكيلي.")
            st.divider()
            st.subheader("🔍 المشكل فين بالضبط؟ + علاش؟ + شنو ندير؟")
            if hook < 25:
                st.error(f"🔴 المشكل هنا: HOOK - {hook:.1f}% (خاصو يكون فوق 25%)")
                st.write("**علاش؟** أول 3 ثواني ما شدّوش الناس. **شنو تدير؟** بدل غير 3 ثواني اللولة: بدا بالمشكل: 'كتعاني من...؟' ولا بنتيجة: 'شوف النتيجة ف 7 أيام'.")
            elif hold < 30:
                st.error(f"🔴 المشكل هنا: HOLD - {hold:.1f}% (خاصو يكون فوق 30%)")
                st.write("**علاش؟** Hook شدّهم ولكن الوسط ممل. **شنو تدير؟** قصر الفيديو ل 25-30 ثانية، العرض يبان قبل 10s.")
            elif r50 - r75 > 10:
                st.error(f"🔴 المشكل هنا: الفيديو طويل - هربو {r50-r75:.1f}% بين 50% و 75%")
                st.write("**شنو تدير؟** قصر الفيديو، دير CTA فالوسط.")
            if ctr_link < 1:
                st.error(f"🟠 المشكل هنا: CTA - CTR {ctr_link:.2f}% (خاصو فوق 1%)")
                st.write("**شنو تدير؟** فاللخر قول: 'كليكي على اللين دابا، العرض كيسالي اليوم' + الثمن واضح + زر كيبان.")
            elif cpc > 3:
                st.error(f"🟠 المشكل هنا: CPC غالي - {cpc:.2f} MAD - جرب Broad بلا اهتمامات.")
            if landing_rate < 70:
                st.error(f"🟠 المشكل هنا: الصفحة ثقيلة - دخلو غير {landing_rate:.0f}% - صغر التصاور، خاصها تحل فأقل من 2s.")
            elif bounce > 70:
                st.error(f"🟠 المشكل هنا: Bounce {bounce:.0f}% - الميساج ديال الفيديو ماشي هو الميساج ديال الصفحة.")
            elif lead_rate < 10:
                st.error(f"🟠 المشكل هنا: الصفحة ما كتقنعش - غير {lead_rate:.1f}% عمرو الفورم - الثمن واضح؟ Reviews؟ زر كبير؟")
            st.divider()
            st.write(f"📉 Funnel: Impressions {impressions:.0f} -> 3s {views_3s} ({hook:.0f}%) -> Link Clicks {clicks_link:.0f} -> Landing {landing:.0f} ({landing_rate:.0f}%) -> Leads {leads:.0f} ({lead_rate:.1f}%) | CPL {cpl:.1f} | CPM {cpm:.1f} | CPC {cpc:.2f} | AOV {aov:.0f} | ROAS {roas:.2f}x")

# ================= TAB 2 =================
with tab2:
    st.subheader("🎬 حط ليا الفيديو و Ad Copy ديالك - نقول ليك فين الخلل")
    product = st.text_input("شنو المنتج؟", placeholder="مثال: كريم تبييض، ساعة، مكينة قهوة...")
    problem_product = st.text_input("شنو المشكل اللي كيحل المنتج؟", placeholder="مثال: البشرة كحلة، النعاس قليل...")
    audience = st.selectbox("شكون الجمهور؟", ["نساء 18-35", "نساء 35-55", "رجال 18-35", "رجال 35-55", "الأمهات", "الشباب"])
    video_type = st.selectbox("شنو نوع الفيديو اللي درتي؟", ["UGC - واحد كيهضر", "Voice Over + تصاور المنتج", "تصاور بلا هدرة", "إنفلونسر", "Before / After", "ما عرفتش"])
    video_length = st.number_input("شحال طول الفيديو؟ (ثواني)", min_value=5, value=30)
    hook_text = st.text_area("شنو قلتي فأول 3 ثواني؟ كتبو هنا بالضبط", placeholder="مثال: سلام عليكم، اليوم جبت ليكم...")
    cta_text = st.text_area("شنو قلتي فاللخر؟ (CTA)", placeholder="مثال: اطلبو دابا...")
    ad_copy = st.text_area("Ad Copy - شنو كتبتي فالنص ديال الإعلان ففيسبوك؟", placeholder="كتب النص كامل هنا...")
    has_price = st.selectbox("واش الثمن كاين فالفيديو؟", ["لا", "إيه فاللخر", "إيه فاللول"])
    has_offer = st.selectbox("واش كاين عرض؟ (توصيل فابور، تخفيض...)", ["لا، ما كاينش عرض", "إيه، توصيل فابور", "إيه، تخفيض", "إيه، 1+1 فابور"])
    video_file = st.file_uploader("📹 Upload الفيديو ديالك هنا (إلا بغيتي)", type=["mp4", "mov"], key="vid")
    if video_file:
        st.video(video_file)
    if st.button("🤖 حلل ليا الفيديو + الكوبي - فين الخلل؟", type="primary", key="ana2"):
        st.divider()
        st.subheader("🔍 تحليل الفيديو - فين الخلل؟")
        if "سلام" in hook_text or "اليوم جبت" in hook_text or len(hook_text) < 10:
            st.error("🔴 الخلل فالـ HOOK - أول 3 ثواني ميتين!")
            st.write(f"**قلتي:** '{hook_text}' - هادا Hook ديال يوتيوب، ماشي ديال فيسبوك. الناس غادي يدوزو.")
        else:
            st.success("✅ Hook مزيان، ما فيهش مشكل كبير.")
        st.write("**🎬 السكريبت الجديد اللي خاصك تدير (30 ثانية):**")
        st.write(f"**0-3s HOOK:** 'كتعاني من {problem_product}؟ شوف هادي...' + وري المشكل فالكاميرا")
        st.write(f"**3-10s المشكل:** 'جربتي بزاف و والو؟ حيت المشكل هو...' + وري قبل / بعد")
        st.write(f"**10-20s الحل:** 'هاد {product} كيحلها ف 7 أيام، حيت...' + وري المنتج كيخدم، وري النتيجة")
        st.write(f"**20-25s الثقة:** 'أكثر من 500 واحد جربوه، شوفو شنو قالو...' + وري Reviews")
        st.write(f"**25-30s CTA:** 'كليكي على اللين دابا، العرض كيسالي اليوم، التوصيل فابور' + الثمن واضح")
        st.divider()
        st.subheader("🎥 نوع الفيديو + Avatar + الصوت - شنو اللي خدام فالمغرب؟")
        if audience in ["نساء 18-35", "الأمهات"]:
            st.write("✅ **UGC - بنت كتهضر بالدارجة** - هي اللي خدامة مزيان فالمغرب دابا.")
            st.write("**Avatar:** بنت مغربية 25-30 سنة، لابسة عادي، كتهضر فالدار، إضاءة طبيعية.")
            st.write("**الصوت:** صوت بنت بالدارجة، هادي و طبيعي، ماشي صوت إشهار.")
        elif "رجال" in audience:
            st.write("✅ **UGC - راجل كيجرب المنتج** - راجل كيهضر بالدارجة، كيوري المنتج فاليد.")
        else:
            st.write("✅ **UGC + Before / After** - وري قبل و بعد، هادي هي اللي كتبيع.")
        st.write("**الكتابة فالفيديو:** كل كلمة مهمة كتبها فالفيديو، حيت 80% كيتفرجو بلا صوت. دير Subtitles بالدارجة.")
        if video_length > 40:
            st.write("طويل بزاف! قصرو لـ 25-30 ثانية.")
        else:
            st.write("مزيان، خليه 25-30 ثانية.")
        st.divider()
        st.subheader("✍️ تحليل Ad Copy - النص ديال الإعلان")
        if len(ad_copy) < 50:
            st.error("🔴 Ad Copy قصير بزاف ولا ما كاينش!")
        if has_price == "لا":
            st.error("🔴 الخلل: الثمن ما كاينش فالفيديو!")
        if has_offer == "لا، ما كاينش عرض":
            st.warning("🟠 ما كاينش عرض! زيد عرض باش الناس يكليكيو دابا.")
        st.write("**✍️ Ad Copy الجديد اللي خاصك تكتب (كوبيه نيشان):**")
        st.code(f"""كتعاني من {problem_product}؟ 😩
جربتي بزاف و والو؟ حيت المشكل ماشي فيك، المشكل فالمنتج اللي كنتي كتستعملي.
{product} كيحلها ليك ف 7 أيام، و أكثر من 500 بنت جربوه فالمغرب و عجبهم.
✅ النتيجة كتبان ف 7 أيام
✅ التوصيل فابور اليوم فقط
✅ الدفع عند التوصيل - ما تخلصي حتى يوصلك
👉 كليكي على اللين دابا و طلبي، العرض كيسالي اليوم!
# {product}""", language="text")

# ================= TAB 4 =================
with tab4:
    st.subheader("🩺 محلل COD - دخل النسب ديالك، نعطيك المشكل + الحل + علاش")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        cod_cpl = st.number_input("CPL - ثمن الليد (DH)", min_value=0.0, value=25.0, key="cod_cpl")
    with c2:
        cod_conf = st.number_input("CONF - نسبة التأكيد %", min_value=0.0, max_value=100.0, value=50.0, key="cod_conf")
    with c3:
        cod_deliv = st.number_input("DELIV - نسبة التوصيل %", min_value=0.0, max_value=100.0, value=60.0, key="cod_deliv")
    with c4:
        cod_price = st.number_input("ثمن البيع (DH)", min_value=0.0, value=200.0, key="cod_price")
        cod_cost = st.number_input("ثمن الشراء + التوصيل (DH)", min_value=0.0, value=100.0, key="cod_cost")
    st.divider()
    st.write("### ❓ جاوب على هاد الأسئلة باش نعرف المشكل بالضبط")
    q1 = st.selectbox("1. شحال كتعطل باش تعيط للكليان من بعد ما يعمر الفورم؟", ["أقل من 5 دقايق", "بين 5 و 30 دقيقة", "بين 1 و 3 ساعات", "حتى للغد"], key="cod_q1")
    q2 = st.selectbox("2. شنو كيقول ليك الكليان ملي كتعيط ليه؟", ["كيقول ليا غالي", "كيقول ليا نشاور و نرجع", "ما كيجاوبش", "كيقول ليا ما عمرتش أنا", "كيأكد عادي"], key="cod_q2")
    q3 = st.selectbox("3. شنو كيوقع ملي كيوصل الكولي للكليان؟", ["ما كيشدوش التليفون", "كيقول ما عنديش فلوس", "كيقول ما بغيتوش", "كيشدو عادي"], key="cod_q3")
    q4 = st.selectbox("4. مناش كتعيط؟", ["نمرة عادية 06", "نمرة Fix", "واتساب فقط", "ما كنعيطش"], key="cod_q4")
    q5 = st.selectbox("5. شحال كيدير التوصيل باش يوصل؟", ["1-2 أيام", "3-4 أيام", "5 أيام و كثر"], key="cod_q5")
    if st.button("🤖 حلل ليا COD - شنو هو المشكل؟", type="primary", key="ana_cod"):
        st.divider()
        profit_per_sale = cod_price - cod_cost
        if cod_conf > 0 and cod_deliv > 0:
            cost_per_delivered = cod_cpl / (cod_conf/100) / (cod_deliv/100)
            net = profit_per_sale - cost_per_delivered
        else:
            cost_per_delivered = 999
            net = -999
        st.subheader("📊 الحساب ديالك")
        st.write(f"**الربح في بياسة وحدة:** {profit_per_sale:.0f} DH | **باش تجيب بياسة وحدة موصلة كتخلص:** {cost_per_delivered:.0f} DH في الإعلان | **النتيجة النهائية:** {net:.0f} DH")
        if net < 0:
            st.error(f"🚨 كتخسر {abs(net):.0f} DH في كل بياسة كتوصل! خاصك تصلح المشكل لتحت دابا.")
        elif net < 30:
            st.warning(f"⚠️ ربح قليل بزاف: غير {net:.0f} DH في البياسة. خاصك تحسن CONF ولا DELIV.")
        else:
            st.success(f"✅ رابح {net:.0f} DH في البياسة. كمل و سكيلي.")
        st.divider()
        st.subheader("🔍 هادا هو المشكل ديالك + هادا هو الحل + علاش")
        if cod_cpl > 35:
            st.error(f"🔴 المشكل رقم 1: CPL طالع - {cod_cpl:.0f} DH (الطبيعي في المغرب 15-30 DH)")
            st.write("**الحل:** بدل Hook ديال الفيديو، و جرب Broad بلا اهتمامات، و نقص البودجيت لـ 200 DH في النهار.")
            st.write("**علاش؟** حيت Facebook كيورّي الإعلان ديالك لناس غالطين ولا الفيديو ما شدّهمش، داكشي علاش كيجيك الليد غالي.")
            if q2 == "كيقول ليا ما عمرتش أنا":
                st.write("**زيد عليها:** بزاف كيقولو ما عمرتش، هادا معناه أن الفورم كيبان ليهم بالغلط ولا كتستهدف ناس كبار ما كيعرفوش يعمرّو.")
        if cod_conf < 60:
            st.error(f"🔴 المشكل رقم 2: CONF طايح - {cod_conf:.0f}% (الطبيعي 60-75%)")
            if q1 in ["بين 1 و 3 ساعات", "حتى للغد"]:
                st.write("**المشكل:** كتعطل باش تعيط. **الحل:** عيط في أقل من 5 دقايق. **علاش؟** حيت الكليان ملي كيعمر الفورم، كيكون سخون و بغا يشري دابا. إلا خليتيه 1 ساعة، كيبرد و كيمشي عند واحد آخر.")
            if q4 in ["نمرة Fix", "واتساب فقط", "ما كنعيطش"]:
                st.write("**الحل الثاني:** عيط من نمرة عادية 06، ماشي Fix و ماشي واتساب فقط. **علاش؟** حيت المغاربة ما كيجاوبوش على Fix.")
            if q2 == "كيقول ليا غالي":
                st.write("**المشكل:** كيقول غالي. **الحل:** ما تنقصش الثمن! قول ليه: 'الثمن فيه التوصيل، و الدفع عند التوصيل'. **علاش؟** حيت ما حسش بالقيمة، ملي كتشرح ليه، كيأكد.")
            if q2 == "كيقول ليا نشاور و نرجع":
                st.write("**المشكل:** كيقول نشاور و نرجع. **الحل:** قول ليه: 'نحجز ليك واحد؟ Stock كيسالي اليوم'. و عاود عيط ليه من بعد 2 ساعات. **علاش؟** حيت 'نشاور و نرجع' معناها 'ما اقتنعتش'. إلا خليتيه يمشي، 90% ما غاديش يرجع.")
            if q2 == "ما كيجاوبش":
                st.write("**المشكل:** ما كيجاوبش. **الحل:** عيط 3 مرات في أوقات مختلفة + واتساب. **علاش؟** حيت بزاف كيكونو خدامين. 3 محاولات كيطلعو CONF بـ 15%.")
        if cod_deliv < 65:
            st.error(f"🔴 المشكل رقم 3: DELIV طايح - {cod_deliv:.0f}% (الطبيعي 65-80%)")
            if q3 == "ما كيشدوش التليفون":
                st.write("**المشكل:** ما كيشدش التليفون ملي كيوصلو الكولي. **الحل:** ملي كتأكد، قول ليه: 'غدا غادي يعيط ليك التوصيل، عافاك شد التليفون'. **علاش؟** حيت كينسى أنه طلب.")
            if q3 == "كيقول ما عنديش فلوس":
                st.write("**المشكل:** كيقول ما عنديش فلوس. **الحل:** ملي كتأكد، سولو: 'واش الفلوس واجدين؟' إلا قال لا، ما تصيفطش ليه. **علاش؟** حيت غادي يرجع و تخسر فلوس التوصيل.")
            if q3 == "كيقول ما بغيتوش":
                st.write("**المشكل:** كيقول ما بغيتوش ملي كيوصل. **الحل:** ملي كتأكد، عاود ليه المنتج + الثمن + المدينة، و قول ليه: 'إلا ما بغيتيهش، قولها ليا دابا'. **علاش؟** حيت التأكيد كان ضعيف.")
            if q5 in ["3-4 أيام", "5 أيام و كثر"]:
                st.write("**المشكل:** التوصيل كيتعطل بزاف. **الحل:** بدل شركة التوصيل. خاص يوصل في 1-2 أيام. **علاش؟** حيت كل نهار كيدوز، الكليان كيبرد و 50% ما غاديش يشدوه.")
        if cod_cpl <= 35 and cod_conf >= 60 and cod_deliv >= 65:
            st.success("✅ كلشي مزيان! CPL + CONF + DELIV كاملين في المستوى الطبيعي. كمل و سكيلي بـ 20% كل يومين.")

# ================= TAB 5 =================
with tab5:
    st.subheader("🌐 حط اللين ديال الستور - هو غادي يجبد التصاور كاملين و يقراهم")
    st.write("عطيه غير اللين، هو غادي يدخل، يجبد التصاور كاملين بالترتيب، يقرا شنو مكتوب فيهم بالـ OCR، و يحكم. بلا ما تحط التصاور بيدك.")
    url_site = st.text_input("🔗 حط اللين ديال الستور ديالك هنا", placeholder="مثال: https://calmida.store", key="lp_url_new")
    st.write("### ❓ غير هاد الجوج اللي ما نقدرش نشوفهم من برا")
    q_upsell_n = st.selectbox("1. واش داير Upsell؟ (ملي كيعمر الفورم، كيبان ليه زيد واحد آخر بنص الثمن؟)", ["لا، ما دايرش", "إيه، داير"], key="lp_upsell_new")
    q_cross_n = st.selectbox("2. واش داير Cross-sell؟ (منتج آخر معاه؟)", ["لا، ما دايرش", "إيه، داير"], key="lp_cross_new")
    st.write("### 📸 ولا حط التصاور كاملين هنا بيدك - في دقة وحدة")
    lp_imgs = st.file_uploader("ختار التصاور كاملين ديال Landing Page (Ctrl + كليكي باش تختار بزاف)", type=["png", "jpg", "jpeg", "webp"], accept_multiple_files=True, key="lp_imgs_all")
    if lp_imgs:
        st.success(f"✅ واخا، وصلوني {len(lp_imgs)} تصاور. هاهوما كاملين:")
        cols = st.columns(3)
        for i, f in enumerate(lp_imgs):
            with cols[i % 3]:
                st.image(f, caption=f"تصويرة {i+1} - {f.name}", use_container_width=True)
        if st.button("🤖 حكم على التصاور كاملين دابا", type="primary", key="btn_imgs_all"):
            st.divider()
            st.subheader(f"🏆 تحليل {len(lp_imgs)} تصاور ديالك - وحدة بوحدة + OCR")
            total_score = 0
            all_text = ""
            for i, f in enumerate(lp_imgs):
                st.divider()
                st.subheader(f"🖼️ التصويرة {i+1} - {f.name}")
                try:
                    bytes_data = f.getvalue()
                    size_kb = len(bytes_data) / 1024
                    img = Image.open(io.BytesIO(bytes_data)).convert("RGB")
                    w, h = img.size
                    ratio = w / h if h > 0 else 0
                    gray = img.convert("L")
                    arr = np.array(gray)
                    brightness = arr.mean()
                    contrast = arr.std()
                except Exception as e:
                    st.error(f"ما قدرتش نقرا هاد التصويرة: {e}")
                    continue
                st.image(f, width=300)
                st.write(f"**الحجم:** {w} x {h} | **الوزن:** {size_kb:.0f} KB | **السطوع:** {brightness:.0f} / 255 | **التباين:** {contrast:.0f}")
                ocr_text = ""
                try:
                    ocr_text = pytesseract.image_to_string(img, lang="ara+fra+eng")
                except Exception:
                    try:
                        ocr_text = pytesseract.image_to_string(img, lang="eng+fra")
                    except Exception:
                        ocr_text = ""
                ocr_text_clean = ocr_text.strip()
                all_text += " " + ocr_text_clean
                if ocr_text_clean:
                    st.write("**🔤 شنو لقيت مكتوب في هاد التصويرة (OCR):**")
                    st.info(ocr_text_clean[:800])
                else:
                    st.warning("⚠️ **ما لقيتش حتى كلمة في هاد التصويرة** - يعني تصويرة بلا كتابة.")
                score_img = 0
                probs = []
                sols = []
                if size_kb > 400:
                    probs.append(f"🚨 **هاد التصويرة تقيلة بزاف: {size_kb:.0f} KB**")
                    sols.append(f"صغر هاد التصويرة لـ أقل من 200KB. سير لـ tinypng.com")
                elif size_kb > 200:
                    score_img += 0.5
                    probs.append(f"🟠 **هاد التصويرة شوية تقيلة: {size_kb:.0f} KB**")
                    sols.append("صغرها لـ أقل من 200KB")
                else:
                    score_img += 1
                    st.write(f"✅ **الوزن مزيان:** {size_kb:.0f} KB")
                if brightness < 70:
                    probs.append(f"🚨 **هاد التصويرة مظلمة بزاف: سطوع {brightness:.0f}/255**")
                    sols.append("صور في الضو الطبيعي، حدا الشرجم")
                elif brightness < 110:
                    score_img += 0.5
                    probs.append(f"🟠 **هاد التصويرة شوية مظلمة: سطوع {brightness:.0f}**")
                    sols.append("زيد ليها شوية ضو")
                else:
                    score_img += 1
                    st.write(f"✅ **الضو مزيان:** سطوع {brightness:.0f}")
                if contrast < 30:
                    probs.append(f"🚨 **هاد التصويرة باهتة: تباين {contrast:.0f}**")
                    sols.append("خاصك تصويرة فيها تباين: منتج واضح + خلفية بيضة")
                else:
                    score_img += 0.5
                    st.write(f"✅ **التباين مزيان:** {contrast:.0f}")
                if w < 800:
                    probs.append(f"🚨 **هاد التصويرة صغيرة بزاف: {w}x{h}**")
                    sols.append("التصويرة خاصها تكون على الأقل 1000px")
                elif ratio > 2.5 or ratio < 0.4:
                    probs.append(f"🟠 **هاد التصويرة طويلة بزاف ولا عريضة بزاف: {w}x{h}**")
                    sols.append("التصاور خاصهم يكونو مربعين ولا عموديين شوية")
                else:
                    score_img += 0.5
                    st.write(f"✅ **الأبعاد مزيانين:** {w}x{h}")
                txt_low = ocr_text_clean.lower()
                if i == 0:
                    st.write("**📌 هادي هي التصويرة اللولة - Hero - أهم تصويرة.**")
                    if "dh" in txt_low or "درهم" in txt_low or "mad" in txt_low:
                        st.write("✅ **الثمن كاين في التصويرة اللولة**")
                        score_img += 0.5
                    else:
                        probs.append("🚨 **التصويرة اللولة ما فيهاش الثمن**")
                        sols.append("زيد الثمن في التصويرة اللولة، كبير و واضح.")
                    if any(x in txt_low for x in ["اطلب", "اشتر", "command", "acheter", "order", "buy"]):
                        st.write("✅ **CTA كاين في التصويرة اللولة**")
                        score_img += 0.5
                    else:
                        probs.append("🟠 **التصويرة اللولة ما فيهاش CTA**")
                        sols.append("زيد: 'اطلب الآن' ولا 'الدفع عند التوصيل'.")
                elif i == 1:
                    st.write("**📌 هادي التصويرة التانية - خاصها تكون المنتج كيخدم ولا قبل / بعد.**")
                elif i == len(lp_imgs)-1:
                    st.write("**📌 هادي التصويرة اللخرة - خاصها تكون Reviews ولا زر الشراء.**")
                if any(x in txt_low for x in ["الدفع عند التوصيل", "cash on delivery", "paiement"]):
                    st.write("✅ **الدفع عند التوصيل كاين مكتوب**")
                if any(x in txt_low for x in ["فابور", "gratuit", "free", "مجاني"]):
                    st.write("✅ **التوصيل فابور كاين مكتوب**")
                st.write(f"**تقييم هاد التصويرة: {score_img:.1f} / 3.5**")
                for p in probs:
                    st.write(p)
                for s in sols:
                    st.write(f"- الحل: {s}")
                total_score += score_img
            st.divider()
            avg = total_score / len(lp_imgs) if len(lp_imgs) > 0 else 0
            score_10 = (avg / 3.5) * 10
            st.subheader(f"🏆 التقييم العام ديال التصاور: {score_10:.1f} / 10")
            if score_10 >= 8:
                st.success(f"✅ **التصاور واجدين يبيعو: {score_10:.1f}/10**")
            elif score_10 >= 5:
                st.warning(f"⚠️ **التصاور متوسطين: {score_10:.1f}/10**")
            else:
                st.error(f"🛑 **التصاور عيانين: {score_10:.1f}/10** - ما تطلقش إعلانات بهاد التصاور")
            st.divider()
            st.subheader("🔤 النص الكامل اللي لقيت في التصاور كاملين (OCR):")
            if all_text.strip():
                st.code(all_text.strip()[:2000], language="text")
                low_all = all_text.lower()
                if "dh" not in low_all and "درهم" not in low_all and "mad" not in low_all:
                    st.error("🚨 **ما لقيتش الثمن في حتى تصويرة!**")
                if not any(x in low_all for x in ["اطلب", "اشتر", "command", "order", "buy"]):
                    st.error("🚨 **ما لقيتش CTA في حتى تصويرة!**")
                if not any(x in low_all for x in ["الدفع عند التوصيل", "cash", "paiement"]):
                    st.warning("⚠️ **ما لقيتش 'الدفع عند التوصيل' مكتوب في التصاور.**")
            else:
                st.error("🚨 **التصاور كاملين بلا كتابة!**")
            st.divider()
            st.subheader("📐 الترتيب الصحيح ديال Landing Page")
            st.write("**1. اللولة:** المنتج بوحدو، كبير، واضح، ضو مزيان - فيها الثمن + العرض + CTA")
            st.write("**2. التانية:** المنتج كيخدم / قبل / بعد")
            st.write("**3. التالتة:** العلبة + شنو فيها")
            st.write("**4. الرابعة:** فيديو 30s ديال المنتج كيخدم")
            st.write("**5. الخامسة:** Reviews بتصاور مغاربة")
            st.write("**6. السادسة:** الثمن + Bundle + زر 'اطلب الآن'")
            if q_upsell_n == "إيه، داير" and q_cross_n == "إيه، داير":
                st.success("✅ Upsell + Cross-sell دايرهم، مزيان.")
            else:
                st.error("🚨 **ما دايرش Upsell / Cross-sell:** كتخلي الفلوس في الطابلة.")

    # ===== FIX V12: اللين كيشوف التصاور كاملين غير من اللين =====
    if st.button("🤖 دخل شوف الستور من اللين و قيمو ليا", type="primary", key="btn_lp_new"):
        if not url_site or "http" not in url_site:
            st.error("🚨 حط اللين كامل، خاص يبدا بـ https://")
        else:
            import time, re
            from urllib.parse import urljoin
            with st.spinner("⏳ دابا داخل للستور... كنجبد التصاور كاملين، كنقراهم بالـ OCR..."):
                try:
                    t0 = time.time()
                    r = requests.get(url_site, timeout=20, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
                    load = time.time() - t0
                    html = r.text
                    soup = BeautifulSoup(html, "html.parser")
                    html_low = html.lower()
                    size_kb = len(r.content) / 1024
                    status = r.status_code
                except Exception as e:
                    st.error(f"🚨 ما قدرتش ندخل للستور. الخطأ: {e}")
                    st.stop()
            st.success(f"✅ دخلت للستور: Status {status} | السرعة: {load:.1f}s | الحجم الكامل: {size_kb:.0f} KB")

            # --- 1. جبد التصاور كاملين من اللين بالترتيب ---
            img_srcs = []
            for im in soup.find_all("img"):
                src = im.get("src") or im.get("data-src") or im.get("data-lazy-src") or ""
                if not src: continue
                low_src = src.lower()
                if any(x in low_src for x in ["svg", "logo", "icon", "pixel", "favicon", "spinner"]): continue
                if src.startswith("//"): src = "https:" + src
                elif src.startswith("/"): src = urljoin(url_site, src)
                elif not src.startswith("http"): src = urljoin(url_site, src)
                if src not in img_srcs:
                    img_srcs.append(src)
            img_srcs = img_srcs[:6]
            nb_img = len(img_srcs)

            # --- 2. قرا التصاور بالـ OCR واحد بواحد ---
            st.subheader(f"🖼️ التصاور اللي لقيت في اللين - {nb_img} تصاور بالترتيب")
            all_ocr_text = ""
            for idx, src in enumerate(img_srcs):
                st.divider()
                st.write(f"**📌 تصويرة {idx+1} من اللين - {'Hero - اللولة' if idx==0 else ''}**")
                try:
                    r2 = requests.get(src, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
                    if r2.status_code == 200 and len(r2.content) > 1000:
                        pil_im = Image.open(io.BytesIO(r2.content)).convert("RGB")
                        st.image(pil_im, caption=f"تصويرة {idx+1}", use_container_width=True)
                        try:
                            t_ocr = pytesseract.image_to_string(pil_im, lang="ara+fra+eng")
                        except:
                            t_ocr = pytesseract.image_to_string(pil_im, lang="eng+fra")
                        t_ocr = t_ocr.strip()
                        all_ocr_text += " " + t_ocr
                        if t_ocr:
                            st.info(f"🔤 شنو لقيت مكتوب في تصويرة {idx+1}: {t_ocr[:600]}")
                        else:
                            st.warning(f"⚠️ تصويرة {idx+1} ما فيهاش كتابة واضحة")
                    else:
                        st.warning(f"ما قدرتش نحمل تصويرة {idx+1}")
                except Exception as e:
                    st.warning(f"ما قدرتش نقرا تصويرة {idx+1}: {e}")

            # --- 3. دمج النص: HTML + OCR ديال التصاور ---
            text_combined = html_low + " " + all_ocr_text.lower()
            st.divider()
            st.subheader("🔤 النص الكامل اللي لقيت في اللين + التصاور (OCR):")
            st.code((all_ocr_text[:2000] if all_ocr_text.strip() else "ما لقيتش كتابة في التصاور - يمكن التصاور فيهم كتابة مزخرفة"), language="text")

            # --- 4. الحساب على النص المدمج - ماشي غير HTML ---
            has_price = any(x in text_combined for x in ["dh", "درهم", "mad", "د.م", "249", "319", "399"])
            has_cta = any(x in text_combined for x in ["اطلب", "add to cart", "buy now", "commander", "acheter", "order", "اشتر"])
            has_cod = any(x in text_combined for x in ["الدفع عند التوصيل", "cash on delivery", "paiement", "عند الاستلام"])
            has_free_ship = any(x in text_combined for x in ["فابور", "free shipping", "gratuit", "مجاني", "livraison gratuite"])
            has_reviews = any(x in text_combined for x in ["review", "avis", "تقييم", "رأي"])
            has_video = any(x in text_combined for x in ["<video", "youtube", ".mp4"]) or "<video" in html_low
            has_bundle = any(x in text_combined for x in ["1+1", "2+1", "bundle", "pack", "علبتين", "3 علب", "2 علب", "319", "399"])
            # الفورم
            forms = re.findall(r'<form.*?</form>', html_low, flags=re.DOTALL)
            inputs = re.findall(r'<input[^>]*>', html_low)
            nb_inputs = len(inputs)
            # الالوان غير من الزر والفورم
            buttons_html = re.findall(r'<button.*?</button>', html_low, flags=re.DOTALL)
            forms_html = re.findall(r'<form.*?</form>', html_low, flags=re.DOTALL)
            cta_html = " ".join(buttons_html + forms_html)
            colors_found = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b', cta_html)
            colors_unique = list(set([c.lower() for c in colors_found if c.lower() not in ["#fff", "#ffffff", "#000", "#000000", "#f5f5f5", "#eeeeee", "#ddd", "#dddddd"]]))
            nb_colors = len(colors_unique)
            is_image_landing = nb_img >= 3

            score = 0
            problems = []
            solutions = []
            details = []
            details.append(f"🖼️ **التصاور في السيت: لقيت {nb_img} تصويرة بالترتيب من اللين**")
            if nb_img == 0:
                problems.append("🚨 **ما كاينش تصاور:** دخلت و ما لقيتش حتى تصويرة!")
                solutions.append("حط 5 تصاور على الأقل")
            elif nb_img < 3:
                score += 0.5
                problems.append(f"🟠 **التصاور قلال بزاف:** غير {nb_img} تصاور.")
                solutions.append("زيد تصاور: المنتج بوحدو، في اليد، كيخدم، قبل / بعد، Reviews")
            else:
                score += 1
                details.append(f"✅ عدد التصاور مزيان: {nb_img} تصاور.")
            # الثمن - من OCR ماشي غير HTML
            if has_price:
                score += 1
                details.append("✅ الثمن كاين - لقيتو في التصاور (OCR) ولا في الموقع.")
                # إلا الثمن في التصويرة اللولة = ممتاز
                first_ocr = all_ocr_text[:800].lower()
                if any(x in first_ocr for x in ["dh", "درهم", "249", "319"]):
                    details.append("✅ الثمن كاين في التصويرة اللولة Hero - هادا هو الصح، الكليان كيشوفو دغيا.")
                else:
                    details.append("🟠 الثمن كاين ولكن ماشي في التصويرة اللولة - طلعو للتصويرة اللولة.")
            else:
                problems.append("🚨 **ما لقيتش الثمن لا في الموقع ولا في التصاور.**")
                solutions.append("زيد الثمن في التصويرة اللولة، كبير و واضح.")
            # CTA
            if has_cta:
                score += 0.5
                details.append("✅ زر الشراء / CTA كاين.")
            else:
                problems.append("🟠 **زر الشراء مخبي ولا ما كاينش واضح.**")
                solutions.append("دير زر 'اطلب الآن' في 3 بلايص: الفوق، في الوسط، و في اللخر.")
            # Reviews - لا نعاقب إلا كان الستور تصاور و Reviews في تصويرة
            if has_reviews:
                score += 0.5
                details.append("✅ Reviews كاينين.")
            else:
                problems.append("🚨 **ما كاينش Reviews واضحين.**")
                solutions.append("زيد 5 Reviews بتصاور مغاربة قبل الفورم.")
            details.append(f"⚡ **السرعة: {load:.1f}s | الحجم: {size_kb:.0f} KB**")
            if load <= 2:
                score += 1.5
                details.append("✅ السرعة مزيانة.")
            elif load <= 3.5:
                score += 0.5
                problems.append(f"🐢 **السرعة:** {load:.1f}s - ثقيلة.")
                solutions.append("صغر التصاور. الصفحة خاصها تحل في أقل من 2s.")
            else:
                problems.append(f"🚨 **السرعة كارثة:** {load:.1f}s - 70% غادي يخرجو قبل ما يشوفو المنتج.")
                solutions.append("السيت ثقيل بزاف. بدل الثيم، صغر التصاور.")
            details.append(f"📝 **الفورم:** لقيت {nb_inputs} خانة")
            if 1 <= nb_inputs <= 3:
                score += 1.5
                details.append("✅ الفورم قصير: سميت + نمرة + مدينة.")
            elif nb_inputs > 3:
                score += 0.5
                problems.append(f"🚨 **الفورم طويل:** {nb_inputs} خانة!")
                solutions.append("خلي غير 3: سميت + نمرة + مدينة.")
            else:
                problems.append("🚨 **ما لقيتش فورم في الكود - يمكن الفورم داخل تصويرة ولا واتساب.**")
                solutions.append("تأكد أن الفورم كاين و خدام، ولا زيد زر واتساب واضح.")
            details.append(f"🎨 **ألوان الزر و الفورم فقط:** لقيت {nb_colors} لون: {', '.join(colors_unique[:5]) if colors_unique else 'غير أبيض و أسود'}")
            if is_image_landing:
                details.append(f"✅ هادي لاندينغ تصاور ({nb_img} تصاور) - حسبنا غير ألوان الزر و الفورم، ماشي التصاور")
                if nb_colors <= 3:
                    score += 1
                    details.append("✅ ألوان الزر و الفورم متناسقين.")
                elif nb_colors <= 5:
                    score += 0.5
                    problems.append(f"🟠 **ألوان الزر و الفورم شوية بزاف:** {nb_colors} ألوان.")
                    solutions.append("خلي الزر و الفورم بلون واحد + أبيض.")
                else:
                    problems.append(f"🟠 **ألوان الزر و الفورم مخربقين:** {nb_colors} لون!")
                    solutions.append("الزر كامل بنفس اللون، و الفورم أبيض.")
            else:
                if nb_colors <= 2:
                    score += 1
                    details.append("✅ الألوان متناسقين.")
                elif nb_colors <= 4:
                    score += 0.5
                    problems.append(f"🟠 **الألوان بزاف شوية:** {nb_colors} ألوان.")
                    solutions.append("خلي لون واحد + أبيض.")
                else:
                    problems.append(f"🚨 **الألوان مخربقين:** {nb_colors} لون!")
                    solutions.append("الستور اللي كيبيع: أبيض + لون واحد.")
            if has_cod:
                score += 0.25
                details.append("💵 الدفع عند التوصيل: ✅ كاين.")
            else:
                problems.append("🚨 **الدفع عند التوصيل ما كاينش واضح.**")
                solutions.append("كتب الفوق: 'الدفع عند التوصيل - ما تخلص حتى يوصلك'.")
            if has_free_ship:
                score += 0.25
                details.append("🚚 التوصيل فابور: ✅ كاين.")
            else:
                problems.append("🟠 **التوصيل فابور ما كاينش.**")
                solutions.append("زيد 'التوصيل فابور' الفوق.")
            if q_upsell_n == "إيه، داير" and q_cross_n == "إيه، داير":
                score += 0.5
            elif q_upsell_n == "إيه، داير" or q_cross_n == "إيه، داير":
                score += 0.25
                problems.append("🟠 **Upsell / Cross-sell ناقص.**")
                solutions.append("زيد بجوج: بعد الفورم، 'زيد واحد آخر بنص الثمن؟' + منتج صغير معاه.")
            else:
                problems.append("🚨 **ما دايرش Upsell ولا Cross-sell.**")
                solutions.append("زيد Upsell بعد الفورم: 'مبروك! بغيتي تزيد واحد آخر بنص الثمن؟'")
            if has_bundle:
                details.append("🎁 Bundle: ✅ كاين - 1 / 2 / 3.")
                score += 0.25
            else:
                problems.append("🟠 **ما كاينش Bundle.**")
                solutions.append("زيد 'خود 2، التانية بنص الثمن'.")
            if has_video:
                details.append("🎬 فيديو: ✅ كاين.")
            else:
                problems.append("🟠 **ما كاينش فيديو في الصفحة.**")
                solutions.append("زيد فيديو 30s ديال المنتج كيخدم، الفوق.")
            st.divider()
            st.subheader(f"🏆 التقييم ديالك من اللين: {score:.1f} / 10")
            if score >= 8:
                st.success(f"✅ **غادي يبيع! {score:.1f}/10** - الستور واجد، أطلق و سكيلي.")
            elif score >= 5:
                st.warning(f"⚠️ **غادي يبيع شوية و لكن كتضيع بزاف: {score:.1f}/10** - صلح المشاكل لتحت عاد أطلق.")
            else:
                st.error(f"🛑 **ما غاديش يبيع: {score:.1f}/10** - ما تطلقش إعلانات دابا.")
            st.divider()
            st.subheader("👀 شنو لقيت ملي دخلت؟")
            for d in details:
                st.write(d)
            st.divider()
            st.subheader("🔍 فين غلطتي؟ - الشرح")
            for p in problems:
                st.write(p)
            st.subheader("🛠️ الحل ديال كل مشكل")
            for s in solutions:
                st.write(f"- {s}")