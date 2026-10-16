"""NUM-40 exact rational state-error enclosures on fixed common windows.
Certificate scope: rational Hermite reconstruction with MP100-rounded slopes,
selected physical windows only. Not an ODE solution/error/stability certificate.
"""
from pathlib import Path
import argparse,bisect,datetime,hashlib,importlib.util,json,signal,time
import mpmath as mp
import sympy as sp
p=Path(__file__).with_name('BT04-D24-W02-NUM-CANDIDATE-001__qw_dense_probe_01.py')
s=importlib.util.spec_from_file_location('extrema_dense',p);dense=importlib.util.module_from_spec(s);s.loader.exec_module(dense)
cp=dense.cp;t=sp.Symbol('t');S=lambda x:mp.nstr(x,40)
PARENT_SHA='dae8c2911aaf80d5168f13c6d7dd7004a846414296a344e436ea37d8334b06d8'
PARENT_FILE_SHA='8dacc65836035b1e3a0f0d1cb01f4b7076c14615c330a57664f15ce048981b43'
OUTPUT=Path('NUM40_STATE_EXTREMA_01.json');SCALE=10**24;EPS=sp.Rational(1,SCALE)
COEFFICIENTS=((1,2,1),(-1,2,2),(-1,5,2),(2,5,3))

def Q(x):
    if isinstance(x,mp.mpf):
        sign,man,exp,_=x._mpf_;return (-1)**sign*sp.Integer(man)*sp.Rational(2)**exp
    return sp.Rational(x)

def hex_q(v):return sp.Rational(*float.fromhex(v).as_integer_ratio())
def M(v):return mp.mpf(int(v.p))/int(v.q)
def packq(v):return str(v)
def poly_hash(p):
    _,integer=p.clear_denoms();_,primitive=integer.primitive()
    return cp.sha(cp.canonical([str(v) for v in primitive.all_coeffs()]))

def protocol():
    return dict(kind='selected-window-rational-state-extrema-v1',parent_payload_sha256=PARENT_SHA,
                variants=['control','half','full'],arm='80',slopes_dps=100,witness_dps=120,witness_gate='1e-70',
                selection='NUM39 q64 local/common state-error witnesses; containing interval and one neighbour each side; union across all variants; evaluate all curves on this same union',
                components=4,root_interval_width='1e-24',outward_value_grid='1e-24',enclosure_gap_gate='1e-20',
                maximum_total_pieces=48,maximum_critical_degree=6,root_seconds_limit=3,batch_seconds_limit=90,
                reconstruction='exact rational Hermite polynomial through exact MP80 states and exact values of MP100-rounded slopes; binary64 coordinates treated as exact rationals',
                completeness='square-free critical polynomial, exact Sturm count and disjoint isolating intervals; endpoints included',
                absolute_value_zeros='zeros of signed error cannot be nonzero absolute maxima; constant/zero error handled separately',
                output='component root brackets and outward rational enclosures; coefficients regenerated from checkpoint',
                new_bvp_solves=0,state_changes=0,residual_extrema_certified=False,whole_domain_certified=False,physical_error_certified=False)

def load_sources():
    parent,info=dense.audit();src=dense.source()
    if info['payload_sha256']!=PARENT_SHA:raise ValueError('Wrong NUM39 parent')
    return parent,src

def common_windows(parent,src):
    selected=[];seeds=[]
    with mp.workdps(120):
        for row in parent['rows']:
            if row['level']!=64:continue
            case=next(r for r in src['cases'] if r['variant']==row['variant']);x=list(map(hex_q,case['mesh']))
            r=Q(dense.o.core.unpack(row['survey']['state_witness']['radius_exact'])[0])
            j=min(max(bisect.bisect_right(x,r)-1,0),61)
            a,b=x[max(j-1,0)],x[min(j+2,62)]
            selected.append((a,b));seeds.append(dict(variant=row['variant'],grid=row['grid'],interval=j,radius=packq(r),span=[packq(a),packq(b)]))
    merged=[]
    for a,b in sorted(selected):
        if merged and a<=merged[-1][1]:merged[-1]=(merged[-1][0],max(b,merged[-1][1]))
        else:merged.append((a,b))
    return merged,seeds

