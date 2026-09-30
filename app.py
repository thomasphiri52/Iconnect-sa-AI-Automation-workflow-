import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="iConnect SA | AI Customer Service", page_icon="🔷", layout="wide")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root{--bg:#06152b;--panel:#0b2040;--border:#183c68;--muted:#a8bdd9}
html,body,[class*="css"]{font-family:Inter,sans-serif}
.stApp{background:var(--bg);color:#eef5ff}
header[data-testid="stHeader"]{background:#06152b}
.block-container{padding-top:1rem;max-width:100%}
section[data-testid="stSidebar"]{background:#071a33;border-right:1px solid #17365d}
div[data-testid="stMetric"]{background:linear-gradient(135deg,#0c2445,#0a1e39);border:1px solid var(--border);border-radius:10px;padding:16px;min-height:110px}
div[data-testid="stMetricLabel"]{color:#c7d7eb}
div[data-testid="stMetricValue"]{color:#f4f8ff;font-weight:800}
.panel{background:linear-gradient(145deg,#0b2040,#081a34);border:1px solid var(--border);border-radius:10px;padding:15px;margin-bottom:14px}
.title{font-size:16px;font-weight:650;margin-bottom:10px}
.muted{color:var(--muted);font-size:12px}
div.stButton>button{background:#0a3970;color:#eef6ff;border:1px solid #2763a2;border-radius:8px}
div.stButton>button:hover{background:#0d58a4;color:white}
</style>""", unsafe_allow_html=True)

if "page" not in st.session_state: st.session_state.page="Dashboard"
if "messages" not in st.session_state:
    st.session_state.messages=[
      ("assistant","Hello! I'm your iConnect SA AI assistant. I can help you classify enquiries, draft responses and suggest the best support team."),
      ("user","I have a problem with my internet connection. It's very slow."),
      ("assistant","I've classified this as a Network / Internet Issue (High Priority).\\n\\nSuggested response: “Hi, thank you for reaching out. Our technical team is investigating. We'll keep you updated. Your reference number is #INC-487.”")
    ]

with st.sidebar:
    st.markdown("<div style='font-size:27px;font-weight:800'>🔷 iConnect SA</div><div class='muted'>Connect · Support · Grow</div><br/>",unsafe_allow_html=True)
    for icon,name in [("🏠","Dashboard"),("♧","Customer Service AI"),("▤","Tickets"),("▢","Live Support"),("🔔","Automated Alerts"),("▥","Reports & Analytics"),("⚙","Settings")]:
        if st.button(f"{icon}   {name}"+("   🔴 3" if name=="Automated Alerts" else ""),key=name,use_container_width=True):
            st.session_state.page=name; st.rerun()
    st.markdown("<div style='height:100px'></div><div class='panel' style='text-align:center;padding:24px 8px'><div style='font-size:38px'>✣</div><br/>Better connections.<br/>A smarter tomorrow.<br/><br/><b>iConnect SA</b></div>",unsafe_allow_html=True)

x,y,z=st.columns([5.8,1.2,1.5])
with x:
    st.markdown("<div style='font-size:25px;font-weight:750'>▣ &nbsp; AI Customer Service Assistant</div><div class='muted'>Smarter support. Faster resolutions. Happier customers.</div>",unsafe_allow_html=True)
with y: st.markdown("<div style='color:#35e4ca;padding-top:8px'>● Live Data Stream</div><div class='muted'>Updated 10:24 AM</div>",unsafe_allow_html=True)
with z: st.markdown("<div style='text-align:right;padding-top:6px'>🔔 &nbsp; <b>Support Team</b><br/><span class='muted'>iConnect SA</span></div>",unsafe_allow_html=True)
st.markdown("<hr style='border-color:#183c68'>",unsafe_allow_html=True)
if st.session_state.page!="Dashboard":
    st.markdown(f"<div class='panel'><div class='title'>{st.session_state.page}</div><div class='muted'>Workspace view — use the sidebar to navigate back to Dashboard.</div></div>",unsafe_allow_html=True)

cols=st.columns(4)
for c,label,value,delta in zip(cols,["Total Customer Enquiries","Open Tickets","Avg. Response Time","Customer Satisfaction"],["482","134","2.4 min","96%"],["↑ 12%","↓ 18%","↓ 32%","↑ 8%"]):
    with c: st.metric(label,value,delta+" vs. last hour")

left,mid,right=st.columns([1.75,1.05,1.25],gap="medium")
hours=["08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00"]
with left:
    st.markdown("<div class='panel'><div class='title'>Live Customer Enquiries Trend</div>",unsafe_allow_html=True)
    f=go.Figure()
    for name,vals,color in [("Total Enquiries",[65,90,90,100,100,120,122,155,138,130,112,105,112],"#087cf0"),("Resolved",[45,60,60,70,72,92,94,120,105,98,80,77,82],"#10c99a"),("Escalated",[10,15,7,15,12,22,22,28,24,24,18,17,21],"#f59e0b")]:
        f.add_trace(go.Scatter(x=hours,y=vals,name=name,mode="lines+markers",line=dict(color=color,width=2)))
    f.update_layout(height=255,margin=dict(l=0,r=0,t=5,b=0),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",font=dict(color="#c7d7eb",size=10),legend=dict(orientation="h",y=1.15,x=0),xaxis=dict(gridcolor="#18365a"),yaxis=dict(gridcolor="#18365a",range=[0,200]))
    st.plotly_chart(f,use_container_width=True,config={"displayModeBar":False}); st.markdown("</div>",unsafe_allow_html=True)
with mid:
    st.markdown("<div class='panel'><div class='title'>Enquiry Channels</div>",unsafe_allow_html=True)
    d=go.Figure(go.Pie(labels=["Chat","Email","Phone","Social Media","Website"],values=[42,28,18,7,5],hole=.62,marker=dict(colors=["#087cf0","#10c99a","#8956ee","#f59e0b","#e748a5"])))
    d.update_layout(height=255,margin=dict(l=0,r=0,t=0,b=0),paper_bgcolor="rgba(0,0,0,0)",font=dict(color="#d7e5f7",size=10),legend=dict(orientation="v",x=1,y=.5))
    st.plotly_chart(d,use_container_width=True,config={"displayModeBar":False}); st.markdown("</div>",unsafe_allow_html=True)
with right:
    st.markdown("<div class='panel'><div class='title'>🤖 AI Customer Service Assistant &nbsp; <span style='color:#35e4ca'>● Online</span></div>",unsafe_allow_html=True)
    for role,msg in st.session_state.messages[-3:]:
        bg="#0878ed" if role=="user" else "#102b50"
        st.markdown(f"<div style='background:{bg};border:1px solid #20466f;border-radius:10px;padding:11px;margin:8px 0;font-size:12px'>{msg.replace(chr(10),'<br/>')}</div>",unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    with c1:
        if st.button("Use This Reply",use_container_width=True): st.session_state.messages.append(("assistant","Suggested reply selected and ready to send.")); st.rerun()
    with c2:
        if st.button("Edit",use_container_width=True): st.session_state.edit=True
    with c3:
        if st.button("Escalate",use_container_width=True): st.session_state.messages.append(("assistant","Ticket #INC-487 flagged for technical escalation.")); st.rerun()
    st.markdown("</div>",unsafe_allow_html=True)
    if st.session_state.get("edit"):
        edit=st.text_area("Edit reply", "Hi, thank you for reaching out. Our technical team is investigating.")
        if st.button("Save reply"): st.session_state.messages.append(("assistant",edit)); st.session_state.edit=False; st.rerun()
    prompt=st.chat_input("Type a message...")
    if prompt:
        st.session_state.messages.extend([("user",prompt),("assistant","Thanks for your message. I've logged it for the support team.")]); st.rerun()

st.markdown("<div class='panel'><div class='title'>Recent Customer Tickets <span style='float:right;color:#31a8ff'>View All →</span></div>",unsafe_allow_html=True)
tickets=pd.DataFrame([
["INC-587","Thabo M.","Slow internet","High","Open","Suggested reply","10:23 AM"],
["INC-586","Sarah L.","Billing enquiry","Medium","In Progress","Assigned to Billing","10:17 AM"],
["INC-585","James K.","VoIP not working","High","Open","Escalate to Tech","10:12 AM"],
["INC-584","Nomsa D.","New connection","Low","Resolved","Auto-resolved","09:58 AM"],
["INC-583","Sipho T.","Email not working","Medium","In Progress","Assigned to IT","09:42 AM"]],columns=["ID","Customer","Issue","Priority","Status","AI Action","Time"])
st.dataframe(tickets,use_container_width=True,hide_index=True,height=225)
st.markdown("</div>",unsafe_allow_html=True)

a,b,c=st.columns([1.15,1,.72],gap="medium")
with a:
    st.markdown("<div class='panel'><div class='title'>🔔 Automated Alerts</div>",unsafe_allow_html=True)
    for icon,msg,t in [("🔴","Network latency detected - Johannesburg","10:18 AM"),("🟠","High volume of chat enquiries","09:54 AM"),("🟡","Customer satisfaction below 90% (N. West)","09:32 AM"),("🟢","System back online - Cape Town","08:21 AM")]:
        st.markdown(f"<div style='padding:8px 0;border-bottom:1px solid #17365d;font-size:12px'>{icon} &nbsp; {msg}<span style='float:right;color:#9db4d2'>{t}</span></div>",unsafe_allow_html=True)
    st.markdown("</div>",unsafe_allow_html=True)
with b:
    st.markdown("<div class='panel'><div class='title'>✦ AI Insights &nbsp; <span style='color:#c7b8ff'>Key Insight</span></div><div style='font-size:13px;line-height:1.7'>💡 Internet connection issues are up 42% compared to this time yesterday. Consider pre-emptive communication to affected customers.</div></div>",unsafe_allow_html=True)
    if st.button("View Details"): st.info("Monitor network latency, notify impacted customers, and review ticket volume by region.")
with c:
    st.markdown("<div class='panel'><div class='title'>⚡ Quick Actions</div>",unsafe_allow_html=True)
    for label,target in [("▤ Create Ticket","Tickets"),("☷ View All Tickets","Tickets"),("♧ Send Alert","Automated Alerts"),("▥ Generate Report","Reports & Analytics")]:
        if st.button(label,use_container_width=True): st.session_state.page=target; st.rerun()
    st.markdown("</div>",unsafe_allow_html=True)
st.markdown("<div class='muted' style='text-align:center;padding:10px'>iConnect SA • AI Automation Console • Illustrative demo data</div>",unsafe_allow_html=True)
