import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
c=json.load(open('counts.json'))
fig,ax=plt.subplots(figsize=(11,13.2)); ax.set_xlim(0,110); ax.set_ylim(4,132); ax.axis('off')
plt.rcParams['font.family']='DejaVu Sans'
def box(x,y,w,h,t,fc='white',fs=9.5,bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='square,pad=0',fc=fc,ec='black',lw=1))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=fs,wrap=True,weight='bold' if bold else 'normal')
def arrow(x1,y1,x2,y2): ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>',lw=1,color='black'))
box(12,124,96,6,'Identification of studies via databases and registers',fc='#F2C94C',fs=11,bold=True)
bands=[('1  Identification',104,18),('2  Screening\n(title/abstract)',80,22),('3  Eligibility\n(full text)',40,38),('4  Included',18,20)]
for t,y,h in bands:
    ax.add_patch(FancyBboxPatch((2,y),8,h,boxstyle='square,pad=0',fc='#9DC3E6',ec='black',lw=1))
    ax.text(6,y+h/2,t,ha='center',va='center',rotation=90,fontsize=9.5,weight='bold')
L,W,R,RW=14,40,62,46
box(L,106,W,14,f"Records identified from:\n{c['database']}\n(n = {c['identified']})")
box(R,106,RW,14,f"Records removed before screening:\nDuplicate records removed (n = {c['duplicates_removed']})\nRecords marked as ineligible by\nautomation tools (n = {c['automation_ineligible']})\nRecords removed for other reasons (n = {c['other_removed']})",fs=9)
arrow(L+W,113,R,113); arrow(L+W/2,106,L+W/2,98)
box(L,90,W,8,f"Records screened\n(n = {c['screened']})")
box(R,88,RW,12,f"Records excluded**\n(n = {c['excluded_ta']})\nby a human: n = {c['excluded_ta_human']}\nby automation tool: n = {c['excluded_ta_automation']}",fs=9)
arrow(L+W,94,R,94); arrow(L+W/2,90,L+W/2,84)
box(L,76,W,8,f"Reports sought for retrieval\n(n = {c['sought']})")
box(R,70,RW,16,f"Reports not retrieved\n(n = {c['not_retrieved']})\n\nReports not assessed: cap of 10 studies\nreached under the pre-specified\nprioritisation rule (n = {c['not_assessed_cap']})",fs=9)
arrow(L+W,80,R,80); arrow(L+W/2,76,L+W/2,64)
box(L,56,W,8,f"Reports assessed for eligibility\n(n = {c['assessed']})")
ex='\n'.join(f"{k} (n = {v})" for k,v in c['excluded_ft'].items())
box(R,48,RW,18,f"Reports excluded (n = {sum(c['excluded_ft'].values())}):\n{ex}",fs=9)
arrow(L+W,60,R,60); arrow(L+W/2,56,L+W/2,34)
box(L,22,W,12,f"Studies included in review\n(n = {c['included_studies']})\nReports of included studies\n(n = {c['included_reports']})")
chk=c['identified']-c['duplicates_removed']==c['screened'] and c['screened']-c['excluded_ta']==c['sought'] and c['sought']-c['not_retrieved']-c['not_assessed_cap']==c['assessed'] and c['assessed']-sum(c['excluded_ft'].values())==c['included_studies'] and c['excluded_ta_human']+c['excluded_ta_automation']==c['excluded_ta']
assert chk
foot=("** Automation tool: AI-assisted first-pass screening (Claude, Anthropic) with a rubric frozen after two blind pilots (n = 50, binary κ = 0.48; n = 20, κ = 0.64).\n"
"Blind human verification of 116 records (all records passed by the tool + random 10% of its exclusions): agreement 96.6%, κ = 0.93;\n"
"1 of 45 sampled exclusions rescued (2.2%). Rapid review (Cochrane RRMG guidance); one human reviewer. Phases numbered 1–4 per course brief;\n"
"in the PRISMA 2020 template, eligibility is reported within Screening.\n"
"Arithmetic check: 617 − 2 = 615; 615 − 507 = 108; 108 − 11 − 75 = 22; 22 − 12 = 10.\n"
"Template: Page MJ, et al. BMJ 2021;372:n71. doi:10.1136/bmj.n71 (CC BY 4.0).")
ax.text(2,15,foot,ha='left',va='top',fontsize=7.2)
for ext in ('png','pdf','svg'): fig.savefig(f'PRISMA_2020_flow_D04.{ext}',dpi=200,bbox_inches='tight')
print('ok')