def pieces(row,windows):
    x=list(map(hex_q,row['mesh']));result=[]
    for wi,(left,right) in enumerate(windows):
        for j,(a,b) in enumerate(zip(x,x[1:])):
            lo,hi=max(a,left),min(b,right)
            if lo<hi:result.append((wi,j,(lo-a)/(b-a),(hi-a)/(b-a)))
    return result

def exact_prepared(row):
    with mp.workdps(100):
        x,y,f=dense.prepare(row)
        return list(map(Q,x)),[[Q(v) for v in line] for line in y],[[Q(v) for v in line] for line in f]

def component(prepared,j,k):
    x,y,f=prepared;a=x[j];h=x[j+1]-a;T=1+a+h*t
    B=(2*t**3-3*t*t+1,t**3-2*t*t+t,-2*t**3+3*t*t,t**3-t*t)
    Y=sp.Poly(sum(b*v for b,v in zip(B,(y[j][k],h*f[j][k],y[j+1][k],h*f[j+1][k]))),t,domain=sp.QQ)
    c,d,power=COEFFICIENTS[k]
    N=sp.Poly(d*T**power*Y.as_expr()-c,t,domain=sp.QQ)
    D=sp.Poly(d*T**power+abs(c),t,domain=sp.QQ)
    critical=sp.Poly(T*Y.diff().as_expr()*(d*T**power+abs(c))+power*h*(abs(c)*Y.as_expr()+c),t,domain=sp.QQ)
    factor=sp.Poly(d*T**(power-1),t,domain=sp.QQ)
    if N.diff()*D-N*D.diff()!=critical*factor:raise ValueError('Derivative identity failed')
    if critical.degree()>6:raise ValueError('Critical polynomial degree cap')
    return N,D,critical,factor

def mul_interval(a,b):
    products=[u*v for u in a for v in b];return min(products),max(products)

def poly_interval(p,a,b):
    value=(sp.Rational(0),sp.Rational(0))
    for c in p.all_coeffs():
        lo,hi=mul_interval(value,(a,b));value=(lo+c,hi+c)
    return value

def absolute_ratio_interval(N,D,a,b):
    nl,nh=poly_interval(N,a,b);dl,dh=poly_interval(D,a,b)
    if dl<=0:raise ValueError('Positive denominator not certified')
    values=[u/v for u in (nl,nh) for v in (dl,dh)];lo,hi=min(values),max(values)
    return (sp.Rational(0) if lo<=0<=hi else min(abs(lo),abs(hi))),max(abs(lo),abs(hi))

def variations(sequence,x):
    signs=[sp.sign(p.eval(x)) for p in sequence];signs=[s for s in signs if s]
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def sturm_count(poly,a,b):
    seq=poly.sturm()
    return variations(seq,a)-variations(seq,b)

def root_brackets(critical,a,b):
    if critical.is_zero:return [],0,True,[True,True]
    if critical.degree()<=0:return [],0,False,[False,False]
    q=critical.sqf_part();endpoints=[q.eval(a)==0,q.eval(b)==0]
    for endpoint,is_root in zip((a,b),endpoints):
        if is_root:q=q.exquo(sp.Poly(t-endpoint,t,domain=sp.QQ))
    if q.degree()<=0:return [],0,False,endpoints
    count=sturm_count(q,a,b)
    def timeout(*args):raise TimeoutError('Root isolation exceeded three seconds')
    old_handler=signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,3)
    try:isolated=q.intervals(eps=EPS,inf=a,sup=b)
    finally:signal.setitimer(signal.ITIMER_REAL,0);signal.signal(signal.SIGALRM,old_handler)
    intervals=[]
    for (lo,hi),multiplicity in isolated:
        if multiplicity!=1 or not a<=lo<=hi<=b or hi-lo>EPS:raise ValueError('Invalid root interval')
        if lo==hi:
            if q.eval(lo)!=0:raise ValueError('Invalid exact root')
        elif q.eval(lo)==0 or q.eval(hi)==0 or sturm_count(q,lo,hi)!=1:raise ValueError('Root count in bracket is not one')
        if intervals and intervals[-1][1]>=lo:raise ValueError('Overlapping root brackets')
        intervals.append((lo,hi))
    if len(intervals)!=count:raise ValueError('Incomplete root isolation')
    return intervals,count,False,endpoints

