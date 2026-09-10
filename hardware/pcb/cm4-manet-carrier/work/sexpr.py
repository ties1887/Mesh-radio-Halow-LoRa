import re,json
def parse(text):
 stack=[];result=None
 for tok in re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+',text):
  if tok=='(':stack.append([])
  elif tok==')':
   a=stack.pop()
   if stack:stack[-1].append(a)
   else:result=a
  else:stack[-1].append(json.loads(tok,strict=False) if tok.startswith('"') else tok)
 return result
def children(x,k):return [v for v in x if isinstance(v,list) and v[0]==k]
def child(x,k):return next((v for v in x if isinstance(v,list) and v[0]==k),None)
def dump(x):
 if isinstance(x,list):return '('+' '.join(dump(i) for i in x)+')'
 if isinstance(x,(int,float)):return str(x)
 return json.dumps(x) if not re.fullmatch(r'[A-Za-z0-9_+./:#~{}$-]+',x) else x
