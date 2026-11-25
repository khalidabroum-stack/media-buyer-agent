import streamlit as st
import pandas as pd

st.set_page_config(page_title="Agent V11 - Expert Complet", page_icon="🤖", layout="wide")
st.title("🤖 Agent V11 - Expert Complet")
st.write("الحملة + الفيديو + الكوبي + السكيلينغ - كلشي فبلاصة وحدة")

tab1, tab2, tab3, tab4 = st.tabs(["📊 1. تحليل الحملة - SCALE or KILL", "🎬 2. تحليل الفيديو + Ad Copy", "🚀 3. بناء حملة بحال Expert", "🩺 4. محلل COD - CPL / CONF / DELIV"])

# ================= TAB 1 - تحليل الحملة =================
with tab1:
    st.subheader("📁 Upload Facebook Export")
    uploaded = st.file_uploader("Upload CSV / Excel من Meta Ads", type=["csv", "xlsx", "xls"], key="exp")
    
    if uploaded is not None:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)
        
        # إلا كان الفايل خاوي - ديال 39 ميتريك ديالك
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

        # ===== حساب الـ 39 ميتريك كاملين =====
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

        # عرض الميتريكس الجداد
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

        # تشخيص AOV
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
                st.info(f"⏳ WAIT - صرفتي غير {spend:.0f} MAD. خليها حتى 300-400 MAD عاد حكم. ما تحبس ما تسكيلي.")
            elif hook >= 25 and ctr_link >= 1 and cpl <= target_cpl and lead_rate >= 10:
                new_budget = current_budget * 1.2
                new_budget_2 = new_budget * 1.2
                st.success(f"🚀 SCALE! - سكيلي دابا!")
                st.write(f"**علاش؟** Hook {hook:.1f}% مزيان + CTR {ctr_link:.2f}% مزيان + CPL {cpl:.1f} MAD أقل من الهدف ديالك {target_cpl:.0f} + Lead Rate {lead_rate:.1f}% مزيان.")
                st.write(f"**شحال نزيد؟**")
                st.write(f"اليوم: {current_budget:.0f} MAD -> بعد 2 أيام: **{new_budget:.0f} MAD** (+20%)")
                st.write(f"من بعد 2 أيام أخرى: **{new_budget_2:.0f} MAD** (+20% عاود)")
                st.write(f"إلا CPL طلع فوق {target_cpl*1.5:.0f} MAD، حبس السكيلينغ و رجع لـ {current_budget:.0f} MAD.")
                st.write("**القاعدة الذهبية:** ما تزيدش كثر من 20% كل يومين، و ما تبدلش الفيديو ولا الجمهور ملي كتسكيلي.")
            elif hook < 20 and ctr_link < 0.8 and cpl > 40 and days >= 3:
                st.error(f"🛑 KILL IT! - حبسها! Hook {hook:.1f}% + CTR {ctr_link:.2f}% + CPL {cpl:.1f} MAD - كلشي طايح و دازو {days} أيام. كتخسر {spend:.0f} MAD بلا فايدة. حبسها و بدا وحدة جديدة.")
            else:
                st.warning("🔧 FIX IT! - صايب المشكل اللي لتحت، ما تحبس ما تسكيلي.")

            st.divider()
            st.subheader("🔍 المشكل فين بالضبط؟ + علاش؟ + شنو ندير؟")
            if hook < 25:
                st.error(f"🔴 المشكل هنا: HOOK - {hook:.1f}% (خاصو يكون فوق 25%)")
                st.write("**علاش كاين المشكل؟** أول 3 ثواني ما شدّوش الناس. الناس ففيسبوك كيسكروليو بسرعة، إلا ما وقفتيهمش ف 3s اللولة، غادي يدوزو.")
                st.write("**شنو خاصك تدير؟** بدل غير 3 ثواني اللولة: بدا بالمشكل: 'كتعاني من...؟' ولا بنتيجة: 'شوف النتيجة ف 7 أيام'. ما تبداش بلوغو ولا سلام. سير لـ Tab 2 و حط الفيديو ديالك، غادي نعطيك سكريبت جديد.")
            elif hold < 30:
                st.error(f"🔴 المشكل هنا: HOLD - {hold:.1f}% (خاصو يكون فوق 30%)")
                st.write("**علاش؟** Hook شدّهم ولكن الوسط ممل، هربو قبل 15s.")
                st.write("**شنو تدير؟** قصر الفيديو ل 25-30 ثانية، العرض يبان قبل 10s، كل 3 ثواني دير شي حاجة جديدة (تصويرة، زوم، كتابة).")
            elif r50 - r75 > 10:
                st.error(f"🔴 المشكل هنا: الفيديو طويل - هربو {r50-r75:.1f}% بين 50% و 75%")
                st.write("**علاش؟** الناس ملّو فالوسط. **شنو تدير؟** قصر الفيديو، دير CTA فالوسط.")
            if ctr_link < 1:
                st.error(f"🟠 المشكل هنا: CTA - CTR {ctr_link:.2f}% (خاصو فوق 1%)")
                st.write("**علاش؟** الناس كملو الفيديو ولكن ما عرفوش شنو يديرو. **شنو تدير؟** فاللخر قول: 'كليكي على اللين دابا، العرض كيسالي اليوم' + الثمن واضح + زر كيبان.")
            elif cpc > 3:
                st.error(f"🟠 المشكل هنا: CPC غالي - {cpc:.2f} MAD")
                st.write("**علاش؟** الجمهور غالط. **شنو تدير؟** جرب Broad بلا اهتمامات.")
            if landing_rate < 70:
                st.error(f"🟠 المشكل هنا: الصفحة ثقيلة - دخلو غير {landing_rate:.0f}%")
                st.write(f"**علاش؟** كليكاو {clicks_link:.0f} ولكن دخلو غير {landing:.0f}. الصفحة كتعطل {load_time:.1f}s. **شنو تدير؟** صغر التصاور، حيد الفيديو الكبير فالبداية، خاصها تحل فأقل من 2s.")
            elif bounce > 70:
                st.error(f"🟠 المشكل هنا: Bounce {bounce:.0f}%")
                st.write("**علاش؟** الميساج ديال الفيديو ماشي هو الميساج ديال الصفحة. **شنو تدير؟** نفس المنتج، نفس الثمن، نفس العرض فالفيديو و فالصفحة.")
            elif lead_rate < 10:
                st.error(f"🟠 المشكل هنا: الصفحة ما كتقنعش - غير {lead_rate:.1f}% عمرو الفورم")
                st.write("**علاش؟** الصفحة ما فيهاش ثقة. **شنو تدير؟** الثمن واضح الفوق؟ Reviews كيبانو؟ عرض: توصيل فابور؟ زر 'اطلب الان' كبير؟")

            st.divider()
            st.write(f"📉 Funnel: Impressions {impressions:.0f} -> 3s {views_3s} ({hook:.0f}%) -> Link Clicks {clicks_link:.0f} -> Landing {landing:.0f} ({landing_rate:.0f}%) -> Leads {leads:.0f} ({lead_rate:.1f}%) | CPL {cpl:.1f} | CPM {cpm:.1f} | CPC {cpc:.2f} | AOV {aov:.0f} | ROAS {roas:.2f}x")