def enclose(N,D,critical,factor,a,b):
    if not 0<=a<b<=1:raise ValueError('Invalid trimmed interval')
    if N.diff()*D-N*D.diff()!=critical*factor:raise ValueError('Wrong derivative factorization')
    if poly_interval(D,a,b)[0]<=0 or poly_interval(factor,a,b)[0]<=0:raise ValueError('Denominator/factor positivity not proved')
    roots,count,constant,endpoints=root_brackets(critical,a,b)
    candidates=[(a,a),(b,b)]+roots;lower=sp.Rational(-1);upper=sp.Rational(-1);best=None
    for lo,hi in candidates:
        midpoint=(lo+hi)/2;value=abs(N.eval(midpoint)/D.eval(midpoint));_,bound=absolute_ratio_interval(N,D,lo,hi)
        if value>lower:lower=value;best=midpoint
        upper=max(upper,bound)
    lower_units=int(sp.floor(lower*SCALE));upper_units=int(sp.ceiling(upper*SCALE))
    return dict(lower_units=lower_units,upper_units=upper_units,degree=int(critical.degree()) if not critical.is_zero else -1,
                critical_polynomial_sha256=poly_hash(critical),interior_roots=count,constant_error=constant,
                endpoint_stationary=[bool(v) for v in endpoints],root_brackets=[[packq(a),packq(b)] for a,b in roots],
                lower_witness_t=packq(best),gap_pass=bool(upper_units-lower_units<=10000))

def witness_check(row,prepared,j,k,best):
    with mp.workdps(120):
        x,y,f=prepared;r=x[j]+(x[j+1]-x[j])*best;rr=M(r)
        # Independent normalized Hermite evaluation, retaining the same frozen slopes.
        frozen=([M(v) for v in x],[[M(v) for v in line] for line in y],[[M(v) for v in line] for line in f])
        state,dy=dense.basis_value(frozen,rr)
        truth=dense.o.exact(rr);observed=abs(state[k]-truth[k])/(1+abs(truth[k]))
        N,D,_,_=component(prepared,j,k);exact=abs(N.eval(best)/D.eval(best))
        delta=abs(observed-M(exact))/(1+abs(M(exact)))
        return dict(radius=S(rr),component=k,scaled_discrepancy=S(delta),passed=bool(delta<=mp.mpf('1e-70')))

def compute(parent,src):
    windows,seeds=common_windows(parent,src);plans={r['variant']:pieces(r,windows) for r in src['cases']}
    if sum(map(len,plans.values()))>48:raise ValueError('Piece budget exceeded before root isolation')
    rows=[];started=time.monotonic()
    for row in src['cases']:
        prepared=exact_prepared(row);records=[]
        for wi,j,a,b in plans[row['variant']]:
            if time.monotonic()-started>90:raise TimeoutError('NUM40 batch limit')
            components=[]
            for k in range(4):
                value=enclose(*component(prepared,j,k),a,b);components.append(value)
            records.append(dict(window=wi,interval=j,t_range=[packq(a),packq(b)],components=components))
        flat=[(c,rec['interval'],k) for rec in records for k,c in enumerate(rec['components'])]
        lower=max(v[0]['lower_units'] for v in flat);upper=max(v[0]['upper_units'] for v in flat)
        best,j,k=max(flat,key=lambda x:x[0]['lower_units'])
        check=witness_check(row,prepared,j,k,sp.Rational(best['lower_witness_t']))
        summary=dict(lower_units=lower,upper_units=upper,denominator=SCALE,gap_pass=upper-lower<=10000,
                     all_piece_gaps_pass=all(v[0]['gap_pass'] for v in flat),witness=check,
                     pieces=len(records),stationary_roots=sum(v[0]['interior_roots'] for v in flat))
        rows.append(dict(variant=row['variant'],arm='80',summary=summary,records=records))
        print(row['variant'],summary,flush=True)
    return dict(windows=[[packq(a),packq(b)] for a,b in windows],seeds=seeds,cases=rows)

