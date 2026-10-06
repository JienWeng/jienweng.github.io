"""Generate editable Excalidraw scenes for the public CRM and payment diagrams.

Run from any directory. SVG previews are rendered from these scenes by
render_excalidraw_diagrams.cjs (requires roughjs and jsdom).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER, INK, ACCENT = '#f6f3ec', '#403f39', '#885b43'
OUTLINE, CONNECTOR = '#aaa69c', '#9c7c69'

class Diagram:
    def __init__(self, title, subtitle, width=1600, height=900):
        self.elements = []
        self.width, self.height = width, height
        self.text(48, 28, title, 32)
        self.text(48, 88, subtitle, 22, '#494944')

    def element(self, kind, x, y, w, h, **extra):
        i = len(self.elements) + 1
        e = dict(id=f'element-{i}', type=kind, x=x, y=y, width=w, height=h,
                 angle=0, strokeColor=INK, backgroundColor='transparent',
                 fillStyle='solid', strokeWidth=1, strokeStyle='solid',
                 roughness=0.5, opacity=100, groupIds=[], frameId=None,
                 roundness=None, seed=i * 12347, version=1, versionNonce=i * 2341,
                 isDeleted=False, boundElements=None, updated=1, link=None, locked=False)
        e.update(extra)
        self.elements.append(e)
        return e

    def text(self, x, y, value, size=24, color=INK):
        lines = value.split('\n')
        return self.element('text', x, y, max(map(len, lines))*size*.65,
                            len(lines)*size*1.25, text=value, originalText=value,
                            fontSize=size, fontFamily=5, textAlign='left',
                            verticalAlign='top', containerId=None, autoResize=True,
                            lineHeight=1.25, strokeColor=color, strokeWidth=1)

    def box(self, x, y, title, body, w=310, h=154, accent=False):
        e = self.element('rectangle', x, y, w, h,
                         strokeColor=OUTLINE,
                         backgroundColor='#f0e7df' if accent else PAPER,
                         roundness=None)
        heading = self.text(x+18, y+18, title, 23, ACCENT if accent else INK)
        copy = self.text(x+18, y+64, body, 20, '#494944')
        for item in (e, heading, copy):
            item['groupIds'] = [f"group-{e['id']}"]
        return e

    def arrow(self, a, b):
        if a['y'] == b['y']:
            right = b['x'] > a['x']
            x = a['x']+a['width']+6 if right else a['x']-6
            endx = b['x']-8 if right else b['x']+b['width']+8
            y = a['y']+a['height']/2
            dx, dy = endx-x, 0
        else:
            x = a['x']+a['width']/2
            y = a['y']+a['height']+6
            dx = b['x']+b['width']/2-x
            dy = b['y']-8-y
        connector = self.element('arrow', x, y, abs(dx), abs(dy), points=[[0,0],[dx,dy]],
                     startBinding={'elementId': a['id'], 'focus': 0, 'gap': 6},
                     endBinding={'elementId': b['id'], 'focus': 0, 'gap': 8}, startArrowhead=None,
                     endArrowhead='arrow', strokeColor=CONNECTOR, elbowed=False)
        for target in (a, b):
            target['boundElements'] = (target['boundElements'] or []) + [
                {'id': connector['id'], 'type': 'arrow'}]

    def chain(self, specs):
        boxes = [self.box(*s) for s in specs]
        for a,b in zip(boxes, boxes[1:]): self.arrow(a,b)
        return boxes

    def save(self, relative):
        path = ROOT / 'static' / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        scene = dict(type='excalidraw', version=2, source='https://excalidraw.com',
                     elements=self.elements, appState=dict(viewBackgroundColor=PAPER,
                     gridSize=None), files={})
        path.write_text(json.dumps(scene, indent=2)+'\n')
        print(path.relative_to(ROOT))


d = Diagram('CRM / Deal to cash', 'Sales, delivery and finance share the approved sales order.', 1600, 1080)
for y,label in [(164,'SALES'),(384,'SALES ADMIN'),(604,'PROJECT'),(824,'FINANCE')]:
    d.text(48,y,label,20,ACCENT)
# Compact swimlanes preserve the existing handoffs and record relationships.
b = d.chain([(230,150,'01  Lead qualified','Account + contact\n+ opportunity'),
             (680,150,'02  Funnel advances','Stage-gated approvals\n1D → 4A'),
             (1130,150,'03  Quote accepted','Revisions preserved\nTaxes and currency fixed')])
order=d.box(1130,370,'04  Sales order','Numbered and approved\nThe pivot record',accent=True)
d.arrow(b[-1],order)
project=d.box(680,590,'05  Project opens','Items, budget, team\nPhases and milestones')
# Route the handoff using a separate segment so it clears the lane label.
d.arrow(order,project)
delivery=d.box(1130,590,'06  Delivery tracked','Progress recorded\nfor each milestone'); d.arrow(project,delivery)
finance=d.chain([(680,810,'07  Milestone due','Invoice instruction\nsent to Autocount'),
                 (1130,810,'08  Payment received','Status returned to\nmilestone and funnel')])
d.arrow(delivery,finance[0])
d.text(48,1010,'Management visibility: pipeline · billing forecast · delivery progress · collections',23)
d.save('img/blog/quandatics/deal-to-cash.excalidraw')

d = Diagram('CRM / Project to cash', 'An approved sale becomes a project; approved milestones become invoices.',1600,850)
specs=[(48,190,'01  Sales order','Won, approved\nand numbered'),
       (440,190,'02  Project','Bound 1:1 to the order\nItems, budget and team'),
       (832,190,'03  Project phases','Deliverables and\nprogress per phase'),
       (1224,190,'04  Milestone claim','Completed phase\nEvidence attached'),
       (1224,490,'05  Approval','Manager sign-off\nrecorded'),
       (832,490,'06  Sales invoice','Issued for the\napproved milestone'),
       (440,490,'07  Payment receipt','Matched against\nthe invoice'),
       (48,490,'08  Margin updated','Project and funnel\nrecords stay current')]
d.chain(specs)
d.text(48,730,'Current limitation: milestones are updated manually until Phase 2 is delivered.',24,ACCENT)
d.save('img/blog/quandatics/project-to-cash.excalidraw')

d=Diagram('CRM / Money in and money out','The sales order links customer revenue and supplier costs to the same project.',1600,850)
for y,label,steps in [(235,'ORDER TO CASH / CUSTOMER',[
    ('Milestone claim','Phase complete\nSubmit for billing'),('Sales invoice','Numbered invoice\nper milestone'),
    ('Payment receipt','Matched against\nthe invoice'),('Autocount','Ledger entry\nNo re-keying'),('Documents','Order, invoice\nand receipt archived')]),
    (545,'PROCURE TO PAY / SUPPLIER',[
    ('Purchase order','Linked to sales\norder and project'),('Supplier invoice','Captured and matched\nto purchase order'),
    ('Payment voucher','Approved payment\nsent through'),('Autocount','Cost recorded\nagainst the project'),('Documents','Order, bill and\nvoucher archived')])]:
    d.text(48,y-58,label,24,ACCENT)
    d.chain([(48+i*310,y,t,b,260,164) for i,(t,b) in enumerate(steps)])
d.text(48,778,'Shared outcome: revenue, costs and supporting records roll up to the same project.',23)
d.save('img/blog/quandatics/o2c-p2p.excalidraw')

d=Diagram('CryptoRails / Deposit to settlement','Browser detection gives feedback. A verified server webhook authorises settlement.',1600,890)
d.chain([(48,190,'01  Receive','Generate customer address\nStore in merchant backend',340,170),
         (436,190,'02  Detect','Customer sends funds\nonDeposit gives feedback',340,170),
         (824,190,'03  Consolidate','Backend requests sweep\nValidate funds server-side',340,170),
         (1212,190,'04  Settle','Confirm sweep on-chain\nSigned webhook to backend',340,170)])
d.box(48,445,'Funds detected','Client-side signal\nUpdate the interface\nDo not credit the ledger yet',650,190)
d.box(824,445,'Funds settled','Verify HMAC against raw body\nReconcile address and reference\nCredit once; reject duplicates',728,190,True)
d.text(48,700,'Gateway states',27,ACCENT)
d.text(48,750,'pending → wait_for_confirmation → confirmed     /     On error → failed',26)
d.text(48,830,'Public integration flow · API key stays in the merchant backend.',22,'#494944')
d.save('img/projects/cryptorails-deposit-flow.excalidraw')