# ================= TAB 2 - تحليل الفيديو + الكوبي =================
with tab2:
    st.subheader("🎬 حط ليا الفيديو و Ad Copy ديالك - نقول ليك فين الخلل")
    st.write("هادي بلاصة بوحدها ديال الفيديو. هنا كنحلو الفيديو بالتفصيل.")
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
            st.write("**الحل:** بدل Hook. جرب واحد من هادو:")
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

# ================= TAB 3 - بناء حملة Expert =================
with tab3:
    st.subheader("🚀 كيفاش تبني حملة بحال Expert - من الزيرو")
    st.write("**المرحلة 1: قبل ما تطلق (1 نهار)**")
    st.write("1. **المنتج:** واش كيحل مشكل حقيقي؟ واش الثمن ديالو بين 150-350 درهم؟")
    st.write("2. **الفيديو:** 3 فيديوهات مختلفين: 1) UGC بنت كتهضر 2) Before / After 3) Voice Over + تصاور.")
    st.write("3. **الصفحة:** الثمن واضح الفوق، Reviews، زر 'اطلب الان' كبير، سرعة أقل من 2s.")
    st.write("**المرحلة 2: الإطلاق (نهار 1-3)**")
    st.write("1. **Campaign Objective:** Sales ولا Leads - ماشي Traffic!")
    st.write("2. **Budget:** 200 درهم فالنهار، CBO.")
    st.write("3. **Audience:** Broad - المغرب كامل، 18-55، بلا اهتمامات.")
    st.write("4. **Ad Sets:** 1 Ad Set فيه 3 فيديوهات.")
    st.write("5. **ما تقيسش والو فأول 3 أيام!**")
    st.write("**المرحلة 3: التحليل (نهار 3)**")
    st.write("1. سير لـ Tab 1، Upload الـ Export، شوف القرار: SCALE ولا FIX ولا KILL")
    st.write("2. شوف الفيديو اللي جاب أقل CPL، حيد لاخرين.")
    st.write("**المرحلة 4: السكيلينغ (نهار 5+) - شحال نزيد؟**")
    st.write("**الطريقة الآمنة:** زيد البودجيت 20% كل يومين. من 200 -> 240 -> 288 -> 345...")
    st.write("**الطريقة السريعة:** دوبلي الحملة كاملة: دير Duplicate للحملة.")
    st.write("**إمتى نحبس؟** إلا CPL طلع 50% فوق الهدف لمدة 2 أيام.")
    st.write("**❌ الأخطاء اللي كيقتلو الحملة:**")
    st.write("- كتبدل البودجيت كل ساعة - فيسبوك كيتلف")
    st.write("- كتطلق بفيديو واحد - خاصك 3 على الأقل")
    st.write("- كتحكم على الحملة فأول نهار - خاصك 3 أيام")
    st.write("- كتزيد البودجيت 100% دقة وحدة")
    st.write("- كتدير Audience ضيق بزاف - خليها Broad")