def comparison(result):
    if [r['variant'] for r in result['cases']]!=['control','half','full']:raise ValueError('Case order')
    control=result['cases'][0]['summary'];rows=[]
    if control['lower_units']<=0:raise ValueError('Nonpositive control lower bound')
    for case in result['cases'][1:]:
        c=case['summary'];lo=sp.Rational(c['lower_units'],control['upper_units']);hi=sp.Rational(c['upper_units'],control['lower_units'])
        valid=all(s['gap_pass'] and s['all_piece_gaps_pass'] and s['witness']['passed'] for s in (c,control))
        rows.append(dict(variant=case['variant'],ratio_lower=packq(lo),ratio_upper=packq(hi),
                         smaller_on_common_windows=bool(valid and c['upper_units']<control['lower_units']),whole_domain_claim=False))
    return rows

def execute():
    if OUTPUT.exists():raise FileExistsError('Refusing to overwrite NUM40')
    parent,src=load_sources();sources=dict(parent['source_hashes'])
    cp.m.compact.checked_source(dense.OUTPUT,PARENT_FILE_SHA);sources[str(dense.OUTPUT)]=PARENT_FILE_SHA
    for suffix in ('state_extrema_01.py','state_extrema_tests_01.py'):
        p=cp.m.HERE/(cp.m.PRE+suffix);sources[str(p)]=cp.sha(p.read_bytes())
    data=dict(protocol=protocol(),source_hashes=sources,sympy_version=sp.__version__,status='running',start_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    data['result']=compute(parent,src);data['comparisons']=comparison(data['result'])
    data.update(status='completed_selected_window_enclosures',end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    if len(cp.readable(data).encode())>180000:raise ValueError('Text output exceeds fixed 180KB budget')
    cp.write_text_new(OUTPUT,dict(payload_sha256=cp.sha(cp.canonical(data)),payload=data))
    return audit()[1]

def audit(replay=False):
    wrapper=json.loads(OUTPUT.read_text());d=wrapper['payload'];parent,src=load_sources()
    if wrapper['payload_sha256']!=cp.sha(cp.canonical(d)) or d['protocol']!=protocol() or d['status']!='completed_selected_window_enclosures':raise ValueError('NUM40 identity/checksum')
    for p,h in d['source_hashes'].items():cp.m.compact.checked_source(p,h)
    windows,seeds=common_windows(parent,src)
    if d['result']['windows']!=[[packq(a),packq(b)] for a,b in windows] or d['result']['seeds']!=seeds:raise ValueError('Window selection mismatch')
    if d['comparisons']!=comparison(d['result']):raise ValueError('Comparison mismatch')
    if replay and d['result']!=compute(parent,src):raise ValueError('Exact enclosure replay mismatch')
    return d,dict(status='audited_selected_window_enclosures',payload_sha256=wrapper['payload_sha256'],bytes=OUTPUT.stat().st_size,full_exact_replay=replay,new_bvp_solves=0)
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--execute',action='store_true');p.add_argument('--replay',action='store_true');a=p.parse_args()
    print(json.dumps(execute() if a.execute else audit(a.replay)[1],indent=2))