# ================= TAB 4 - محلل COD =================
with tab4:
    st.subheader("🩺 محلل COD - دخل النسب ديالك، نعطيك المشكل + الحل + علاش")
    st.write("دخل الأرقام الحقيقية ديالك ديال آخر 3 أيام، و جاوب على الأسئلة، و غادي نعطيك التشخيص بالضبط.")

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
        # حساب التكلفة الحقيقية
        profit_per_sale = cod_price - cod_cost
        # التكلفة ديال كليان واحد مؤكد و موصل
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

        # --- منطق التشخيص ---
        # 1. CPL
        if cod_cpl > 35:
            st.error(f"🔴 المشكل رقم 1: CPL طالع - {cod_cpl:.0f} DH (الطبيعي في المغرب 15-30 DH)")
            st.write("**هادا هو الحل:** بدل Hook ديال الفيديو، و جرب Broad بلا اهتمامات، و نقص البودجيت لـ 200 DH في النهار.")
            st.write("**علاش؟** حيت Facebook كيورّي الإعلان ديالك لناس غالطين ولا الفيديو ما شدّهمش، داكشي علاش كيجيك الليد غالي. ملي كيكون Hook ضعيف، Facebook كيحسب أن الإعلان ديالك ماشي مزيان و كيغلي عليك الثمن. إلا صايبتي Hook، CPL غادي يطيح بوحدو.")
            if q2 == "كيقول ليا ما عمرتش أنا":
                st.write("**زيد عليها:** بزاف ديال الناس كيقولو ما عمرتش، هادا معناه أن الفورم ديالك كيبان ليهم بالغلط ولا كتستهدف ناس كبار ما كيعرفوش يعمرّو. بدّل الصفحة و دير زر واضح 'اطلب الآن'.")

        # 2. CONF
        if cod_conf < 60:
            st.error(f"🔴 المشكل رقم 2: CONF طايح - {cod_conf:.0f}% (الطبيعي 60-75%)")
            if q1 in ["بين 1 و 3 ساعات", "حتى للغد"]:
                st.write("**هادا هو المشكل ديالك بالضبط:** كتعطل باش تعيط.")
                st.write("**هادا هو الحل:** عيط في أقل من 5 دقايق. دير Notification في التليفون ديالك ملي يدخل Lead جديد، و عيط دغيا.")
                st.write("**علاش؟** حيت الكليان ملي كيعمر الفورم، كيكون سخون و متحمس و بغا يشري دابا. إلا خليتيه 1 ساعة، كيبرد، كيمشي عند واحد آخر، ولا كينسى، ولا كيبدل رايو. 5 دقايق اللولة هي اللي كتقرر واش غادي يأكد ولا لا.")
            if q4 in ["نمرة Fix", "واتساب فقط", "ما كنعيطش"]:
                st.write("**هادا هو الحل الثاني:** عيط من نمرة عادية 06، ماشي Fix و ماشي واتساب فقط.")
                st.write("**علاش؟** حيت المغاربة ما كيجاوبوش على النمرة Fix، كيحساب ليهم شركة ولا بنك. و واتساب بوحدو ما كافيش، حيت بزاف ما كيشوفوش الميساج. النمرة العادية 06 هي اللي كيجاوبو عليها.")
            if q2 == "كيقول ليا غالي":
                st.write("**هادا هو المشكل ديالك:** الكليان كيقول غالي.")
                st.write("**هادا هو الحل:** ما تنقصش الثمن! قول ليه: 'الثمن فيه التوصيل، و الدفع عند التوصيل، و إلا ما عجبكش ما تخلصش'. و زيد عرض: 'إلا خديتي 2، التانية بنص الثمن'.")
                st.write("**علاش؟** حيت الكليان ما كيقولش غالي حيت فعلا غالي، كيقولها حيت ما حسش بالقيمة. ملي كتشرح ليه التوصيل و الدفع عند التوصيل و الضمان، كيحس بالثقة و كيأكد.")
            if q2 == "كيقول ليا نشاور و نرجع":
                st.write("**هادا هو المشكل ديالك:** الكليان كيقول نشاور و نرجع.")
                st.write("**هادا هو الحل:** ما تخليهش يمشي. قول ليه: 'واخا شاوري، ولكن نحجز ليك واحد؟ حيت Stock كيسالي اليوم و الثمن غادي يطلع غدا'. و عاود عيط ليه من بعد 2 ساعات.")
                st.write("**علاش؟** حيت 'نشاور و نرجع' معناها 'ما اقتنعتش'. إلا خليتيه يمشي بلا ما تحجز ليه، 90% ما غاديش يرجع. إلا حجزتي ليه و عاودتي عيطتي، غادي يأكد.")
            if q2 == "ما كيجاوبش":
                st.write("**هادا هو المشكل ديالك:** الكليان ما كيجاوبش.")
                st.write("**هادا هو الحل:** عيط 3 مرات في أوقات مختلفة: مرة في الصباح، مرة في العشية، مرة في الليل. و صيفط ليه واتساب: 'السلام، أنا فلان، عمرتي الفورم على المنتج، بغيتي نأكد ليك الطلب؟'")
                st.write("**علاش؟** حيت بزاف ديال الناس كيكونو خدامين و ما كيجاوبوش في النهار. إلا عيطتي مرة وحدة و حبستي، غادي تخسر Lead خلصتي عليه فلوس. 3 محاولات كيطلعو CONF ديالك بـ 15%.")

        # 3. DELIV
        if cod_deliv < 65:
            st.error(f"🔴 المشكل رقم 3: DELIV طايح - {cod_deliv:.0f}% (الطبيعي 65-80%)")
            if q3 == "ما كيشدوش التليفون":
                st.write("**هادا هو المشكل ديالك:** الكليان ما كيشدش التليفون ملي كيوصلو الكولي.")
                st.write("**هادا هو الحل:** ملي كتأكد، قول ليه: 'غدا غادي يعيط ليك التوصيل من هاد النمرة، عافاك شد التليفون'. و نهار التوصيل، صيفط ليه واتساب: 'الكولي ديالك خرج اليوم، وجد الفلوس عافاك'.")
                st.write("**علاش؟** حيت الكليان كينسى أنه طلب، و ملي كيشوف نمرة غريبة ديال التوصيل، ما كيجاوبش. إلا وجدتيه قبل، غادي يشد التليفون و يشد الكولي.")
            if q3 == "كيقول ما عنديش فلوس":
                st.write("**هادا هو المشكل ديالك:** الكليان كيقول ما عنديش فلوس.")
                st.write("**هادا هو الحل:** ملي كتأكد، سولو: 'واش الفلوس واجدين؟ واش غادي تكون في الدار نهار كدا؟' إلا قال ليك لا، ما تصيفطش ليه، غادي يرجع و تخسر فلوس التوصيل.")
                st.write("**علاش؟** حيت بزاف ديال الناس كيأكدو و هما ما عندهمش الفلوس، و ملي كيوصل الكولي كيقولو ما عنديش. التأكيد الحقيقي هو ملي كتسولو على الفلوس و على الوقت، ماشي غير 'واخا صيفط'.")
            if q3 == "كيقول ما بغيتوش":
                st.write("**هادا هو المشكل ديالك:** الكليان كيقول ما بغيتوش ملي كيوصل.")
                st.write("**هادا هو الحل:** هادا معناه أن التأكيد ديالك كان ضعيف. ملي كتأكد، عاود ليه المنتج + الثمن + المدينة بالضبط، و قول ليه: 'إلا ما بغيتيهش، قولها ليا دابا باش ما نصيفطوش و ما نخسروش بجوج'.")
                st.write("**علاش؟** حيت الكليان ملي كيأكد و هو ما متأكدش، ملي كيوصل الكولي كيتراجع. إلا خليتيه يقول 'لا' في التأكيد، غادي توفر فلوس التوصيل و الإرجاع.")
            if q5 in ["3-4 أيام", "5 أيام و كثر"]:
                st.write("**هادا هو الحل الثاني:** التوصيل كيتعطل بزاف.")
                st.write("**هادا هو الحل:** بدل شركة التوصيل، ولا صيفط من المدينة اللي قريبة للكليان. خاص التوصيل يوصل في 1-2 أيام.")
                st.write("**علاش؟** حيت الكليان كيكون سخون نهار كيأكد، و كل نهار كيدوز، كيبرد. إلا وصل الكولي من بعد 5 أيام، 50% ديال الناس ما غاديش يشدوه، حيت نساو ولا لقاو واحد آخر ولا ما بقاوش بغاوه.")

        # إلا كلشي مزيان
        if cod_cpl <= 35 and cod_conf >= 60 and cod_deliv >= 65:
            st.success("✅ كلشي مزيان! CPL + CONF + DELIV كاملين في المستوى الطبيعي. كمل و سكيلي بـ 20% كل يومين، و ما تبدل والو.")